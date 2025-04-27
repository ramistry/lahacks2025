from flask import Flask, render_template, request
import aiohttp
import asyncio

app = Flask(__name__)

# Function to send the query to Linkd API
async def send_query_to_linkd(query):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://search.linkd.inc/api/search/users",
                headers={"Authorization": "Bearer lk_f5376bd6583e4519bcd14c6299d5d24c"},
                params={"query": query},
                ssl=False  # <-- IMPORTANT: to fix SSL error
            ) as resp:
                if resp.status != 200:
                    return f"Error: Linkd API failed with status: {resp.status}"

                data = await resp.json()
                results = data.get("results", [])
                total = data.get("total", 0)

                return results, total

    except Exception as e:
        return f"Exception during search: {e}"

# Flask route to render the homepage and handle form submission
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        loop = asyncio.new_event_loop()  # Create a new event loop for the async function
        asyncio.set_event_loop(loop)
        results, total = loop.run_until_complete(send_query_to_linkd(query))
        return render_template("index.html", query=query, results=results, total=total)
    return render_template("index.html", query=None, results=None, total=None)

if __name__ == "__main__":
    app.run(debug=True)
