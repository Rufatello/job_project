from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, TemplateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect
from register.forms import RegisterUserForm, LoginUserForm, PatientCreateView
from register.models import Patient

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreateView
    template_name = 'register/CreatePatient.html'

    def get_success_url(self):
        return reverse_lazy('register:home')


class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'register/UpdatePatient.html'
    success_url = reverse_lazy('register:home')

class PatientDeleteeView(DeleteView):
    model = Patient
    fields = '__all__'
    template_name = 'register/delete_patient.html'
    success_url = reverse_lazy('register:home')
class PatientListView(ListView):
    model = Patient
    template_name = 'register/index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            return Patient.objects.filter(doctor_id=user_id)
        else:
            return Patient.objects.none()



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('register:home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'


    def get_success_url(self):
        return reverse_lazy('register:home')

def LogoutUser(request):
    logout(request)

    return redirect('register:home')

