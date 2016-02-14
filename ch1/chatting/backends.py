from django.conf import settings
from django.contrib.auth.hashers import check_password
from chatting.models import Member

class MemberAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, username=None, password=None):
        """
        Authentication method
        """
        try:
            user = Member.objects.get(username=username)
            if user.check_password(password):
                return user
        except Member.DoesNotExist:
            return None

    def get_user(self, member_id):
        try:
            user = Member.objects.get(pk=member_id)
            if user.is_active:
                return user
            return None
        except Member.DoesNotExist:
            return None
