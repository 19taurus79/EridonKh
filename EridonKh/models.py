# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContractNumber(models.Model):
    id = models.UUIDField(primary_key=True)
    contract_supplement = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "contract_number"

    def __str__(self):
        return self.contract_supplement


class GuideClient(models.Model):
    id = models.UUIDField(primary_key=True)
    client = models.TextField(blank=True, null=True)
    company_group = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_client"

    def __str__(self):
        return self.client


class GuideDivisions(models.Model):
    id = models.UUIDField(primary_key=True)
    division = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_divisions"

    def __str__(self):
        return self.division


class GuideLineOfBusiness(models.Model):
    id = models.UUIDField(primary_key=True)
    line_of_business = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_line_of_business"

    def __str__(self):
        return self.line_of_business


class GuideManagers(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_managers"

    def __str__(self):
        return self.manager


class GuideManufacturer(models.Model):
    id = models.UUIDField(primary_key=True)
    manufacturer = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_manufacturer"

    def __str__(self):
        return self.manufacturer


class GuideProducts(models.Model):
    id = models.UUIDField(primary_key=True)
    product = models.CharField(blank=True, null=True)
    manufacturer = models.ForeignKey(
        GuideManufacturer,
        models.DO_NOTHING,
        db_column="manufacturer",
        blank=True,
        null=True,
    )
    parent_element = models.TextField(blank=True, null=True)
    active_ingredient = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_products"

    def __str__(self):
        return self.product


class GuideShippingWarehouses(models.Model):
    id = models.UUIDField(primary_key=True)
    shipping_warehouse = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "guide_shipping_warehouses"

    def __str__(self):
        return self.shipping_warehouse


class MovedProducts(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ContractNumber, models.DO_NOTHING, db_column="contract", blank=True, null=True
    )
    product = models.ForeignKey(
        GuideProducts, models.DO_NOTHING, db_column="product", blank=True, null=True
    )
    qt_moved = models.TextField(blank=True, null=True)
    series = models.ForeignKey(
        "NomenclatureSeries",
        models.DO_NOTHING,
        db_column="series",
        blank=True,
        null=True,
    )
    order = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "moved_products"


class NomenclatureSeries(models.Model):
    id = models.UUIDField(primary_key=True)
    product = models.ForeignKey(
        GuideProducts, models.DO_NOTHING, db_column="product", blank=True, null=True
    )
    nomenclature_series = models.TextField(blank=True, null=True)
    mtn = models.FloatField(blank=True, null=True)
    origin_country = models.TextField(blank=True, null=True)
    germination = models.BigIntegerField(blank=True, null=True)
    crop_year = models.BigIntegerField(blank=True, null=True)
    quantity_per_pallet = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    certificate_start_date = models.TextField(blank=True, null=True)
    certificate_end_date = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "nomenclature_series"

    def __str__(self):
        return self.nomenclature_series


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    contract_supplement = models.ForeignKey(
        ContractNumber,
        models.DO_NOTHING,
        db_column="contract_supplement",
        blank=True,
        null=True,
    )
    contract_type = models.TextField(blank=True, null=True)
    prepayment_amount = models.FloatField(blank=True, null=True)
    amount_of_credit = models.FloatField(blank=True, null=True)
    prepayment_percentage = models.FloatField(blank=True, null=True)
    loan_percentage = models.FloatField(blank=True, null=True)
    planned_amount = models.FloatField(blank=True, null=True)
    planned_amount_excluding_vat = models.FloatField(blank=True, null=True)
    actual_sale_amount = models.FloatField(blank=True, null=True)
    actual_payment_amount = models.FloatField(blank=True, null=True)
    paid = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = "payment"


class Remains(models.Model):
    id = models.UUIDField(primary_key=True)
    line_of_business = models.ForeignKey(
        GuideLineOfBusiness,
        models.DO_NOTHING,
        db_column="line_of_business",
        blank=True,
        null=True,
    )
    warehouse = models.TextField(blank=True, null=True)
    product = models.ForeignKey(
        GuideProducts, models.DO_NOTHING, db_column="product", blank=True, null=True
    )
    nomenclature_series = models.ForeignKey(
        NomenclatureSeries,
        models.DO_NOTHING,
        db_column="nomenclature_series",
        blank=True,
        null=True,
    )
    buh = models.FloatField(blank=True, null=True)
    skl = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = "remains"

    def __str__(self):
        return f"{self.product.product} {self.nomenclature_series.nomenclature_series}"


class ShippingAddress(models.Model):
    id = models.UUIDField(primary_key=True)
    client = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    contract_supplement = models.UUIDField(blank=True, null=True)

    class Meta:

        db_table = "shipping_address"

    def __str__(self):
        return self.shipping_address


class Submissions(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ContractNumber,
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_column="contract",
    )
    manager = models.ForeignKey(
        GuideManagers, models.DO_NOTHING, blank=True, null=True, db_column="manager"
    )
    client = models.ForeignKey(
        GuideClient, models.DO_NOTHING, blank=True, null=True, db_column="client"
    )
    manufacturer = models.ForeignKey(
        GuideManufacturer,
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_column="manufacturer",
    )
    line_of_business = models.ForeignKey(
        GuideLineOfBusiness,
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_column="line_of_business",
    )
    period = models.BigIntegerField(blank=True, null=True)
    shipping_warehouse = models.TextField(blank=True, null=True)
    shipping_address = models.UUIDField(blank=True, null=True)
    product = models.ForeignKey(GuideProducts, models.DO_NOTHING, db_column="product")
    plan = models.FloatField(blank=True, null=True)
    fact = models.FloatField(blank=True, null=True)
    different = models.FloatField(blank=True, null=True)
    payment = models.ForeignKey(
        Payment, models.DO_NOTHING, db_column="payment", blank=True, null=True
    )

    class Meta:

        db_table = "submissions"

    def __str__(self):
        return f"{self.contract} {self.client} {self.line_of_business}"


class AvailableStocks(models.Model):
    id = models.UUIDField(primary_key=True)
    division = models.ForeignKey(
        "GuideDivisions", models.DO_NOTHING, db_column="division", blank=True, null=True
    )
    product = models.ForeignKey(
        "GuideProducts", models.DO_NOTHING, db_column="product", blank=True, null=True
    )
    available = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "available_stocks"
