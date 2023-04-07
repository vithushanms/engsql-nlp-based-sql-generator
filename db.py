'''
Filename: db.py
Created Date: Friday, April 7th 2023, 1:59:59 am
Author: Vithushan Sylvester

Copyright (c) 2023 Vithushan Sylvester
'''

import psycopg2
import re
from dotenv import load_dotenv
import os

load_dotenv()

class DB_CONTEXT:
    def __init__(self):
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        self.connection = connection

    #execute queries in the current db context
    def cursor(self, query):
        # Create a cursor object
        cursor = self.connection.cursor()
        query = self.querybuilder(query)
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()

    def querybuilder(self,sql_query):
        def add_quotes(match):
            return f'"{match.group(1)}"'

        pattern = r'\b(AI[a-zA-Z0-9_]*)\b'
        formatted_sql_query = re.sub(pattern, add_quotes, sql_query)
        formatted_sql_query = formatted_sql_query.replace('" "', ' ')  # Remove the extra double quotes between the double quotes
        return formatted_sql_query


    

