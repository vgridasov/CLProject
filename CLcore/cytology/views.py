from django.views import generic
from django.views.generic.dates import DayArchiveView, \
    YearArchiveView, MonthArchiveView, WeekArchiveView, TodayArchiveView

from .models import Analysis


class IndexView(generic.ListView):
    template_name = 'cytology/home.html'
    context_object_name = 'latest_analysis_list'

    def get_queryset(self):
        """Return the last five analysis."""
        return Analysis.objects.order_by('-v_date')[:10]


class AListView(generic.ListView):
    paginate_by = 25

    def get_queryset(self):
        return Analysis.objects.order_by('-reg')


class ADetailView(generic.DetailView):
    model = Analysis


class ADayArchiveView(DayArchiveView):
    queryset = Analysis.objects.all()
    date_field = "v_date"


class AYearArchiveView(YearArchiveView):
    queryset = Analysis.objects.all()
    date_field = "v_date"
    week_format = "%W"


class AMonthArchiveView(MonthArchiveView):
    queryset = Analysis.objects.all()
    date_field = "v_date"


class AWeekArchiveView(WeekArchiveView):
    queryset = Analysis.objects.all()
    date_field = "v_date"


class ATodayArchiveView(TodayArchiveView):
    queryset = Analysis.objects.all()
    date_field = "v_date"
    template_name = 'cytology/analysis_archive_today.html'


class SearchResultsView(generic.ListView):
    model = Analysis
    paginate_by = 25
    template_name = 'cytology/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Analysis.objects.filter(
            last_name__icontains=query           # поиск по фамилии
            # | Q(first_name__icontains=query)   # дополнительный поиск по имени
            # | Q(middle_name__icontains=query)  # дополнительный поиск по отчеству
            # | Q(address__icontains=query)      # дополнительный поиск по адресу
        ).distinct()
        return object_list