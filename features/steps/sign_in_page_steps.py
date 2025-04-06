from behave import given, when, then


@when('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    context.app.sign_in_page.verify_username_field()


@then('Enter username')
def enter_valid_username(context):
    context.app.sign_in_page.input_username()


@then('Click "Continue" button')
def click_continue_btn(context):
    context.app.sign_in_page.click_signin_continue_btn()


@then('Enter invalid password')
def input_invalid_password(context):
    context.app.sign_in_page.input_invalid_password()


@then('Click "Sign in with password" button')
def click_sign_in_password_btn(context):
    context.app.sign_in_page.click_signin_continue_btn()


@then('"{error_msg}" error is shown')
def verify_pw_error_msg(context, error_msg):
    context.app.sign_in_page.verify_pw_error_msg(error_msg)


@then('Click Sign In button')
def click_sign_in_btn(context):
    context.app.sign_in_page.click_sign_in_btn()


@then('Input username and password on Sign In page')
def input_username_and_password(context):
    context.app.sign_in_page.verify_username_field()
    context.app.sign_in_page.verify_password_field()
    context.app.sign_in_page.input_username_and_password()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_url()
    context.app.sign_in_page.verify_page_header()
    context.app.sign_in_page.verify_username_field()
    context.app.sign_in_page.verify_password_field()


@then('Verify user is logged in and redirected to home page')
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_is_logged_in()
