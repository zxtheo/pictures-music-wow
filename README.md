# pictures-music-wow

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
