from .conf import \
    NotifierAction, \
    ClientAction, \
    Data, \
    Icon


class ContextFactory:
    def __init__(self, instance, action,  *args, **kwargs):
        self.instance = instance
        self.action = action
        self.__dict__.update(kwargs)

    def create_context(self):
        if self.action == NotifierAction.ARTICLE_POST_SAVE.value:
            recipients = self.instance.recipients.all()
            body = self.instance.body
            data = Data(name='New article available',
                        body=body,
                        recipients=recipients,
                        client_action=ClientAction.OPEN_ARTICLE,
                        is_notify_screen=True,
                        is_push=True,
                        icon=Icon.MAIL)

            return data

        if self.action == NotifierAction.ARTICLE_COMMENT_POST_SAVE.value:
            recipients = self.instance.article.recipients.all()
            data = Data(name='New comment',
                        body=self.instance.body,
                        client_action=ClientAction.OPEN_MESSAGE,
                        recipients=recipients,
                        is_notify_screen=True,
                        is_push=True,
                        icon=Icon.INFO)
            return data

        if self.action == NotifierAction.GIFT_POST_SAVE.value:
            recipients = [self.instance.owner]
            data = Data(
                name='Gift for you!',
                body='You got a new gift!',
                recipients=recipients,
                client_action=ClientAction.OPEN_GIFTS,
                is_notify_screen=True,
                is_push=True,
                icon=Icon.GIFT
            )

            return data
