from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "The Interrelations of Finance and Economics: Theoretical Perspectives : https://www.jstor.org/stable/1805425",
        "A new mutation operator for real coded genetic algorithms",
        "Landslide susceptibility mapping & prediction using Support Vector Machine for Mandakini River Basin, Garhwal Himalaya, India",
        "Dynamical analysis of a prey–predator model with Beddington–DeAngelis type function response incorporating a prey refuge"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

template = load_prompt("template.json")

if st.button("Summarize"):
    chain = template | llm

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)