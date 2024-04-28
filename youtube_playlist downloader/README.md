# YouTube Playlist Downloader

This is a simple YouTube playlist downloader program that allows you to easily download YouTube playlists. You provide the link to the playlist you want to download, and the program extracts all the video URLs and saves them locally. It then proceeds to download the videos for offline viewing.

## Features

- Download YouTube playlists effortlessly.
- Save extracted video URLs locally for resuming downloads.
- Download videos in various formats and qualities.

## Requirements

- Python 3.x
- Docker (optional)
- Xming (for running with Docker on Windows)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/kyrolloszakaria/youtube_playlist_downloader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd youtube_playlist_downloader
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
4.  Get your API key from [Google Cloud Console](https://console.cloud.google.com/cloud-resource-manager). And save it into `private.py` file in the same working directory. It is free, don't worry :wink:. 
## Usage

You can run the YouTube playlist downloader program using Python directly or through Docker.

### Running with Python

1. Run the following command to start the program:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to input the YouTube playlist URL and download options.

### Running with Docker (optional)

1. Download the image:
    ```bash
    docker push kyrolloszakaria/youtube_playlist_downloader:tagname
    ```
2. Download Xming from [here](https://sourceforge.net/projects/xming/).

3. Install Xming by following the installation instructions provided by the installer.

4. After installation, navigate to the directory where Xming is installed (typically `C:\Program Files\Xming`).

5. Run the following command in the command prompt to start Xming with access control disabled:

   ```bash
   .\Xming.exe -ac
   ```

6. Run the Docker container:

    ```bash
    docker run -it --rm -e DISPLAY=10.40.43.192:0 --network="host" --name youtube_downloader_container youtube_downloader_image
    ```

7. Follow the on-screen instructions to input the YouTube playlist URL and download options.

### Resuming Downloads

If you have a file containing previously extracted video URLs, you can continue downloading from a certain video by providing the file as input when prompted.

## Notes

- Make sure to comply with YouTube's terms of service and the applicable laws when using this program.
