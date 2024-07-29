from django.views.generic import RedirectView
from allauth.account.views import LoginView, LogoutView

class GoogleLoginView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'account_login'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class GoogleLogoutView(LogoutView):
    template_name = 'account/logout.html'
