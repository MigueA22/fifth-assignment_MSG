class DragDropPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(
            "https://the-internet.herokuapp.com/drag_and_drop",
            timeout=120000
        )

    def get_title(self):
        return self.page.title()

    def get_column_a_text(self):
        return self.page.locator("#column-a header").text_content()

    def get_column_b_text(self):
        return self.page.locator("#column-b header").text_content()

    def drag_a_to_b(self):
        self.page.locator("#column-a").drag_to(
            self.page.locator("#column-b")
        )