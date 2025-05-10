
import streamlit as st
import os
from openai import OpenAI

OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="Chatbot Juridique Selom", layout="centered")
st.title("⚖️ Chatbot Juridique – Maître SELOM")
st.markdown("Posez votre question sur le droit des contrats ou droit informatique.")

langue = st.selectbox("Choisissez la langue de réponse :", ["fr", "en"])
question = st.text_area("Votre question juridique :", height=150)

def obtenir_reponse(question, langue="fr"):
    prompt_systeme = (
        "Tu es un assistant juridique expert en droit des contrats et droit informatique."
        " Donne des réponses fiables, claires, synthétiques et adaptées à un non-juriste."
        f" Réponds uniquement en {langue}."
    )
    try:
        reponse = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_systeme},
                {"role": "user", "content": question}
            ]
        )
        return reponse.choices[0].message.content
    except Exception as e:
        return f"⚠️ Erreur lors de la génération : {str(e)}"

if st.button("Obtenir une réponse"):
    if question.strip():
        with st.spinner("Analyse juridique en cours..."):
            reponse = obtenir_reponse(question, langue)
            st.success("Réponse du chatbot :")
            st.markdown(reponse)
    else:
        st.warning("❗ Veuillez entrer une question.")

st.markdown("---")
st.caption("Développé pour Maître SELOM Yves Rowland – Juriste / Legal Counsel")
