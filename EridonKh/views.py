import uuid
from django.core import serializers
from .storage import QuerySetStorage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django_filters.views import FilterView
from django.db.models import Q, Sum

from .filters import SubmissionsFilters, RemainsFilters
from .forms import LoginForm
from .models import Submissions, Remains, GuideClient, Payment


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


def submissions_view(request):
    # определяем поля фильтров из реквеста
    search_field = request.GET.get("client_search")
    manager = request.GET.getlist("man")
    payment = request.GET.get("pay")
    complete = request.GET.get("completed")
    # если пользователь авторизирован и является суперпользователем
    if request.user.is_authenticated:
        if request.user.is_superuser:
            queryset = Submissions.objects.values(
                "contract__contract_supplement",
                "client__client",
                "client",
                "line_of_business",
                "line_of_business__line_of_business",
            ).distinct("client__client")
            # если пользователь авторизирован и не суперпользователь
        else:
            queryset = (
                Submissions.objects.values(
                    "contract__contract_supplement",
                    "client__client",
                    "client",
                    "line_of_business",
                    "line_of_business__line_of_business",
                )
                .filter(manager__manager__startswith=request.user.last_name)
                .distinct("client__client")
            )
        if search_field:
            queryset = queryset.filter(client__client__icontains=search_field)
        if manager:
            queryset = queryset.filter(manager__manager__in=manager)
        if payment:
            if payment == "Оплачені":
                queryset = queryset.filter(payment__paid=True)
            else:
                queryset = queryset.filter(payment__paid=False)
        if complete:
            if complete == "Виконані":
                queryset = queryset.filter(different=0)
            else:
                queryset = queryset.filter(different__gt=0)
        manager_filter = Submissions.objects.values(
            "manager", "manager__manager"
        ).distinct("manager__manager")
        payment = ["Оплачені", "Не_оплачені"]
        type_submissions = ["Виконані", "Не_виконані"]
        manager = request.GET.getlist("man")
        paid = request.GET.get("pay")
        completed = request.GET.get("completed")
        request.session["previous_data_manager"] = manager
        request.session["previous_data_payment"] = paid
        request.session["previuos_data_completed"] = completed
        return render(
            request,
            "EridonKh/../djangoProjectKh/submissions.html",
            {
                "object_list": queryset,
                "manager_filter": manager_filter,
                "payment": payment,
                "type_submissions": type_submissions,
                "previous_type": request.session.get("previuos_data_completed"),
                "previous_manager": request.session.get("previous_data_manager"),
                "previous_payment": request.session.get("previous_data_payment"),
            },
        )

    else:
        queryset = []
        return render(
            request,
            "EridonKh/../djangoProjectKh/submissions.html",
            {"object_list": queryset},
        )


class ClientView(FilterView):
    template_name = "EridonKh/clients.html"
    model = Submissions
    context_object_name = "clients"
    filterset_class = SubmissionsFilters

    # def get(self, request, *args, **kwargs):
    #     self.request["clients"] = self.get_queryset()
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # data = (
        #     Submissions.objects.values_list("client")
        #     .select_related("client")
        #     .order_by("client__client")
        #     .distinct()
        # )
        # client = GuideClient.objects.all()
        submissions = Submissions.objects.all().select_related(
            "client",
            "contract",
            "line_of_business",
            "manager",
            "manufacturer",
            "product",
            "payment",
        )
        # QuerySetStorage.save("submissions_queryset", submissions)
        # QuerySetStorage.save("client_queryset", client)
        # self.request.session["client"] = serializers.serialize("json", data)
        return submissions.distinct("client__client")

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ClientView, self).get_context_data(*args, **kwargs)
        QuerySetStorage.save("submissions_queryset", object_list)
        return context


class SubmissionsView(ListView):
    template_name = "EridonKh/submissions.html"
    model = Submissions
    context_object_name = "submissions"
    # filterset_class = SubmissionsFilters
    queryset = Submissions.objects.all().select_related(
        "client",
        "contract",
        "line_of_business",
        "manager",
        "manufacturer",
        "product",
        "payment",
    )


# def submissions_number_detail(request, client):
#     previous_complete = (request.session.get("previuos_data_completed"),)
#     previous_manager = (request.session.get("previous_data_manager"),)
#     previous_payment = (request.session.get("previous_data_payment"),)
#     cl_list = (
#         Submissions.objects.values("client__client", "client")
#         .filter(client=client)
#         .distinct()
#     )
#
#     data = (
#         Submissions.objects.values(
#             "contract",
#             "contract__contract_supplement",
#             "client",
#             "client__client",
#             "line_of_business",
#             "line_of_business__line_of_business",
#         )
#         .filter(client=client)
#         .distinct()
#         .order_by("contract__contract_supplement")
#     )
#     if previous_complete[0] is not None:
#         if previous_complete == "Виконані":
#             data = data.filter(different=0)
#         else:
#             data = data.filter(different__gt=0)
#
#     manager_filter = Submissions.objects.values("manager", "manager__manager").distinct(
#         "manager__manager"
#     )
#     payment = ["Оплачені", "Не_оплачені"]
#     type_submissions = ["Виконані", "Не_виконані"]
#     return render(
#         request,
#         "EridonKh/../djangoProjectKh/submissions.html",
#         {
#             "submissions": data,
#             "object_list": cl_list,
#             "manager_filter": manager_filter,
#             "payment": payment,
#             "previous_manager": request.session.get("previous_data_manager"),
#             "previous_payment": request.session.get("previous_data_payment"),
#             "type_submissions": type_submissions,
#             "previous_type": request.session.get("previuos_data_completed"),
#         },
#     )


class ClientSubmissions(FilterView):
    model = Submissions
    template_name = "EridonKh/client_submissions.html"
    context_object_name = "client_submissions"
    filterset_class = SubmissionsFilters

    def get_queryset(self):
        # data = serializers.deserialize("json", self.request.session.get("client"))
        # data_deserializer = [obj.object for obj in data]
        client = self.kwargs["client"]
        storage_data = QuerySetStorage.get("submissions_queryset")
        storage_data = storage_data.distinct("contract__contract_supplement").order_by(
            "contract__contract_supplement"
        )
        return storage_data.filter(client=client)

        # return (
        #     Submissions.objects.filter(client=client)
        #     .select_related(
        #         "client",
        #         "contract",
        #         "line_of_business",
        #         "manager",
        #         "manufacturer",
        #         "product",
        #         "payment",
        #     )
        #     .order_by("contract__contract_supplement")
        #     .distinct("contract__contract_supplement")
        # )


class ContractDetails(ListView):
    model = Submissions
    template_name = "EridonKh/contract_detail.html"
    context_object_name = "contracts"

    def get_queryset(self):
        contract = self.kwargs["contract"]
        return Submissions.objects.values(
            "product__product", "plan", "fact", "different"
        ).filter(contract=contract)


def submissions_prod_details(request, client, cont_sub):
    cl_list = Submissions.objects.values("client__client", "client").filter(
        client=client
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
        "EridonKh/../djangoProjectKh/submissions.html",
        {
            "products": data,
            "object_list": cl_list,
            "submissions": contract,
            "previous_manager": request.session.get("previous_data_manager"),
            "previous_payment": request.session.get("previous_data_payment"),
        },
    )


class RemainsView(FilterView):
    model = Remains
    template_name = "EridonKh/remains.html"
    filterset_class = RemainsFilters
    queryset = (
        Remains.objects.filter(
            Q(
                line_of_business__line_of_business__in=[
                    "ЗЗР",
                    "Позакореневi добрива",
                    "Міндобрива (основні)",
                    "Власне виробництво насіння",
                    "Насіння",
                ]
            )
            & Q(warehouse='Харківський підрозділ  ТОВ "Фірма Ерідон" с.Коротич')
        )
        .select_related("product", "line_of_business", "nomenclature_series")
        .order_by("product__product")
    )
    queryset = queryset.values_list("product", "product__product").annotate(
        total_buh=Sum("buh"), total_skl=Sum("skl")
    )

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
        context["remains_without_series"] = (
            context["filter"]
            .qs.values_list("product__product", "product")
            .annotate(
                buh_sum=Sum("buh"),
                skl_sum=Sum("skl"),
            )
            .order_by("product__product")
        )
        # context["sum_skl"] = Remains.objects.values("product__product").annotate(
        #     skl_sum=Sum("skl")
        # )
        return context


class RemainsDetailView(DetailView):
    model = Remains
    template_name = "EridonKh/remains_detail.html"

    def get_object(self, queryset=None):
        obj = (
            Remains.objects.all()
            .filter(
                Q(product=self.kwargs["product"])
                & Q(warehouse='Харківський підрозділ  ТОВ "Фірма Ерідон" с.Коротич')
            )
            .select_related("nomenclature_series")
        )
        return obj

    # def get_queryset(self):
    #     product = self.kwargs["product"]
    #     return Remains.objects.all().filter(product=product)

    # def get_object(self):
    #     return Remains.objects.all().filter(
    #         Q(product=self.kwargs["product"]),
    #         Q(warehouse='Харківський підрозділ  ТОВ "Фірма Ерідон" с.Коротич'),
    #     )
    #
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seeds"] = ["Власне виробництво насіння", "Насіння"]
        context["lob"] = (
            Remains.objects.values("line_of_business__line_of_business")
            .filter(product=self.kwargs["product"])
            .first()
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
        "EridonKh/../djangoProjectKh/submissions.html",
        {"object_list": data, "manager_filter": manager_filter},
    )


def submissions_pay(request):
    payment = request.GET.get("pay")
    if payment == "Оплачені":
        data = (
            Submissions.objects.values(
                "contract__contract_supplement",
                "client__client",
                "client",
                "line_of_business",
                "line_of_business__line_of_business",
            )
            .distinct("client")
            .filter(payment__paid=True)
            .order_by("client__client")
        )
    else:
        data = (
            Submissions.objects.values(
                "contract__contract_supplement",
                "client__client",
                "client",
                "line_of_business",
                "line_of_business__line_of_business",
            )
            .distinct("client__client")
            .filter(payment__paid=False)
            .order_by("client__client")
        )
        return render(
            request,
            "EridonKh/../djangoProjectKh/submissions.html",
            {"object_list": data},
        )
