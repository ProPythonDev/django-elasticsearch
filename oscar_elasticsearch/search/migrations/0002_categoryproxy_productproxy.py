# Generated by Django 2.0.8 on 2019-02-07 15:49

from django.db import migrations
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=(wagtail.search.index.Indexed, 'catalogue.category'),
        ),
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=(wagtail.search.index.Indexed, 'catalogue.product'),
        ),
    ]
