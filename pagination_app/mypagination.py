from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class MypageNumberPagination(PageNumberPagination):
    page_size=4
    page_query_param='p'
    page_size_query_param='records'
    max_page_size=3
    last_page_strings='end'
    
class MyLimitOffestPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='setlimit'
    offset_query_param='setoffset'
    max_limit=6
    