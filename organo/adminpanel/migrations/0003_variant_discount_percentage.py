# Generated by Django 4.2.3 on 2023-08-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Discount percentage for this variant (e.g., 10.50 for 10.50% off).', max_digits=5),
        ),
    ]
