from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Submissions, Remains


# Create your views here.
# def index_view(request):
#     data = Submissions.objects.values("client").order_by("client").distinct()
#     return render(request, "EridonKh/submissions.html", {"data": data})


class IndexView(ListView):
    model = Submissions
    template_name = "EridonKh/submissions.html"
    queryset = Submissions.objects.values("client").order_by("client").distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "test"
        return context


class RemainsView(ListView):
    model = Remains
    template_name = "EridonKh/remains.html"
    queryset = Remains.objects.filter(
        line_of_business__in=[
            "ЗЗР",
            "Позакореневi добрива",
            "Міндобрива (основні)",
            "Власне виробництво насіння",
            "Насіння",
        ]
    ).select_related("product")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["line_of_business"] = (
            Remains.objects.values("line_of_business")
            .filter(
                line_of_business__in=[
                    "ЗЗР",
                    "Позакореневi добрива",
                    "Міндобрива (основні)",
                    "Власне виробництво насіння",
                    "Насіння",
                ]
            )
            .order_by("line_of_business")
            .distinct()
        )
        return context


class RemainsFiltered(RemainsView, ListView):
    def get_queryset(self):
        queryset = Remains.objects.filter(
            line_of_business__in=self.request.GET.getlist("lob")
        )
        return queryset


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
