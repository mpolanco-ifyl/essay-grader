import os
import openai
import streamlit as st

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


def grade_essay(essay):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Please grade the following essay on a scale of 1-10: {essay}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message

st.title("Essay Grader")

essay = st.text_area("Enter your essay")

if st.button("Grade"):
    result = grade_essay(essay)
    st.success(result)
