# Generated by Django 4.2.7 on 2024-01-19 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teto', '0005_alter_post_options_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('thought', '感想'), ('advertisement', '宣伝')], max_length=100),
        ),
    ]
