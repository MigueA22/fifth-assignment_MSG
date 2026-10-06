class BasicAuthPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):

        self.page.goto(
            "https://the-internet.herokuapp.com/",
            timeout=120000
        )

    def get_title(self):

        return self.page.title()

    def open_basic_auth(self):

        self.page.goto(
            "https://admin:admin@the-internet.herokuapp.com/basic_auth",
            timeout=120000
        )

    def get_success_message(self):

        return self.page.locator("p").text_content()
