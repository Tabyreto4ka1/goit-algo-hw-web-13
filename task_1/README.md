In the first you need to create and start docker container with command "docker compose up -d".
After you need to create ".env" based on .env.example and do migrations in your db.
In the end just use "uvicorn main:app --host localhost --port 8000 --reload"
and server would be allowed on your host and port like this "http://localhost:8000/"