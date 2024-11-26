# E-Commerce-Customer-Relationship 

This project implements a simple Customer and Order management system using Django. It allows you to create customers and manage orders associated with each customer.  

## Requirements  

 The following should be installed:

- Python  
- pip (Python package installer)  
- Django   

## Setup Instructions  

Follow these steps to set up the project environment:  

1. **Clone the Repository**:  

   ```bash  
   git clone https://github.com/Bakhitarose/E-Commerce-Customer-Relationship.git
   cd customer_relationship

 2. **Create a Virtual Environment**
Virtual environment to isolate project dependencies:

```bash
py -m venv .venv
```

Activate the virtual environment:
In Powershell,
 ```bash
 .\.venv\Scripts\Activate.ps1
```

3. **Install the Dependencies**:
```bash
 py -m pip install Django
```

4. **Create a Project**:
   ```bash
   django-admin startproject customer_relationship
   ```
   
5. **Running the Project**:
   ```bash
   py manage.py runserver
   ```
   Open browser (ctrl+click).
   
7. **Create App**:
   ```bash
   py manage.py startapp customer
   ```

8. **Views**
Locate the `views.py` file in the app folder.
```
#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def customer(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
```

9. **URLs**
Add a file calleed `urls.py` in the app folder.
Add:
```
from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name='customer')
]
```

10. **Create Web Page**  
Created a new folder under the customer app called _Templates_.
In Templates add a new file _index.html_ and added the expected content.
**Change settings in the _settings.py_ file of the project**:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer',
]
```
Run:
```bash
py manage.py migrate
```
(Reload server)

## Created Model
```
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer.customer')),
            ],
        ),
    ]
```

## Licence
