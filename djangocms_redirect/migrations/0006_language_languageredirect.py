# Generated by Django 3.2.17 on 2023-09-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_redirect', '0005_auto_20210514_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_path', models.CharField(blank=True, help_text='Enter the redirect path for this language.', max_length=700, null=True, verbose_name='Redirect Path')),
                ('language_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_code', to='djangocms_redirect.language', verbose_name='Language_code')),
                ('redirect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_redirects', to='djangocms_redirect.redirect', verbose_name='Redirect')),
            ],
        ),
    ]
