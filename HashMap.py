INITIAL_SIZE = 6

class HashMap(object):
    def __init__(self):
        self.size = INITIAL_SIZE
        self.map = [None] * self.size

    def _get_hash(self, key):
        # index = sum(ASII value for each letter in key) % size
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
    
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

print("----- My HashMap -----")
h = HashMap()
h.add('Shane', '123-4567')
h.add('enahS', '765-4321')
h.add('Bekah', '321-7654')
h.add('GC', '098-7654')
h.add('GC', '000-0000')
h.add('Abi', '890-4567')
h.print()
h.remove('Tom')
h.remove('enahS')
h.print()
print("Shane's value: " + h.get('Shane'))

# Python Dictionary
print("----- Python Dictionary -----")
myDict = {
    'Shane': '123-4567',
    'enahS': '765-4321',
    'Bekah': '321-7654',
    'GC': '098-7654',
    'GC': '000-0000',
    'Abi': '890-4567'
}
print(myDict)
# myDict.pop('Tom')
myDict.pop('enahS')
print(myDict)
print("Shane's value: " + myDict['Shane'])