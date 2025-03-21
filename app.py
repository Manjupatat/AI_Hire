import google.generativeai as genai
import streamlit as st

st.title("AI Interview Bot")

# Retrieve API key
api_key = st.secrets["general"]["AIzaSyBsNUps9NoF8011ZilZm6cMgq4igSbgHEY"]
genai.configure(api_key=api_key)

# Initialize session state variables
if "name" not in st.session_state:
    st.session_state.name = ""
if "skills" not in st.session_state:
    st.session_state.skills = ""
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "messages" not in st.session_state:
    st.session_state.messages = []  # Store entire chat history
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

# Step 1: Ask for user's name
if not st.session_state.name:
    st.session_state.name = st.text_input("Enter your name:")
    if st.session_state.name.strip():
        st.rerun()
    st.stop()

# Step 2: Ask for technical skills
if not st.session_state.skills:
    st.session_state.skills = st.text_input(f"Hi {st.session_state.name}, what are your technical skills? (e.g., Python, Django, React)")
    if st.session_state.skills.strip():
        st.rerun()
    st.stop()

# Step 3: Generate questions based on skills
if not st.session_state.questions and not st.session_state.interview_started:
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Generate exactly 5 technical interview questions for someone skilled in {st.session_state.skills}. 
    Return only the questions, numbered 1 to 5, in this format:
    
    1. <question>
    2. <question>
    3. <question>
    4. <question>
    5. <question>
    6. <question>
    Do not include any extra text before or after the questions.
    """

    response = model.generate_content(prompt)

    # Extract and store questions
    st.session_state.questions = [
        q.strip() for q in response.text.split("\n") if q.strip() and q.strip()[0].isdigit()
    ][:6]  

    st.session_state.interview_started = True
    st.rerun()

# Step 5: Conduct the interview
if st.session_state.current_question < len(st.session_state.questions):
    question = st.session_state.questions[st.session_state.current_question]
    st.write(f"**{question}**")

    user_answer = st.text_input("Your answer:", key=f"answer_{st.session_state.current_question}")

    if user_answer:
        # Save user response to chat history
        st.session_state.messages.append({"role": "user", "content": user_answer})

        # Get AI response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Evaluate this answer: {user_answer}")

        # Save AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})

        # Display AI response
        with st.chat_message("assistant"):
            st.write(response.text)

        # Thank the user
        st.success("Thank you for your answer, we will review it.")

        # Move to the next question
        st.session_state.current_question += 1
        st.rerun()

# Step 6: Show completion message after all questions
if st.session_state.current_question >= len(st.session_state.questions):
    st.write(f"🎉 Thanks for completing the interview, {st.session_state.name}! 🎉")
