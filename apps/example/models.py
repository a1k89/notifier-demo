from django.db import models

from django.contrib.auth import get_user_model


class Article(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()
    recipients = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.body

    def __repr__(self):
        return self.__str__()


class ArticleComment(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body

    def __repr__(self):
        return self.__str__()


class Gift(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
