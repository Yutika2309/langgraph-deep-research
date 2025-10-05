# Langgraph based Deep Research

My attempt at replicating a langgraph-based deep research multi-agent architecture

To install using UV
    
    pip install uv

    # initiate creation of env
    uv init . 

    # activate the env
    source .venv/bin/activate

    uv add <package-name>

To run the code for basic agents

    cd basics

    uvicorn main:app --reload