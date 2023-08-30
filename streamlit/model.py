import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import yaml 
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import pickle
import os
import streamlit as st

def playlist_model(url, model, max_gen=3, same_art=5):
    log = []
    Fresult = []
    try:
        log.append('Start logging')
        uri = url.split('/')[-1].split('?')[0]
    try:
        log.append('spotify local method')
        stream = open("Spotify/Spotify.yaml")
        spotify_details = yaml.safe_load(stream)
        auth_manager = SpotifyClientCredentials(client_id=spotify_details['Client_id'], client_secret=spotify_details['client_secret'])
    except:
        log.append('spotify .streamlit method')
        try:
            Client_id=st.secrets["Client_ID"]
            client_secret=st.secrets["Client_secret"]
            auth_manager = SpotifyClientCredentials(client_id=Client_id, client_secret=client_secret)
        except:
            log.append('spotify hug method')
            Client_id=os.environ['Client_ID']
            client_secret=os.environ['Client_secret']
            auth_manager = SpotifyClientCredentials(client_id=Client_id, client_secret=client_secret)
     sp = spotipy.client.Spotify(auth_manager=auth_manager)       