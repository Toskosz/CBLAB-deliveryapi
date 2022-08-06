up:
	docker compose --env-file env up --build -d

down: 
	docker compose down

# -ti == -i -t
shell:
	docker exec -ti deliveryapi bash