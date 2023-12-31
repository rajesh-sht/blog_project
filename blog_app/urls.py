"""
URL configuration for BLOG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog_app import views as v
urlpatterns = [
    path('', v.post_list, name='post-list'),
    path('post-detail/<int:id>/', v.post_detail, name='post-detail'),
    path('draft-list/', v.draft_list, name='draft-list'),
    path('post-create/', v.post_create, name='post-create'),
    path('post-publish/<int:id>/', v.post_publish, name='post-publish'),
    path('post-delete/<int:id>/', v.post_delete, name='post-delete'),
    path('post-update/<int:id>/', v.post_update, name='post-update'),

]
