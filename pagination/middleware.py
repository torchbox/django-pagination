def get_page(self, suffix):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        page_key = 'page%s' % suffix
        get = self.GET
        if page_key in get:
            page = get[page_key]
        else:
            post = self.POST
            if page_key in post:
                page = post[page_key]
            else:
                return 1
        return int(page)
    except (AttributeError, KeyError, ValueError, TypeError):
        return 1

class PaginationMiddleware(object):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def process_request(self, request):
        request.__class__.page = get_page
