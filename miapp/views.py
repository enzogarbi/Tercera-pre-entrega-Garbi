from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

class PaginaInicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')

class PaginaRegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario registrado correctamente. Por favor, inicie sesión.')
            return redirect('login')
        else:
            return render(request, 'registro.html', {'form': form})

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PaginaLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos.'})

class PaginaMenuView(View):
    def get(self, request):
        return render(request, 'menu.html')

class AccionesVentaView(View):
    def get(self, request):
        acciones_venta = AccionVenta.objects.all()
        return render(request, 'acciones_venta.html', {"acciones_venta": acciones_venta})

class PaginaClientesView(View):
    def get(self, request):
        return render(request, 'clientes_list.html')

class PaginaProveedoresView(View):
    def get(self, request):
        return render(request, 'proveedor_list.html')

class PaginaPresupuestosView(View):
    def get(self, request):
        return render(request, 'presupuestos.html')

class PaginaOrdenesCompraView(View):
    def get(self, request):
        return render(request, 'orden_de_compra.html')

class ClienteList(ListView):
    model = Cliente
    template_name = "clientes_list.html"
    context_object_name = "clientes"

    def get_queryset(self):
        # Obtener la lista de clientes
        queryset = super().get_queryset()
        
        # Agregar un mensaje de depuración para verificar si se obtuvieron los clientes correctamente
        messages.info(self.request, f"Se encontraron {queryset.count()} clientes.")
        
        return queryset

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente_form.html"
    success_url = reverse_lazy('cliente_list')

class ClienteEditView(UpdateView):
    model = Cliente
    template_name = 'cliente_edit.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list') 

class ProveedorList(ListView):
    model = Proveedor
    template_name = "proveedor_list.html"
    context_object_name = "proveedor"

    def get_queryset(self):
        # Obtener la lista de proveedores
        queryset = super().get_queryset()
        
        # Agregar un mensaje de depuración para verificar si se obtuvieron los proveedores correctamente
        messages.info(self.request, f"Se encontraron {queryset.count()} proveedores.")
        
        return queryset

class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedor_form.html"
    success_url = reverse_lazy('proveedor_list')

class ProveedorEditView(UpdateView):
    model = Proveedor
    template_name = 'proveedor_edit.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list') 


class PaginaOrdenesCompraView(View):
    def get(self, request):
        form = OrdenDeCompraForm()
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra.html', {'form': form, 'ordenes': ordenes})

    def post(self, request):
        form = OrdenDeCompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de compra subida correctamente.')
            return redirect('subir_orden_compra_exitosa')
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra.html', {'form': form, 'ordenes': ordenes})

class PaginaOrdenesCompraListView(View):
    def get(self, request):
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra_list.html', {'ordenes': ordenes})

class SubirOrdenCompraExitosa(View):
    def get(self, request):
        return render(request, 'subir_orden_compra_exitosa.html')

def subir_orden_compra(request):
    if request.method == 'POST':
        form = OrdenDeCompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de compra subida correctamente.')
            return redirect('subir_orden_compra_exitosa')
    else:
        form = OrdenDeCompraForm()
    return render(request, 'subir_orden_compra.html', {'form': form})
