run:
	docker run -v C:\Users\axeno\OneDrive\Документы\Personal_projects\AI_Robot:/app/ai_robot --gpus device=0 -it --entrypoint /bin/bash --name ai_robot ai_robot:latest
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