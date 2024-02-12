docker build -t strudel ./app
docker run -p 0.0.0.0:4321:4321 strudel
