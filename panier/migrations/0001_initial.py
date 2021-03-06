# Generated by Django 3.1.5 on 2021-01-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chariot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name="Image de l'article")),
                ('nom_article_commande', models.CharField(max_length=255, null=True, verbose_name="nom de l'article")),
                ('prix_article', models.IntegerField(null=True, verbose_name="prix de l'article")),
                ('quantite', models.IntegerField(default=0, null=True, verbose_name='quantite commandé')),
                ('total', models.IntegerField(default=0, null=True, verbose_name="Prix total de l'article commandé")),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
