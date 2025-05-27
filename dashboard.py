import streamlit as st
import pandas as pd
from llm_utils import query_openai, query_claude
from data_ingestion import load_financials, fetch_news
from compare_models import compare

st.title("DueDiligenceAI Dashboard")

option = st.radio("Choose analysis type:", ["Upload CSV", "Fetch News", "Compare Models"])

if option == "Upload CSV":
    file = st.file_uploader("Upload a CSV file")
    if file:
        df = pd.read_csv(file)
        st.write(df.head())
        summary = query_openai(f"Summarize this data:\n{df.head(20).to_string()}")
        st.subheader("LLM Summary")
        st.write(summary)

elif option == "Fetch News":
    url = st.text_input("Paste news article URL")
    if url:
        article = fetch_news(url)
        summary = query_claude(f"Summarize this news for risk or red flags:\n{article}")
        st.subheader("Claude Summary")
        st.write(summary)

elif option == "Compare Models":
    user_input = st.text_area("Enter text or paste structured data")
    if user_input:
        results = compare(user_input)
        st.subheader("OpenAI Output")
        st.write(results["OpenAI"])
        st.subheader("Claude Output")
        st.write(results["Claude"])