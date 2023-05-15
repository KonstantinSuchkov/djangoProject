import adminapp.views as adminapp
from django.urls import path


app_name = 'adminapp'

urlpatterns = [
    path('users/read/', adminapp.ClientUsersListView.as_view(), name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('kindergardens/read/', adminapp.kindergardens, name='kindergardens'),
    path('kindergardens/create/', adminapp.KindergardenCreateView.as_view(), name='kindergarden_create'),
    path('kindergardens/update/<int:pk>/', adminapp.KindergardenUpdateView.as_view(), name='kindergarden_update'),
    path('kindergardens/delete/<int:pk>/', adminapp.KindergardenDeleteView.as_view(), name='kindergarden_delete'),
    path('accommodation/read/kindergardens/<int:pk>/', adminapp.accommodations, name='accommodations'),
    path('accommodation/update/<int:pk>/', adminapp.accommodation_update, name='accommodation_update'),
    path('accommodation/create/kindergardens/<int:pk>/', adminapp.accommodation_create, name='accommodation_create'),
    path('accommodation/read/<int:pk>/', adminapp.AccommodationDetailView.as_view(), name='accommodation_read'),
    path('accommodation/delete/<int:pk>/', adminapp.accommodation_delete, name='accommodation_delete'),
    path('areas/read/kindergardens/<int:pk>/', adminapp.areas, name='areas'),
    path('areas/update/<int:pk>/', adminapp.areas_update, name='areas_update'),
    path('areas/create/kindergardens/<int:pk>/', adminapp.areas_create, name='areas_create'),
    path('areas/read/<int:pk>/', adminapp.AreasDetailView.as_view(), name='areas_read'),
    path('areas/delete/<int:pk>/', adminapp.areas_delete, name='areas_delete'),
]
