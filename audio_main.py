import audio_utility_new

def main_fun(tracks):

    # New stuff
    track_list = ["Don't_Stop_The_Music.wav", "Disturbia.wav", "Only_Girl.mp3"]
    track_lista = ["Don't_Stop_The_Music.wav", "Only_Girl.mp3", "Disturbia.wav"]
    track_list1 = ["Don't_Stop_The_Music.wav", "Disturbia.wav"]
    track_list2 = ["Don't_Stop_The_Music.wav", "Only_Girl.mp3"]
    track_list3 = ["Don't_Stop_The_Music.wav"]

    track_list4 = ["Disturbia.wav", "Don't_Stop_The_Music.wav", "Only_Girl.mp3"]
    track_list5 = ["Disturbia.wav", "Don't_Stop_The_Music.wav"]
    track_list6 = ["Disturbia.wav", "Only_Girl.mp3"]
    track_list6 = ["Disturbia.wav"]


    track_list6 = ["Only_Girl.mp3", "Don't_Stop_The_Music.wav", "Disturbia.wav"]
    track_list7 = ["Only_Girl.mp3", "Disturbia.wav"]
    track_list9 = ["Only_Girl.mp3", "Don't_Stop_The_Music.wav"]
    track_list9 = ["Only_Girl.mp3"]
    

    #testing cases
    track_test1 = ["Don't_Stop_The_Music.wav", "Disturbia.wav"]
    track_test2 = ["Don't_Stop_The_Music.wav", "Only_Girl.mp3"]
    track_test3 = ["Disturbia.wav", "Don't_Stop_The_Music.wav"]
    track_test4 = ["Disturbia.wav", "Only_Girl.mp3"]
    track_test5 = ["Only_Girl.mp3", "Disturbia.wav"]
    track_test6 = ["Only_Girl.mp3", "Don't_Stop_The_Music.wav"]

    # Example usage
    instructions = audio_utility_new.create_instructions_from_options(tracks)
    print("Audio Files:", tracks)
    print("Instructions:", instructions)
    
    # Mix the audio files based on instructions
    mixed_audio, sr = audio_utility_new.mix_audio(tracks, instructions)
    print(mixed_audio)

    print("playing audio")
    # Play the mixed audio
    audio_utility_new.play_audio(mixed_audio, sr)



