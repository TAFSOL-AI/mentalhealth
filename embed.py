import json
import numpy as np
import ollama
import faiss



def add_to_faiss(data, user_number):
    dimensions = 768
    index = faiss.IndexFlatL2(dimensions)
    metadata = []
    response = ollama.embeddings(model="nomic-embed-text", prompt=data)
    embedding = response['embedding']
    embedding_vector = np.array(embedding).reshape(1, -1)
    index.add(embedding_vector)
    metadata.append(data)

    faiss.write_index(index, f"Mental_Health_Advisor\\{user_number}_Faiss.bin")
    with open(f"Mental_Health_Advisor\\{user_number}_metadata.json", "w") as f:
        json.dump(metadata, f)