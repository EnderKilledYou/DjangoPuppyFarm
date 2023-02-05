import datetime
import logging

from django.db.models import F

from app.strings.models import Key
from app.hello_doggo.queueboss.queueboss import QueueBossBase

"""
But... throttling is builter innz!!!

from the docs:
#A note on concurrency
#The built-in throttle implementations are open to race conditions, so under high concurrency they may allow a few extra requests through.

#If your project relies on guaranteeing the number of requests during concurrent requests, you will need to implement your own throttle class. See issue #5181 for more details.
"""

logger = logging.getLogger(__name__)


class KeyJob:
    key_id: object
    key_name: str
    key_increment: int
    exists: bool

    def __init__(self, id, key_name: str, key_increment: int, exists=False):
        self.exists = exists
        self.key_increment = key_increment
        self.key_name = key_name
        self.key_id = id


def create_key(job):
    with Key.objects.create(last_update=datetime.datetime.now()) as key:
        return key.id


def increment_key(job: KeyJob):
    time_threshold = datetime.now() - datetime.timedelta(seconds=10)
    with Key.objects.filter(id=job.key_id, last_update__lte=time_threshold).first() as key:
        if key is None:
            logger.warning(f'Key attempted to increment either too early or does not exist {job.key_id}')
            return None
        key.value = F('value') + 1
        Key.save()
        return key.id


class KeyBoss(QueueBossBase):
    def _process(self, job: KeyJob):
        if job.exists:
            return create_key(job);
        else:
            return increment_key(job);
