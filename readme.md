Author: vithushan sylvester <vsylvester@mitrai.com>

# GPT-based SQL Generation API

This application uses a GPT model to generate SQL queries based on natural language prompts. The application is built using FastAPI and serves a single endpoint for submitting prompts and receiving generated SQL queries.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI
- Gradio
- PostgreSQL database
- psycopg2

## Pre-requisites

Before running the application, ensure you have a running PostgreSQL database instance with the necessary tables and data.

1. Set up a PostgreSQL database and create tables with sample data.
2. Configure the connection details in the .env file.
3. Update the table_names list in the .env file to include the table names to train the model.
   Now, the application is ready to generate SQL queries based on your database tables and columns.

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
```

```
cd your_repository
```

2. Create a virtual environment (optional, but recommended):

```
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```
.\venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. add your key to OpenAI secret model.py file

6. Get an OpenAI API key by signing up for an account on the OpenAI website. After signing up, you can find your API key in the API Keys section of your account.

7. Add your OpenAI API key to the .env file.

8. Set up the PostgreSQL database and configure the connection details in the .env file.

## Running the Application

1. Start the FastAPI server:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Access the Swagger UI for testing the API in your browser:
   `http://127.0.0.1:8000/docs`

3. Send a POST request to the `/generate_sql_query/` endpoint with a JSON payload containing the prompt text:

```
curl -X POST "http://127.0.0.1:8000/generate_sql_query/" -H "accept: application/json" -H "Content-Type: application/json" -d "{"text":"what is the total salary paid to employees?"}"
```

4. The API will return a JSON object containing the generated SQL query.

# Gradio UI

Run the Gradio UI:

```
python gradio_ui.py
```

Access the Gradio UI via your browser and start generating SQL queries with natural language prompts.
