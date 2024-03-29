# Generated by Django 2.2.7 on 2019-11-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_every'),
    ]

    operations = [
        migrations.AddField(
            model_name='every',
            name='decimal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='every',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='every',
            name='foreign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza.Ingredient'),
        ),
    ]
