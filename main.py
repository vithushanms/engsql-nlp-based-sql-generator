'''
Filename: main.py
Created Date: Friday, April 7th 2023, 1:59:59 am
Author: Vithushan Sylvester

Copyright (c) 2023 Vithushan Sylvester
'''

from fastapi import FastAPI
from pydantic import BaseModel
from model import model, get_predicted_query, train_from_db
from db import DB_CONTEXT

app = FastAPI()

class Prompt(BaseModel):
    text: str

dbContext = DB_CONTEXT()
gpt = model(dbContext)

@app.post("/generate_sql_query/")
async def generate_sql_query(prompt: Prompt):
    print(f"prompt: {prompt}")
    sql_query = get_predicted_query(gpt, prompt.text)
    return {"sql_query": sql_query}

@app.post("/get_result/")
async def generate_sql_query(prompt: Prompt):
    print(f"prompt: {prompt}")
    sql_query = dbContext.cursor(prompt.text)
    return {"sql_query": sql_query}

@app.post("/execute_first_query/")
async def execute_first_query(prompt: Prompt):
    print(f"prompt: {prompt}")
    sql_query = get_predicted_query(gpt, prompt.text)
    queries = sql_query.split("\n")
    first_query = None
    for query in queries:
        if query.startswith("A:"):
            first_query = query[3:].strip()
            break

    if first_query:
        try:
            result = dbContext.cursor(first_query)
            return {"result": result}
        except Exception as e:
            dbContext.connection.rollback()
            return {"error": str(e)}
    else:
        return {"error": "No query found in the response"}
