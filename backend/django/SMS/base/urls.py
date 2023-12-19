# ----- 3rd Party Libraries
from django.urls import path

# ----- In-Built Libraries -----
from base import views


contact_list = views.ContactView.as_view({
    'get': 'list',
    'post': 'create'
})
contact_detail = views.ContactView.as_view({
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns=[
        path('contact/', contact_list, name='contact_list'),
        path('contact/<int:pk>', contact_detail, name='contact_detail'),
    ]

