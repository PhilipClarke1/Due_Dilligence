import streamlit as st
import pandas as pd
from llm_utils import query_openai, query_claude
from data_ingestion import load_financials, fetch_news
from compare_models import compare
import matplotlib.pyplot as plt

st.title("📊 DueDiligenceAI: Generative Analytics for Investment Intelligence")

tab1, tab2, tab3 = st.tabs(["📄 Financial Upload", "📰 News Risk Scan", "🤖 LLM Benchmarking"])

with tab1:
    file = st.file_uploader("Upload a structured company dataset (.csv)")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df.head(), use_container_width=True)
        summary = query_openai(f"Summarize this dataset:\n{df.head(20).to_string()}")
        st.subheader("🧠 OpenAI Summary of Financial Insights")
        st.write(summary)

        st.subheader("📊 Revenue Distribution")
        fig1, ax1 = plt.subplots()
        df.plot(kind='bar', x='Company', y='Revenue ($M)', ax=ax1, color='skyblue', legend=False)
        ax1.set_ylabel("Revenue ($M)")
        ax1.set_xlabel("")
        ax1.set_title("Revenue by Company")
        st.pyplot(fig1)

        st.subheader("💰 Profit Margin Overview")
        fig2, ax2 = plt.subplots()
        df.plot(kind='bar', x='Company', y='Profit ($M)', ax=ax2, color='lightgreen', legend=False)
        ax2.set_ylabel("Profit ($M)")
        ax2.set_xlabel("")
        ax2.set_title("Profit by Company")
        st.pyplot(fig2)

        st.subheader("📈 Year-over-Year Growth Trajectory")
        fig3, ax3 = plt.subplots()
        df.plot(kind='line', x='Company', y='YOY Growth (%)', marker='o', ax=ax3, color='orange', legend=False)
        ax3.set_ylabel("YOY Growth (%)")
        ax3.set_title("Growth Trends by Company")
        st.pyplot(fig3)

with tab2:
    url = st.text_input("Enter the URL of a relevant news article")
    if url:
        article = fetch_news(url)
        summary = query_claude(f"Summarize this news item and highlight potential risk factors:\n{article}")
        st.subheader("🧾 Claude Risk Summary")
        st.write(summary)

with tab3:
    user_input = st.text_area("Input structured data or context to evaluate across models")
    if user_input:
        results = compare(user_input)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔷 OpenAI (GPT-4o)")
            st.write(results["OpenAI"])

        with col2:
            st.subheader("🔶 Claude (Opus)")
            st.write(results["Claude"])
