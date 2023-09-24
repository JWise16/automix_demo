import streamlit as st
import random
import audio_main

def play_songs():
    selected_songs = st.multiselect("Select songs to play", song_list)
    if selected_songs:
        try:
            audio_main.main_fun(selected_songs)
            st.success("Success! Playing selected songs.")
        except Exception as e:
            st.error(f"Error: {e}")

def auto_mix():
    random.shuffle(song_list)
    try:
        audio_main.main_fun(song_list)
        st.success("Success! Playing auto mixed songs.")
    except Exception as e:
        st.error(f"Error: {e}")

st.title("DJRihannaSpinnz")

# Sidebar for image and auto-mix button
with st.sidebar:
    st.image("rihanna_dj_pic.png")  # Update the file name to your image's name
    st.button("AutoMix", auto_mix)

# Main content
st.header("Select Songs to Play")

song_list = ["Don't_Stop_The_Music.wav", "Disturbia.wav", "Only_Girl.mp3"] # Add your list of song names here
selected_songs = st.multiselect("Select songs to play", song_list)

if selected_songs:
    play_button = st.button("Play Selected Songs")
    if play_button:
        try:
            audio_main.main_fun(selected_songs)
            st.success("Success! Playing selected songs.")
        except Exception as e:
            st.error(f"Error: {e}")
