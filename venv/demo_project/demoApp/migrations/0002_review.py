# Generated by Django 4.1.4 on 2022-12-29 13:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoApp.project')),
            ],
        ),
    ]
