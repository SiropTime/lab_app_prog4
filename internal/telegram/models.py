from pydantic import BaseModel


class BestsellerBookResponse(BaseModel):
    rank: int
    title: str
    description: str
    book_image: str
    author: str

    def __str__(self):
        return f"""
        #{self.rank} [Название]({self.book_image}): ***{self.title}***
        ___Автор___: {self.author}
        ___Описание___: {self.description}
        """


class ArticleResponse(BaseModel):
    web_url: str
    lead_paragraph: str
    headline: str
    section_name: str
    type_of_material: str
    pub_date: str
    word_count: str

    def __str__(self):
        return f"""
        [{self.headline}]({self.web_url})
        ___Тип материала___: {self.type_of_material}
        ___Раздел___: {self.section_name}
        ___Дата публикации___: {self.pub_date}
        ___Количество слов___: {self.word_count if self.word_count != 0 else 'Неизвестно'}
        ***Абзац***: {self.lead_paragraph}
        """


class MovieReviewResponse(BaseModel):
    display_title: str
    summary_short: str
    publication_date: str
    url: str
    byline: str

    def __str__(self):
        return f"""
        [{self.display_title}]({self.url})
        ___Автор___: {self.byline}
        ___Дата публикации___: {self.publication_date}
        ***Краткое содержание***: {self.summary_short}
        """
