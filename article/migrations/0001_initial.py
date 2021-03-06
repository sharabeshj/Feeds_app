# Generated by Django 2.0.3 on 2018-03-20 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('L', 'Like'), ('C', 'Comment')], max_length=1)),
                ('article', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content', models.TextField()),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('like', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('article', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to='article.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
