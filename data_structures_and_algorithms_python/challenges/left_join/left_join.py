class Hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = [[key, value],]
        else:
            self.map[idx].append([key, value])

    def get(self, key):
        idx = self.hash(key)
        if self.map[idx]:
            for k in self.map[idx]:
                if k[0] == key:
                    return k[1]
            return None
            
    def contains(self, key):
        idx = self.hash(key)

        if self.map[idx]:
            for k in self.map[idx]:
                if k[0] == key:
                    return True
        return False

    def hash(self, key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = (ascii_total * 17) % self.size
        return hashed


def join(dic1,dic2):
    output = []
    for i in dic1.map:
        if i != None:
            for k in i:
                i_list = []
                i_list.append(k[0])
                i_list.append(k[1])
                if dic2.contains(k[0]):
                    i_list.append(dic2.get(k[0]))
                else:
                    i_list.append(None)
                output.append(i_list)
    return output

