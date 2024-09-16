class QuerySetStorage:
    storage = {}

    @classmethod
    def save(cls, key, queryset):
        cls.storage[key] = queryset

    @classmethod
    def get(cls, key):
        return cls.storage.get(key)
