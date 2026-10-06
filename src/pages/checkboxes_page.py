class CheckboxesPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(
            "https://the-internet.herokuapp.com/checkboxes",
            timeout=120000
        )

    def get_title(self):
        return self.page.title()

    def select_checkbox_1(self):
        self.page.locator("#checkboxes input").nth(0).click()

    def unselect_checkbox_2(self):
        self.page.locator("#checkboxes input").nth(1).click()

    def is_checkbox_1_checked(self):
        return self.page.locator(
            "#checkboxes input"
        ).nth(0).is_checked()

    def is_checkbox_2_checked(self):
        return self.page.locator(
            "#checkboxes input"
        ).nth(1).is_checked()