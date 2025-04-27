from uagents import Agent, Context
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    results: list
    total: int
    query: str

query_agent = Agent(
    name="query_sender",
    seed="query_sender_secret",
    port=8001,
    endpoint=["http://localhost:8001/submit"]
)

@query_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Sending query to Linkd Search Agent...")
    # Send the query using send_message() method
    await query_agent.send_message(
        "linkd_search_agent",  # Target agent name (ensure this matches the linkd_search_agent name)
        QueryRequest(query="People working on AI at FAANG")
    )

@query_agent.on_message(model=QueryResponse)
async def handle_response(ctx: Context, sender: str, response: QueryResponse):
    ctx.logger.info(f"Received response from {sender}:")
    ctx.logger.info(f"Total Results: {response.total}")
    ctx.logger.info(f"First Result Example: {response.results[0] if response.results else 'No results found'}")

# Run the query_agent
if __name__ == "__main__":
    query_agent.run()
