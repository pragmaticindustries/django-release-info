# django release info app

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