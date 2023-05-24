from datetime import datetime

from celery import shared_task
from .management.commands.kaktus import Command

from .models import BannedWord


@shared_task
def create_banned_word(date: str) -> str:
    Command().handle(date=date)
    return 'Success'
