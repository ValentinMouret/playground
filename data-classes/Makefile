all: run

build:
	@docker build . -t data-classes

run: build
	@docker run \
	  -v $$(pwd)/src:/src \
	  -it data-classes \
	  python3 main.py
