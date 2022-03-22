from enum import Enum
import json
import logging

import nats
from typing import Any

from refactor.queuer.app.core.config import settings

class QueueTopics(Enum):
    DIPATCH = settings.MQ_DISPATCH_TOPIC

class Queuer():

    topics: QueueTopics = QueueTopics

    def get_client(self) -> Any:
       return nats.connect(settings.MQ_CONNECTION_URI)

    async def publish(self, topic: str, msg: Any) -> Any:
        # get enum value
        topic = topic.value
        client = await self.get_client()
        msg_json = json.dumps(msg)
        logging.info(f"Publishing message to topic {topic}:")
        logging.info(msg_json)
        res = await client.publish(topic, msg_json.encode())
        return res