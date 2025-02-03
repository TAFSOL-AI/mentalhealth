import json
import faiss
import numpy as np
import ollama
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ.get("OPEN_API_KEY")

client = OpenAI(
    api_key= key
)



def search_faiss(user_number, query: str, top_k: int = 5,):
    index = faiss.read_index(f"{user_number}_Faiss.bin")
    with open(f"{user_number}_metadata.json", "r") as f:
        metadata = json.load(f)


    response = ollama.embeddings(model="nomic-embed-text", prompt=query)

    
    query_embedding = response["embedding"]
    query_vector = np.array(query_embedding).reshape(1, -1)
    distances, indices =index.search(query_vector, top_k)
    results = [metadata[i] for i in indices[0]]
    return results

def startChat(summary):
    
    system_prompt = f"""You are a helpful AI Mental Health Wellness Advisor. Your goal is to provide user with full Mental Health
                    Advise in a conversational way. Here is the User summary: {summary}
                    -The summary provided is of a previous session
                    -This is a new session, therefore user summary is of the past, now in the present you have to advise.
                    -Also Try as much as you can to make a brief and small 
                    -Start by greeting user by his/her name.
                    -Ask first 2 - 3 questions related to the user summary just to get the user comfortable.
                    -Ask one question at a time.
                    -Start Advising the user after evaluating his/her mental health problems.
                    """
    messages = []
    messages.append({"role":"system", "content": system_prompt})

    while True:
        print("\n\n*****************************************************************")
        print("\nHello! I am your AI mental health advisor.\n")
        user_prompt = input("\nYOU: ")
        messages.append({"role":"user", "content": user_prompt})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        bot_response = response.choices[0].message.content

        print(f"\nBOT: {bot_response}")
