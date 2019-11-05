import speech_recognition as sr
import os 

AUDIO_FILE = os.getcwd() + "\My Heart Will Go On (Love Theme from Titanic).wav"

def getAudioLength(recognizer, file_name):
    """docstring for getAudioLength in secs"""
    with sr.AudioFile(file_name) as source:
        audio = r.record(source)
    
    # length = no. rawsamples / (sample_size * sample_rate)
    return len(audio.frame_data)/(audio.sample_rate*audio.sample_width)

def getAudioSegment(recognizer, file_name, offset, duration):
    """docstring for getAudioSegment"""
    with sr.AudioFile(file_name) as source:
        audio = recognizer.record(source,offset=offset,duration=duration)
    
    return audio

def recognize(recognizer, audio):
    """docstring for recognize"""
    # recognize speech using Google Speech Recognition
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

 
# use the audio file as the audio source
r = sr.Recognizer()


lenght_s = getAudioLength(r,AUDIO_FILE)
print("File is " + str(lenght_s) + " secs long")


step_dur=5
for offset in range(0,int(lenght_s),step_dur):
    audio = getAudioSegment(r,AUDIO_FILE,offset,step_dur)
    print("From " + str(offset) + " to " + str(offset+step_dur) + " => " + recognize(r,audio))
