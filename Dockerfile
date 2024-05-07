FROM ubuntu:22.04

RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

RUN apt update && apt upgrade -y && \
    apt install -y git python3-pip python3.11 && \
    apt install -y ffmpeg libsm6 libxext6 && \
    apt install -y python3-tk && \
    apt autoremove -y --purge && apt clean

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 0

RUN python -m pip install -U pip

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Set working directory
WORKDIR /home/SLT_AI_Developmen

ENV PYTHONPATH "${PYTHONPATH}:src"

