from rest_framework.throttling import UserRateThrottle

class TestRateThrottle(UserRateThrottle):
    scope='Test'