from behave import *

from pageobjects.alerts import AlertsPage

use_step_matcher('re')


@given('the user is in main page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    assert "javascript_alerts" in context.driver.current_url


@when('the user clicks the simple alert button')
def step_impl(context):
    page = AlertsPage(context.driver)
    page.btn__simple().click()


@when('the user clicks the accept/dismiss alert button')
def step_impl(context):
    page = AlertsPage(context.driver)
    page.btn__ad().click()


@when('the user accepts the alert')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.accept()


@when('the user dismiss the alert')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.dismiss()


@then('the message "(?P<text>.+)" is displayed')
def step_impl(context, text):
    page = AlertsPage(context.driver)
    assert page.result().text == text

