import pyttsx3


def text_to_speech(text):
    """
    Converts the input text to speech and plays it using the pyttsx3 engine.

    :param text: The text that needs to be converted to speech.
    """
    if not text.strip():
        print("Error: No text provided.")
        return

    try:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set properties for speech rate (speed) and volume
        engine.setProperty('rate', 150)  # Speed of speech (default is 200)
        engine.setProperty('volume', 1)  # Volume (range 0.0 to 1.0)

        # Optional: Set the voice property to a different voice (male/female)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Index 1 for female voice, 0 for male voice

        # Convert text to speech and play it
        engine.say(text)
        engine.runAndWait()  # Wait until the speech is finished
        print("✅ Audio played successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Take user input for the text to be converted to speech
    text = input("Enter text for TTS: ")
    text_to_speech(text)
