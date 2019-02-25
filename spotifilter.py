#Author: Christian F. Sousa
#hackcu V project

#$https://open.spotify.com/user/dlu950yaxcioasmyl8zq38tle?si=npAstWIzSl-1Ptxh20p9_g
#required imports
import spotipy
import spotipy.util as util
from keys import CLIENT_ID, CLIENT_SECRET
import sys
import json
import time
#authenticator for app, authenticates client
#print(json.dumps(VAR, sort_keys=True, indent=4))
#this is the username
USER= "dlu950yaxcioasmyl8zq38tle?si=npAstWIzSl-1Ptxh20p9_g"
def auth():
    username= "dlu950yaxcioasmyl8zq38tle?si=npAstWIzSl-1Ptxh20p9_g"
    scope= "user-read-currently-playing user-modify-playback-state playlist-read-private playlist-modify-private"
    token =util.prompt_for_user_token(USER, scope, client_id= CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri= "http://google.com/")
    spo= spotipy.Spotify(auth=token)
    return spo
def get_curr_song(spo):
    user=spo.current_user()
    song_data= spo.current_user_playing_track()
    #print(json.dumps(user, sort_keys=True, indent=4))
    #print(json.dumps(song_data, sort_keys=True, indent=4))
    #print(song_data["item"]["name"])
    #print(song_data["item"]["album"]["artists"][0]["name"])
    #print(json.dumps(song_data, sort_keys=True, indent=4))
    song_name= song_data["item"]["name"]
    song_art= song_data["item"]["album"]["artists"][0]["name"]
    #print(song_name)
    #print(song_art)
    return [song_name, song_art]

#retruns playlist data
def play_data(spo):
    play_lists= spo.current_user_playlists()
    #print(json.dumps(play_lists["items"][0], sort_keys=True, indent=4))
    for i in range(0, len(play_lists["items"])):
        if play_lists["items"][i]["name"] == "Blocked_Songs":
            play_id= play_lists["items"][i]["id"]
            play_uri= play_lists["items"][i]["uri"]
            #print(play_uri)
            #print(json.dumps(play_lists["items"][i], sort_keys=True, indent=4))
            #print(play_id)
    track_list=spo.user_playlist_tracks(play_uri.split(':')[2], play_uri.split(':')[4])
    #ßprint(track_list)
    tracks=track_list["items"]
    #print(json.dumps(tracks[0], sort_keys=True, indent=4))
    #print(tracks[0]["track"]["name"])
    Tracks=[]
    for i  in range(0,len(tracks)):
        Tracks.append([tracks[i]["track"]["name"], tracks[i]["track"]["artists"][0]["name"]])
        #print(tracks[i]["track"]["name"])
        #print(tracks[i]["track"]["artists"][0]["name"])
    return Tracks
#asyc function to controll unit 
def execute(spo, blocked_tracks):
    current_song=spo.current_user_playing_track()
    holder=get_curr_song(spo)
    for i in range(0,len(blocked_tracks)):
        #print(blocked_tracks[i][0] + ", "+ blocked_tracks[i][1])
        if blocked_tracks[i]==current_song:
            spo.next_track()
            execute(spo, blocked_tracks)
            return
    while holder==get_curr_song(spo):
        time.sleep(1)
    execute(spo, blocked_tracks)


            
        

#main controller
def main():
    spo=auth()
    print(json.dumps(spo.current_user_playing_track(), sort_keys=True, indent=4))
    #test2(spo)
    blocked_tracks=play_data(spo)
    execute(spo,blocked_tracks)
main()