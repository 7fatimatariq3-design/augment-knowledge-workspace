"""
Milestone 3: Wrapper around OpenAI / OpenRouter chat completion API.
"""
from app.core.config import settings


def build_rag_prompt(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    return (
        "Answer the question using only the context below. "
        "If the answer isn't in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )


def call_llm(prompt: str) -> str:
    # TODO: call OpenAI/OpenRouter chat completion endpoint using settings.OPENROUTER_API_KEY
    raise NotImplementedError("Implement in Milestone 3")
