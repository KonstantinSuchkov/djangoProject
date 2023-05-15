from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from mainapp.models import Accommodation
from mainapp.models import ListOfKindergarden
from authapp.models import ClientUser
from authapp.forms import ClientUserRegisterForm
from adminapp.forms import ClientUserAdminEditForm
from adminapp.forms import AccommodationEditForm


# админка - список пользователей
class ClientUsersListView(ListView):
    model = ClientUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# админка - создание пользователя
@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ClientUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ClientUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', content)


# админка - редактирование пользователя
@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ClientUser, pk=pk)

    if request.method == 'POST':
        edit_form = ClientUserAdminEditForm(request.POST,
                                            request.FILES,
                                        instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update',
                                                args=[edit_user.pk]))
    else:
        edit_form = ClientUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', content)


# админка - удаление пользователя
@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ClientUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', content)


# админка - список садиков
@user_passes_test(lambda u: u.is_superuser)
def kindergardens(request):
    title = 'админка/садики'

    kindergardens_list = ListOfKindergarden.objects.all()

    content = {
        'title': title,
        'objects': kindergardens_list
    }

    return render(request, 'adminapp/kindergardens.html', content)


# админка - создание садика
class KindergardenCreateView(CreateView):
    model = ListOfKindergarden
    template_name = 'adminapp/kindergarden_update.html'
    success_url = reverse_lazy('admin:kindergardens')
    fields = '__all__'


# админка - редактирование садика
class KindergardenUpdateView(UpdateView):
    model = ListOfKindergarden
    template_name = 'adminapp/kindergarden_update.html'
    success_url = reverse_lazy('admin:kindergardens')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'садики/редактирование'

        return context


# админка - удаление садика
class KindergardenDeleteView(DeleteView):
    model = ListOfKindergarden
    template_name = 'adminapp/kindergarden_delete.html'
    success_url = reverse_lazy('admin:kindergardens')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# админка - список предложений компании
@user_passes_test(lambda u: u.is_superuser)
def accommodations(request, pk):
    title = 'админка/размещение'

    kindergarden = get_object_or_404(ListOfKindergarden, pk=pk)
    accommodation_list = Accommodation.objects.filter(
        kindergarden__id=pk).order_by('name')

    content = {
        'title': title,
        'kindergarden': kindergarden,
        'objects': accommodation_list,
    }

    return render(request, 'adminapp/accommodations.html', content)


# админка - создание нового предложения
@user_passes_test(lambda u: u.is_superuser)
def accommodation_create(request, pk):
    title = 'размещение/создание'
    kindergarden = get_object_or_404(ListOfKindergarden, pk=pk)

    if request.method == 'POST':
        pass
        accommodation_form = AccommodationEditForm(request.POST, request.FILES)
        if accommodation_form.is_valid():
            accommodation_form.save()
            return HttpResponseRedirect(reverse('admin:accommodations', args=[pk]))

    else:

        accommodation_form = AccommodationEditForm(
            initial={'kindergarden': kindergarden})
    content = {
        'title': title,
        'update_form': accommodation_form,
        'kindergarden': kindergarden,
    }
    return render(request, 'adminapp/accommodation_update.html', content)


# админка - редактирование предложения
@user_passes_test(lambda u: u.is_superuser)
def accommodation_update(request, pk):
    title = 'размещение/редактирование'
    edit_accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        accommodation_edit_form = AccommodationEditForm(
            request.POST, request.FILES, instance=edit_accommodation)
        if accommodation_edit_form.is_valid():
            accommodation_edit_form.save()
            return HttpResponseRedirect(
                reverse('admin:accommodation_update', args=[edit_accommodation.pk]))
    else:
        accommodation_edit_form = AccommodationEditForm(instance=edit_accommodation)
    content = {
        'title': title,
        'update_form': accommodation_edit_form,
        'kindergarden': edit_accommodation.kindergarden,
    }
    return render(request, 'adminapp/accommodation_update.html', content)


# админка - карточка предложения компании
class AccommodationDetailView(DetailView):
    model = Accommodation
    template_name = 'adminapp/accommodation_read.html'


# админка - удаление предложения
@user_passes_test(lambda u: u.is_superuser)
def accommodation_delete(request, pk):
    title = 'размещение/удаление'
    accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        accommodation.is_active = False
        accommodation.save()
        return HttpResponseRedirect(reverse('admin:accommodations', args=[accommodation.country.pk]))
    content = {
        'title': title,
        'accommodation_to_delete': accommodation,
    }
    return render(request, 'adminapp/accommodation_delete.html', content)
