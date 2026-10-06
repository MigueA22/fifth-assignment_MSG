from src.pages.basic_auth_page import BasicAuthPage


def test_basic_auth(page):

    basic_auth = BasicAuthPage(page)

    # Step 1
    basic_auth.navigate()

    assert basic_auth.get_title() == "The Internet"

    # Step 2 y 3
    basic_auth.open_basic_auth()

    # Step 4
    success_message = basic_auth.get_success_message()

    assert (
        "Congratulations! You must have the proper credentials."
        in success_message
    )