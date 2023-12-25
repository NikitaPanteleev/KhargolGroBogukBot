

# HOW TO RUN LOCALLY
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

# HOW TO BUILD THE PRODUCTION VERSION
Run `./build.sh` (and `chmod +x ./build.sh` if you can't execute it)

# HOW TO CONFIGURE ENG
`pipenv shell` & select in VS code via cmd+shift+P -> 'python select interpretor' \
