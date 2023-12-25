pipenv run pip freeze > requirements.txt
docker build -t khargol .
docker run -p 5000:5000 khargol