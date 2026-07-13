"""
Milestone 3: Basic RAG pipeline.

Indexing phase:
    document text -> chunk -> embed -> store in vector index

Query phase:
    user question -> embed -> similarity search -> top-k chunks -> build prompt -> LLM
"""


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    # TODO: implement chunking strategy
    raise NotImplementedError


def index_document(document_id: int, text: str):
    # TODO: chunk, embed, store vectors (e.g. pgvector table or FAISS index)
    raise NotImplementedError


def retrieve_relevant_chunks(query: str, top_k: int = 4):
    # TODO: embed query, run similarity search, return top-k chunks
    raise NotImplementedError
