

class Hdict:

    def init(self):
        self.dic = [[]]*10

    def _hash(self, value):
        total = 0
        for v in value:
            total += ord(v)

        return total%10

    def _insert(self, key, value):

        index = self._hash(key)

        for i, pair in enumerate(self.dic[index]):
            if pair[0] == key:
                self.dic[index][i] = (key, value)
                return
        self.dic[index].append((key, value))


    def _get(self, key, alt_return):

        index = self._hash(key)

        for pair in self.dic[index]:
            if pair[0] == key:
                return pair[1]
        return alt_return



