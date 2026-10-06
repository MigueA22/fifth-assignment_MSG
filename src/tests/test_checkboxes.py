from src.pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):

    checkboxes = CheckboxesPage(page)

    # Step 1
    checkboxes.navigate()

    assert checkboxes.get_title() == "The Internet"

    # Step 2 y 3
    checkboxes.select_checkbox_1()

    assert checkboxes.is_checkbox_1_checked()

    # Step 4
    checkboxes.unselect_checkbox_2()

    assert not checkboxes.is_checkbox_2_checked()