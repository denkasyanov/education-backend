from abc import ABCMeta, abstractmethod
from django.conf import settings
from urllib.parse import urljoin

from orders.models import Order
from users.models import User


class Bank(metaclass=ABCMeta):
    def __init__(self, order: Order, success_url=None, fail_url=None):
        self.order = order
        self._success_url = success_url
        self._fail_url = fail_url

    @abstractmethod
    def get_initial_payment_url(self) -> str:
        raise NotImplementedError()

    @property
    def success_url(self) -> str:
        return self._success_url or urljoin(settings.FRONTEND_URL, '/success/')

    @property
    def fail_url(self) -> str:
        return self._fail_url or urljoin(settings.FRONTEND_URL, '/error/?code=banking')

    @property
    def price(self) -> int:
        return int(self.order.price * 100)

    @property
    def user(self) -> User:
        return self.order.user
