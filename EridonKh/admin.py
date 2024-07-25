from django.contrib import admin
from .models import Submissions


# Register your models here.
@admin.register(Submissions)
class SubmissionsAdmin(admin.ModelAdmin):
    list_filter = ["manager", "line_of_business"]
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
