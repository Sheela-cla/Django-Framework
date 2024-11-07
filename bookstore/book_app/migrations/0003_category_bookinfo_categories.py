# Generated by Django 5.0.4 on 2024-05-19 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_bookinfo_publication_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='categories',
            field=models.ManyToManyField(related_name='bookinfos', to='book_app.category'),
        ),
    ]
