import allure
from selene import browser, by, have, be


@allure.step('Открытие страницы https://github.com')
def open_page():
    browser.open('/')


@allure.step('Поиск репозитория по названию: {repo_name}')
def search_repo(repo_name):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo_name).press_enter()


@allure.step('Переход по найденной ссылке: {repo_name}')
def go_to_repo(repo_name):
    browser.element(by.link_text(repo_name)).click()


@allure.step('Открытие вкладки "Issues')
def go_to_issue():
    browser.element('#issues-tab').click()


@allure.step('Проверка наличия задачи {number}')
def check_issue(number):
    browser.all('[aria-label=Issues][role=group]').element_by(have.text(number)).should(be.visible)


@allure.title('Проверка наличия названия Issue в репозитории')
@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Тест decorator steps")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'div50015')
def test_with_allure_labels():
    open_page()
    search_repo('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    go_to_issue()
    check_issue('#84')