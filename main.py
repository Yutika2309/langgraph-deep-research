from fastapi import FastAPI
from utils import graph

app = FastAPI()


@app.post('/chat')
def post_query(user_query: str) -> str:
    """
    endpoint for chat
    """
    state = graph.invoke({"messages": [{"role": "user", "content": user_query}]})
    return state["messages"][-1].content