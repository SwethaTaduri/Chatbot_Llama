import random

import requests
import streamlit as st


def fetch_responses(prompt):
    url = "https://8714-35-197-2-152.ngrok-free.app/llm_response"
    data = {"prompt": prompt}
    response = requests.post(url, json=data)
    return response.json()

def main():
    st.title("TCGA Report Analyzer - LLaMA-2")

    prompt = st.text_input("Enter a prompt:")

    if st.button("Analyse using LLM"):
        if prompt:
            with st.spinner("Fetching responses..."):
                responses = fetch_responses(prompt)
            st.subheader('Without-Index Response :')
            st.write("Response without index:", responses["response_without_index"])
            st.subheader('With-Index Response :')
            st.write("Response with index:", responses["response_with_index"])
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
