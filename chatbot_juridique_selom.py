import streamlit as st
import os
from openai import OpenAI, OpenAIError

# Clé API via variable d’environnement uniquement
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("❌ Clé API OpenAI manquante. Définissez-la comme variable d’environnement.")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

st.title("⚖️ Chatbot Juridique Selom")

question = st.text_area("Posez votre question juridique :")
langue = st.selectbox("Langue :", ["fr", "en"])

def obtenir_reponse(question, langue="fr"):
    prompt = (
        "Tu es un assistant juridique spécialisé en droit des contrats et droit informatique. "
        f"Réponds uniquement en {langue}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"Erreur OpenAI : {str(e)}"

if st.button("Envoyer"):
    if question.strip():
        reponse = obtenir_reponse(question, langue)
        st.write(reponse)
    else:
        st.warning("Veuillez poser une question.")
