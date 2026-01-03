import streamlit as st
import random

st.title("Rock Paper Scissors – First to 5 Wins!")

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

user_choice = st.selectbox("Choose your move:", ["rock", "paper", "scissors"])

if st.button("Play Round"):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    st.write(f"Computer chose: {computer_choice}")

    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        st.session_state.user_score += 1
        st.write("You win this round!")
    elif user_choice == computer_choice:
        st.write("It's a tie!")
    else:
        st.session_state.computer_score += 1
        st.write("Computer wins this round!")

    st.write(f"User Score: {st.session_state.user_score}")
    st.write(f"Computer Score: {st.session_state.computer_score}")

    if st.session_state.user_score == 5:
        st.success("🎉 You won the game!")
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        exit
    elif st.session_state.computer_score == 5:
        st.error("💻 The computer won the game!")
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        exit

    