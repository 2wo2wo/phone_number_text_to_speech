import random
from gtts import gTTS
import os


def random_phone():
    arr = list()
    counter=0
    for _ in range(16):
        arr.append(str(random.randrange(10)))
        counter+=1
        if counter==4:
            arr.append(" ")
            counter=0
    return arr
#print(''.join(arr))




language = 'en'
for i in range(11,20):
    mytext = ''.join(random_phone())
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("random{}.mp3".format(i))
    #os.system("mpv welcome.mp3")  #to play
