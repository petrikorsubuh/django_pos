from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, ValidatePermissionMixin
from .forms import *
from django.http import HttpResponse
from mypermissionmixin.custommixin import ValidatePermissionMixin



class ListItemView(LoginRequiredMixin, ValidatePermissionMixin, View):
    permission_required = 'items.view_items'
    template_name = 'sales/list_item.html'
    login_url = '/login'

    def get(self, request):
        obj = Items.objects.all()
        print(request.user.is_authenticated)
        return render(request, self.template_name, {
            'obj': obj,
        })


class AddItemView(LoginRequiredMixin, ValidatePermissionMixin, View):

    template_name = 'sales/add_item.html'
    login_url = '/login'
    permission_required = [('items.add_items')]

    def get(self, request):
        form = ItemForm()
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        print('isi request.POST : ', request.POST)
        print('isi request.FILES :', request.FILES)
        print('isi form :', form)
        if form.is_valid():
            print('Valid Bre...')
            obj = Items()
            obj.categories = form.cleaned_data['category']
            obj.name = form.cleaned_data['name']
            obj.price = int(form.cleaned_data['price'])
            obj.description = form.cleaned_data['description']
            obj.item_img = request.FILES['item_img']
            obj.save()
            return redirect('/items')
        return HttpResponse(request, form.errors)


class UpdateItemView(LoginRequiredMixin, ValidatePermissionMixin, View):
    permission_required = [('items.change_items')]
    template_name = 'sales/update_item.html'
    login_url = '/login'

    def get(self, request, id):
        item = Items.objects.get(id=id)
        print(item)
        print(item.categories)
        print(type(item.categories))
        data = {
            'id': item.id,
            'category': item.categories,
            'name': item.name,
            'unit': item.unit,
            'price': item.price,
            'description': item.description,
            'item_img': item.item_img
        }
        form = ItemForm(initial=data)
        return render(request, self.template_name, {
            'form': form,
            'id': id
        })

    def post(self, request, id):
        obj = Items.objects.get(id=id)
        form = UpdateItemForm(request.POST, request.FILES)
        if form.is_valid():
            obj.categories = form.cleaned_data['category']
            print('isi categories', form.cleaned_data['category'])
            obj.name = form.cleaned_data['name']
            obj.price = form.cleaned_data['price']
            obj.unit = form.cleaned_data['unit']
            obj.description = form.cleaned_data['description']
            try:
                obj.item_img = request.FILES['item_img']
                obj.save()
            except:
                obj.save()
            return redirect('/items')
        return HttpResponse(form.errors)


class DeleteItemView(LoginRequiredMixin, View):
    def get(self, request, id):
        obj = Items.objects.get(id=id)
        obj.delete()
        return redirect('/items')

class ListCategoriesView(View):
    template_name = 'list_categories.html'

    def get(self, request):
        obj = Categories.objects.all()
        return render(request, self.template_name, {
            'obj': obj
        })



class AddCategoriesView(View):
    template_name = 'add_categories.html'

    def get(self, request):
        form = AddCategoriesForm(request.POST)
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = AddCategoriesForm(request.POST)
        if form.is_valid():
            obj = Categories()
            obj.name = form.cleaned_data['name']
            obj.save()
            return redirect('/items/categories')
        return HttpResponse(form.errors)

class EditCategoriesView(View):
    template_name = 'edit_categories.html'

    def get(self, request, id):
        obj = Categories.objects.get(id=id)
        data = {
            'name': obj.name
        }
        form = AddCategoriesForm(initial=data)
        return render(request, self.template_name, {
            'form': form,
            'id': id
        })

    def post(self, request, id):
        form = AddCategoriesForm(request.POST)
        if form.is_valid():
            obj = Categories.objects.get(id=id)
            obj.name = form.cleaned_data['name']
            obj.save()
            return redirect('/items/categories')
        return HttpResponse(form.errors)


class DeleteCategoriesView(View):
    def get(self, request, id):
        obj = Categories.objects.get(id=id)
        obj.delete()
        return redirect('/items/categories')


class ListUnitView(View):
    template_name = 'list_unit.html'

    def get(self, request):
        obj = Unit.objects.all()
        return render(request, self.template_name,{
            'obj': obj
        })

class AddUnitView(View):
    template_name = 'add_unit.html'

    def get(self, request):
        form = UnitForm(request.POST)
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = UnitForm(request.POST)
        if form.is_valid():
            obj = Unit()
            obj.name = form.cleaned_data['name']
            obj.save()
            return redirect('/items/unit')
        return HttpResponse(form.errors)


class EditUNitView(View):
    template_name = 'edit_unit.html'

    def get(self, request, id):
        obj = Unit.objects.get(id=id)
        data = {
            'name': obj.name
        }
        form = UnitForm(initial=data)
        return render(request, self.template_name, {
            'form': form,
            'id': id
        })

    def post(self, request, id):
        form = UnitForm(request.POST)
        if form.is_valid():
            obj = Unit.objects.get(id=id)
            obj.name = form.cleaned_data['name']
            obj.save()
            return redirect('/items/unit')
        return HttpResponse(form.errors)


class DeleteUnitView(View):
    def get(self, request, id):
        obj = Unit.objects.get(id=id)
        obj.delete()
        return redirect('/items/unit')
