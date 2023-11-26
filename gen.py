from pydub import AudioSegment

def convert_ogg_to_wav(input_file, output_file):
    # Load OGG file
    audio = AudioSegment.from_ogg(input_file)
    
    # Export as WAV file
    audio.export(output_file, format="mp3")

if __name__ == "__main__":
    input_ogg_file = "menu1"  # Replace with the path to your OGG file

    convert_ogg_to_wav(input_ogg_file+".ogg", input_ogg_file+".mp3")
