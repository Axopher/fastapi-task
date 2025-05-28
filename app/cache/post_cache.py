import time

class PostCache:
    def __init__(self):
        self.cache = {}

    def get(self, user_id: int):
        data = self.cache.get(user_id)
        if data and (time.time() - data["timestamp"] < 300):  # 5 minutes
            return data["posts"]
        return None

    def set(self, user_id: int, posts):
        self.cache[user_id] = {
            "posts": posts,
            "timestamp": time.time()
        }

    def invalidate(self, user_id: int):
        if user_id in self.cache:
            del self.cache[user_id]

post_cache = PostCache()
