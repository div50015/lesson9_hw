import allure
from selene import browser, by, have, be


def test_with_allure_steps():
    allure.dynamic.title('Проверка наличия названия Issue в репозитории')
    allure.dynamic.tag('web')
    allure.dynamic.severity(severity_level='Critical')
    allure.dynamic.feature("Issues")
    allure.dynamic.story("Тест lambda steps")
    allure.dynamic.link("https://github.com/", name='Testing')
    allure.dynamic.label('owner', 'div50015')

    with allure.step('Открытие страницы https://github.com'):
        browser.open('/')

    with allure.step('Поиск репозитория по названию: eroshenkoam/allure-example'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переход по найденной ссылке'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открытие вкладки "Issues"'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия задачи 84'):
        browser.all('[aria-label=Issues][role=group]').element_by(have.text('#84')).should(be.visible)