NAME=configs

all: run

build:
	@docker build . -t ${NAME}

run: build
	@docker run \
	  -v $$(pwd)/data:/data \
	  -v $$(pwd)/src:/src \
	  ${NAME}
