from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shakeHtra.views.home', name='home'),
    # url(r'^shakeHtra/', include('shakeHtra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', "shakeHtra.graphIO.views.index"),
    url(r'^test/', "shakeHtra.graphIO.views.test"),
    url(r'^initialJson',"shakeHtra.graphIO.views.initialJson"),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
     {'document_root': 'C:/Users/30ryo/Documents/GitHub/shakeHtra/src/ShakeHandsTranslation/StaticFile'}),
)
