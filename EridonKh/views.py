import uuid

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from .forms import LoginForm
from .models import Submissions, Remains, GuideClient
from django.db.models import Q


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


class SubmissionsClientView(ListView):
    template_name = "EridonKh/submissions.html"

    def get_queryset(self):
        search_field = self.request.GET.get("client_search")
        if search_field is not None:
            if self.request.user.is_authenticated:
                if self.request.user.is_superuser:

                    queryset = (
                        Submissions.objects.values(
                            "contract__contract_supplement",
                            "client__client",
                            "client",
                            "line_of_business",
                            "line_of_business__line_of_business",
                        )
                        .filter(client__client__icontains=search_field)
                        .distinct("client__client")
                    )
                    return queryset
                else:
                    queryset = (
                        Submissions.objects.values(
                            "contract__contract_supplement",
                            "client__client",
                            "client",
                            "line_of_business",
                            "line_of_business__line_of_business",
                        )
                        .filter(
                            manager__manager__startswith=self.request.user.last_name
                        )
                        .filter(Q(client__client__icontains=search_field))
                        .distinct("client__client")
                    )
                    return queryset
        else:
            if self.request.user.is_authenticated:
                if self.request.user.is_superuser:

                    queryset = Submissions.objects.values(
                        "contract__contract_supplement",
                        "client__client",
                        "client",
                        "line_of_business",
                        "line_of_business__line_of_business",
                    ).distinct("client__client")
                    return queryset
                else:
                    queryset = Submissions.objects.values(
                        "contract__contract_supplement",
                        "client__client",
                        "client",
                        "line_of_business",
                        "line_of_business__line_of_business",
                    ).filter(manager__manager__startswith=self.request.user.last_name)
                    return queryset
            else:
                queryset = []
                return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_o_b"] = Submissions.objects.values(
            "line_of_business__line_of_business", "line_of_business"
        ).distinct("line_of_business__line_of_business")
        context["manager_filter"] = Submissions.objects.values(
            "manager", "manager__manager"
        ).distinct("manager__manager")
        return context


def submissions_number_detail(request, client):
    cl_list = (
        Submissions.objects.values("client__client", "client")
        .filter(client=client)
        .distinct()
    )
    data = (
        Submissions.objects.values(
            "contract",
            "contract__contract_supplement",
            "client",
            "client__client",
            "line_of_business",
            "line_of_business__line_of_business",
        )
        .filter(client=client)
        .distinct()
        .order_by("contract__contract_supplement")
    )
    manager_filter = Submissions.objects.values("manager", "manager__manager").distinct(
        "manager__manager"
    )
    return render(
        request,
        "EridonKh/submissions.html",
        {
            "submissions": data,
            "object_list": cl_list,
            "manager_filter": manager_filter,
        },
    )


def submissions_prod_details(request, client, cont_sub):
    cl_list = (
        Submissions.objects.values("client__client", "client")
        .filter(client=client)
        .distinct()
    )
    contract = (
        Submissions.objects.values(
            "contract__contract_supplement",
            "contract",
            "line_of_business",
            "line_of_business__line_of_business",
        )
        .filter(contract=cont_sub)
        .distinct()
    )
    data = (
        Submissions.objects.values("product__product", "different", "plan", "fact")
        .filter(contract=cont_sub)
        .distinct()
    )
    return render(
        request,
        "EridonKh/submissions.html",
        {"products": data, "object_list": cl_list, "submissions": contract},
    )


class RemainsView(ListView):
    model = Remains
    template_name = "EridonKh/remains.html"
    queryset = Remains.objects.filter(
        line_of_business__line_of_business__in=[
            "ЗЗР",
            "Позакореневi добрива",
            "Міндобрива (основні)",
            "Власне виробництво насіння",
            "Насіння",
        ]
    ).select_related("product", "line_of_business", "nomenclature_series")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["line_of_business"] = (
            Remains.objects.values(
                "line_of_business__line_of_business", "line_of_business"
            )
            .filter(
                line_of_business__line_of_business__in=[
                    "ЗЗР",
                    "Позакореневi добрива",
                    "Міндобрива (основні)",
                    "Власне виробництво насіння",
                    "Насіння",
                ]
            )
            .order_by("line_of_business__line_of_business")
            .distinct()
        )
        return context


class RemainsFiltered(RemainsView, ListView):
    def get_queryset(self):
        lob = self.request.GET.getlist("lob")
        queryset = (
            Remains.objects.filter(line_of_business__line_of_business__in=lob)
            .select_related("product", "line_of_business", "nomenclature_series")
            .order_by("product__product")
        )
        return queryset



def submissions_manager(request):
    manager_filtered = request.GET.getlist("man")
    data = (
        Submissions.objects.values(
            "contract__contract_supplement",
            "client__client",
            "client",
            "line_of_business",
            "line_of_business__line_of_business",
        )
        .filter(manager__manager__in=manager_filtered)
        .distinct("client__client")
    )
    manager_filter = Submissions.objects.values("manager", "manager__manager").distinct(
        "manager__manager"
    )
    return render(
        request,
        "EridonKh/submissions.html",
        {"object_list": data, "manager_filter": manager_filter},
    )



# def remains_view(request):
#     data = Remains.objects.filter(
#         line_of_business__in=[
#             "ЗЗР",
#             "Позакореневi добрива",
#             "Міндобрива (основні)",
#             "Власне виробництво насіння",
#             "Насіння",
#         ]
#     ).select_related("product")
#     guide_line_of_business = (
#         Remains.objects.values("line_of_business")
#         .order_by("line_of_business")
#         .distinct()
#     )
#     return render(
#         request,
#         "EridonKh/remains.html",
#         context={"data": data, "line_of_business": guide_line_of_business},
#     )
