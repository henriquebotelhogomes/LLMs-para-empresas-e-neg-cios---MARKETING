import streamlit as st
from core.agent import MarketingAgent

st.set_page_config(page_title="AI Marketing Assistant", layout="centered")

st.title("🤖 AI Marketing Assistant")
st.markdown("Geração estratégica de conteúdo com Inteligência Artificial")

topic = st.text_input("Tema do conteúdo")

platform = st.selectbox(
    "Plataforma",
    ["Instagram", "LinkedIn", "Facebook", "Blog", "E-mail"]
)

tone = st.selectbox(
    "Tom",
    ["Normal", "Informativo", "Inspirador", "Urgente", "Informal"]
)

length = st.selectbox(
    "Tamanho",
    ["Curto", "Médio", "Longo"]
)

if st.button("Gerar Conteúdo"):

    if not topic:
        st.warning("Informe um tema.")
    else:
        with st.spinner("Gerando conteúdo..."):
            agent = MarketingAgent()
            result = agent.generate(topic, platform, tone, length)

        st.markdown("### Resultado")
        st.write(result)