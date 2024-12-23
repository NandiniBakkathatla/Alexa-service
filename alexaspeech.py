import sounddevice as sd
import numpy as np
import webbrowser
import threading
import speech_recognition as sr
import time

# Constants
SAMPLERATE = 44100  # Hertz
CHANNELS = 1
DURATION = 5  # seconds

# Flag to stop the command listener thread
stop_flag = False

# Function to open YouTube and search for song
def open_youtube():
    print("Opening YouTube...")
    webbrowser.open('https://www.youtube.com')
    time.sleep(2)  # Give it some time to open the page

# Function to listen for commands
def listen_for_commands():
    global stop_flag
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while not stop_flag:
        print("Listening for commands...")
        
        # Listen to audio
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Convert speech to text
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")

            # Process the command
            if 'open google' in command:
                webbrowser.open('http://www.google.com')
                print("Opening Google")
            elif 'open youtube' in command:
                open_youtube()
                print("Opened YouTube.")
            elif 'song' in command:
                # Open YouTube search for song
                print("Searching for a song on YouTube...")
                webbrowser.open('https://www.youtube.com/results?search_query=song')
            elif 'stop' in command:
                stop_flag = True  # Set stop flag to True to exit the loop
                print("Goodbye!")
            else:
                print(f"Command not recognized. You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

# Start listening in a separate thread
command_thread = threading.Thread(target=listen_for_commands)
command_thread.daemon = True
command_thread.start()

# Main program will keep running until you press Enter
try:
    while not stop_flag:
        time.sleep(1)  # Keep the program running
except KeyboardInterrupt:
    print("Exiting program.")
