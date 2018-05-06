# itunes-playlists-to-spotify

Created by Ryan Murphy (https://www.rmurph.com)

This is a simple script that will copy all playlists and playlist contents from iTunes to Spotify.

In order for this to work, you must have a Spotify developer account.
Learn more: https://beta.developer.spotify.com/documentation/web-api/quick-start/

Make sure to install all requirements listed in requirements.txt

**Before using libpytunes it is recommended that you backup your iTunes Library XML file. Use libpytunes at your own risk - there is no guarantee that it works or will not blow-up your computer!**

If you don't see an .xml library file in `~/Music/iTunes`, you probably started using iTunes after version 12.2, and have never enabled sharing between iTunes and other apps. To generate one, go to iTunes Preferences | Advanced and select "Share iTunes Library XML with other applications." ([Apple docs](https://support.apple.com/en-us/HT201610))

## Usage:

In the script, make sure to review the follow:
- sp_username = Your Spotify username
- sp_scope = 'playlist-modify-public' # This can be left as default
- sp_client_id = Your Spotify client ID from your developer account
- sp_client_secret = Your Spotify client secret from your developer account
- sp_redirect_uri = 'http://localhost/' # This can be left as default
- playlist_exclusions = ['Downloaded', 'Audiobooks', 'Genius', 'Top 25 Most Played'] # This can be left as default
- itunes_lib_loc = Location of your 'iTunes Music Library.xml' 