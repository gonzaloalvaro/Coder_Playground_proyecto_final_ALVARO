from django.urls import path
from ventas.views import crear_cliente, leer_clientes, eliminar_cliente, editar_cliente, VentaListView, VentaCreateView, VentaDeleteView, VentaUpdateView, VentaDetailView

urlpatterns = [
    # CRUD de clientes creado con vistas basadas en funciones:
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    path('leer_clientes/', leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', editar_cliente, name='editar cliente'),
    path('ventas_listas/', VentaListView.as_view(), name='ventas listas'),
    path('ventas_crear/', VentaCreateView.as_view(), name='ventas crear'),
    path('<pk>/eliminar/', VentaDeleteView.as_view(), name='ventas eliminar'),
    path('<pk>/editar/', VentaUpdateView.as_view(), name='ventas editar'),
    path('<pk>/detalle/', VentaDetailView.as_view(), name='ventas detalle')

]