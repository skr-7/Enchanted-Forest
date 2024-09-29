import streamlit as st
import GameLibrary as GL
#import pygame as pg

# Store the current state of the game in session_state to manage game progress
if 'game_state' not in st.session_state:
    st.session_state.game_state = "introduction"  # Start at the introduction
    st.session_state.history = []  # To track user choices and path

# Function to update the game state and add to history
def update_game_state(new_state):
    st.session_state.game_state = new_state
    st.session_state.history.append(new_state)

# Streamlit-based version of the make_choice function
def make_choice_streamlit(option1, option2, result1, result2, next_step1=None, next_step2=None):
    st.write("You have two options:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(option1):
            st.write(result1)
        #    if next_step1:
            update_game_state(next_step1.__name__)
            st.write("Hello")
    
    with col2:
        if st.button(option2):
            st.write(result2)
        #    if next_step2:
            update_game_state(next_step2.__name__)
            st.write("Why")

# Mapping the game state names to actual functions from GameLibrary
game_map = {
    "introduction": GL.introduction,
    "enter_forest": GL.enter_forest,
    "turn_back": GL.turn_back,
    "follow_the_path": GL.follow_the_path,
    "left_path": GL.left_path,
    "right_path": GL.right_path,
    "hermit_help": GL.hermit_help,
    "hermit_refuse": GL.hermit_refuse,
    "help_creatures": GL.help_creatures,
    "follow_the_voice": GL.follow_the_voice,
    "trust_the_figure": GL.trust_the_figure,
    "distrust_the_figure": GL.distrust_the_figure
}

# Main loop to control the flow of the game based on the state
def run_game():
    st.title("The Enchanted Forest")
    st.write("Welcome to 'The Enchanted Forest'!")
    
    # Check the current game state and call the corresponding function
    current_state = st.session_state.game_state
    st.write(f"Current game state: {current_state}")
    
    # Call the function corresponding to the current state from the map
    if current_state in game_map:
        game_map[current_state]()
    else:
        st.write("Game over. Restart to play again.")
    
    # Add a back option
    #def back_button():
    #    if st.session_state.step_history:
    #        if st.button("Back"):
    #        st.session_state.current_step = st.session_state.step_history.pop()  # To rerun the app and reset the state

    # Add a restart option
    if st.button("Restart"):
        st.session_state.game_state = "introduction"
        st.session_state.history.clear()
            #    st.experimental_rerun()  # To rerun the app and reset the state

# Override the functions in GameLibrary to use the Streamlit make_choice
GL.make_choice = make_choice_streamlit

# Run the game
run_game()
