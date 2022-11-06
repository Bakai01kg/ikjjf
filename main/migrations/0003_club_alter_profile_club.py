# Generated by Django 4.1.2 on 2022-11-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.club'),
        ),
    ]
