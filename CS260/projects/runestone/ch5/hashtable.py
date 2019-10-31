class HashTable:
    def __init__(self):
        self.size = 101
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                firsttry = nextslot

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                    if nextslot == firsttry:
                        self.size = self.size + 1
                        self.slots.append(None)
                        self.data.append(None)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        if self.get(key) != None:
            contains = True
        else:
            contains = False
        return contains

    def delete(self, key):
        if self.get(key) != None:
            hashvalue = self.hashfunction(key, len(self.slots))
            self.slots[hashvalue] = None
            self.data[hashvalue] = None
        else:
            pass
