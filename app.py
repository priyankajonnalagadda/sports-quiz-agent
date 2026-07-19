import streamlit as st
from src.generator import generate_quiz

st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI-Powered Sports Quiz Generator")

st.write(
    "Generate quizzes using historical sports facts "
    "and the latest sports news."
)

sport = st.selectbox(
    "Select Sport",
    [
        "Cricket",
        "Football",
        "Tennis",
        "Basketball",
        "Badminton"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

if st.button("Generate Quiz"):

    with st.spinner("Generating Quiz..."):

        quiz = generate_quiz(
            sport=sport,
            difficulty=difficulty
        )

    st.success("Quiz Generated Successfully!")

    st.markdown("---")

    st.text(quiz)