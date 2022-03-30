# Generated by Django 4.0.1 on 2022-03-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
                ('loan_amount', models.IntegerField()),
                ('amount_paid', models.IntegerField()),
            ],
        ),
    ]
