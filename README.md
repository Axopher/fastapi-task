# To Run the project:
1. Create virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
2. Install requirements:
```
pip install -r requirements.txt
```
3. Setup Mysql DB using docker:
```
docker run --name fastapi-mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=fastapi_db \
  -e MYSQL_USER=fastapi_user \
  -e MYSQL_PASSWORD=fastapi_pass \
  -p 3306:3306 \
  -d mysql:8.0
```
4. Migrate Tables:
```
python create_tables.py
```
5. Run Project:
```
uvicorn app.main:app --reload
```

*** Please don't mind as I have hardcoded the environment variables for now. ***
