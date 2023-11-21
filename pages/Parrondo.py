import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt


# ---------------- HELPERS ---------------- #

def game_func(amount, win_loss_condition_true, win_loss_condition_false, win_probability, condition):
    #return amount + win_loss_condition_true if condition(amount) else amount + win_loss_condition_false

    if random.random() < win_probability:
        return amount + win_loss_condition_true if condition(amount) else amount + win_loss_condition_false  # Win scenario
    else:
        return amount - win_loss_condition_true if condition(amount) else amount + win_loss_condition_false  # Lose scenario


# ----------------- WIDGETS ----------------- #

st.title("Parrondo's Playground")

# Game A settings
st.header("Game A Settings")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Even Rules")
    # Add your inputs for Even rules of Game A
    win_loss_a_even = st.number_input("Win/Loss Amount (Even)", step=1, key="a_even")
    # Add more parameters as needed

with col2:
    st.subheader("Odd Rules")
    # Add your inputs for Odd rules of Game A
    win_loss_a_odd = st.number_input("Win/Loss Amount (Odd)", step=1, key="a_odd")
    # Add more parameters as needed

win_probability_a = st.slider('Win Probability for Game A', 0.0, 1.0, 1.0)

# Game B settings
st.header("Game B Settings")
col3, col4 = st.columns(2)
with col3:
    st.subheader("Even Rules")
    # Add your inputs for Even rules of Game B
    win_loss_b_even = st.number_input("Win/Loss Amount (Even)", step=1, key="b_even")
    # Add more parameters as needed

with col4:
    st.subheader("Odd Rules")
    # Add your inputs for Odd rules of Game B
    win_loss_b_odd = st.number_input("Win/Loss Amount (Odd)", step=1, key="b_odd")
    # Add more parameters as needed

win_probability_b = st.slider('Win Probability for Game B', 0.0, 1.0, 1.0)

# Game sequence and execution
st.header("Game Sequence")
sequence = st.text_input("Enter Game Sequence (e.g., 'AABBA')", "AB")
start_amount = st.number_input("Starting Amount", value=100)

if st.button("Run Games"):
    # Loop for 100 iterations
    amount = start_amount
    num_shots = 100
    results = np.zeros((1, num_shots))
    for i in range(num_shots):
        for game in sequence:
            if game == "A":
                amount = game_func(amount, win_loss_a_even, win_loss_a_odd, win_probability_a, lambda x: x % 2 == 0)
            elif game == "B":
                amount = game_func(amount, win_loss_b_even, win_loss_b_odd, win_probability_b, lambda x: x % 2 == 0)
            else:
                raise ValueError(f"Invalid game: {game}")
            results[0, i] = amount
    print(results[0])
    fig, ax = plt.subplots()
    ax.plot(results[0])
    ax.set_title("Game Results")
    ax.set_xlabel("Shot Iteration")
    ax.set_ylabel("Your Amount")
    # Display the pot in Streamlit
    st.pyplot(fig)
