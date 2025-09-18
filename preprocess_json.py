import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

# Embedding Function
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json = {
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"]
    return embedding

# Listing Files
jsons = os.listdir("jsons")                   # List all the jsons
my_dicts = []
chunk_id = 0

# Processing Each File
for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating embeddings for {json_file}")
    # Creating Embeddings for All Chunks
    embeddings = create_embedding([c["text"] for c in content["chunks"]])
    
    # Attaching Embeddings & Chunk IDs
    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        # if(i==3):               # Read only 3 chunks
        #     break
#print(my_dicts)

# Convert to DataFrame
df = pd.DataFrame.from_records(my_dicts)

# Save this Dataframe
joblib.dump(df , "embeddings.joblib")


    



