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
    pass