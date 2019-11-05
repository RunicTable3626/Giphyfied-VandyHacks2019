import moviepy.editor as mp
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips
from mp4Concat import FFConcat
concat = FFConcat(path='Base path containing folders with tracks')
concat.run()


def close_clip(clip):
  try:
    clip.reader.close()
    if clip.audio != None:
      clip.audio.reader.close_proc()
      del clip.audio
    del clip
  except Exception as e:
    print("Error in close_clip() ", e)


def gifToMp4(gif):
    filename= gif
    os.chdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/GIFS')
    clip = mp.VideoFileClip(filename)
    filename2= filename[:-4] +".mp4"
    os.chdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/Videos')
    clip.write_videofile(filename2)
    os.chdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/GIFS')


def video_sequencify(song_name):
#we will take all the gif videos and put them into one dictionary in which the
#keys will be the timestamp in tuple form such as (begin, end) and the values will be the mp4 arrays of each key word
#we will iterate through the keys in a for loop
#we will set the bounds of videos between their respective time stamps
#if the length of the timestamp exceeds first gif-video, we iterate to second then third, before looping back to first
#Based on this order, we will then create an array of these full and semi-cropped videos which we will then concatenate
#after concatenation, we will combine with audio and return result.
    gifvid_dict = {}
    PATH_TO_JSON = 'C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/aeneastest/output/'+song_name+'.json'
    for file in os.listdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/GIFS'):
        gifToMp4(file)
    os.chdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/Videos')
    with open(PATH_TO_JSON,'r') as jsonfile:
        json_content = json.load(jsonfile) # this is now in memory! you can use it outside 'open'
        i = 0
    for json_entry in json_content['fragments']:
        key = (float(json_entry['begin']),float(json_entry['end']))
        value = []
        for file in os.listdir('C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/Videos'):
            if json_entry['key_word'] in file:
                #this is just storing file names not mp4 files
                value.append(file)
        gifvid_dict[key] = value
    for key in gifvid_dict:
        clip0 = mp.VideoFileClip(gifvid_dict[key][0])
        if clip0.duration >= key[1] - key[0]:
##            gifvid_dict[key][0].duration = key[1] - key[0]
            new_name1 = gifvid_dict[key][0][:-4]+'3.mp4'
            ffmpeg_extract_subclip(gifvid_dict[key][0],
                                   0.0,
                                   key[1] - key[0],
                                   targetname=new_name1)
            gifvid_dict[key] = gifvid_dict[key][0]
        elif clip0.duration < key[1] - key[0]:
            temp_array = []
            difference = key[1] - key[0]
            i = 0
            while(difference > 0):
                clipi = mp.VideoFileClip(gifvid_dict[key][i%3])
                difference -= clipi.duration
                temp_array.append(gifvid_dict[key][i%3])
                i+=1
##            temp[i-1].duration += difference
                clipiminus = mp.VideoFileClip(temp_array[i-1])
                new_name2 = temp_array[i-1][:-4]+str(i)+'.mp4'
                ffmpeg_extract_subclip(temp_array[i-1],0.0,
                                       clipiminus.duration + difference,
                                       targetname= new_name2)
            #now we have to merge these clips
            close_clip(clipiminus)
            close_clip(clip0)
            mp4_array = []
            for file in temp_array:
                clip = mp.VideoFileClip(file)
                mp4_array.append(clip)
                close_clip(clip)
            final_clip = concatenate_videoclips(mp4_array, method='compose')
            final_clip.write_videofile(temp_array[0][:-5] + '.mp4')
            close_clip(final_clip)
            gifvid_dict[key] = temp_array[0][:-5] + '.mp4'
    mega_array = gifvid_dict.values()
    mega_mp4_array = []
    for file in mega_array:
        clip = mp.VideoFileClip(file)
        mega_mp4_array.append(clip)
        close_clip(clip) 
    super_final_clip = concatenate_videoclips(mega_mp4_array, method='compose')
    super_final_clip.write_videofile('super_final_gif.mp4')
#this takes a super long time so we will need to find a quicker way



    
        
                
                
                    
                
                
            
        
                
            
        
        
