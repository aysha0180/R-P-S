import streamlit as st
import random

st.title("🪨📄✂️ Rock, Paper, Scissors Game!")

rock = "🪨 Rock"
paper = "📄 Paper"
scissors = "✂️ Scissors"

choices = [rock, paper, scissors]

player_choice = st.radio("Choose your move:", choices)

if st.button("Play!"):
    st.write(f"You chose: **{player_choice}**")

    computer_choice = random.choice(choices)
    st.write(f"Computer chose: **{computer_choice}**")

    if player_choice == computer_choice:
        st.success("It's a draw!")
    elif (
            (player_choice == rock and computer_choice == scissors) or
            (player_choice == paper and computer_choice == rock) or
            (player_choice == scissors and computer_choice == paper)
    ):
        st.success("You win! 🎉")
    else:
        st.error("Computer wins! 😢")
