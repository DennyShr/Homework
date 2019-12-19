# Generated by Django 2.2.7 on 2019-12-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0002_auto_20191209_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishes_order', models.ManyToManyField(related_name='dishes', to='dishes.InstanceDish')),
            ],
        ),
    ]
