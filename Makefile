up:
	docker-compose up -d

down:
	docker-compose down

login:
	$(eval TARGET := $(shell docker-compose ps -q))
	docker exec -it $(TARGET) bash