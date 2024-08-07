# Generated by Django 5.0.7 on 2024-08-06 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContractNumber",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("contract_supplement", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "contract_number",
            },
        ),
        migrations.CreateModel(
            name="GuideClient",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("client", models.TextField(blank=True, null=True)),
                ("company_group", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_client",
            },
        ),
        migrations.CreateModel(
            name="GuideDivisions",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("division", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_divisions",
            },
        ),
        migrations.CreateModel(
            name="GuideLineOfBusiness",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("line_of_business", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_line_of_business",
            },
        ),
        migrations.CreateModel(
            name="GuideManagers",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("manager", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_managers",
            },
        ),
        migrations.CreateModel(
            name="GuideManufacturer",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("manufacturer", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_manufacturer",
            },
        ),
        migrations.CreateModel(
            name="GuideShippingWarehouses",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("shipping_warehouse", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "guide_shipping_warehouses",
            },
        ),
        migrations.CreateModel(
            name="ShippingAddress",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("client", models.TextField(blank=True, null=True)),
                ("shipping_address", models.TextField(blank=True, null=True)),
                ("contract_supplement", models.UUIDField(blank=True, null=True)),
            ],
            options={
                "db_table": "shipping_address",
            },
        ),
        migrations.CreateModel(
            name="GuideProducts",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("product", models.CharField(blank=True, null=True)),
                ("parent_element", models.TextField(blank=True, null=True)),
                ("active_ingredient", models.TextField(blank=True, null=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        blank=True,
                        db_column="manufacturer",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidemanufacturer",
                    ),
                ),
            ],
            options={
                "db_table": "guide_products",
            },
        ),
        migrations.CreateModel(
            name="AvailableStocks",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("available", models.TextField(blank=True, null=True)),
                (
                    "division",
                    models.ForeignKey(
                        blank=True,
                        db_column="division",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidedivisions",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        db_column="product",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideproducts",
                    ),
                ),
            ],
            options={
                "db_table": "available_stocks",
            },
        ),
        migrations.CreateModel(
            name="NomenclatureSeries",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("nomenclature_series", models.TextField(blank=True, null=True)),
                ("mtn", models.FloatField(blank=True, null=True)),
                ("origin_country", models.TextField(blank=True, null=True)),
                ("germination", models.BigIntegerField(blank=True, null=True)),
                ("crop_year", models.BigIntegerField(blank=True, null=True)),
                ("quantity_per_pallet", models.TextField(blank=True, null=True)),
                ("weight", models.TextField(blank=True, null=True)),
                ("certificate_start_date", models.TextField(blank=True, null=True)),
                ("certificate_end_date", models.TextField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        db_column="product",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideproducts",
                    ),
                ),
            ],
            options={
                "db_table": "nomenclature_series",
            },
        ),
        migrations.CreateModel(
            name="MovedProducts",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("qt_moved", models.TextField(blank=True, null=True)),
                ("order", models.TextField(blank=True, null=True)),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        db_column="contract",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.contractnumber",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        db_column="product",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideproducts",
                    ),
                ),
                (
                    "series",
                    models.ForeignKey(
                        blank=True,
                        db_column="series",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.nomenclatureseries",
                    ),
                ),
            ],
            options={
                "db_table": "moved_products",
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("contract_type", models.TextField(blank=True, null=True)),
                ("prepayment_amount", models.FloatField(blank=True, null=True)),
                ("amount_of_credit", models.FloatField(blank=True, null=True)),
                ("prepayment_percentage", models.FloatField(blank=True, null=True)),
                ("loan_percentage", models.FloatField(blank=True, null=True)),
                ("planned_amount", models.FloatField(blank=True, null=True)),
                (
                    "planned_amount_excluding_vat",
                    models.FloatField(blank=True, null=True),
                ),
                ("actual_sale_amount", models.FloatField(blank=True, null=True)),
                ("actual_payment_amount", models.FloatField(blank=True, null=True)),
                (
                    "contract_supplement",
                    models.ForeignKey(
                        blank=True,
                        db_column="contract_supplement",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.contractnumber",
                    ),
                ),
            ],
            options={
                "db_table": "payment",
            },
        ),
        migrations.CreateModel(
            name="Remains",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("warehouse", models.TextField(blank=True, null=True)),
                ("buh", models.FloatField(blank=True, null=True)),
                ("skl", models.FloatField(blank=True, null=True)),
                (
                    "line_of_business",
                    models.ForeignKey(
                        blank=True,
                        db_column="line_of_business",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidelineofbusiness",
                    ),
                ),
                (
                    "nomenclature_series",
                    models.ForeignKey(
                        blank=True,
                        db_column="nomenclature_series",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.nomenclatureseries",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        db_column="product",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideproducts",
                    ),
                ),
            ],
            options={
                "db_table": "remains",
            },
        ),
        migrations.CreateModel(
            name="Submissions",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("period", models.BigIntegerField(blank=True, null=True)),
                ("shipping_warehouse", models.TextField(blank=True, null=True)),
                ("shipping_address", models.UUIDField(blank=True, null=True)),
                ("plan", models.FloatField(blank=True, null=True)),
                ("fact", models.FloatField(blank=True, null=True)),
                ("different", models.FloatField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        db_column="client",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideclient",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        db_column="contract",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.contractnumber",
                    ),
                ),
                (
                    "line_of_business",
                    models.ForeignKey(
                        blank=True,
                        db_column="line_of_business",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidelineofbusiness",
                    ),
                ),
                (
                    "manager",
                    models.ForeignKey(
                        blank=True,
                        db_column="manager",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidemanagers",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        blank=True,
                        db_column="manufacturer",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guidemanufacturer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        db_column="product",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EridonKh.guideproducts",
                    ),
                ),
            ],
            options={
                "db_table": "submissions",
            },
        ),
    ]