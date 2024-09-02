# flying-flask-app
Basic Flask app that runs on fly.io, for full deployment example visit my [blog post](https://foxsy.dev/blog/deploying-flask-app-flyio/)

# Create a virtual env
```
python -m .venv ./
```

# Activate python venv
```
source ./.venv/bin/activate
```

# Install requirements
```
pip install -r requirements.txt
```

# Run Flask App
```
python3 -m flask run --host=127.0.0.1 --port=8080
```
or
```
./start-local-env.sh
```
