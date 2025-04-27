from flask import Flask, request, render_template, redirect, session
import requests
import json
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
import asyncio
import aiohttp

app = Flask(__name__)
app.secret_key = "supersecretkey"

ASI_API_KEY = "sk_5e8dbfb687c84cc0b32ca1ef309e329d6e49084d44aa4c61a9a1bc5fbd92064f"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Mentor model
class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    display_name = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    education = db.Column(db.String(100))
    field = db.Column(db.String(100))
    career_stage = db.Column(db.String(100))
    bio = db.Column(db.String(500))
    resume = db.Column(db.Text)
    personality = db.Column(db.String(100))
    hobbies = db.Column(db.Text)
    tone = db.Column(db.String(100))
    mascot = db.Column(db.String(100))


with app.app_context():
    db.create_all()
    


# ---------------- LANDING PAGE ---------------- #
@app.route('/')
def landing():
    return render_template('landing.html')

# ---------------- QUESTIONNAIRE PAGE ---------------- #
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        new_mentor = Mentor(
            full_name=request.form['full_name'],
            display_name=request.form['display_name'],
            institution=request.form['institution'],
            gender=request.form['gender'],
            education=request.form['education'],
            field=request.form['field'],
            career_stage=request.form['career_stage'],
            bio=request.form['bio'],
            resume=request.form['resume'],
            personality=request.form['personality'],
            hobbies=request.form['hobbies'],
            tone=request.form['tone'],
            mascot=request.form['mascot']
        )
        db.session.add(new_mentor)
        db.session.commit()

        return redirect('/network')

    return render_template('questionnaire.html')

import random


import aiohttp

async def send_query_to_linkd(query):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://search.linkd.inc/api/search/users",
                headers={"Authorization": "Bearer lk_f5376bd6583e4519bcd14c6299d5d24c"},
                params={"query": query},
                ssl=False
            ) as resp:
                if resp.status != 200:
                    return [], 0

                data = await resp.json()

                results = data.get("results", [])[:4]
                total = data.get("total", 0)

                # Parse the results
                parsed_results = []
                for result in results:
                    profile = result.get("profile", {})
                    experience = result.get("experience", [{}])[0]
                    education = result.get("education", [{}])[0]

                    selected_image = random.choice(['chai-latte.png', 'cold-brew.png', 'espresso.png', 'latte.png', 'matcha.png'])
                    profile_picture_url = f"/static/{selected_image}"

                    # Prepare parsed result for display
                    parsed_result = {
                        "all": profile,
                        "display_name": profile.get("name", "No name"),
                        "institution": experience.get("company_name", "No company"),
                        "school": education.get("school_name", "No school"),
                        "field": profile.get("headline", "No field"),
                        "profile_picture_url": profile_picture_url
                    }

                    parsed_results.append(parsed_result)
                    
                    # Add mentor data to the database
                    new_mentor = Mentor(
                        full_name=profile.get("name", "No name"),
                        display_name=profile.get("name", "No name"),
                        institution=experience.get("company_name", "No company"),
                        field=profile.get("title", "No field"),
                        bio=profile.get("experience", " "),
                        personality=profile.get("description", "Unknown"),
                        hobbies=profile.get("hobbies", "Unknown"),
                        tone=profile.get("tone", "Friendly"),
                        mascot=profile_picture_url 
                    )

                    # Save the new mentor to the database
                    db.session.add(new_mentor)
                    db.session.commit()

                # Return the parsed results and the total count
                return parsed_results, total
    except Exception as e:
        print(f"Error fetching mentor data: {e}")
        return [], 0

    
# Routes for the Linkd Search functionality (App 1)
@app.route("/network", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        loop = asyncio.new_event_loop()  # Create a new event loop for the async function
        asyncio.set_event_loop(loop)
        results, total = loop.run_until_complete(send_query_to_linkd(query))
        return render_template("network.html", query=query, results=results, total=total, mentors=Mentor.query.all())
    return render_template("network.html", query=None, results=None, total=None, mentors=Mentor.query.all())



# ---------------- CHAT PAGE ---------------- #
@app.route('/chat/<int:mentor_id>', methods=['GET', 'POST'])
def chat(mentor_id):
    mentor = Mentor.query.get_or_404(mentor_id)

    if str(mentor_id) not in session:
        session[str(mentor_id)] = []

        # First system prompt
        intro_prompt = {
            "role": "user",
            "content": f"""
            You are a personalized AI mentor:
            - Name: {mentor.display_name}
            - Field: {mentor.field}
            - Bio: {mentor.bio}
            - Personality: {mentor.personality}
            - Hobbies: {mentor.hobbies}
            Speak with a {mentor.tone} tone.
            NEVER share private information. Respond like a real mentor version of {mentor.display_name}. Do not share any information about yourself, unless asked to do so. Do not give an output in Markdown. Talk normally. Do not talk about the tone you are using. 
            """
        }
        session[str(mentor_id)].append(intro_prompt)

        # Friendly welcome message
        welcome_message = {
            "role": "assistant",
            "content": f"Hey there! 👋 I'm {mentor.display_name} from {mentor.institution}. I'm your AI mentor, excited to help you with anything you need!"
        }
        session[str(mentor_id)].append(welcome_message)

    if request.method == 'POST':
        user_message = request.form['message']
        session[str(mentor_id)].append({"role": "user", "content": user_message})

        url = "https://api.asi1.ai/v1/chat/completions"
        payload = {
            "model": "asi1-mini",
            "messages": session[str(mentor_id)],
            "temperature": 0.7,
            "stream": False,
            "max_tokens": 500
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {ASI_API_KEY}'
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        assistant_reply = data.get('choices', [{}])[0].get('message', {}).get('content', 'No response')
        session[str(mentor_id)].append({"role": "assistant", "content": assistant_reply})

    return render_template('chat.html', messages=session[str(mentor_id)], name=mentor.display_name)

# ---------------- RESET PAGE ---------------- #
@app.route('/reset/<int:mentor_id>')
def reset_mentor_chat(mentor_id):
    session.pop(str(mentor_id), None)
    return redirect(f'/chat/{mentor_id}')

# ---------------- NETWORK PAGE ---------------- #
@app.route('/network')
def network():
    mentors = Mentor.query.all()
    return render_template('network.html', mentors=mentors)

# ---------------- MAIN ---------------- #
if __name__ == '__main__':
    app.run(debug=True, port=5001)