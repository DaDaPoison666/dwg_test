import allure
import pytest
from allure_commons.types import AttachmentType
from db_requests.postgre_requests import Db
from pom.wiki_page import WikiPage


@pytest.mark.usefixtures('setup')
@allure.epic('Wikipedia testing')
@allure.feature('Main page of Wikipedia')
class TestMainWikiPage:
    @allure.story('Test of searching bar using Search button')
    @allure.severity('Normal')
    def test_search_using_button(self):
        """Test of searching bar using Search button"""
        wiki = WikiPage(self.driver)
        try:
            wiki.search_data('Bill Gates')
            wiki.push_search_btn()
            with allure.step('Check if link is correct'):
                assert wiki.get_current_page_url() == '/wiki/%D0%93%D0%B5%D0%B9%D1%82%D1%81,_%D0%91%D0%B8%D0%BB%D0%BB'
        except AssertionError or Exception as e:
            with allure.step('Failed to use search field'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Failed_search',
                              attachment_type=AttachmentType.PNG)
                raise e

    @allure.story('Test of searching bar using submit')
    @allure.severity('Normal')
    def test_search_with_submit(self):
        wiki = WikiPage(self.driver)
        try:
            wiki.search_data('Bill Gates')
            wiki.submit_by_enter()
            with allure.step('Check if link is correct'):
                assert wiki.get_current_page_url() == '/wiki/%D0%93%D0%B5%D0%B9%D1%82%D1%81,_%D0%91%D0%B8%D0%BB%D0%BB'
        except AssertionError or Exception as e:
            with allure.step('Failed to use search field'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Failed_search',
                              attachment_type=AttachmentType.PNG)
                raise e

    @allure.story('Test of main page of WIKI in different languages')
    @allure.severity('High')
    @pytest.mark.parametrize('language, local_link, local_main_page', [('english', 'en.',
                                                                        '/wiki/Main_Page'),
                                                                       ('spanish', 'es.',
                                                                        '/wiki/Wikipedia:Portada'),
                                                                       ('italian', 'it.',
                                                                        '/wiki/Pagina_principale')])
    def test_wiki_multilang(self, language, local_link, local_main_page):
        wiki = WikiPage(self.driver, local_link)
        try:
            with allure.step(f'Check if the main page opened in {language}'):
                assert wiki.get_current_page_url() == local_main_page
        except AssertionError or Exception as e:
            with allure.step(f'Failed to load local page in {language}'):
                allure.attach(self.driver.get_screenshot_as_png(), name=f'Failed load {language} main page',
                              attachment_type=AttachmentType.PNG)
                raise e

    with (Db() as db):
        query = db.select_name_query()

        @allure.story('Test of search people from DB in WIKI')
        @allure.severity('High')
        @pytest.mark.parametrize('first_name, last_name', query)
        def test_search_people_from_db(self, first_name, last_name):
            wiki = WikiPage(self.driver)
            name_tuple = first_name, last_name
            name = ' '.join(name_tuple)
            wiki.search_data(name)
            wiki.push_search_btn()
            if wiki.check_failed_search_result() == "No such person":
                with Db() as db:
                    db.update_table(first_name=first_name, last_name=last_name)
            else:
                with allure.step('Person is found!'):
                    allure.attach(self.driver.get_screenshot_as_png(), name=f'wiki_page',
                                  attachment_type=AttachmentType.PNG)
                with Db() as db:
                    db.update_table(first_name=first_name, last_name=last_name,
                                    link=f'https://ru.wikipedia.org{wiki.get_current_page_url()}', state='true')

