import random
import asyncio
from flask import Flask, render_template, request, jsonify
import aiohttp

app = Flask(__name__)

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

                # Parse and return results
                parsed_results = []
                for result in results:
                    profile = result.get("profile", {})
                    experience = result.get("experience", [{}])[0]
                    education = result.get("education", [{}])[0]

                    selected_image = random.choice(['chai-latte.png', 'cold-brew.png', 'espresso.png', 'latte.png', 'matcha.png'])
                    profile_picture_url = f"/static/{selected_image}"

                    parsed_results.append({
                        "display_name": profile.get("name", "No name"),
                        "institution": experience.get("company_name", "No company"),
                        "school": education.get("school_name", "No school"),
                        "field": profile.get("headline", "No field"),
                        "profile_picture_url": profile_picture_url
                    })
                
                return parsed_results, total
    except Exception as e:
        print(f"Error fetching mentor data: {e}")
        return [], 0


# Create a Flask route that will call send_query_to_linkd and return results
@app.route('/search_mentor', methods=['GET'])
async def search_mentor():
    query = request.args.get('query', '')
    if query:
        results, total = await send_query_to_linkd(query)
        return render_template('mentor_results.html', results=results, total=total)
    return render_template('mentor_search.html')


# Flask route for displaying the search form
@app.route('/')
def index():
    return render_template('mentor_search.html')


if __name__ == '__main__':
    app.run(debug=True)
