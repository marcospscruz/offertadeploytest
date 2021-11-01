from django.urls import path
from ofertas import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('supermercados/', views.SupermercadoListView.as_view(), name='supermercados'),
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('ofertas/', views.Em_OfertaListView.as_view(), name='ofertas'),
    path('ofertasporsuper/<int:pk>', views.ofertasporsuper, name='ofertasporsuper'),
    path('ondeencontrar/<int:pk>', views.ondeencontrar, name='ondeencontrar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)