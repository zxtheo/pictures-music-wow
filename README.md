# pictures-music-wow

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
I will pick 14:0 as my device for these examples.

In docker:
```
docker run --rm zxtheo/pictures-music-wow doge.jpg | aplaymidi -p 14:0 -
```

On a Linux system:
```
python3 main.py doge.jpg g b 180 - | aplaymidi -p 14:0 -
```

Will run the container for 3 minutes playing music derived from picture doge.jpg in the data directory.

To save to a file from docker, just redirect the output to a file.
To save to a file without docker, use:
```
python3 main.py doge.jpg g b 180 outfile.midi
```

