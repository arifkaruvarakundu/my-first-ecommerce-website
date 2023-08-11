# Generated by Django 4.2.3 on 2023-08-01 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminpanel', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('payment_status', models.CharField(choices=[('PENDING', 'pending'), ('PAID', 'paid'), ('CANCELLED', 'cancelled'), ('DELIVERED', 'Delivered'), ('SHIPPED', 'Shipped')], default='ordered', max_length=20)),
                ('payment_method', models.CharField(choices=[('PAYPAL', 'PayPal'), ('CASH_ON_DELIVERY', 'Cash on Delivery')], max_length=20)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('razor_pay_order_id', models.CharField(blank=True, max_length=150, null=True)),
                ('razor_pay_payment_id', models.CharField(blank=True, max_length=150, null=True)),
                ('razor_pay_payment_signature', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.variant')),
            ],
        ),
    ]
