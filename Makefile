help:
	echo "available commands" && cat Makefile | grep ":" |  grep -v help | xargs

flags:
	echo "-s = silent"

set:
	export $(cat .env | xargs)

check:
	cat .env

