# Generated by Django 4.0 on 2022-02-13 22:41

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', markdownx.models.MarkdownxField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'posts',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('comment_text', markdownx.models.MarkdownxField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'verbose_name_plural': 'comments',
                'ordering': ['-created'],
            },
        ),
    ]