sut/logs:
	docker compose -f ./compose.yaml logs --tail=100 --timestamps sut
e2e/logs:
	docker compose -f ./compose.e2e.yaml logs --tail=100 --timestamps --follow e2e
e2e/build:
	docker compose -f ./compose.e2e.yaml build
e2e/up:
	docker compose -f ./compose.e2e.yaml up --detach
e2e/reup: e2e/build e2e/up
e2e/run: e2e/up e2e/logs
e2e/enter:
	docker compose -f ./compose.e2e.yaml run --no-deps e2e /bin/bash
