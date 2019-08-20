all: run

build:
	@docker build . -t memory-debug

run: build
	@docker run \
	  -v $$(pwd)/src:/src \
	  -v $$(pwd)/data:/data \
	  -it memory-debug \
	  python3 debug.py
