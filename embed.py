import json
import numpy as np
from advisor import getData
import ollama
import faiss
dimensions = 768
index = faiss.IndexFlatL2(dimensions)
metadata = []

data = getData()
response = ollama.embeddings(model="nomic-embed-text", prompt=data)
embedding = response['embedding']
embedding_vector = np.array(embedding).reshape(1, -1)
index.add(embedding_vector)
metadata.append(data)

faiss.write_index(index, "Mental_Health_Advisor\\faiss_MH.bin")
with open("Mental_Health_Advisor\\metadata.json", "w") as f:
    json.dump(metadata, f)

