Before starting server you need to run migrations "alembic init migrations",
alembic revision --autogenerate -m 'Init'  ", "alembic upgrade head" and create ".env" based on .env.example.
Also don`t forget to create and start docker with your db if it isn't.
When you in environment you need go to "cd web_site" and use "python manage.py" to up server
