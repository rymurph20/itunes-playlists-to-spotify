# itunes-playlists-to-spotify

Created by Ryan Murphy (https://www.rmurph.com)

This is a simple script that will copy all playlists and playlist contents from iTunes to Spotify.

**Before using libpytunes it is recommended that you backup your iTunes Library XML file. Use libpytunes at your own risk - there is no guarantee that it works or will not blow-up your computer!**

If you don't see an .xml library file in `~/Music/iTunes`, you probably started using iTunes after version 12.2, and have never enabled sharing between iTunes and other apps. To generate one, go to iTunes Preferences | Advanced and select "Share iTunes Library XML with other applications." ([Apple docs](https://support.apple.com/en-us/HT201610))

## Usage:

In the script, make sure to set:
- sp_username: Spotify username
- playlist_exclusions: Any playlists you'd like to exclude.
- it_lib: Location of your 'iTunes Library.xml'
- SPOTIPY_CLIENT_ID: Environment variable for your Spotify Client ID
- SPOTIPY_CLIENT_SECRET: Environment variable for your Spotify Client Secret
- SPOTIPY_REDIRECT_URI: Environment variable for your Spotify Redirect URL (can be http://localhost/)
