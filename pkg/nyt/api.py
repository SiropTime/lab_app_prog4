import requests

from .models import BestsellerBook, Article, MovieReview
from .constants import API_URL, API_KEY


def get_bestsellers() -> list[BestsellerBook | None]:
    response = requests.get(f"{API_URL}svc/books/v3/lists/current/hardcover-fiction.json?api-key={API_KEY}")
    if response.status_code != 200:
        return []
    response_body = response.json()
    result_array: list[BestsellerBook] = []
    for book in response_body["results"]["books"]:
        result_array.append(BestsellerBook(**book))

    return result_array


def get_article_by_query(query: str, page: int = 0) -> list[Article | None]:
    print(f"{API_URL}svc/search/v2/articlesearch.json?q={query}?page={page}?api-key={API_KEY}")
    response = requests.get(f"{API_URL}svc/search/v2/articlesearch.json?q={query}&page={page}&api-key={API_KEY}")
    if response.status_code != 200:
        return []
    response_body = response.json()
    result_array: list[Article] = []

    for article in response_body["response"]["docs"]:
        try:
            result_array.append(Article(web_url=article["web_url"], lead_paragraph=article["lead_paragraph"],
                                        headline=article["headline"]["main"], section_name=article["section_name"],
                                        type_of_material=article["type_of_material"], pub_date=article["pub_date"],
                                        word_count=article["word_count"]))
        except KeyError:
            pass

    return result_array


def get_popular_articles() -> list[Article | None]:
    response = requests.get(f"{API_URL}svc/mostpopular/v2/viewed/7.json?api-key={API_KEY}")
    if response.status_code != 200:
        return []
    response_body = response.json()
    result_array: list[Article] = []
    for article in response_body["results"]:
        try:
            result_array.append(Article(web_url=article["url"], lead_paragraph=article["abstract"],
                                        headline=article["title"], section_name=article["section"],
                                        type_of_material=article["type"], pub_date=article["published_date"],
                                        word_count=0))
        except KeyError:
            pass

    return result_array


def get_movie_reviews_by_query(query: str) -> list[MovieReview | None]:
    response = requests.get(f"{API_URL}svc/movies/v2/reviews/search.json?query={query}&api-key={API_KEY}")
    if response.status_code != 200:
        return []
    response_body = response.json()
    if response_body["results"] is None:
        return []

    result_array: list[MovieReview] = []

    for review in response_body["results"]:
        try:
            result_array.append(MovieReview(display_title=review["display_title"],
                                            byline=review["byline"],
                                            summary_short=review["summary_short"],
                                            publication_date=review["publication_date"],
                                            url=review["link"]["url"]))
        except KeyError:
            pass

    return result_array
