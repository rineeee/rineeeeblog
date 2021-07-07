from django import contrib
from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('mypost', blog.views.my_post, name="my-post"),
    path('new', blog.views.new_post, name="new"),
    path('post/<int:pk>', blog.views.post_detail, name="post-detail"),
    path('post/edit/<int:pk>', blog.views.post_update, name = "post-edit"),
    path('post/delete/<int:pk>', blog.views.post_delete, name="post-delete"),
    path('accounts/', include('accounts.urls')),
    path('comment/write/<int:pk>', blog.views.comment_write, name='comment_write'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


