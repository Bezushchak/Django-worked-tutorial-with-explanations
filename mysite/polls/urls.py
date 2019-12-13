from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [

    # If somebody goes to a url like this ex: /polls/ it will redirect him to
    # the page
    path('', views.IndexView.as_view(), name='index'),
    # If smbdy goes to the url like so ex: /polls/5/ it will redirect
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/ meaning any number followed by results will take
    # him-her to the results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote any number followed by the vote word
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
