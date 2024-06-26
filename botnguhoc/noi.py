
# from gtts import gTTS
# import os


# robot_brain = "Hello thằng mặt lờ"

# def robot_mouth(robot_brain):
#     # Initialize gTTS with the text to convert
#     speech = gTTS(robot_brain, lang='vi', slow='false', tld='com')

#     # Save the audio file to a temporary file
#     speech_file = 'speech.mp3'
#     speech.save(speech_file)

#     # Play the audio file
#     os.system('afplay ' + speech_file)


# robot_mouth(robot_brain) 

from datetime import date

today = date.today()
print("Today's date:", today)

d2 = today.strftime("%B %d, %Y")
print(d2)