import os
import openai
import streamlit as st



def grade_essay(essay):
    completions = openai.Completion.create(
        engine="text-davinci-002",
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
