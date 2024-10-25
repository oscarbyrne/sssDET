from e2e.pages import (
    common,
    login,
    product,
    basket,
)


USERNAME = 'bjoern.kimminich@gmail.com'


def with_name(items, name):
    return [
        item for item in items
        if item.name == name
    ]


def test_add_remove_item(page, user_with_email):
    user = user_with_email(USERNAME)
    item_name = 'Carrot Juice'
    
    page.goto('http://sut:3000')

    # Given I'm logged in
    common.WelcomeModal(page).dismiss()
    common.Header(page).toggle_account_modal()
    common.AccountModal(page).login()
    login.Form(page).enter_email(user.email)
    login.Form(page).enter_password(user.password)
    login.Form(page).submit()
    
    # When I add item
    matching_items = with_name(
        product.List(page).items,
        item_name
    )
    next(matching_items).add_to_basket()
    
    # Then item appears in basket
    common.Header(page).view_basket()
    matching_items = with_name(
        basket.List(page).items,
        item_name
    )
    assert len(matching_items) == 1

    # When I delete item
    next(matching_items).delete()
    
    # Then item no longer in basket
    matching_items = with_name(
        basket.List(page).items,
        item_name
    )
    assert len(matching_items) == 0

    # And I can log out
    common.Header(page).show_account_modal()
    common.AccountModal(page).logout()
    common.Header(page).show_account_modal()
    expect(
        common.AccountModal(page).login_button
    ).to_be_visible()
