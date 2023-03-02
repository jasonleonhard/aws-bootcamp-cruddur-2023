help:
	echo "available commands" && cat Makefile | grep ":" |  grep -v help | xargs
	echo "you must signin to see all content"

todo:
	echo "activity_avatar not showing user"

docker-helper:
	make open-docker
	psql -h localhost # bc docker containerized
	echo "# consider removing images # docker image prune -a -f ; docker images"

flags:
	echo "-s = silent"

set:
	export $(cat .env | xargs)

check:
	cat .env


install-back:
	pip install -r ./backend-flask/requirements.txt

install-front:
	# this presumes you have already setup nvm such as # nvm install --lts; nvm use --lts; node -v; # v18.14.1
	cd frontend-react-js; \
	npm i; \
	npm audit; \
	npm audit fix; \
	npm audit; \
	cd ..; \
	# npm i ./frontend-react-js
	# npm i ./frontend-react-js/package.json # does this work instead?

reinstall-front:
	rm -rf node_modules; \
	npm i;

open-docker:
	open -a /Applications/Docker.app
	echo "Note Docker Desktop App takes time to open and initialize be please be patient"
	# sleep 30

open-endpoint:
	open http://localhost:4567/api/activities/home
	echo "refresh browser when terminal stops outputting new logs"

build-back:
	docker build -t backend-flask ./backend-flask; # without tag

build-back-tag:
	docker build -t backend-flask/latest:my-tag ./backend-flask; #  with tag

run-back:
	docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask # will produce dangling iamges
	# docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask

dev:
	# make -s open-docker && make -s build-back && make -s open-endpoint && make -s run
	make -s set && make -s install-back && make -s install-front && make -s build-front && make -s open-endpoint && make -s open-docker && make -s build-back && make -s run-back 		# && make -s run-front

front:
	open http://localhost:3000
	docker run -p 3000:3000 -d frontend-react-js

close:
	echo "terminal command to close mac application"
	pkill -x Docker	# Or: # killall Docker
	# sleep 10

img:
	echo "IMAGES:"
	docker images

img2:
	echo "IMAGES:"
	docker images --no-trunc -a

ps:
	echo "PS:"
	docker ps

ps2:
	echo "PS:"
	docker ps --no-trunc -a

info:
	echo "________________________________________________________________________"
	make -s img
	echo "________________________________________________________________________"
	make -s ps
	echo "________________________________________________________________________"

info2:
	echo "________________________________________________________________________"
	make -s img2
	echo "________________________________________________________________________"
	make -s ps2
	echo "________________________________________________________________________"

info3:
	clear
	make -s info
	make -s info2

home:
	curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json" | jq

groups:
	curl -X GET http://localhost:4567/api/message_groups -H "Accept: application/json" -H "Content-Type: application/json" | jq

logs:
	echo "________________________________________________________________________"
	echo "CONTAINER_ID:"
	docker logs CONTAINER_ID -f
	echo "________________________________________________________________________"
	echo "backend-flask:"
	docker logs backend-flask -f
	echo "________________________________________________________________________"
	echo "$CONTAINER_ID"
	docker logs $CONTAINER_ID -f

scan:
	echo "Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them.	refresh browser when terminal stops outputting new logs."
	docker scan

build-front:
	docker build -t frontend-react-js ./frontend-react-js

run-front:
	docker run -p 3000:3000 -d frontend-react-js

dev2:
	make -s build-front
	open http://localhost:3000
	make -s run-front

dev3:
	# docker compose up # shows front and back but not data in front
	docker compose -f "docker-compose.yml" up -d --build

