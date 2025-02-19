FROM mcr.microsoft.com/playwright:v1.41.1-jammy

RUN apt update
RUN apt install -y python3-pip

WORKDIR /app
RUN mkdir -p ./data
RUN mkdir -p ./e2e

COPY ./src/data/requirements.txt ./data
COPY ./src/e2e/requirements.txt ./e2e

RUN pip install -r ./data/requirements.txt
RUN pip install -r ./e2e/requirements.txt
ENV PYTHONPATH=/app
RUN playwright install

COPY ./sut/juice-shop/data/static ./data/static
COPY ./src/data ./data
COPY ./src/e2e ./e2e

CMD pytest --tracing on --video on --output ./results
