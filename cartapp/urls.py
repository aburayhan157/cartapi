from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from cartapp.views import ProductView, UserView, OrderView, LogoutView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>', OrderView.as_view()),
    path('register/', UserView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view()),
]
