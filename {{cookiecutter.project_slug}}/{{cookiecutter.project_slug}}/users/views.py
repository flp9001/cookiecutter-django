# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserEditMultiForm
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditMultiForm
    success_url = reverse_lazy('users:redirect')

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)
        
    def get_form_kwargs(self):
        kwargs = super(UserUpdateView, self).get_form_kwargs()
        user = self.object
        profile = self.object.profile

        kwargs.update(instance={
            'user': user,
            'profile': profile,
        })

        return kwargs

    def form_valid(self, form):
        user_form = form.forms['user']
        profile_form = form.forms['profile']
        super(UserUpdateView, self).form_valid(user_form)
        super(UserUpdateView, self).form_valid(profile_form)
        return super(UserUpdateView, self).form_valid(form)



class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
