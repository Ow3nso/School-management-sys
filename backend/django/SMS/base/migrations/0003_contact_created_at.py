# Generated by Django 5.0 on 2023-12-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_contact_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default="2023-03-17T00:04:32"
            ),
            preserve_default=False,
        ),
    ]
