import lyricsgenius
import os
def GeniusLyricsScraper(song_name):
    print('Retrieving lyrics from Genius.com...')
    client_access_token = 'Sdhj1_Mn_1nnBpFxpb09p_GuSEC1RL5BqqCIOlvhceqrAd4ay7alY71Mx-8DcXdA'
    genius = lyricsgenius.Genius(client_access_token)
    song = genius.search_song(song_name)
    cleaned_lyrics = ''
    flag = 0
    for char in song.lyrics:
        if char == '[':
            flag = 1
        if flag == 0:
            cleaned_lyrics+= char
        if char == ']':
            flag = 0
    cleaned_lyrics = cleaned_lyrics.replace('\n\n\n\n\n','\n')
    cleaned_lyrics = cleaned_lyrics.replace('\n\n\n\n','\n')
    cleaned_lyrics = cleaned_lyrics.replace('\n\n\n','\n')
    cleaned_lyrics = cleaned_lyrics.replace('\n\n','\n')
    cleaned_lyrics = cleaned_lyrics.splitlines()[1:]
    cleaned_lyrics = "\n".join(line.strip() for line in cleaned_lyrics)
    file1 = open("Lyrics/" + song_name + ".txt",'w')
    file1.write(cleaned_lyrics)
    file1.close()
    print('Retrieved lyrics from Genius.com')





