# Quiz 3 — Django Model → View → URL → Template Demo

A minimal Django app showing how a Model, View, URL, and Template connect.
The app is called `main` and manages a simple `Student` model.

## Project structure

```
quiz3_django/
├── manage.py
├── requirements.txt
├── config/                 # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── main/                   # the app
    ├── models.py           # Student model
    ├── views.py            # home() view
    ├── urls.py             # app routes
    ├── admin.py            # admin registration
    ├── migrations/         # includes 3 auto-loaded sample students
    └── templates/main/home.html
```

## 1. Run it locally

```bash
# create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# install Django
pip install -r requirements.txt

# create the database tables (this also inserts 3 sample students
# automatically via a data migration — no manual step needed)
python manage.py makemigrations
python manage.py migrate

# (optional) create an admin account to add/edit students yourself
python manage.py createsuperuser

# run the dev server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** to see the student list, and
**http://127.0.0.1:8000/admin/** to manage records.

## 2. How the pieces connect

1. **Model** (`main/models.py`) — defines the `Student` table.
2. **View** (`main/views.py`) — `home()` pulls all `Student` rows and passes
   them to a template.
3. **URL** — `main/urls.py` maps `''` to the `home` view; `config/urls.py`
   includes `main.urls` under the site root.
4. **Template** (`main/templates/main/home.html`) — receives `students` and
   `total_students` from the view's context and renders them as a styled
   HTML table.

## 3. Push to GitHub

```bash
git init
git add .
git commit -m "Quiz 3: Django Model-View-URL-Template demo"
git branch -M main
git remote add origin https://github.com/<your-username>/quiz3-django.git
git push -u origin main
```

`.gitignore` already excludes `venv/` and `db.sqlite3`, so only source code
is uploaded.

## 4. Deploy on PythonAnywhere

1. Create a free PythonAnywhere account.
2. Open a **Bash console** and clone your repo:
   ```bash
   git clone https://github.com/<your-username>/quiz3-django.git
   ```
3. Create a virtualenv and install requirements:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 quiz3-env
   pip install -r quiz3-django/requirements.txt
   ```
4. Go to the **Web** tab → **Add a new web app** → **Manual configuration**
   (choose the Python version matching your virtualenv).
5. Set:
   - **Source code**: path to the cloned `quiz3-django` folder.
   - **Virtualenv**: path to `quiz3-env`.
   - **WSGI configuration file**: edit it so it points to
     `config.wsgi.application` (mirror the content of `config/wsgi.py`,
     adjusting `sys.path` to include your project folder).
6. In a Bash console, run migrations inside the project folder:
   ```bash
   cd quiz3-django
   python manage.py migrate
   python manage.py createsuperuser
   ```
7. Reload the web app from the **Web** tab, then open your
   `https://<your-username>.pythonanywhere.com` URL to test it.

## 5. Submit

- PythonAnywhere link (your live app)
- GitHub link (this source code)
