# Generated by Django 5.0.3 on 2024-03-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_name_post_title_remove_post_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dicription', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]