# Generated by Django 3.0.1 on 2019-12-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=96)),
                ('no_of_tasks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=96)),
                ('pwrd', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('of_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.List')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='of_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.User'),
        ),
    ]
