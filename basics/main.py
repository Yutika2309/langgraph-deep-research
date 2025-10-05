from fastapi import FastAPI
from basics.utils import graph

app = FastAPI()


@app.post('/chat')
def run_chatbot(user_query:str):
    state = {"messages": [], "message_type": None}
    state["messages"] = state.get("messages", []) + [
        {"role":"user", "content": user_query}
    ]
    state = graph.invoke(state)

    if state.get("messages") and len(state["messages"]) > 0:
        last_message = state["messages"][-1]
        print("State of this message:".upper(), state.get("message_type"), "\n")
        return last_message.content

# @app.post('/chat')
# def post_query(user_query: str) -> str:
#     """
#     endpoint for chat
#     """
#     state = graph.invoke({"messages": [{"role": "user", "content": user_query}]})
#     print("ALL_MESSAGES:", state["messages"])
#     return state["messages"][-1].content