import redis
from app.config import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)


def get_cached_paste(paste_id: str):
    return r.get(f"paste:{paste_id}")


def cache_paste(paste_id: str, content: str, ttl: int = 3600):
    r.setex(f"paste:{paste_id}", ttl, content)
