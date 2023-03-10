# Generated by Django 3.0.14 on 2022-12-30 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Tytuł książki.', max_length=70)),
                ('publication_date', models.DateField(verbose_name='Data publikacji książki.')),
                ('isbn', models.CharField(max_length=20, verbose_name='Numer ISBN książki.')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(help_text='Imiona współtwórców.', max_length=50)),
                ('last_names', models.CharField(help_text='Nazwiska współtwórców.', max_length=90)),
                ('email', models.EmailField(help_text='Adres e-mail współtwórcy', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Tekst Recenzji.')),
                ('rating', models.IntegerField(help_text='Ocena użytkownika.')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Data i czas utworzenia recenzji.')),
                ('date_edited', models.DateTimeField(help_text='Data i czas ostatniej edycji recenzji.', null=True)),
                ('book', models.ForeignKey(help_text='Recenzowana książka.', on_delete=django.db.models.deletion.CASCADE, to='reviews.Book')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookContributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='Rola współtwórcy w książce')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Book')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Contributor')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(through='reviews.BookContributor', to='reviews.Contributor'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Publisher'),
        ),
    ]
