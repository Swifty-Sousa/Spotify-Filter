#Author: Christian F. Sousa
#hackcu V project

#$https://open.spotify.com/user/dlu950yaxcioasmyl8zq38tle?si=npAstWIzSl-1Ptxh20p9_g
#required imports
import spotipy
import spotipy.util as util
from keys import CLIENT_ID, CLIENT_SECRET
import sys
import json
#authenticator for app, authenticates client
#print(json.dumps(VAR, sort_keys=True, indent=4))
username= "dlu950yaxcioasmyl8zq38tle?si=npAstWIzSl-1Ptxh20p9_g"
scope= "app-remote-control"
token =util.prompt_for_user_token(username, scope, client_id= CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri= "http://google.com/")
spo= spotipy.Spotify(auth=token)
user=spo.current_user()
current_song= spo.current_user_playing_track()
print(json.dumps(user, sort_keys=True, indent=4))


