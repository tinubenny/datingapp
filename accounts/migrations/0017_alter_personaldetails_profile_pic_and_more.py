# Generated by Django 4.2.15 on 2024-09-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_customuser_additional_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='relationship_goals',
            field=models.CharField(blank=True, choices=[('long_term', 'long_term'), ('short_term', 'short_term')], default='', max_length=25, null=True),
        ),
    ]