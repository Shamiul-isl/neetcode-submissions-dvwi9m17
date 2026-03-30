class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = {}
        self.storage[key][timestamp] = value
        print(self.storage)


    def get(self, key: str, timestamp: int) -> str:
        # print(self.storage)
        # return self.storage[key][timestamp]
        if key not in self.storage:
            return ""
        keys = list(self.storage[key].keys())
        if timestamp < keys[0]:
            return ""
        l, r, minimum = 0, len(keys) - 1, keys[-1]
        while l <= r:
            mid = (l + r) // 2
            if keys[mid] < timestamp:
                minimum = keys[mid]
                l = mid + 1
            elif keys[mid] > timestamp:
                r = mid - 1
            else:
                minimum = keys[mid]
                break

        return self.storage[key][minimum]
