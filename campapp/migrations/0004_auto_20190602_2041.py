# Generated by Django 2.2.1 on 2019-06-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campapp', '0003_auto_20190602_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamscheduledactivity',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='max_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='camper',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campapp.CampTeam'),
        ),
        migrations.AlterField(
            model_name='camperactivity',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teamscheduledactivity',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campapp.CampTeam'),
        ),
        migrations.DeleteModel(
            name='TeamActivity',
        ),
    ]
