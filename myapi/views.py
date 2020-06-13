from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import MovieForm
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
#from datetime import datetime, date
import datetime


def sort_m(st, ft):
    result = []
    ft = sorted(ft)  # soritng the finish time
    n = len(ft)  # count total finish time
    i = 0  # select by default first value
    result.append(i)  # adding first value to dictionary
    for j in range(n):
        # checking if start time of next activity is greater then or equal to
        # finish time of previously
        if st[j] >= ft[i]:
            # adding to list
            result.append(j)
            i = j
    return set(result)


class WorkingMovieResult(APIView):

    def get(self, request):
        dates = [{'start_date': ed['starting_date'], 'end_date':ed['ending_date']} for ed in Hero.objects.filter(
            starting_date__year='2020', ending_date__year='2020').values('starting_date', 'ending_date').order_by("ending_date")]
        f_sdate = []
        f_edate = []
        s_date = []
        e_date = []
        for d in dates:
            s_date.append(d['start_date'])
            e_date.append(d['end_date'])
        res = sort_m(s_date, e_date)
        for r in res:
            dts = dates[r]
            f_sdate.append(dts['start_date'])
            f_edate.append(dts['end_date'])

        fr = Hero.objects.filter(
            starting_date__in=f_sdate, ending_date__in=f_edate).values().distinct()
        final_results = {'data': fr, 'count': len(fr)}
        return Response(final_results)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


def showform(request):
    q1 = Hero.objects.all()
    #first_date = datetime.date(2020, 1, 1)
    #last_date = datetime.date(2020, 1, 15)
    #endfirst_date = datetime.date(2020, 1, 16)
    #endlast_date = datetime.date(2020, 1, 31)
    # q2 = Hero.objects.filter(starting_date__year='2020', ending_date__year='2020',
    #                 starting_date__month='01',ending_date__month='01')
    #q2 = Hero.objects.filter(starting_date__range=(first_date, last_date)).filter(ending_date__range=(endfirst_date, endlast_date))
    #q2 = Hero.objects.filter(starting_date__gte=datetime.date(2020, 1, 1),
     #                        ending_date__lte=datetime.date(2020, 1, 15)).distinct()
    #print(q2)
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form, 'q1': q1, }

    return render(request, 'movie_form.html', context)
