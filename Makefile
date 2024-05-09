run:
	docker run -v /Users/artem/Documents/AI_Robot:/app/ai_robot -it --entrypoint /bin/bash --name ai_robot ai_robot:latest
build:
	docker build . -t ai_robot
stop:
	docker stop ai_robot

start: 
	docker start -ai ai_robot

remove:
	docker rm ai_robot


chat:
	python src/chat/chat.py

venv:
	source ai_robot/bin/activate