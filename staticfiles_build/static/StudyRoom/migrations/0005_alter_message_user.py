# Generated by Django 4.1.5 on 2024-03-16 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyRoom', '0004_alter_message_options_message_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
