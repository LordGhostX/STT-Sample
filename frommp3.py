from pydub import AudioSegment
from stt import recognise_wav

def from_mp3(name):
    song = AudioSegment.from_mp3(name)
    song.export(name + ".wav", format="wav")

    return name + ".wav"

if __name__ == "__main__":
    name = input("Enter mp3 name: ")
    song = from_mp3(name)

    text = recognise_wav(song)
    with open(name + ".txt", "w") as f:
        f.write(text)
