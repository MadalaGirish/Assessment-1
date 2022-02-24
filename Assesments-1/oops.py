from this import s
import self as self
class StringClass():
    def __init__(self,s):
     self.string= s

    def len_str(self):
        return len(self.string)
    def cvt_list(self):
        return list(self.string)

class PairPossible(StringClass):
    def __init_(self,s):
      super()._init_(s)
      self.pair_list=[]

    def store_pair(self):
        for i in self.string:
            for j in self.string:
                self.pair_list.append([i,j])

    def print_pair(self):
        if self.pair_list==[]:
            self.store_pair()
        for i in self.pair_list:
            print(i,end='')

class SearchCommonElements():
    def _init_(self,new_string):
        self.stclass = StringClass('Aditya')
        self.pairclass=PairPossible('girish')


