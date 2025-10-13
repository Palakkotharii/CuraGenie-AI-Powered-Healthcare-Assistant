import speech_recognition as sr
import pyttsx3  # Importing pyttsx3 for text-to-speech

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)  # Increased timeout and phrase_time_limit
        try:
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return listen_to_user()
        except Exception as e:
            print("Error:", str(e))
            return "Sorry, I couldn't understand."

def speak_response(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()