import json
import os
import chromadb
from chromadb.utils import embedding_functions

from src.config import CHROMA_DB_PATH, COLLECTION_NAME

# Default embedding model
embedding_function = embedding_functions.DefaultEmbeddingFunction()


def get_collection():
    """
    Create (or load) the ChromaDB collection.
    """
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    return collection


def populate_database(json_path="data/sports_facts.json"):
    """
    Read sports facts from JSON and insert them into ChromaDB.
    This runs only once.
    """

    collection = get_collection()

    # Avoid duplicate inserts
    if collection.count() > 0:
        print(f"Database already contains {collection.count()} documents.")
        return

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"{json_path} not found")

    with open(json_path, "r", encoding="utf-8") as f:
        facts = json.load(f)

    documents = []
    metadatas = []
    ids = []

    for i, item in enumerate(facts):
        documents.append(item["fact"])

        metadatas.append({
            "sport": item["sport"]
        })

        ids.append(f"fact_{i}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Inserted {len(documents)} facts successfully.")


def search_historical_facts(sport, query, n_results=3):
    """
    Retrieve relevant historical facts from ChromaDB.
    """

    collection = get_collection()

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={
            "sport": sport
        }
    )

    return results.get("documents", [[]])[0]


if __name__ == "__main__":
    populate_database()

    print("\nTesting retrieval...\n")

    docs = search_historical_facts(
        sport="Cricket",
        query="World Cup history"
    )

    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc}")