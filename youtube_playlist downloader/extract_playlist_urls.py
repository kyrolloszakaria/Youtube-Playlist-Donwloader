from googleapiclient.discovery import build
import private as private

def extract_playlist_urls(playlist_url, output_file='playlist_urls.txt'):
    # Extract playlist ID from URL
    playlist_id = playlist_url.split('list=')[1]
    api_key = private.api_key
    youtube = build('youtube', 'v3', developerKey=api_key)
    # Retrieve playlist items
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50  # Adjust as needed to retrieve all items
    ).execute()
    # Extract video URLs from playlist items
    video_urls = []
    for item in playlist_items['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_urls.append(video_url)
    with open(output_file, 'w') as f:
        for url in video_urls:
            f.write(f'{url}\n')
    return video_urls

url = 'https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'

print(extract_playlist_urls(url))