# Generated by Django 4.0 on 2023-07-28 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_attendance_salon_alter_attendance_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='inhouseproductuse',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='loyaltypointmaster',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='salaryandcommission',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='salonname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='salonownerrights',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
        migrations.AlterField(
            model_name='salonstaff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.user'),
        ),
    ]