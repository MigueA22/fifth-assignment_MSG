from src.pages.data_tables_page import DataTablesPage


def test_data_tables(page):

    data_tables = DataTablesPage(page)

    # Step 1
    data_tables.navigate()

    assert data_tables.get_title() == "The Internet"

    # Step 2 y 3
    due_total = data_tables.get_due_total()

    assert due_total == 251