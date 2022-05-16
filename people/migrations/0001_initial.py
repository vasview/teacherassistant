# Generated by Django 4.0.3 on 2022-05-16 06:33

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Города',
                'verbose_name_plural': 'Справочник городов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Национальности',
                'verbose_name_plural': 'Справочник национальностей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Области',
                'verbose_name_plural': 'Справочник областей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(blank=True, max_length=350)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('NA', 'Не задано'), ('M', 'Мужчина'), ('F', 'Женцина')], default='NA', max_length=2)),
                ('registration_address', models.CharField(blank=True, max_length=200, null=True)),
                ('actual_address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('contact_type', models.CharField(choices=[('NON', 'Не задано'), ('STD', 'Студент'), ('PRT', 'Родитель')], default='STD', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.city')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.nationality')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.region')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Список контактов',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
