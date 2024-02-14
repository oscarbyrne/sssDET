FROM mcr.microsoft.com/playwright:v1.41.1-jammy

RUN apt update
RUN apt install -y python3-pip

WORKDIR /app
RUN mkdir -p ./e2e

COPY ./src/e2e/requirements.txt ./e2e
RUN pip install -r ./e2e/requirements.txt
RUN playwright install

COPY ./src/e2e . 
