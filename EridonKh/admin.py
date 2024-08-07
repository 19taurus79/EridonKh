from django.contrib import admin

from .models import (
    Submissions,
    Remains,
    GuideProducts,
    NomenclatureSeries,
    ContractNumber,
)


#
#
# # Register your models here.
@admin.register(Remains)
class RemainsAdmin(admin.ModelAdmin):
    list_select_related = ["line_of_business", "product", "nomenclature_series"]
    ordering = ["product__product"]
    list_filter = ["warehouse"]
    search_fields = ["product__product"]


@admin.register(Submissions)
class SubmissionsAdmin(admin.ModelAdmin):
    list_select_related = [
        "client",
        "contract",
        "line_of_business",
        "manager",
        "manufacturer",
        "product",
    ]
    ordering = ["client__client"]
    list_filter = ["manager__manager"]
    search_fields = ["client__client"]


@admin.register(GuideProducts)
class GuideProductsAdmin(admin.ModelAdmin):
    ordering = ["product"]
    search_fields = ["product"]


@admin.register(NomenclatureSeries)
class NomenclatureSeriesAdmin(admin.ModelAdmin):
    ordering = ["nomenclature_series"]


@admin.register(ContractNumber)
class ContractNumberAdmin(admin.ModelAdmin):
    pass


# list_filter = ["manager", "line_of_business"]
# list_select_related = [
#     "product",
# ]
# search_fields = ["client"]
# ordering = ["manager", "client"]
# fieldsets = [
#     (
#         None,
#         {
#             "fields": [
#                 "contract_supplement",
#                 ("manager", "division"),
#                 ("product", "plan", "fact", "different"),
#             ]
#         },
#     )
# ]


# @admin.register(ManagerClient)
# class ManagerClientAdmin(admin.ModelAdmin):
#     list_select_related = ["client", "manager"]
#     search_fields = ["client__client"]
#     list_filter = ["manager__manager"]
#     ordering = ["client__client"]
