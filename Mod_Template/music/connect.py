import os
from pydub import AudioSegment

def concatenate_songs(song_list):
    combined = AudioSegment.silent(duration=0)

    for song in song_list:
        audio = AudioSegment.from_mp3(song)
        combined += audio

    return combined

if __name__ == "__main__":
    # Specify the path to your FFmpeg executable
    ffmpeg_path = r'C:\\Users\\umtaa005\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

    # Add the FFmpeg directory to the system PATH temporarily
    os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

    # List of MP3 files to concatenate
    song_files = ["track_1.mp3", "track_2.mp3", "track_3.mp3", "track_4.mp3", "track_5.mp3"]

    # Call the function to concatenate the songs
    combined_song = concatenate_songs(song_files)

    # Play or export the combined song as needed
    combined_song.export("combined_track.mp3", format="mp3")
