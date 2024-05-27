# Django - Understanding the differences between veiws and urls

This is my project helps in understanding how start django project for the first time,
and the differencies between veiws and urls

## Table of contents

- [Overview](#overview)
  - [What is Django](#What-is-Django)
  - [Requirements](#requirement)
- [My process](#my-process)
  - [Challenges](#challenges)
   
## Overview

In this project you will understand Django, how to get stated with Django and the differences between veiws and urls

### What-is-Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Requirements

1. Install the latest version of python
2. Install django
3. You must have the basic understanding of python

### Links

- Django Doc: [https://www.djangoproject.com/]
 

## My process

1. To start a django project you first need a virtal enviroment which helps in storing our dependencies we need for our project

```
  python -m venv venv
```

2. Activate virtual environment

```
   venv\Scripts\activate
```

3. Install Django

```
  pip install django
```

4. Start project by using this command

```
   django-admin startproject (projectname)
```

5. Start server by typing

```
  python manage.py runserver
```

6. Django consist of projects and multiple apps, create your app

```
   django-admin startapp (appName)
```

7. In your project folder there'sa file called setting.py,
   open it and navigate Installed_apps and add the name of your app

8. In your project folder you have a file called urls.py and in your apps folder you will have views.py
   these files works as for examples: when you go to a restaurant you make your order (url) and the waiter will deliver
   what you ordered (views), That's how this concept works in django.

   8.i. Open veiws.py

   ```
    from django.shortcuts import render,HttpResponse


      # Create your views here.

      def index(request):
      return HttpResponse("Hello world, i'm soo exited")
   ```

   8.ii. open urls.py

   ```
    from django.urls import path
    from my_app.views import index,about,hello,my_age


    # from my_app.views import about

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    ]
   ```

 