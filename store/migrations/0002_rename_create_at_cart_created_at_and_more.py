# Generated by Django 4.1.5 on 2023-01-13 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='create_at',
            new_name='placed_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update_at',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='promotion',
            new_name='promotions',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='creat_at',
        ),
        migrations.AddField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1),
        ),
    ]