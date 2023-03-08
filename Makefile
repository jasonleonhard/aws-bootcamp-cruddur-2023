SHELL := /bin/zsh
.SILENT:

help:
	clear
	make gotchas
	make line
	echo "make ____ # make run any below method"
	cat Makefile | grep ":$$" | grep -v "^#" | grep -v "^\ " | grep -v "^\." | tr -d ":" | sort | xargs; # IN MAKEFILE
	# cat Makefile | grep ":$" | grep -v "^#" | grep -v "^\ " | grep -v "^\." | tr -d ":" | sort | xargs; # NOT A MAKEFILE

gotchas:
	echo "CAREFUL you must signin to see all content"
	echo "CAREFUL you cannot have commented code inside a method unless its the last line even if backslash escaped"
	echo "CAREFUL notice check-yourself requires back slash escapes bc of the conditional. The last line backslash is optional"
	echo "CAREFUL"

check-yourself:
	if [[ $$(whoami) = "gitpod" ]]; then \
		echo "you are gitpod"; \
	else \
		echo "you are local"; \
	fi; \

example:
	echo "Notice that none of these commands require any backslash at all"
	echo "Probably bc no conditional. Even the make commands do not require them."
	make check-yourself
	make check-yourself && make check-yourself

shell:
	echo $(SHELL)

browsers:
	if [[ $$(whoami) = "gitpod" ]]; then \
		echo "you are gitpod"; \
		gp preview --external "https://3000-jasonleonha-awsbootcamp-f5djeabluiq.ws-us89b.gitpod.io"; \
		gp preview --external "https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-us89b.gitpod.io/api/activities/home"; \
	else \
		echo "local"; \
		open "http://localhost:3000/"; \
		open "http://localhost:4567/api/activities/home"; \
	fi; \
	# gp preview $(FRONTEND_URL); # note must be last line of method or breaks

ref:
	open https://docs.oracle.com/cd/E19504-01/802-5880/6i9k05dhe/index.html

line:
	echo "_______________________________________"

user:
	clear
	git config  --local user.name  "Jason Leonhard"
	git config  --local user.email "jasonleonhard@users.noreply.github.com"
	git config --global user.name  "Jason Leonhard"
	git config --global user.email "jasonleonhard@users.noreply.github.com"
	echo "global"
	git config --list --global | grep user
	echo "local"
	git config --list --local | grep user

stop:
	docker-compose down
	make rm-imgs

imgs:
	if [[ $$(whoami) = "gitpod" ]]; then \
		echo "you are gitpod"; \
	else \
		echo "you are local"; \
		echo "REMEMBER To view images docker app must be open first when local"; \
		make open-docker; \
	fi; \
	docker images

ps:
	docker ps # List containers

down:
	make stop

start:
	make user
	make browsers
	echo "be patient, creating 5 docker containers, browsers need a moment to render"

	# Start Docker Compose services
	docker compose -f "docker-compose.yml" up -d --build
	# docker-compose up -d
	# docker-compose up --build
	# docker-compose up

up:
	make start

restart-back:
	docker restart backend-flask

restart:
	docker restart $(docker ps -q)

restart2:
	make stop
	make start

clean:
	docker-compose down -v

rm-imgs:
	docker rmi $$(docker images -a -q) # if 	in Makefile
	# docker rmi $(docker images -a -q)  # if Not in Makefile
	docker images

rm-imgs2:
	docker image prune -a -f

who:
	whoami
	if [[ $(shell whoami) == "gitpod" ]]; then \
		echo "you are gitpod"; \
	else \
		echo "local"; \
	fi;

open-docker:
	open -a /Applications/Docker.app
	echo "PATIENCE Docker Desktop App takes time to open and initialize"
	# sleep 30

close-docker:
	echo "PATIENCE Docker Desktop App takes time to close"
	# killer docker
	osascript -e "quit app \"Docker\""

	# killall docker
	# osascript -e "quit app /Applications/Docker.app"

todo:
	echo "activity_avatar not showing user"

docker-helper:
	echo "if docker is not opening or not respoding consider killing it # make close-docker"
	make open-docker
	psql -h localhost # bc docker containerized
	echo "# consider removing images # make rm-imgs # or make rm-imgs2;"

# open-browsers:
# 	open -a 'google chrome' http://localhost:3000/
# 	# open -a 'google chrome' http://localhost:4567/
# 	open -a 'google chrome' http://localhost:4567/api/activities/home
# 	# open -a 'google chrome' http://localhost:4567/api/activities/notifications

# flags:
# 	echo "-s = silent"

# honeycomb:
# 	echo "https://ui.honeycomb.io/jl-2c/environments/bootcamp/send-data#"
# 	pip install opentelemetry-api \
# 		opentelemetry-sdk \
# 		opentelemetry-exporter-otlp-proto-http \
# 		opentelemetry-instrumentation-flask \
# 		opentelemetry-instrumentation-requests
# 	# [notice] A new release of pip available: 22.3.1 -> 23.0.1
# 	# [notice] To update, run: pip install --upgrade pip
# 	pip intall --upgrade pip

# set-env:
# 	# each level can be set individually via
# 	export $(cat .env | grep -v "^#" | xargs)
# 	# then checked via 							env | grep -i honey # or other variable
# 	# ignore bash: export: `#': not a valid identifier
# 	# cd backend-flask \
# 	# export $(cat .env | grep -v "^#" | xargs) \
# 	# cd ..

# check:
# 	cat .env

# install-back:
# 	# Defaulting to user installation because normal site-packages is not writeable
# 	pip install -r ./backend-flask/requirements.txt
# 	/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pi
# 	# python3.11 -m pip install --upgrade pip # pip==21.0.1 to pip==21.3.1
# 	python3 -m pip install --upgrade pip # pip==21.0.1 to pip==21.3.1

# install-front:
# 	# this presumes you have already setup nvm such as # nvm install --lts; nvm use --lts; node -v; # v18.14.1
# 	cd frontend-react-js; \
# 	npm i; \
# 	npm audit; \
# 	npm audit fix; \
# 	npm audit; \
# 	cd ..; \
# 	# npm i ./frontend-react-js
# 	# npm i ./frontend-react-js/package.json # does this work instead?

# reinstall-front:
# 	rm -rf node_modules; \
# 	npm i;

# open-endpoint:
# 	open http://localhost:4567/api/activities/home
# 	echo "refresh browser when terminal stops outputting new logs"

# build-back:
# 	docker build -t backend-flask ./backend-flask; # without tag

# build-back-tag:
# 	docker build -t backend-flask/latest:my-tag ./backend-flask; #  with tag

# run-back:
# 	docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask # will produce dangling iamges
# 	# docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask

# dev:
# 	# make open-docker && make build-back && make open-endpoint && make run
# 	make set-env && make install-back && make install-front && make build-front && make open-endpoint && make open-docker && make build-back && make run-back 		# && make run-front

# front:
# 	open http://localhost:3000
# 	docker run -p 3000:3000 -d frontend-react-js

# close:
# 	echo "terminal command to close mac application"
# 	pkill -x Docker	# Or: # killall Docker
# 	# sleep 10

# img:
# 	echo "IMAGES:"
# 	docker images

# img2:
# 	echo "IMAGES:"
# 	docker images --no-trunc -a

# ps:
# 	echo "PS:"
# 	docker ps

# ps2:
# 	echo "PS:"
# 	docker ps --no-trunc -a

# info:
# 	echo "________________________________________________________________________"
# 	make img
# 	echo "________________________________________________________________________"
# 	make ps
# 	echo "________________________________________________________________________"

# info2:
# 	echo "________________________________________________________________________"
# 	make img2
# 	echo "________________________________________________________________________"
# 	make ps2
# 	echo "________________________________________________________________________"

# info3:
# 	clear
# 	make info
# 	make info2

# home:
# 	curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json" | jq

# groups:
# 	curl -X GET http://localhost:4567/api/message_groups -H "Accept: application/json" -H "Content-Type: application/json" | jq

# logs:
# 	echo "________________________________________________________________________"
# 	echo "CONTAINER_ID:"
# 	docker logs CONTAINER_ID -f
# 	echo "________________________________________________________________________"
# 	echo "backend-flask:"
# 	docker logs backend-flask -f
# 	echo "________________________________________________________________________"
# 	echo "$CONTAINER_ID"
# 	docker logs $CONTAINER_ID -f

# scan:
# 	echo "Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them.	refresh browser when terminal stops outputting new logs."
# 	docker scan

# build-front:
# 	docker build -t frontend-react-js ./frontend-react-js

# run-front:
# 	docker run -p 3000:3000 -d frontend-react-js

# dev2:
# 	make build-front
# 	open http://localhost:3000
# 	make run-front

# dev3:
# 	# docker compose up # shows front and back but not data in front
# 	docker compose -f "docker-compose.yml" up -d --build

