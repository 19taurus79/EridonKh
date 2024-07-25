from django.db.models import Count
from django.shortcuts import render
from .models import Submissions, Remains


# Create your views here.
def index_view(request):
    data = Submissions.objects.values("client").order_by("client").distinct()
    return render(request, "EridonKh/home.html", {"data": data})


def remains_view(request):
    data = Remains.objects.filter(
        line_of_business__in=[
            "ЗЗР",
            "Позакореневi добрива",
            "Міндобрива (основні)",
            "Власне виробництво насіння",
            "Насіння",
        ]
    ).select_related("product")
    guide_line_of_business = (
        Remains.objects.values("line_of_business")
        .order_by("line_of_business")
        .distinct()
    )
    return render(
        request,
        "EridonKh/remains.html",
        context={"data": data, "line_of_business": guide_line_of_business},
    )
