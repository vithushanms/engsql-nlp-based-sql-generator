'''
Filename: model.py
Created Date: Friday, April 7th 2023, 1:59:59 am
Author: Vithushan Sylvester

Copyright (c) 2023 Vithushan Sylvester
'''

import json
import openai
from gpt import GPT,Example
from dotenv import load_dotenv
import os

load_dotenv()

#method to initialize the model
def model(dbContext):
    openai.api_key = os.getenv("API_KEY")
    #davinci
    gpt = GPT(engine="text-davinci-003",
            temperature=0.5,
            max_tokens=100)
    # Read the table names from the .env file
    table_names_str = os.getenv("TABLE_NAMES")

    # Split the table names into a list
    table_names = table_names_str.split(',')

    # Train the model with each table
    for table_name in table_names:
        gpt = train_from_db(gpt, dbContext, table_name.strip())

    return gpt

#method to train the model with the examples
def train_from_db(gpt, db_context, table_name):
    cursor = db_context.connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
    columns = cursor.fetchall()

    example_prompt = f"Fetch all columns from the {table_name} table."
    example_query = f"SELECT * FROM {table_name};"
    gpt.add_example(Example(example_prompt, example_query))

    for column in columns:
        print("training.....")
        column_name = column[0]
        example_prompt = f"Fetch the {column_name} column from the {table_name} table."
        example_query = f"SELECT {column_name} FROM {table_name};"
        gpt.add_example(Example(example_prompt, example_query))
    
    return gpt

#method to get the predicted query from the model
def get_predicted_query(gpt, prompt):
    response = gpt.submit_request(prompt)
    if response['choices']:
        query = response['choices'][0]['text'].strip()
        return query
    else:
        return "No query generated."

