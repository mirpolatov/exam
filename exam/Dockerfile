FROM python:3.11-alpine
RUN mkdir /bot_img
WORKDIR /bot_img
COPY exam.py /bot_img
COPY requirement.txt /bot_img
RUN pip3 install -r requirement.txt
ENTRYPOINT ["python","exam.py"]
