from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

import requests
from bs4 import BeautifulSoup


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
        # date format: 2023-05-19
        response = self.get_html(f"{self.base_url}/?lable=8&date={date}&order=time")
        soup = self.get_soup(response)
        news_block = soup.find('div', {'class': 'Tag--articles'})
        print(len(news_block.find_all('div', {'class': 'Tag--article'})))