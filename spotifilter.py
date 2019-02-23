#Author: Christian F. Sousa
#hackcu V project


#required imports
import spotipy
import spotipy.util as util
from keys import CLIENT_ID, CLIENT_SECRET
import sys
#authenticator for app, authenticates client
def authen():
    token =util.oauth2.SpotifyClientCredentials(client_id= CLIENT_ID, client_secret= CLIENT_SECRET)
authen()

    
