# pictures-music-wow

Music made from pictures...
Pixels are converted to notes by mapping the pixel values to note pitches and lengths. 
These notes are added to the music score and that score is then passed into the midi making service.
This service is where some musicality is put in, by ensuring that the socre is split up into bars of 4 beats.
It is then exported to MIDI and you can then listen to what your face sounds like (if you put your face in as the input jpg)
Enjoy!

## Build:

In docker environment: `docker build -t zxtheo/pictures-music-wow .`

In normal environment:
```
apt-get install -y portaudio19-dev python3-pyaudio python3-pillow
pip3 install --proxy=${HTTP_PROXY} --no-cache-dir -r requirements.txt
```

## Running

In docker:
```
docker run --rm --device /dev/snd zxtheo/pictures-music-wow
```

On a Linux system:
```
python3 main.py doge.jpg g b 180
```

Will run the container for 3 minutes playing music derived from picture doge.jpg in the data directory.
