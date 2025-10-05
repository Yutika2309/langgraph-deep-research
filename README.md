To install using UV
    
    pip install uv

    # initiate creation of env
    uv init . 

    # activate the env
    source .venv/bin/activate
    
    uv add <package-name>

To run the code

    

    cd basics

    uvicorn main:app --reload