# pictures-music-wow

## Build:

In docker environment: `docker build -t zxtheo/pictures-music-wow .`

In normal environment:
```
apt-get install -y portaudio19-dev python3-pyaudio python3-pillow python3-midiutil
pip3 install --proxy=${HTTP_PROXY} --no-cache-dir -r requirements.txt
```

## Running

Find your midi device:
```
$ aplaymidi -l
 Port    Client name                      Port name
 14:0    Midi Through                     Midi Through Port-0
```
I will pick 14:0 as my device for these examples.

In docker:
```
docker run --rm zxtheo/pictures-music-wow doge.jpg - | aplaymidi -p 14:0 -
```

On a Linux system:
```
python3 main.py doge.jpg g b 180 - | aplaymidi -p 14:0 -
```

Will run the container for 3 minutes playing music derived from picture doge.jpg in the data directory.
