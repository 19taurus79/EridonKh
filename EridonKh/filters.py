import django_filters
from django_filters.filters import ChoiceFilter
from django_filters.filterset import FilterSet
from .models import Submissions, GuideLineOfBusiness, Remains


class SubmissionsFilters(FilterSet):

    # line_of_business = django_filters.ModelChoiceFilter(
    #     label="Від діяльності",
    #     queryset=GuideLineOfBusiness.objects.all(),
    # )
    # payment = django_filters.ModelChoiceFilter(
    #     label="Оплата", queryset=Submissions.objects.all().distinct("payment__paid")
    # )
    line_of_business = django_filters.ModelChoiceFilter(
        label="Від діяльності",
        queryset=GuideLineOfBusiness.objects.all(),
    )

    payment_status = ((True, "Оплачено"), (False, "Не оплачено"))
    payment = ChoiceFilter(
        choices=payment_status, label="Оплата", field_name="payment__paid"
    )

    class Meta:
        model = Submissions
        fields = ["payment"]
        # label = {"Payment paid": "Оплата", "line_of_business": "Від діяльності"}

    # field_name = {"payment__paid": "Payment"}


class RemainsFilters(FilterSet):
    line_of_business = django_filters.ModelChoiceFilter(
        label="Від діяльності",
        queryset=GuideLineOfBusiness.objects.all(),
    )
