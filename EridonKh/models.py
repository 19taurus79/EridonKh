# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import CASCADE


class AvailableStock(models.Model):
    id = models.UUIDField(primary_key=True)
    nomenclature = models.CharField(max_length=255, blank=True, null=True)
    party_sign = models.CharField(max_length=255, blank=True, null=True)
    buying_season = models.CharField(max_length=255, blank=True, null=True)
    division = models.CharField(max_length=255, blank=True, null=True)
    line_of_business = models.CharField(max_length=255, blank=True, null=True)
    available = models.FloatField()
    product = models.ForeignKey(
        "ProductGuide", models.DO_NOTHING, db_column="product", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "available_stock"


class ClientContract(models.Model):
    id = models.UUIDField(primary_key=True)
    client = models.UUIDField(blank=True, null=True)
    contract = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "client_contract"


class ClientGuide(models.Model):
    id = models.UUIDField(primary_key=True)
    client = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.client

    class Meta:
        managed = False
        db_table = "client_guide"


class ContractProduct(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.UUIDField(blank=True, null=True)
    product = models.CharField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    in_delivery = models.BooleanField()

    class Meta:
        managed = False
        db_table = "contract_product"


class Delivery(models.Model):
    id = models.UUIDField(primary_key=True)
    contract_supplement = models.CharField(blank=True, null=True)
    product = models.CharField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    manager = models.CharField(blank=True, null=True)
    client = models.CharField(blank=True, null=True)
    quantity_delivery = models.FloatField(blank=True, null=True)
    date_delivery = models.DateField(blank=True, null=True)
    proove = models.BooleanField(blank=True, null=True)
    key = models.CharField(blank=True, null=True)
    delivery_manager_key = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "delivery"


class Documents(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.ForeignKey(
        "ManagerGuideTable",
        models.DO_NOTHING,
        db_column="manager",
        blank=True,
        null=True,
    )
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "documents"


class GuideContract(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "guide_contract"


class ManagerGuideTable(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.CharField(blank=True, null=True)
    manager_email = models.CharField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.manager

    class Meta:
        managed = False
        db_table = "manager_guide_table"


class ManagerClient(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.ForeignKey(
        ManagerGuideTable, on_delete=CASCADE, db_column="manager"
    )
    client = models.ForeignKey(ClientGuide, on_delete=CASCADE, db_column="client")

    # manager = models.UUIDField(blank=True, null=True)
    # client = models.UUIDField(blank=True, null=True)
    def __str__(self):
        return f"{self.client} / {self.manager}"

    class Meta:
        managed = False
        db_table = "manager_client"


class MovedData(models.Model):
    id = models.UUIDField(primary_key=True)
    product = models.CharField(max_length=255)
    contract = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    line_of_business = models.CharField(max_length=255)
    qt_order = models.CharField(max_length=255)
    qt_moved = models.CharField(max_length=255)
    party_sign = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    order = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "moved_data"


class Orders(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.ForeignKey(
        ManagerGuideTable, models.DO_NOTHING, db_column="manager", blank=True, null=True
    )
    client = models.UUIDField(blank=True, null=True)
    contract = models.ForeignKey(
        GuideContract, models.DO_NOTHING, db_column="contract", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "orders"


class OrdersForDelivery(models.Model):
    id = models.UUIDField(primary_key=True)
    manager = models.CharField(blank=True, null=True)
    client = models.CharField(blank=True, null=True)
    contract = models.CharField(blank=True, null=True)
    product = models.CharField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    quantity_in_contract = models.FloatField(blank=True, null=True)
    document = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orders_for_delivery"


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    contract_supplement = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=255)
    prepayment_amount = models.FloatField()
    amount_of_credit = models.FloatField()
    prepayment_percentage = models.FloatField()
    loan_percentage = models.FloatField()
    planned_amount = models.FloatField()
    actual_sale_amount = models.FloatField()
    actual_payment_amount = models.FloatField()
    planned_amount_excluding_vat = models.FloatField()

    class Meta:
        managed = False
        db_table = "payment"


class ProductGuide(models.Model):
    id = models.UUIDField(primary_key=True)
    product = models.CharField(unique=True, max_length=255)
    line_of_business = models.CharField(max_length=255, blank=True, null=True)
    active_substance = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.product

    class Meta:
        managed = False
        db_table = "product_guide"


class ProductUnderSubmissions(models.Model):
    id = models.UUIDField(primary_key=True)
    product = models.ForeignKey(
        ProductGuide, models.DO_NOTHING, db_column="product", blank=True, null=True
    )
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = "product_under_submissions"


class Remains(models.Model):
    id = models.UUIDField(primary_key=True)
    line_of_business = models.CharField(max_length=255)
    warehouse = models.CharField(max_length=255, blank=True, null=True)
    parent_element = models.CharField(max_length=255, blank=True, null=True)
    nomenclature = models.CharField(max_length=255, blank=True, null=True)
    party_sign = models.CharField(max_length=255, blank=True, null=True)
    buying_season = models.CharField(max_length=255, blank=True, null=True)
    nomenclature_series = models.CharField(max_length=255, blank=True, null=True)
    mtn = models.CharField(max_length=255, blank=True, null=True)
    origin_country = models.CharField(max_length=255, blank=True, null=True)
    germination = models.CharField(max_length=255, blank=True, null=True)
    crop_year = models.CharField(max_length=255, blank=True, null=True)
    quantity_per_pallet = models.CharField(max_length=255, blank=True, null=True)
    active_substance = models.CharField(max_length=255, blank=True, null=True)
    certificate = models.CharField(max_length=255, blank=True, null=True)
    certificate_start_date = models.CharField(max_length=255, blank=True, null=True)
    certificate_end_date = models.CharField(max_length=255, blank=True, null=True)
    buh = models.FloatField()
    skl = models.FloatField()
    weight = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(
        ProductGuide, models.DO_NOTHING, db_column="product", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "remains"


class Submissions(models.Model):
    id = models.UUIDField(primary_key=True)
    division = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Підрозділ"
    )
    manager = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Менеджер"
    )
    company_group = models.CharField(max_length=255, blank=True, null=True)
    client = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Контрагент"
    )
    contract_supplement = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Доповнення"
    )
    parent_element = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    active_ingredient = models.CharField(max_length=255, blank=True, null=True)
    nomenclature = models.CharField(max_length=255, blank=True, null=True)
    party_sign = models.CharField(max_length=255, blank=True, null=True)
    buying_season = models.CharField(max_length=255, blank=True, null=True)
    line_of_business = models.CharField(max_length=255, blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    shipping_warehouse = models.CharField(max_length=255, blank=True, null=True)
    document_status = models.CharField(max_length=255, blank=True, null=True)
    delivery_status = models.CharField(max_length=255, blank=True, null=True)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    transport = models.CharField(max_length=255, blank=True, null=True)
    plan = models.FloatField(verbose_name="Заплановано")
    fact = models.FloatField(verbose_name="Реалізовано")
    different = models.FloatField(verbose_name="Залишилось реалізувати")
    product = models.ForeignKey(
        ProductGuide,
        models.DO_NOTHING,
        db_column="product",
        blank=True,
        null=True,
        verbose_name="Товар",
    )

    def __str__(self):
        return f"{self.client} {self.line_of_business} {self.contract_supplement}"

    class Meta:
        managed = False
        db_table = "submissions"
