from django.conf.urls import patterns, include, url

import djangowars.views.crimes
import djangowars.views.hospital
import djangowars.views.inventario
import djangowars.views.loja
import djangowars.views.luta
import djangowars.views.player
import djangowars.views.site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
                       url(r'^$', djangowars.views.site.index, name='pagina_inicial'),
                       
                       url(r'^registrar/$', djangowars.views.player.registrar, name='pagina_de_registro'), # pagina de cadastro
                       url(r'^login/$', djangowars.views.player.logar, name='pagina_de_login'), # pagina de login
                       
                       url(r'^crimes/$', djangowars.views.crimes.crimes, name='pagina_de_crimes'),
                       url(r'^crimes/cometer/1/$', djangowars.views.crimes.cometer_crime1),
                       url(r'^crimes/cometer/2/$', djangowars.views.crimes.cometer_crime2),
                       url(r'^crimes/cometer/3/$', djangowars.views.crimes.cometer_crime3),
                       url(r'^crimes/cometer/4/$', djangowars.views.crimes.cometer_crime4),
                       
                       url(r'^loja/$', djangowars.views.loja.loja, name='pagina_da_loja'), # pagina de loja
                       url(r'^loja/comprar/armadura/(\d+)/$', djangowars.views.loja.comprar_armadura), # pagina de loja
                       url(r'^loja/vender/armadura/(\d+)/$', djangowars.views.loja.vender_armadura), # pagina de loja
                       url(r'^loja/comprar/arma/(\d+)/$', djangowars.views.loja.comprar_arma), # pagina de loja
                       url(r'^loja/vender/arma/(\d+)/$', djangowars.views.loja.vender_arma), # pagina de loja
                       
                       url(r'^inventario/$', djangowars.views.inventario.inventario, name='pagina_do_inventario'),
                       url(r'^inventario/equipar/armadura/(\d+)/$', djangowars.views.inventario.equipar_armadura),
                       url(r'^inventario/equipar/arma/(\d+)/$', djangowars.views.inventario.equipar_arma),
                       
                       url(r'^stats/$', djangowars.views.player.stats, name='pagina_de_stats'),
                       url(r'^stats/adicionar/(\w+)$', djangowars.views.player.adicionar),
                       
                       url(r'^alvos/$', djangowars.views.luta.alvos, name='pagina_de_alvos'),
                       url(r'^alvos/atacar/(\d+)/$', djangowars.views.luta.atacar),

                       url(r'^hospital/$', djangowars.views.hospital.hospital, name='pagina_do_hospital'),
                       url(r'^hospital/curar/(\d+)/$', djangowars.views.hospital.curar),
                       url(r'^hospital/curar/x/$', djangowars.views.hospital.curarx),
                       
                       url(r'^rank/$', djangowars.views.player.rank, name='pagina_do_rank'),
                       
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)