class DataTablesPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(
            "https://the-internet.herokuapp.com/tables",
            timeout=120000
        )

    def get_title(self):
        return self.page.title()

    def get_due_total(self):

        due_values = self.page.locator(
            "#table1 tbody tr td:nth-child(4)"
        ).all_text_contents()

        total = 0

        for value in due_values:
            amount = float(
                value.replace("$", "")
            )
            total += amount

        return total