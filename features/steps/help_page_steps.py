from behave import given, when, then


@given('Open help.target.com/help')
def open_help_page(context):
    context.app.help_page.open_help_page()


@given('Open Help page for Returns')
def open_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {dropdown_option}')
def select_help_topic(context, dropdown_option):
    context.app.help_page.select_help_topic(dropdown_option)


@then('Verify help {header} page opened')
def verify_help_topic_page(context, header):
    context.app.help_page.verify_help_topic_page(header)


@then('"Target Help" header is shown')
def verify_target_help_header(context):
    context.app.help_page.verify_target_help_header()


@then('Search input is shown')
def verify_search_input(context):
    context.app.help_page.verify_search_input()


@then('Search icon is shown')
def verify_search_icon_is_shown(context):
    context.app.help_page.verify_search_icon()


@then('"What would you like to do" section is shown')
def verify_ask_section(context):
    context.app.help_page.verify_ask_section()


@then('"contact us" and "product recalls" section is shown')
def verify_contact_us_links(context):
    context.app.help_page.verify_contact_us_links()


@then('"Browse all Help pages" header is shown')
def verify_browse_all_header(context):
    context.app.help_page.verify_browse_all_header()
