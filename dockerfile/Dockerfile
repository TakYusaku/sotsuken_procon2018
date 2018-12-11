FROM ubuntu:18.04

RUN apt update && echo "successful!"
RUN apt install -y python3-pip && echo "successful!"
RUN apt install -y curl && echo "successful!"
RUN apt install -y nano && echo "successful!"
RUN apt install -y git && echo "successful!"
RUN apt install -y golang-go && echo "successful!"
RUN pip3 install gym && pip3 install matplotlib && echo "successful!"
RUN cd home && git clone https://github.com/TakYusaku/sotsuken_procon2018.git #&& cd sotsuken_procon2018/
#RUN mkdir /usr/local/lib/python3.6/dist-packages/gym/envs/myenv2 && cp -r gym_myenvs/myenv2/* /usr/local/lib/python3.6/dist-packages/gym/envs/myenv2
#RUN cp gym_myenvs/__init__.py /usr/local/lib/python3.6/dist-packages/gym/envs/
RUN echo "successful!"

CMD echo 'Hello docker of sotsuken world!'
