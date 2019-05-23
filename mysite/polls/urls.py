# from .views import index, detail, results, vote
# from django.urls import path


# app_name = 'polls'
# urlpatterns = [


#     path('', index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', vote, name='vote'),

# ]


# generic view  url pattern

from django.urls import path

from . import views, views1

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),


    # for password grant type
    path('register/', views1.register),
    path('token/', views1.token),
    path('token/refresh/', views1.refresh_token),
    path('token/revoke/', views1.revoke_token),
]
