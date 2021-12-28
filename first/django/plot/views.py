from django.shortcuts import render

# Create your views here.

from plot.function import make_df, make_bar_plot, make_bar_plot2, make_bar_plot3, make_bar_plot4,make_bar_plot5



def index(request):
     return render(request, "plot/select.html")


def graph(request):
     if request.method == "POST":
          area = request.POST.getlist('area')
          data = {'area' : area}
          #   print(data)
     
     # area = ['부산','서울','제주']
     df_total = make_df(area)
     make_bar_plot(df_total[0])
     make_bar_plot2(df_total[1])  
     make_bar_plot3(df_total[2])
     make_bar_plot4(df_total[3])
     make_bar_plot5(df_total[2])
     return render(request, 'plot/graph.html', data)