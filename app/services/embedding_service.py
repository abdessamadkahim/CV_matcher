from sentence_transformers import SentenceTransformer
import numpy as np
MODEL_NAME="all-MiniLM-L6-v2"
model =SentenceTransformer(MODEL_NAME)
def create_embedding(text:str)->list[float]:
  if not text.strip:
    return []
  embedding=model.encode(text)
  return embedding.tolist()




