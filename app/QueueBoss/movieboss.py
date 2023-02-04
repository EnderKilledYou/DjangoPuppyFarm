from app.QueueBoss.queueboss import QueueBossBase


class MovieBoss(QueueBossBase):
    def _process(self, job):
        console.log(job)
        pass
