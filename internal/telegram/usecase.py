from .models import BestsellerBookResponse, ArticleResponse, MovieReviewResponse

from pkg.nyt.api import get_bestsellers, get_article_by_query, get_popular_articles, get_movie_reviews_by_query


def return_all_books() -> list[str]:
    books_input = get_bestsellers()
    if len(books_input) == 0:
        return ["Нет книг. Попробуйте позже или обновите вашу сессию с ботом"]
    result_array: list[str] = []
    for book in books_input:
        result_array.append(str(BestsellerBookResponse(
            rank=book.rank, title=book.title, description=book.description,
            book_image=book.book_image, author=book.author
        )))

    return result_array


def find_articles(query: str, page: int = 0) -> list[str]:
    articles_input = get_article_by_query(query, page)
    if len(articles_input) == 0:
        return ["Нет статей. Попробуйте позже или обновите вашу сессию с ботом"]
    result_array: list[str] = []
    for article in articles_input:
        result_array.append(str(ArticleResponse(
            web_url=article.web_url, lead_paragraph=article.lead_paragraph,
            headline=article.headline, section_name=article.section_name,
            type_of_material=article.type_of_material, pub_date=article.pub_date,
            word_count=article.word_count
        )))

    return result_array


def find_popular_articles() -> list[str]:
    articles_input = get_popular_articles()
    if len(articles_input) == 0:
        return ["Нет статей. Попробуйте позже или обновите вашу сессию с ботом"]
    result_array: list[str] = []
    for article in articles_input:
        result_array.append(str(ArticleResponse(
            web_url=article.web_url, lead_paragraph=article.lead_paragraph,
            headline=article.headline, section_name=article.section_name,
            type_of_material=article.type_of_material, pub_date=article.pub_date,
            word_count=article.word_count
        )))

    return result_array


def find_movie_reviews(query: str) -> list[str]:
    reviews_input = get_movie_reviews_by_query(query)
    if len(reviews_input) == 0:
        return ["Нет рецензий. Попробуйте позже или обновите вашу сессию с ботом"]
    result_array: list[str] = []
    for review in reviews_input:
        result_array.append(str(MovieReviewResponse(
            display_title=review.display_title, summary_short=review.summary_short,
            publication_date=review.publication_date, url=review.url, byline=review.byline
        )))

    return result_array
