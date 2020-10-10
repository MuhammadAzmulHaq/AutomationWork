import pytest
from pages.result import DuckduckGoResultpage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'azmul'])
def test_basic_duckduckgo_search(browser,phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckduckGoResultpage(browser)


    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "Testing"
    search_page.search(phrase)

    # Then the search result title contains "Testing"
   # assert PHRASE in result_page.title()

    # And the search result query is "Testing"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "Testing"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    assert phrase in result_page.title()