# from __future__ import annotations

# from typing import List

from pydantic import BaseModel


class Isbn(BaseModel):
    isbn10: str
    isbn13: str


class BuyLink(BaseModel):
    name: str
    url: str


class BestsellerBook(BaseModel):
    rank: int
    rank_last_week: int
    weeks_on_list: int
    asterisk: int
    dagger: int
    primary_isbn10: str
    primary_isbn13: str
    publisher: str
    description: str
    price: str
    title: str
    author: str
    contributor: str
    contributor_note: str
    book_image: str
    book_image_width: int
    book_image_height: int
    amazon_product_url: str
    age_group: str
    book_review_link: str
    first_chapter_link: str
    sunday_review_link: str
    article_chapter_link: str
    isbns: list[Isbn]
    buy_links: list[BuyLink]
    book_uri: str


from typing import Any, List, Optional

from pydantic import BaseModel


class Headline(BaseModel):
    main: str
    kicker: Any
    content_kicker: Any
    print_headline: Any
    name: Any
    seo: Any
    sub: Any


class Keyword(BaseModel):
    name: str
    value: str
    rank: int
    major: str


class Byline(BaseModel):
    original: Any
    person: List
    organization: Any


class Article(BaseModel):
    web_url: str
    lead_paragraph: str
    headline: str
    section_name: str
    type_of_material: str
    pub_date: str
    word_count: str


class MovieReview(BaseModel):
    display_title: str
    summary_short: str
    publication_date: str
    url: str
    byline: str
