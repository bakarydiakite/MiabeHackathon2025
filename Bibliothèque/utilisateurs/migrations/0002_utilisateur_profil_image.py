# Generated by Django 5.2 on 2025-04-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='profil_image',
            field=models.ImageField(null=True, upload_to='img_profile'),
        ),
    ]
