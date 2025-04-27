from uagents import Agent, Context, Model
from pydantic import BaseModel
import aiohttp


class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    results: list
    total: int
    query: str



linkd_search_agent = Agent(
    name="linkd_search_agent",
    seed="linkd_search_agent_secret",
    port=8000,
    endpoint=["http://localhost:8000/submit"]
)



@linkd_search_agent.on_message(model=QueryRequest)
async def handle_query(ctx: Context, sender: str, query: QueryRequest):
    ctx.logger.info(f"Received search query: {query.query}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://search.linkd.inc/api/search/users",
                headers={"Authorization": "Bearer lk_f5376bd6583e4519bcd14c6299d5d24c"},
                params={"query": query.query},
                ssl=False  # <-- IMPORTANT: to fix SSL error
            ) as resp:
                if resp.status != 200:
                    ctx.logger.error(f"Linkd API failed with status: {resp.status}")
                    return

                data = await resp.json()

                results = data.get("results", [])
                total = data.get("total", 0)

                ctx.logger.info(f"Sending {total} results back to {sender}")
                await ctx.send(sender, QueryResponse(results=results, total=total, query=query.query))

    except Exception as e:
        ctx.logger.error(f"Exception during search: {e}")



if __name__ == "__main__":
    linkd_search_agent.run()
