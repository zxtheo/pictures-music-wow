FROM python:3

RUN echo "Acquire::http::Proxy \"${HTTP_PROXY}\";"    > /etc/apt/apt.conf.d/mcafee-proxy
RUN apt-get update
RUN apt-get install -y portaudio19-dev python3-pyaudio python3-pillow
RUN rm -rf /var/lib/apt/lists

COPY requirements.txt ./
RUN pip3 install --proxy=${HTTP_PROXY} --no-cache-dir -r requirements.txt
RUN pip3 show pillow
COPY main.py /
COPY run.sh /
COPY service /service
COPY data /data

CMD []
ENTRYPOINT ["/bin/bash","/run.sh"]
