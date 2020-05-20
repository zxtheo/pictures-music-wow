# pictures-music-wow

Music made from pictures...

Pixels are converted to notes by mapping the pixel values to note pitches and lengths. 

These notes are added to the music score and that score is then passed into the midi making service.

This service is where some musicality is put in, by ensuring that the socre is split up into bars of 4 beats.

It is then exported to MIDI and you can then listen to what your face sounds like (if you put your face in as the input jpg)

Enjoy!

## Build:

In docker environment: `docker build -t zxtheo/pictures-music-wow .`

In normal Linux environment:
```
apt-get install -y portaudio19-dev
pip3 install --proxy=${HTTP_PROXY} --no-cache-dir -r requirements.txt
```

On Windows the pip3 command should work but I don't know if there are other requirements to be able to get pyaudio working...

## Running

Find your midi device:
```
$ aplaymidi -l
 Port    Client name                      Port name
 14:0    Midi Through                     Midi Through Port-0
```
I will pick 14:0 as my device for these examples, using the built in doge.jpg image.

In docker:
```
docker run --rm zxtheo/pictures-music-wow doge.jpg | aplaymidi -p 14:0 -
```
And to render mypic.jpg which is outside the container.
```
docker run --rm -i zxtheo/pictures-music-wow - - </path/to/mypic.jpg | aplaymidi -p 14:0 -
```

On a Linux system:
```
python3 main.py doge.jpg g b 300 - | aplaymidi -p 14:0 -
```
or
```
python3 main.py /path/to/mypic.jpg g b 300 - | aplaymidi -p 14:0 -
```

Will run the container for 3 minutes playing music derived from picture doge.jpg in the data directory.

To save to a file from docker, just redirect the output to a file.
To save to a file without docker, use:
```
python3 main.py doge.jpg g b 180 outfile.midi
```
