FROM ubuntu:22.04

RUN apt update && apt upgrade -y && \
    apt install -y git python3-pip python3.11 && \
    apt autoremove -y --purge && apt clean

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 0
RUN python -m pip install -U pip

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Set working directory
WORKDIR /home/SLT_AI_Developmen
