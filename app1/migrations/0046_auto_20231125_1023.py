# Generated by Django 3.2.22 on 2023-11-25 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0045_employee_loan_tran_balance_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bankacc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cheq_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='creditcard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='upi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paymentitems',
            name='invtype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='DeletedPaymentReceived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referno', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedChallan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
