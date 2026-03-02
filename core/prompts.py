from typing import Literal


Platform = Literal["Instagram", "LinkedIn", "Facebook", "Blog", "E-mail"]
Tone = Literal["Normal", "Informativo", "Inspirador", "Urgente", "Informal"]
Length = Literal["Curto", "Médio", "Longo"]


def build_marketing_prompt(
    topic: str,
    platform: Platform,
    tone: Tone,
    length: Length
) -> str:
    return f"""
Você é um especialista em marketing digital estratégico.

Crie um conteúdo com as seguintes características:

Tema: {topic}
Plataforma: {platform}
Tom: {tone}
Tamanho: {length}

O conteúdo deve:
- Ser estratégico
- Adaptado ao público da plataforma
- Ter clareza e persuasão
- Incluir call-to-action quando apropriado
"""