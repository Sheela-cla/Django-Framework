# Generated by Django 5.0.6 on 2024-05-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('location', models.CharField(choices=[('alvik', 'ALVIK'), ('axelsberg', 'AXELSBERG'), ('akalla', 'AKALLA'), ('sickla', 'SICKLA'), ('ropsten', 'ROPSTEN'), ('vällingby', 'VÄLLINGBY'), ('solna', 'SOLNA'), ('barkarby', 'BARKARBY'), ('stockholmcity', 'STOCKHOLMCITY')], default='STOCKHOLMCITY', max_length=50)),
                ('miles', models.IntegerField()),
                ('passengers', models.IntegerField()),
                ('no_of_owners', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
