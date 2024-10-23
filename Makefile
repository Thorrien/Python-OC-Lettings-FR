IMAGE_NAME=thorrien/oc_lettings_build
COMMIT_HASH=$(shell git rev-parse --short HEAD)

build:
	docker build -t $(IMAGE_NAME):$(COMMIT_HASH) .

push: build
	docker push $(IMAGE_NAME):$(COMMIT_HASH)

deploy: push
	@echo "L'image $(IMAGE_NAME):$(COMMIT_HASH) construite et poussee avec succes."

run:
	docker run -d -p 8000:8000 $(IMAGE_NAME):$(COMMIT_HASH)

all: deploy run
	@echo "Le projet a été construit, déployé et exécuté avec succès."

clean:
	docker rmi $(IMAGE_NAME):$(COMMIT_HASH)