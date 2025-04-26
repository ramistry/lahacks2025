from flask import Flask, request, render_template, redirect
import requests
import json

app = Flask(__name__)

# ⚡ Replace with your real ASI API key
ASI_API_KEY = "sk_5e8dbfb687c84cc0b32ca1ef309e329d6e49084d44aa4c61a9a1bc5fbd92064f"

# ⚡ SERVER-SIDE MEMORY
chat_state = {
    "is_mentor": None,
    "full_name": None,
    "display_name": None,
    "gender": None,
    "education": None,
    "field": None,
    "career_stage": None,
    "resume": None,
    "bio": None,
    "personality": None,
    "hobbies": None,
    "tone": None,
    "messages": []
}

# ✅ GLOBAL LIST to store mentors
mentors = []

# ---------------- LANDING PAGE ---------------- #
@app.route('/')
def landing():
    return render_template('landing.html')

# ---------------- QUESTIONNAIRE PAGE ---------------- #
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # Save user input to chat_state
        chat_state["is_mentor"] = request.form['is_mentor']
        chat_state["full_name"] = request.form['full_name']
        chat_state["display_name"] = request.form['display_name']
        chat_state["gender"] = request.form['gender']
        chat_state["education"] = request.form['education']
        chat_state["field"] = request.form['field']
        chat_state["career_stage"] = request.form['career_stage']
        chat_state["resume"] = request.form['resume']
        chat_state["bio"] = request.form['bio']
        chat_state["personality"] = request.form['personality']
        chat_state["hobbies"] = request.form['hobbies']
        chat_state["tone"] = request.form['tone']
        chat_state["messages"] = []

        # ✅ Save new mentor to list
        new_mentor = {
            "id": len(mentors) + 1,
            "name": chat_state["display_name"],
            "field": chat_state["field"],
            "bio": chat_state["bio"],
            "resume": chat_state["resume"],
            "personality": chat_state["personality"],
            "hobbies": chat_state["hobbies"],
            "tone": chat_state["tone"]
        }
        mentors.append(new_mentor)

        return redirect('/network')

    return render_template('questionnaire.html')

# ---------------- CHAT PAGE ---------------- #
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if not chat_state["full_name"] or not chat_state["resume"]:
        return redirect('/questionnaire')

    response_text = None

    # ✅ ONLY 1 SYSTEM MESSAGE on new session
    if len(chat_state["messages"]) == 0:
        intro_message = {
            "role": "user",
            "content": f"""
You are an AI mentor named {chat_state['display_name']}.
- Field: {chat_state['field']}
- Bio: {chat_state['bio']}
- Personality: {chat_state['personality']}
- Tone: {chat_state['tone']}
- Hobbies: {chat_state['hobbies']}
- Resume: {chat_state['resume']}

✅ Start by introducing yourself in ONLY ONE short paragraph in a friendly tone.
❌ DO NOT repeat your introduction.
❌ DO NOT mention your name twice.
✅ After your single intro, wait for the user's questions.
"""
        }
        chat_state["messages"].append(intro_message)

    if request.method == 'POST':
        user_message = request.form['message']
        chat_state["messages"].append({"role": "user", "content": user_message})

        url = "https://api.asi1.ai/v1/chat/completions"

        payload = {
            "model": "asi1-mini",
            "messages": chat_state["messages"],
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

        chat_state["messages"].append({"role": "assistant", "content": assistant_reply})

        response_text = assistant_reply

    return render_template('chat.html', messages=chat_state["messages"], response_text=response_text, name=chat_state["display_name"])

# ---------------- RESET PAGE ---------------- #
@app.route('/reset')
def reset():
    for key in chat_state.keys():
        chat_state[key] = None if key != "messages" else []
    return redirect('/questionnaire')

# ---------------- NETWORK PAGE ---------------- #
@app.route('/network')
def network():
    return render_template('network.html', mentors=mentors)

# ---------------- MAIN ---------------- #
if __name__ == '__main__':
    app.run(debug=True, port=5000)
