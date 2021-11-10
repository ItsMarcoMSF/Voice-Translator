import speech_recognition as sr


class SpeechRecog:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=1)

    def listen(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

        result = self.r.recognize_google(audio)
        return result
