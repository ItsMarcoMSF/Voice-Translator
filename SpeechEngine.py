import pyttsx3


class SpeechEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        self.female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    def speak(self, translated, voiceSelection):
        if voiceSelection == "male":
            self.engine.setProperty('voice', self.male_voice_id)
            self.engine.say(translated)
            self.engine.runAndWait()
        elif voiceSelection == "female":
            self.engine.setProperty('voice', self.female_voice_id)
            self.engine.say(translated)
            self.engine.runAndWait()
