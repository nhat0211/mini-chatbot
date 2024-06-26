import speech_recognition 

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print ("Botnguhoc: Tau đang nghe đây tml, sủa điiiiii :) ")
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you = "mày nói cái lz gì thế thằng cờ hó :)"
print ("You: " + you)