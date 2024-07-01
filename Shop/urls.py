from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import ShopSitemap


sitemaps = {
    'shop': ShopSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)