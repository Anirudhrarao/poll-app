from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 

def create_user(self,email,password,**extra_fields):
    if not email:
        raise ValueError(_('email should be there'))
    email = self.normalize_email(email)
    