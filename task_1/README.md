In the first you need to create ".env" based on .env.example. 
After you need to run migrations "alembic init migrations","alembic revision --autogenerate -m 'Init'" 
 and start docker container with command "docker compose up -d".
and server would be allowed on your host and port like this "http://localhost:8000/"