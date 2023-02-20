help:
	echo "available commands" && cat Makefile | grep ":" |  grep -v help | xargs

flags:
	echo "-s = silent"

set:
	export $(cat .env | xargs)

check:
	cat .env

open-docker:
	open -a /Applications/Docker.app
	echo "Note Docker Desktop App takes time to open and initialize be please be patient"
	# sleep 30

open-endpoint:
	open http://localhost:4567/api/activities/home
	echo "refresh browser when terminal stops outputting new logs"

build:
	docker build -t backend-flask ./backend-flask;

run:
	docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask

dev:
	make -s open-docker && make -s build && make -s open-endpoint && make -s run

close:
	echo "terminal command to close mac application"
	pkill -x Docker	# Or: # killall Docker
	# sleep 10
