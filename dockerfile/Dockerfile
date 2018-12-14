FROM ubuntu:18.04

# 学外でbuildするならば，以下のENVをコメントアウト
ENV http_proxy="http://http-p.srv.cc.suzuka-ct.ac.jp:8080/"
ENV https_proxy="http://http-p.srv.cc.suzuka-ct.ac.jp:8080/"
ENV no_proxy=127.0.0.1,localhost

RUN apt update && echo "successful!"
RUN apt install -y python3-pip && echo "successful!"
RUN apt install -y curl && echo "successful!"
RUN apt install -y nano && echo "successful!"
RUN apt install -y git && echo "successful!"
RUN apt install -y golang-go && echo "successful!"
RUN pip3 install gym && pip3 install matplotlib && pip3 install && pip3 install retry && echo "successful!"
RUN cd home && git clone https://github.com/TakYusaku/sotsuken_procon2018.git && cd sotsuken_procon2018/gym_myenvs/myenv2/ && mkdir /usr/local/lib/python3.6/dist-packages/gym/envs/myenv2 && cp -rp * /usr/local/lib/python3.6/dist-packages/gym/envs/myenv2 && cd ../ && cp __init__.py /usr/local/lib/python3.6/dist-packages/gym/envs/
RUN echo "successful!"

CMD echo 'Hello docker of sotsuken world!'
