from core.llm import get_llm
from core.prompts import build_marketing_prompt


class MarketingAgent:
    """
    Agente responsável por gerar conteúdo estratégico de marketing
    utilizando LLMs.
    """

    def __init__(self):
        self.llm = get_llm()

    def generate(
        self,
        topic: str,
        platform: str,
        tone: str,
        length: str
    ) -> str:

        prompt = build_marketing_prompt(topic, platform, tone, length)

        response = self.llm.invoke(prompt)

        return response.content