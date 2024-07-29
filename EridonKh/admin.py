from django.contrib import admin
from .models import Submissions, ManagerClient


# Register your models here.
@admin.register(Submissions)
class SubmissionsAdmin(admin.ModelAdmin):
    list_filter = ["manager", "line_of_business"]
    list_select_related = [
        "product",
    ]
    search_fields = ["client"]
    ordering = ["manager", "client"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "contract_supplement",
                    ("manager", "division"),
                    ("product", "plan", "fact", "different"),
                ]
            },
        )
    ]


@admin.register(ManagerClient)
class ManagerClientAdmin(admin.ModelAdmin):
    list_select_related = ["client", "manager"]
    search_fields = ["client__client"]
    list_filter = ["manager__manager"]
    ordering = ["client__client"]
