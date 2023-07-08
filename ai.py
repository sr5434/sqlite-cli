import os
import openai

openai.api_key = os.environ["OPENAI_KEY"]

def text2sql(prompt):
    """Returns a SQLite command for the given prompt."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Return an appropriate SQLite command for what the user wants to do. Only return the command."}, 
                  {"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]
