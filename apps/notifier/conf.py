from enum import Enum
from collections import namedtuple
from django.db import models

PostSaveContext = namedtuple('PostSaveContext',
                              'module '
                              'class_name '
                              'instance_identifier '
                              'action')

Data = namedtuple('Data', 'name '
                          'body '
                          'recipients '
                          'is_notify_screen '
                          'is_push '
                          'client_action '
                          'icon ')

class ClientAction( models.TextChoices ):
    OPEN_ARTICLE = 'OPEN_ARTICLE', 'Open article page'
    OPEN_GIFTS = 'OPEN_GIFTS', 'Open gifts page'
    NONE = 'None', 'Nothing to do'


class NotifierAction(Enum):
    ARTICLE_POST_SAVE = 'ARTICLE_POST_SAVE'
    ARTICLE_COMMENT_POST_SAVE = 'ARTICLE_COMMENT_POST_SAVE'
    GIFT_POST_SAVE = 'GIFT_POST_SAVE'


class Icon( models.TextChoices ):
    INFO = 'info.png', 'info.png'
    MAIL = 'mail.png', 'mail.png'
    GIFT = 'gift.png', 'gift.png'
