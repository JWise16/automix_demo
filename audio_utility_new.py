from pydub import AudioSegment
from pydub.playback import play
import librosa
import numpy as np
import pandas as pd
import sounddevice as sd

def import_audio_files(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path)
    
    # Get the audio file names as a list
    audio_files = data['Audio Files'].tolist()
    
    return audio_files

def import_instructions(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path)
    
    # Create a dictionary to store instructions
    instructions = {}
    
    # Iterate through rows and extract instructions
    for index, row in data.iterrows():
        audio_file = row['Audio File']
        song_start = row.get('Song Start', 0)
        song_end = row.get('Song End', None)
        main_start = row.get('Main Start', 0)
        main_end = row.get('Main End', None)
        
        # Add instructions to the dictionary
        instructions[audio_file] = {
            'song_start': song_start,
            'song_end': song_end,
            'main_start': main_start,
            'main_end': main_end
        }
    
    return instructions

def create_instructions_from_options(track_list):

    
    # Create a dictionary to store instructions
    instructions = {}

    for track_number in range(len(track_list)):
        if track_number  == 0:
            track = track_list[0]
            transition_options = pd.read_excel("Transition_Options.xlsx", sheet_name=track)
            prev_track = 'First'

            song_start = 0
            song_end = 0
            main_start = 0
            main_end = 0
            if not transition_options.empty:
                for index, row in transition_options.iterrows():
                    if row['Song B4'] == prev_track:
                        song_start = row['Song Start']
                        song_end = row['Song End']
                        main_start = 0
                        main_end = main_start + (song_end-song_start)
                        
            # Add instructions to the dictionary
            instructions[track] = {
            'song_start': song_start,
            'song_end': song_end,
            'main_start': main_start,
            'main_end': main_end
             }
        else:
            previous_track_number = track_number-1
            prev_track = track_list[previous_track_number]
            track = track_list[track_number]
            # get track_list[track_number] sheet

            transition_options = pd.read_excel("Transition_Options.xlsx", sheet_name=track)

            song_start = 0
            song_end = 0
            main_start = 0
            main_end = 0
            if not transition_options.empty:
                for index, row in transition_options.iterrows():
                    if row['Song B4'] == prev_track:
                        song_start = row['Song Start']
                        song_end = row['Song End']
                        main_start = row["PrevSongTime"] - instructions[prev_track]['song_start'] +instructions[prev_track]["main_start"]
                        main_end = main_start + (song_end-song_start)
                        
            # Add instructions to the dictionary
            instructions[track] = {
            'song_start': song_start,
            'song_end': song_end,
            'main_start': main_start,
            'main_end': main_end
             }
            
    return instructions

def sec_to_millisec(seconds):
    return int(seconds * 1000)

def mix_audio(audio_files, instructions):
    # Mix the audio files based on instructions

    # Initialize an empty numpy array to hold the final mix
    final_mix = np.array([])
    sr = None  # Initialize sample rate

    for audio_file in audio_files:
        print(audio_file)

        # Load the audio using librosa
        audio, sr = librosa.load("audio_files/" + audio_file, sr=None)

        # Get the instructions for the current audio file
        file_instructions = instructions.get(audio_file, {})
        song_start = int(file_instructions.get("song_start", 0) * sr)
        song_end = int(file_instructions.get("song_end", len(audio)) * sr)
        main_start = int(file_instructions.get("main_start", 0) * sr)
        main_end = int(file_instructions.get("main_end", len(final_mix) / sr) * sr)

        # Trim the audio based on sample positions
        song_segment = audio[song_start:song_end]

        # Calculate the overlay position in samples
        overlay_position = main_start

        # Extend the final mix array if necessary
        if len(final_mix) < overlay_position + len(song_segment):
            silence_length = overlay_position + len(song_segment) - len(final_mix)
            final_mix = np.append(final_mix, np.zeros(silence_length))

        # Overlay the song segment on the final mix
        final_mix[overlay_position:overlay_position + len(song_segment)] += song_segment

    return final_mix, sr

def play_audio(audio, sr):
    sd.play(audio, sr)
    sd.wait()  # Wait for the audio to finish playing

def audio_main(track_list):
    # Example usage
    audio_files = import_audio_files('songs1.xlsx')
    instructions = import_instructions('instructions1.xlsx')
    print("Audio Files:", audio_files)
    print("Instructions:", instructions)
    
    # Mix the audio files based on instructions
    mixed_audio = mix_audio(audio_files, instructions)
    
    # Play the mixed audio
    play(mixed_audio)
