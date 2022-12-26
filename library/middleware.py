import threading
from django.db import connections
from .utils import get_db_name

ThreadLocal = threading.local()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = get_db_name(request)
        setattr(ThreadLocal, 'tenant', db)
        response = self.get_response(request)
        return response


def get_current_tenant():
    return getattr(ThreadLocal, 'tenant', 'default')

def set_current_tenant(db):
    setattr(ThreadLocal, 'tenant', db)
        