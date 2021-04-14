# Generated by Django 3.1.7 on 2021-04-14 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0017_TinkoffCreditPromoCode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('slug', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('text', markdownx.models.MarkdownxField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course')),
            ],
            options={
                'verbose_name': 'Homework',
                'verbose_name_plural': 'Homeworks',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('slug', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('text', markdownx.models.MarkdownxField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.question')),
            ],
            options={
                'verbose_name': 'Homework answer',
                'verbose_name_plural': 'Homework answers',
            },
        ),
    ]
