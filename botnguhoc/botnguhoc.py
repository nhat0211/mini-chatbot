import speech_recognition 
from gtts import gTTS
import os
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print ("Robotnguhoc: Sủa đi thằng ml ")
        audio = robot_ear.listen(mic)
    print ("Robotnguhoc: ba chấm, ẻ xong rồi nghĩ :) ")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "mày nói cái lz gì thế thằng cờ hó :)"
    print ("You: " + you)

    if  you == "":
        robot_brain = "Tau đéo hiểu, sủa lại coi :)"
    elif "hello" in you:
        robot_brain = "hello Đức Cống"
    elif "fun" in you:
        robot_brain = "Xăng nay xuống 21 ngàn 900 nhé bạn 23 ngàn 500 ahihi"
    elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%d/%m/%Y") + " ok chưa thằng mặt lờ, hỏi lắm vờ cờ lờ"
    elif "now" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H Giờ %M Phút %S Giây") + " rồi, ngủ đi thằng lờ, khuya rồi đm"
    elif "wife" in you:
        robot_brain = "Võ Lê Quỳnh Lâm, đéo nói nhiều, vợ tau"
    elif "bye" in you:
        robot_brain = "bái bai thằng lờ, biến hộ tau, bot ngu học bãi triều"
        print ("Robotnguhoc: " + robot_brain)
        def robot_mouth(robot_brain):
            speech = gTTS(robot_brain, lang='vi', slow='true', tld='com')
            speech_file = 'speech.mp3'
            speech.save(speech_file)

        # Play the audio file
            os.system('afplay ' + speech_file)


        robot_mouth(robot_brain) 
        break
    elif "buddy" in you:
        robot_brain = "thằng cờ hó Đức chớ ai :) "
    else :
        robot_brain = "tau bảo sủa lại mà cứ lì đm"

    print ("Robotnguhoc: " + robot_brain)


    def robot_mouth(robot_brain):
        # Initialize gTTS with the text to convert
        speech = gTTS(robot_brain, lang='vi', slow='true', tld='com')

        # Save the audio file to a temporary file
        speech_file = 'speech.mp3'
        speech.save(speech_file)

        # Play the audio file
        os.system('afplay ' + speech_file)


    robot_mouth(robot_brain) 