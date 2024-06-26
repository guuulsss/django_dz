# Generated by Django 5.0.4 on 2024-04-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_rename_created_ad_bugreport_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugreport',
            name='status',
            field=models.CharField(choices=[('New', 'Новая'), ('In progress', 'В работе'), ('Completed', 'Завершена')], default='New', max_length=50),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='status',
            field=models.CharField(choices=[('Review', 'Рассмотрение'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')], default='Review', max_length=50),
        ),
    ]
