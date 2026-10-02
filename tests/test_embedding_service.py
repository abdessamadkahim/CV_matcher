from app.services.embedding_service import create_embedding


def test_create_embedding():

    text = "Machine Learning"

    embedding = create_embedding(text)

    print("\n========== EMBEDDING ==========")
    print("Texte :", text)
    print("Nombre de dimensions :", len(embedding))
    print("Premiers nombres :", embedding[:10])

    assert len(embedding) > 0