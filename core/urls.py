from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView
from blog.views import TagDetail


urlpatterns = [
    path('moria/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('tag/<slug:slug>/', TagDetail.as_view(), name='tag_list'),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns