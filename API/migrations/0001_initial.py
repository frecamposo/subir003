# Generated by Django 4.0.1 on 2022-10-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('idpersonas', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('sueldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField(db_column='userId')),
                ('title', models.CharField(max_length=45)),
                ('body', models.CharField(max_length=255)),
            ],
        ),
    ]