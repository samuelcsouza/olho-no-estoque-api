run-local:
	docker-compose -f docker-compose-db.yml down
	docker-compose -f docker-compose-db.yml stop
	docker-compose -f docker-compose-db.yml build --force-rm
	docker-compose -f docker-compose-db.yml up