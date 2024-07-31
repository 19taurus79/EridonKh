from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from .forms import LoginForm
from .models import Submissions, Remains, ManagerClient, ClientGuide


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home_page"))

    return render(request, "EridonKh/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_page"))


# Create your views here.
# def index_view(request):
#     data = Submissions.objects.values("client").order_by("client").distinct()
#     return render(request, "EridonKh/submissions.html", {"data": data})


class SubmissionsClientView(ListView):

    # model = Submissions
    template_name = "EridonKh/submissions.html"
    # queryset = Submissions.objects.values("client").order_by("client").distinct()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["test"] = "test"
    #     context["user"] = self.request.user
    #     return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                queryset = (
                    ManagerClient.objects.values("client__client", "client")
                    .distinct("client__client")
                    .order_by("client__client")
                )
                return queryset
            else:
                queryset = (
                    ManagerClient.objects.values("client__client", "client")
                    .filter(manager__manager__startswith=self.request.user.last_name)
                    .distinct("client__client")
                    .order_by("client__client")
                )
                return queryset
        else:
            queryset = []
            return queryset


def submissions_number_detail(request, client):
    cl = ClientGuide.objects.all().get(id=client)
    cl_list = ManagerClient.objects.values("client__client", "client").filter(
        client=client
    )
    data = (
        Submissions.objects.values("contract_supplement")
        .filter(client=cl)
        .distinct()
        .order_by("contract_supplement")
    )
    return render(
        request,
        "EridonKh/submissions.html",
        {
            "submissions": data,
            "object_list": cl_list,
        },
    )


def submissions_prod_details(request, client, cont_sub):
    client = ManagerClient.objects.values("client__client", "client").filter(
        client=client
    )
    contract = (
        Submissions.objects.values("contract_supplement")
        .filter(contract_supplement=cont_sub)
        .distinct()
    )
    data = Submissions.objects.values("product__product", "different").filter(
        contract_supplement=cont_sub
    )
    return render(
        request,
        "EridonKh/submissions.html",
        {"products": data, "object_list": client, "submissions": contract},
    )


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
        ).select_related("product")
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
