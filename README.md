# Django Release Info

Show you CHANGELOG.md in your application

![screenshot of page](screenshot.png)

## How to use

Install the python package and add the app to installed apps

`pip install django-release-info`

Add you assets like logo and fonts to static files.

Add the config to settings.py

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "release_info"
]
```


```python
RELEASE_INFO = {
    "product_name": "Django Release Info",
    "author": "pragmatic minds",
    "author_url": "https://pragmaticminds.de",
    "contact_email": "info@pragmaticminds.de",
    "contact_text": "You need help or have a question?",
    "picture_path": "images/logo.svg",
    "fonts": {
        "header": {"name": "FuturaStd-Medium", "url": "fonts/FuturaStd-Medium.woff2"},
        "content" : {"name": "FuturaStd-Book", "url": "fonts/FuturaStd-Book.woff2"},
    },
}
```

Add the page URL to urls.py

```
urlpatterns = [
    .....
    path("release", include("release_info.urls")),
    ......
]
```

![screenshot of page](screenshot.png)

## Development

This repo has a test project so you can clone it and run the app.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### How to build

```bash
cd release_info
python -m build
```

###  How release

Pypi: `twine upload dist/*`
