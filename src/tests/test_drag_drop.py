from src.pages.drag_drop_page import DragDropPage


def test_drag_and_drop(page):

    drag_drop = DragDropPage(page)

    # Step 1
    drag_drop.navigate()

    assert drag_drop.get_title() == "The Internet"

    # Step 2 y 3
    assert drag_drop.get_column_a_text() == "A"
    assert drag_drop.get_column_b_text() == "B"

    # Step 4
    drag_drop.drag_a_to_b()

    # Step 5
    assert drag_drop.get_column_b_text() == "A"
