from django.db import models

# Steps after creating models ->
# 1. Run migrations
# 2. Do migrate

# makemigrations - create changes and store in a file
# migrate - apply the pending changes by makemigrations -> write the changes in the DB

# Model defines your database

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def _str_(self):
        return self.name
    

# python manage.py makemigrations -> Creates a file of whatever the changes that is made in the models.py file.
# To reflect the changes two things need to do ->
# 1. Register the model in 'admin.py'
# 2. Register the app / appname from 'apps.py' in home to 'settings.py' in project
# 3. Then run the migrations

# Note: No table has been created in the Django database after running the migration command. To create the tables in the Django database we need to run the migrate command.