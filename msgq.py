class BaseMessageQueue:
    pass


class RedisMessageQueue(BaseMessageQueue):
    def __init__(self, redis_host, redis_port, redis_db, ):
        import redis
        r = redis.StrictRedis()
