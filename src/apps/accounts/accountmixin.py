from django.contrib.auth.models import Group
from django.shortcuts import redirect


class ValidatePermissionMixin:
    url_redirect = None
    permission_required = ''

    def get_perm(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perm()):
            return super().dispatch(request, *args, **kwargs)
        return redirect('/login')

