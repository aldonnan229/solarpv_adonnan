# Generated by Django 3.0.4 on 2020-05-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarpv', '0002_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address_1',
            field=models.CharField(default='12 office road.', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='address_2',
            field=models.CharField(default='unit 2', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default='spartanburg', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.CharField(default='USA', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='fax_number',
            field=models.CharField(default=12758693, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default=2298699044, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(default='SC', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='zipcode',
            field=models.IntegerField(default=29302),
            preserve_default=False,
        ),
    ]
