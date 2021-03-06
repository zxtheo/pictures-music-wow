FROM python:3

RUN [ -z $HTTP_PROXY ] || echo "Acquire::http::Proxy \"${HTTP_PROXY}\";"    > /etc/apt/apt.conf.d/mcafee-proxy
RUN apt-get update
RUN apt-get install -y portaudio19-dev
RUN rm -rf /var/lib/apt/lists

COPY requirements.txt ./
RUN pip3 install ${HTTP_PROXY:+--proxy=${HTTP_PROXY}} --no-cache-dir -r requirements.txt
COPY main.py /
COPY run.sh /
COPY service /service
COPY data /data

ENTRYPOINT ["/run.sh"]
