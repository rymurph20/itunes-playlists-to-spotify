#!/usr/local/bin/python3
#
# This will take all local iTunes playlists and convert
# them to Spotify playlists. Most songs are able to be migrated,
# however, there will be cases where songs are unable to be found in
# Spotify.
#
# User specific variables:
#   sp_username: Spotify Username
#   playlist_exclusions: Any playlists you'd like to exclude.
#   it_lib: Location of iTunes 'iTunes Music Library.xml'
#
# Spotify Web API requires the following env variables to be set...
#   SPOTIPY_CLIENT_ID
#   SPOTIPY_CLIENT_SECRET
#   SPOTIPY_REDIRECT_URI

import re
import spotipy
import spotipy.util as util

from libpytunes import Library

def get_playlist_tracks(username, playlist_id):
    """Gets tracks in a given playlist. Accounts for
    playlists with greater than 100 songs"""
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

# Exclude iTunes default playlists
playlist_exclusions = ['Downloaded', 'Audiobooks', 'Genius', 'Top 25 Most Played']

sp_username = 'USERNAME'
sp_scope = 'playlist-modify-public'
sp_token = util.prompt_for_user_token(sp_username, sp_scope)
sp = spotipy.Spotify(auth=sp_token)
sp.trace = False

it_lib = Library.Library('ITUNES MUSIC LIBRARY.XML LOCATION')
it_playlists = it_lib.getPlaylistNames()
sp_playlists = sp.user_playlists(sp_username)

for it_playlist in it_playlists:
  if it_playlist not in playlist_exclusions:
	  
    # Get playlist ID from existing Spotify playlist
    sp_playlist_id = None
    for i, sp_playlist in enumerate(sp_playlists['items']):
      if sp_playlist["name"] == it_playlist:
       sp_playlist_id = sp_playlist["id"]  

    # If the playlist doesn't exist, create it
    if sp_playlist_id is None:
      sp_playlist_id = sp.user_playlist_create(sp_username,it_playlist,public=True)
      sp_playlist_id = sp_playlist_id["id"] 

    # Get tracks from Spotify playlist
    sp_playlist_tracks = get_playlist_tracks(sp_username, sp_playlist_id)

    for it_song in it_lib.getPlaylist(it_playlist).tracks:
      it_title = "{a} - {n}".format(a=it_song.artist, n=it_song.name)
      exists = False

      # Find iTunes song in Spotify
      # TODO: Improve search
      results = sp.search(it_title, limit=1)

      try:
        sp_track_id = [results['tracks']['items'][0]['id']] 
      except:
          print('Could not find track: ' + it_title)
          continue

      # Check if the song is already in the playlist.
      #
      # We keep track of 'exists_in_itunes' to remove any
      # tracks that exist in Spotify that no longer exist
      # in iTunes.
      for i, sp_playlist_track in enumerate(sp_playlist_tracks):
        if sp_playlist_track['track']['id'] == sp_track_id[0]:
          sp_playlist_track['track']['exists_in_itunes'] = True
          exists = True

      # Add track to playlist if it doesn't exist
      if exists == False:
        sp.user_playlist_add_tracks(sp_username, sp_playlist_id, sp_track_id)
        sp_playlist_track['track']['exists_in_itunes'] = True
        print('Added to Playlist: ' + it_title)

    # Remove any occurances of a song in a Spotify playlist that aren't in the corresponding iTunes playlist
    for i, sp_playlist_track in enumerate(sp_playlist_tracks):
      if not 'exists_in_itunes' in sp_playlist_track['track']:
        try:
          sp.user_playlist_remove_all_occurrences_of_tracks(sp_username, sp_playlist_id, [sp_playlist_track['track']['id']], snapshot_id=None)
        except:
          print('Failed to remove: ' + sp_playlist_track['track']['id'])
