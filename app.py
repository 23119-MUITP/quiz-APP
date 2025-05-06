import streamlit as st
from utils.quiz_utils import load_questions, calculate_score

st.title("🧠 Interactive Quiz App")

questions = load_questions("data/questions.csv")

# Track whether quiz has been submitted
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Only show quiz if not yet submitted
if not st.session_state["submitted"]:
    user_answers = []

    for i, row in questions.iterrows():
        st.subheader(f"Q{i+1}: {row['question']}")
        answer = st.radio(
            "Choose an answer:",
            [row['option1'], row['option2'], row['option3'], row['option4']],
            key=f"q{i}_{row['question']}"  # unique key per question
        )
        user_answers.append(answer)

    if st.button("Submit"):
        score = calculate_score(questions, user_answers)
        st.session_state["score"] = score
        st.session_state["submitted"] = True
        st.rerun()  # force refresh to clear quiz
else:
    st.success(f"🎯 Your Score: {st.session_state['score']}/{len(questions)}")
    if st.session_state["score"] >= len(questions) * 0.7:
        st.balloons()
        st.write("👏 Great job!")
    else:
        st.write("🙌 Keep practicing!")