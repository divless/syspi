# Generated by Django 5.1.1 on 2024-10-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clientes", "0002_rename_clientes_cliente_rename_contratos_contrato_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="addr",
            field=models.TextField(verbose_name="Endereço"),
        ),
    ]
