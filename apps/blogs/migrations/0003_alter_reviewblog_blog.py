# Generated by Django 4.1.7 on 2023-06-08 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_backgroung_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewblog',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_blog', to='blogs.blog', verbose_name='Блог'),
        ),
    ]
