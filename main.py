import pyttsx3

from SpeechRecog import SpeechRecog
from Translator import Trans
from SpeechEngine import SpeechEngine


def main():
    sr = SpeechRecog()
    t = Trans()

    voice = input("Please enter 'male' or 'female' to select voice")

    print("Listening...")
    phrase = sr.listen()
    print("Your phrase is:", phrase)

    print("Translating...")
    result = t.trans(phrase)
    print("Your translation is:", result)

    se = SpeechEngine()
    se.speak(result, voice.lower())


if __name__ == "__main__":
    main()
