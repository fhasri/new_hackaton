# Generated by Django 4.2.1 on 2023-05-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
