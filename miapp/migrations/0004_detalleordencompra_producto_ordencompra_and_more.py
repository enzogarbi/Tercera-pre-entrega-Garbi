# Generated by Django 4.2.3 on 2023-07-30 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_delete_usuario_alter_proveedor_insumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleOrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cantidad_disponible', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.cliente')),
                ('productos', models.ManyToManyField(through='miapp.DetalleOrdenCompra', to='miapp.producto')),
            ],
        ),
        migrations.AddField(
            model_name='detalleordencompra',
            name='orden_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.ordencompra'),
        ),
        migrations.AddField(
            model_name='detalleordencompra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.producto'),
        ),
    ]
