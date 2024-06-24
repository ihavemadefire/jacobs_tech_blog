from django.urls import path, include
from .views import WritingList, WritingDetail

urlpatterns = [
    path('', WritingList.as_view(), name='writing'),
    path('<slug:slug>/', WritingDetail.as_view(), name='piece'),
]
