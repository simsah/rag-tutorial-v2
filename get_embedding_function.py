from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    print("Initializing embeddings...")
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        print("Embeddings initialized successfully.")
        return embeddings
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function
get_embedding_function()
