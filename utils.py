from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


load_dotenv()


# you can load any model of your choice, i decided to go with an open-source model
llm = init_chat_model(
        "groq:llama-3.1-8b-instant"
)

class State(TypedDict):
    '''
    messages are going to be of type list and will be collected using add_messages func
    '''
    messages: Annotated[list, add_messages] 


# instantiating the message graph
graph_builder = StateGraph(State)


# nodes
def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

# building the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()




