from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from adopter.view import AdopterCreateView, AdopterLoginView
from pet.view import PetListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", AdopterCreateView.as_view(), name="register"),
    path("login/", AdopterLoginView.as_view(next_page="login"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("pets/", PetListView.as_view(), name="pet_list"),
    # path("adopter/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
