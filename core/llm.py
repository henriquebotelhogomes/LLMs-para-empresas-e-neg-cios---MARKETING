from langchain_groq import ChatGroq
from config.settings import settings


def get_llm() -> ChatGroq:
    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY não configurada.")

    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE
    )