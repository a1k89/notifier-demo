import uuid

from django.db.models.signals import post_save
from django.db import transaction
from django.apps import apps

from apps.example.models import \
    Article,\
    ArticleComment, \
    Gift

from .conf import PostSaveContext

from .factory import ContextFactory
from .models import Notification

from run_celery import app

models = [
    Article,
    ArticleComment,
    Gift,
]


def register_models():
    for model in models:
        post_save.connect( _post_save,
                           sender=model,
                           dispatch_uid=uuid.uuid4() )


def _post_save(sender, instance, **kwargs):
    """
    Handler for our post_save.
    PostSaveContext is a namedtuple - context from sync post_save to async post_save handler

    """
    created = kwargs.get( 'created' )
    if not created:
        return

    class_name = instance.__class__.__name__
    action = f'{class_name}_POST_SAVE'.upper()

    post_save_context = PostSaveContext( module=instance.__module__,
                                         class_name=class_name,
                                         instance_identifier=instance.pk,
                                         action=action )

    transaction.on_commit(
        lambda: _async_post_save_handler.delay( post_save_context._asdict() )
    )


@app.task
def _async_post_save_handler(post_save_context):
    perform_action( post_save_context )


def perform_action(post_save_context):
    """
    The core of notifier

    """
    module = post_save_context.get('module')
    class_name = post_save_context.get('class_name')
    instance_identifier = post_save_context.get('instance_identifier')
    action = post_save_context.get( 'action' )

    module = module.split( '.' )[1]
    model = apps.get_model( app_label=module,
                            model_name=class_name )

    instance = model.objects \
        .filter( pk=instance_identifier ) \
        .first()

    if instance is None:
        return

    factory = ContextFactory(instance, action)
    context = factory.create_context()  # Create context to our model
    Notification.actions.create_notification(context)  # Create new notification
