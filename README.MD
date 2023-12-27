# Bot.py
## Ask questions based on the telegram chat history.
1. First you need to export telegram data in json format.
2. Run `app/tg_loader.py` to create openAI embeddings & save them locally in FAIS.
3. run `bot.py`. On `/ask_question` command it would search for nearest telegram history chunks & provide them as context to chat-gpt.

# Environment

## (In Progress) HOW TO RUN LOCALLY
1. run the dependencies: (postgres) via `docker-compose up -d`
2. run the server itself:
```
pipenv shell
flask run
```

connect to database  with password `postgrespassword`
```
psql -h localhost -p 5432 -U postgres -d postgres
```

## (In progress) HOW TO BUILD THE PRODUCTION VERSION
Run `./build.sh` (and `chmod +x ./build.sh` if you can't execute it)

## (In progress) HOW TO CONFIGURE local environment
`pipenv shell` & select in VS code via cmd+shift+P -> 'python select interpretor' \
