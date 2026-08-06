import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os

# Configure Gemini API
genai.configure(api_key="YOUR_API")

# Load Gemini model
model = genai.GenerativeModel("gemini-3.6-flash")

# Initialize Speech Recognition
recognizer = sr.Recognizer()

try:
    # Capture voice input
    with sr.Microphone() as source:
        print("🎤 Listening... Please speak.")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    print("Converting speech to text...")

    # Convert speech to text
    text = recognizer.recognize_google(audio, language="en-US")

    print("\nYou said:")
    print(text)

    # Send text to Gemini
    response = model.generate_content(text)

    reply = response.text

    print("\nGemini Response:")
    print(reply)

    # Convert response to speech
    tts = gTTS(text=reply, lang="en")
    tts.save("response.mp3")

    print("\nResponse saved as response.mp3")

    # Play the audio file
    os.system("start response.mp3")

except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")

except sr.RequestError as e:
    print(f"Speech Recognition Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")