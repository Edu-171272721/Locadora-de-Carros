# Generated by Django 5.1.2 on 2024-10-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='veiculos/'),
        ),
    ]
