FROM debain:latest

RUN apt update && apt upgrade -y
RUN cd /
RUN git clone https://github.com/sinofarmonovzfkrvjl/translator-bot.git
RUN cd translator-bot
WORKDIR /translator-bot
RUN pip install -r requirements.txt
CMD [ "python3", "main.py" ]