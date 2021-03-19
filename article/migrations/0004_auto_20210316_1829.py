# Generated by Django 3.1.7 on 2021-03-16 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_a_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=51, verbose_name='yazar')),
                ('comment_content', models.CharField(max_length=211, verbose_name='yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='yorum_tarihi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='makale')),
            ],
        ),
    ]
