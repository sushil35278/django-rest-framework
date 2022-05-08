from django.urls import path, include
from .views import ArticleApiView, ArticleDetail
from api_app import views

urlpatterns = [
    # path('article/', views.article_list),
    # path('detail/<int:pk>/', views.article_detail)
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:id>/', ArticleDetail.as_view())
]