# Run with flask

1. Install virtualenv

```
pip install virtualenv
```

2. Create virtualenv

```
virtualenv venv
```

3. Activate virtualenv

```
source venv/bin/activate
```

4. Install requirements

```
pip3 install -r requirements.txt
```

5. Run

```
set FLASK_APP=app.py
.\venv\Scripts\flask run
```

# Run with docker

```
docker-compose up -d --buid
```

# link swagger

http://127.0.0.1:5002/apidocs/
