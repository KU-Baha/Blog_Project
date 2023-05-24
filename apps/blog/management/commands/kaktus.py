from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

import requests
from bs4 import BeautifulSoup

from apps.blog.models import Post, Category, Tag


class Command(BaseCommand):
    help = _('Parse data from external source')
    base_url = 'https://kaktus.media'

    def add_arguments(self, parser):
        parser.add_argument('--date', type=str, help=_('Date in format: YYYY-mm-dd'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(_('Parsing starting!')))
        self.parse(options['date'])
        self.stdout.write(self.style.SUCCESS(_('Parsing finished!')))

    def get_html(self, url):
        response = requests.get(url)
        return response.content

    def get_soup(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def parse(self, date):
        url = f"{self.base_url}/?lable=8&date={date}&order=time"
        self.stdout.write(self.style.SUCCESS(_(f"Start parsing {url}")))

        main_html = self.get_html(url)
        soup = self.get_soup(main_html)

        news_block = soup.find('div', {'class': 'Tag--articles'})

        news_list = news_block.find_all('div', {'class': 'Tag--article'})

        for news in news_list:
            try:
                post = Post()
                news_url = news.find('a', {'class': 'ArticleItem--name'}).get('href')
                post.origin_url = news_url
                self.stdout.write(self.style.SUCCESS(_(f"Start parsing news - {news_url}")))

                post.logo = news.find('img', {'class': 'ArticleItem--image-img'}).get('src')

                news_html = self.get_html(news_url)
                news_soup = self.get_soup(news_html)

                post.title = news_soup.find('h1', {'class': 'Article--title'}).text

                news_info = news_soup.find('div', {'class': 'Article--info'})

                news_category = news_info.find('a', {'class': 'Article--category-link'}).text.strip().title()
                category = Category.objects.get_or_create(name=news_category)
                post.category = category[0]

                news_pub_date = news_info.find('time', {'class': 'Article--createAt'}).get('datetime')
                post.pub_date = news_pub_date

                news_author = news_info.find('a', {'class': 'Article--author'}).text.strip().title()
                post.author = news_author

                news_content_block = news_soup.find('div', {'class': 'Article--text'})

                content = ''

                for p in news_content_block.find_all('p'):
                    content += f"{p.text}\n"

                post.content = content
                post.save()

                news_tag_block = news_soup.find('ul', {'class': 'Article--tags'})

                for tag in news_tag_block.find_all('li', {'class': 'Article--tags-tag'}):
                    tag_name = tag.text.strip().title()
                    tag = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag[0])

                self.stdout.write(self.style.SUCCESS(_(f"News - {news_url} parsed!")))

            except Exception as e:
                self.stdout.write(self.style.ERROR(_(f"Error: {e}")))

    # def parse_article(self, url):
