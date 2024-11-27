#Overview
**[Get Start with Django](https://docs.chaicode.com/getting-started-with-django/)** &nbsp;&nbsp;&nbsp;&nbsp;[Ignore UV and go with regular pip.]

- What is Django?

        Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

        Django is a full-featured web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a set of tools and libraries for building web applicationss, including an ORM, a templating engine, and a built-in admin interface

 - Environment Setup  <br/>

        python3 -m venv .venv
        source .venv/bin/activate

        pip install django
        pip install -r requirements.txt


 - Django Project  <br/>

        django-admin startproject chaiaurdjango
        cd chaiaurdjango

 - Start a Django Server  <br/>

        python manage.py runserver

 - Creating our first views  <br/>

        <!-- Views.py -->
        from django.http import HttpResponse

        def home(request):
            return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")

        def about(request):
            return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

        def contact(request):
            return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")

        <!-- urls.py -->
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.home, name='home'),
            path('about/', views.about, name='about'),
            path('contact/', views.contact, name='contact'),
        ]

 - Adding Templates  <br/>

        <!DOCTYPE html>
        <html>
        <head>
            <title>Welcome to Chai's Django Project</title>
        </head>
        <body>
            <h1>Welcome to Chai's Django Project</h1>
        </body>
        </html>

 - Adding CSS and JavaScript  <br/>

        import os # at the top of settings.py
        'DIRS': ['templates'], # inside template section

        STATIC_URL = '/static/' # below this add the following line
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

        {% load static %} #In the index.html file, add the following line, at the top of the file:
        <link rel="stylesheet" href="{% static 'css/style.css' %}">

        <!-- Edit Views.py -->
        from django.shortcuts import render

        def home(request):
            return render(request, 'index.html')

 - Conclusion  <br/>
<br/>


---

**[Jinja2 Basics](https://docs.chaicode.com/jinja-templates-app-in-django/)**

 - Introduction  <br/>
 - Installation  <br/>
 - Common Template Tags  <br/>
 - % if %  <br/>
 - {% for %}  <br/>
 - {% block %}  <br/>
 - {% include %}  <br/>
 - {% extends %}  <br/>
 - {% load %}  <br/>
 - {% static %}  <br/>
 - {% url %}  <br/>
 - Apps in Django  <br/>
 - Templates in Apps and layout extension  <br/>
 - Common Layout for all pages  <br/>
 - Conclusion  <br/>
<br/>


---


**[Tailwind Installation](https://docs.chaicode.com/tailwind-to-django/)**

 - Install Tailwind CSS in your Django project <br/>
 - Hot Reloading <br/>
 - Enable the admin panel in Django <br/>
 - Conclusion <br/>


---

**[Django Models](https://docs.chaicode.com/django-models/)**

 - Defining a model <br>
 - Adding data to the database <br>
 - Creating a view to display the data <br>
 - Get data in the template <br>
 - Adding description to the model and details page <br>
 - Adding a details view <br>
 - Configuring the urls.py file <br>
 - Create chai_detail.html template <br>
 - Conclusion <br>
<br/>

---

**[Relationships and Forms](https://docs.chaicode.com/relationships-and-forms/)**

<th>Relationships in Django<th/>
    <br>&nbsp;&nbsp;&nbsp;&nbsp; -One-to-many
    <br>&nbsp;&nbsp;&nbsp;&nbsp; -Many-to-many
    <br>&nbsp;&nbsp;&nbsp;&nbsp; -one-to-one<br>
    <br>
<th>Update the admin<th/><br><br>

Adding a form on frontend<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;- Handle the view for the form<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Add the template<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Update the urls<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Run the server<br>
<br>Conclusion<br>


---
