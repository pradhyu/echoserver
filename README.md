# echoserver

Simple `echoserver`, which dumps HTTP requests.

- `/`: Dump the HTTP request.
- `/health`: Return a 200 status code.
- `/status`: Return a random status code, via the `?status=random` parameter or a the defined status code via the `?status=200` parameter.
- `/timeout`: Wait the given amount of time (`?timeout=1m`) before returning a 200 status code.

## Build

The `echoserver` can be built with the following command:

```sh
go build
./echoserver
```

When you are using Docker, you can use the following commands:

```sh
docker build -f Dockerfile -t ricoberger/echoserver:latest .
docker run -it --rm --name echotest -p 8080:8080 ricoberger/echoserver:latest
```

## Deploy

To deploy the `echoserver` at Kubernetes run the following commands:

```sh
kubectl create namespace test
kubectl label namespace test istio-injection=enabled

kubectl apply -n test -f https://github.com/ricoberger/echoserver/blob/main/deploy/echoserver-deploy.yaml
kubectl apply -n test -f https://github.com/ricoberger/echoserver/blob/main/deploy/echoserver-svc.yaml
```

## Exmples

```sh
curl -vvv http://localhost:8080/
curl -vvv http://localhost:8080/status?status=400
curl -vvv http://localhost:8080/timeout?timeout=10s
```
