from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from shop.models import *

User = get_user_model()

signup = CreateView.as_view(model=User, form_class=UserCreationForm, template_name='accounts/signup.html',
                            success_url='/')


# class SignupCreateView(UserCreationForm, CreateView):
#     model = User
#     form_class = UserCreationForm


# def signup(request):
#     pass


@login_required
def profile(request):
    order_list = Order.objects.all()
    return render(request, 'accounts/profile.html', {
        'order_list': order_list,
    })
