from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PyPDF2 import PdfReader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt

# Load Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

st.title("📚 AI Research Paper Summarizer")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a Research Paper (PDF)",
    type=["pdf"]
)

# Explanation Style
style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

# Explanation Length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed Explanation)"
    ]
)

# Load Prompt Template
template = load_prompt("template1.json")

# If PDF uploaded
if uploaded_file is not None:

    st.success("✅ PDF uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    paper_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            paper_text += text

    st.write(f"**Total Pages:** {len(reader.pages)}")
    st.write(f"**Characters Extracted:** {len(paper_text)}")

    if st.button("Summarize"):

        with st.spinner("Generating Summary..."):

            chain = template | llm

            result = chain.invoke({
                "paper_text": paper_text,
                "style_input": style_input,
                "length_input": length_input
            })

        st.subheader("📄 Summary")
        st.write(result.content)