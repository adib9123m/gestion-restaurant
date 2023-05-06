# Generated by Django 4.2 on 2023-04-15 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Tanger', 'Tanger'), ('Tétouan', 'Tétouan'), ('Chefchaouen', 'Chefchaouen'), ('Fnideq', 'Fnideq'), ('Oujda', 'Oujda'), ('Nador', 'Nador'), ('Berkane', 'Berkane'), ('Ifrane', 'Ifrane'), ('Azrou', 'Azrou'), ('Rabat', 'Rabat'), ('Temara', 'Temara'), ('Azilal', 'Azilal'), ('Casablanca', 'Casablanca'), ('Settat', 'Settat'), ('Mohammedia', 'Mohammedia'), ('Bouskoura', 'Bouskoura'), ('Marrakech', 'Marrakech')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
