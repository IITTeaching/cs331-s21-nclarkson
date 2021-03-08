from unittest import TestCase
import random

class ConstrainedList (list):
    """Constrains the list class so it offers only the following primitive array API:
        - `lst[i]` for getting and setting a value at an *existing, positive* index `i`
        - `len(lst)` to obtain the number of slots
       All other operations will result in an exception being raised.
       DO NOT CHANGE THIS CODE!!!!!
    """

    def __init__(self, n=10):
        super().__init__([None] * n)

    @staticmethod
    def create(l):
        r = ConstrainedList(len(l))
        for i in range(0,len(l)):
            r[i] = l[i]
        return r

    def __getitem__(self, idx):
        if idx < 0 or idx >= len(self):
            raise ValueError('Can only use positive, valid indexes on constrained lists!')
        return super().__getitem__(idx)

    def __setitem__(self, idx, value):
        if idx < 0 or idx >= len(self):
            raise ValueError('Can only use positive, valid indexes on constrained lists!')
        super().__setitem__(idx, value)

    def __getattribute__(self, name):
        if name in ('insert', 'min', 'max', 'append', 'extend'
                    'index', 'count', 'clear', 'copy'):
            raise AttributeError('Method "' + name + '" not supported on constrained list!')
        else:
            return super().__getattribute__(name)

    # __getattribute__ isn't called for special methods, so the following are needed
    def __delitem__(self, value):
        raise AttributeError('Constrained lists do not support `del`!')

    def __add__(self, value):
        raise AttributeError('Constrained lists do not support `+`!')

    def __contains__(self, value):
        raise AttributeError('Constrained lists do not support `in`!')

    def __eq__(self, value):
        raise AttributeError('Constrained lists do not support `==`!')

    def __iter__(self):
        raise AttributeError('Constrained lists do not support iteration!')

    def __str__(self):
        raise AttributeError('Constrained lists do not support stringification!')

    def __repr__(self):
        raise AttributeError('Constrained lists do not support stringification!')

    # for testing only! (don't use this in your ArrayList implementation)

    def _as_list(self):
        return list(super().__iter__())

################################################################################
# YOU SHOULD IMPLEMENT THIS CLASS
class ArrayList:
    def __init__(self, n=1):
        self.data = ConstrainedList(n) # don't change this line!
        self.len = 0 # the attribute self.len should be record the length of the list (do not rename!)

    ### subscript-based access ###

    def _normalize_idx(self, idx):
        idx1=idx
        if idx1<0:
            idx1 += self.len
            if idx1<0:
                idx1=0
        return idx1

    def __getitem__(self, idx):
      #  return self[idx]
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        idx1=self._normalize_idx(idx)
        if idx1>=self.len:
            raise IndexError
        return self.data[idx1]

    def __setitem__(self, idx, value):
      #  self[idx] = value
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        idx1=self._normalize_idx(idx)
        if idx1>=self.len:
            raise IndexError
        self.data[idx1]=value

    def __delitem__(self, idx):

       ## self = self[idx - 1] + self[idx + 1]
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        idx1=self._normalize_idx(idx)
        if idx1 >= self.len:
            raise IndexError
        for i in range(idx1+1, self.len):
            self.data[i-1] = self.data[i]
        self.len+=-1

    ### stringification ###

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        ### BEGIN SOLUTION
        if(self.len==0):
            return "[]"
        s="["
        x=0 
        while(x<self.len): 
            s=s+str(self.data[x])+", "
            x+=1
        s=s[0:len(s) - 2]    
        s=s+"]"
        return s
        ### END SOLUTION

    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        ### BEGIN SOLUTION
        if(self.len==0):
            return "[]"
        s="[" 
        x=0
        while(x<self.len): 
            s=s+repr(self.data[x])+", "
            x+=1
        s=s[0:len(s)-2]    
        s=s+"]"
        return s.format()
        ### END SOLUTION


    ### single-element manipulation ###

    def append(self, value):
        """Appends value to the end of this list."""
        if(self.len >= len(self.data)):
            new = ConstrainedList((self.len)*2)
            i = 0
            while(i < self.len):
                new[i] = self.data[i]
                i += 1
            self.data = new   
        self.data[self.len] = value
        self.len += 1     
        ### BEGIN SOLUTION
        ### END SOLUTION

    def insert(self, idx, value):
       # if(idx == len(self)):
       #     self.append(value)
       # elif(self.len >= len(self.data)):
       #     ls = ConstrainedList((self.len)* 2)
       #     i = 0
        #    while(i < idx):
       #         ls[i] = self.data[i]
       # #        i += 1       
        #    i = idx 
        #    ls[i] = value
       #     i += 1
        #    while(i < self.len):
        #        ls[i] = self.data[i]
        #        i += 1
        #    self.data = ls
        ##    self.len += 1
        #else: 
       #     ls = ConstrainedList(self.len)
        #    i = 0
        #    while(i < idx):
        #        ls[i] = self.data[i]
        #        i += 1       
        #    i = idx 
        #    ls[i] = value
        #    i += 1
        #    while(i < self.len):
        #        ls[i] = self.data[i]
        #        i += 1 
        #    self.data = ls 
        #      
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note thatself.data = ls inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        ### BEGIN SOLUTION
        ls = ConstrainedList((self.len)+1)
        if(self._normalize_idx((idx)) > len(self.data)):
            raise IndexError("idx invalid")
        i = 0
        while(i < self.len):   
        #for j in range(0,self.len):
            ls[i] = self.data[i]
            i+=1
        self.data = ls
     #   if(self._normalize_idx((idx)) > len(self.data)):
      #      raise IndexError("idx invalid")
        z = self.len
        while(z > idx):
        #for x in range(self.len,idx,-1):
            self.data[z] = self.data[z-1]
            ls = list(self.data._as_list())
            z -= 1        
        self.data[idx] = value
        self.len +=1    
        ### END SOLUTION

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        ### BEGIN SOLUTION
        if(self._normalize_idx((idx)) > len(self.data)):
            raise IndexError("idx invalid")
        d = self.data[idx]
        li = ConstrainedList((self.len)-1)
        for i in range(0,idx):
            li[i] = self.data[i]
        for i in range(idx,self.len-1):
            li[i] = self.data[i +1]
            #self.data[i] = self.data[i+1]
           # testlst = list(self.data._as_list())
       # newlst = ConstrainedList((self.len)-1)
        #for j in range(0,self.len-1):
          #  newlst[j] = self.data[j]
        self.data = li
      #  testdata = list(self.data._as_list())
        self.len -=1
        return d
        ### END SOLUTION

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        ### BEGIN SOLUTION
    #    i = 0
    #    while(self.data[i] != value):
    #        if(i >= self.len):
    #            raise ValueError("value not found")
    #        i+= 1
    #    l = ConstrainedList(self.len - 1)
     #   for x in range(0,i):
    #        l[x] = self.data[x]
    #   for x in range(i,self.len):
    #        l[x] = self.data[x + 1]
    #    self.len -= 1
    #    self.data = l
        for i in range(0,self.len):
            if(self.data[i] == value):
                li = ConstrainedList((self.len)-1)
                for k in range(0,i):
                    li[k] = self.data[k]
                for x in range(i,self.len-1):
                    li[x] = self.data[x+1]
                    #testlst = list(self.data._as_list())
               # newlst = ConstrainedList((self.len)-1)
               # for j in range(0,self.len-1):
               #     newlst[j] = self.data[j]
                self.data =  li
                #testdata = list(self.data._as_list())
                self.len -=1
                return
        raise ValueError("value not found")
        ### END SOLUTION


    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as
        other. If other is not an ArrayList, returns False."""
        ### BEGIN SOLUTION
        if(not isinstance(other, ArrayList)):
            return False
        if(self.len != other.len):
            return False
        x = 0
        while(x < self.len):
            if(self.data[x] != other.data[x]):
                return False
            x +=1
        return True
        ### END SOLUTION

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        ### BEGIN SOLUTION
        x = 0
        while(x < self.len):
            if(value == self.data[x]):
                return True
            x += 1
        return False
        ### END SOLUTION


    ### queries ###

    def __len__(self):
        return self.len
        """Implements `len(self)`"""
        ### BEGIN SOLUTION
        ### END SOLUTION

    def min(self):
        min = self.data[0]
        for x in range(0,self.len):
            if(self.data[x] < min):
                min = self.data[x]
        return min        
        """Returns the minimum value in this list."""
        
        ### BEGIN SOLUTION
        ### END SOLUTION

    def max(self):
        """Returns the maximum value in this list."""
        ### BEGIN SOLUTION
        max = self.data[0]
        for x in range(0,self.len):
            if(self.data[x] > max):
                max = self.data[x]
        return max 
        ### END SOLUTION

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        ### BEGIN SOLUTION
        if(j == None or j == -1):
            for x in range(i,self.len):
                if(value == self.data[x]):
                    return x
        else:
            for x in range(i,j):
                if(value == self.data[x]):
                    return x
        raise ValueError("error")
        ### END SOLUTION

    def count(self, value):
        """Returns the number of times value appears in this list."""
        ### BEGIN SOLUTION
        num = 0
        for z in range(0,self.len):
            if(value == self.data[z]):
                num += 1
        return num
        ### END SOLUTION


    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those
        of other."""
        ### BEGIN SOLUTION
        l = ArrayList()
        l.len = self.len + len(other)
        l.data = ConstrainedList(self.len + len(other))
        z = 0
        for x in range(0,self.len):
            l.data[x] = self.data[x]
            z = x
        z += 1    
        for k in range(0,len(other)):
            l.data[z] = other[k]
            z += 1
        return l
        ### END SOLUTION

    def clear(self):
        self.data = ConstrainedList() # don't change this!
        self.len = 0 # don't change this!

    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""
        ### BEGIN SOLUTION
        a = ArrayList()
        a.len = self.len
        for x in range(0, self.len):
            a.data[x] = self.data[x]
        return a
        ### END SOLUTION

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        
        ### BEGIN SOLUTION
        for x in other: 
            self.append(x)
        ### END SOLUTION


    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        ### BEGIN SOLUTION
        for c in range(0,self.len):
            yield self.data[c]
        ### END SOLUTION

################################################################################
# TEST CASES
def arrayListToList(a):
    return list(a.data._as_list()[:len(a)])


########################################
# 15 points
def test_case_1():
    test_log("testing subscript-based acess ")

    tc = TestCase()
    lst = ArrayList()
    data = [1, 2, 3, 4]
    lst.data = ConstrainedList.create(data)
    lst.len = len(lst.data)

    for i in range(len(data)):
        tc.assertEqual(lst[i], data[i])

    with tc.assertRaises(IndexError):
        x = lst[100]

    with tc.assertRaises(IndexError):
        lst[100] = 0

    with tc.assertRaises(IndexError):
        del lst[100]

    lst[1] = data[1] = 20
    del data[0]
    del lst[0]

    for i in range(len(data)):
        tc.assertEqual(lst[i], data[i])

    data = [random.randint(1, 100) for _ in range(100)]
    lst.data = ConstrainedList.create(data)
    lst.len = len(lst.data)
    for i in range(len(data)):
        lst[i] = data[i] = random.randint(101, 200)
    for i in range(50):
        to_del = random.randrange(len(data))
        del lst[to_del]
        del data[to_del]

    for i in range(len(data)):
        tc.assertEqual(lst[i], data[i])

    for i in range(0, -len(data), -1):
        tc.assertEqual(lst[i], data[i])
    suc()

########################################
# 10 points
def test_case_2():     # (4 points) test stringification
    test_log("test stringification ")

    tc = TestCase()

    lst = ArrayList()
    tc.assertIsInstance(lst.data, ConstrainedList)
    tc.assertEqual('[]', str(lst))
    tc.assertEqual('[]', repr(lst))

    lst.data = ConstrainedList.create([1])
    lst.len = len(lst.data)
    tc.assertEqual('[1]', str(lst))
    tc.assertEqual('[1]', repr(lst))

    lst.data = ConstrainedList.create([10, 20, 30, 40, 50])
    lst.len = len(lst.data)
    tc.assertEqual('[10, 20, 30, 40, 50]', str(lst))
    tc.assertEqual('[10, 20, 30, 40, 50]', repr(lst))
    suc()

########################################
# 15 points
def test_case_3():
    test_log("testing single-element manipulation ")
    tc = TestCase()
    lst = ArrayList()
    data = []

    for _ in range(100):
        to_add = random.randrange(1000)
        data.append(to_add)
        lst.append(to_add)

    tc.assertIsInstance(lst.data, ConstrainedList)
    tc.assertEqual(data, arrayListToList(lst))

    for _ in range(100):
        to_ins = random.randrange(1000)
        ins_idx = random.randrange(len(data)+1)
        data.insert(ins_idx, to_ins)
        lst.insert(ins_idx, to_ins)

    tc.assertEqual(data, arrayListToList(lst))

    for _ in range(100):
        pop_idx = random.randrange(len(data))
        tc.assertEqual(data.pop(pop_idx), lst.pop(pop_idx))

    tc.assertEqual(data, arrayListToList(lst))

    for _ in range(25):
        to_rem = data[random.randrange(len(data))]
        data.remove(to_rem)
        lst.remove(to_rem)

    tc.assertEqual(data, arrayListToList(lst))

    with tc.assertRaises(ValueError):
        lst.remove(9999)
    suc()

########################################
# 15 points
def test_case_4():
    test_log("testing predicates")
    tc = TestCase()
    lst = ArrayList()
    lst2 = ArrayList()

    lst.data = ConstrainedList.create([])
    lst.len = len(lst.data)
    lst2.data = ConstrainedList.create([1, 2, 3])
    lst2.len = len(lst2.data)
    tc.assertNotEqual(lst, lst2)

    lst.data = ConstrainedList.create([1, 2, 3])
    lst.len = len(lst.data)
    tc.assertEqual(lst, lst2)

    lst.data = ConstrainedList.create([])
    lst.len = len(lst.data)
    tc.assertFalse(1 in lst)
    tc.assertFalse(None in lst)

    lst.data = ConstrainedList.create(range(100))
    lst.len = len(lst.data)
    tc.assertFalse(100 in lst)
    tc.assertTrue(50 in lst)
    suc()

########################################
# 15 points
def test_case_5():
    test_log("testing queries")
    # (10 points) test queries
    tc = TestCase()
    lst = ArrayList()

    tc.assertEqual(0, len(lst))
    tc.assertEqual(0, lst.count(1))
    with tc.assertRaises(ValueError):
        lst.index(1)

    import random
    data = [random.randrange(1000) for _ in range(100)]
    lst.data = ConstrainedList.create(data)
    lst.len = len(lst.data)

    tc.assertEqual(100, len(lst))
    tc.assertEqual(min(data), lst.min())
    tc.assertEqual(max(data), lst.max())
    for x in data:
        tc.assertEqual(data.index(x), lst.index(x))
        tc.assertEqual(data.count(x), lst.count(x))

    with tc.assertRaises(ValueError):
        lst.index(1000)

    lst.data = ConstrainedList.create([1, 2, 1, 2, 1, 1, 1, 2, 1])
    lst.len = len(lst.data)
    tc.assertEqual(1, lst.index(2))
    tc.assertEqual(1, lst.index(2, 1))
    tc.assertEqual(3, lst.index(2, 2))
    tc.assertEqual(7, lst.index(2, 4))
    tc.assertEqual(7, lst.index(2, 4, -1))
    with tc.assertRaises(ValueError):
        lst.index(2, 4, -2)
    suc()

########################################
# 15 points
# test bulk operations
def test_case_6():
    test_log("testing bulk operations")
    tc = TestCase()
    lst = ArrayList()
    lst2 = ArrayList()
    lst3 = lst+lst2

    tc.assertIsInstance(lst3, ArrayList)
    tc.assertEqual([], arrayListToList(lst3))

    data  = [random.randrange(1000) for _ in range(50)]
    data2 = [random.randrange(1000) for _ in range(50)]
    lst.data = ConstrainedList.create(data)
    lst.len = len(lst.data)
    lst2.data = ConstrainedList.create(data2)
    lst2.len = len(lst.data)
    lst3 = lst + lst2
    tc.assertEqual(100, len(lst3))
    tc.assertEqual(data + data2, arrayListToList(lst3))

    lst.clear()
    tc.assertEqual([], arrayListToList(lst))

    lst.data = ConstrainedList.create([random.randrange(1000) for _ in range(50)])
    lst2 = lst.copy()
    tc.assertIsNot(lst, lst2)
    tc.assertIsNot(lst.data, lst2.data)
    tc.assertEqual(arrayListToList(lst), arrayListToList(lst2))

    lst.clear()
    lst.extend(range(10))
    lst.extend(range(10,0,-1))
    lst.extend(data.copy())
    tc.assertEqual(70, len(lst))
    tc.assertEqual(list(range(10))+list(range(10,0,-1))+data, arrayListToList(lst))
    suc()

########################################
# 15 points
def test_case_7():
    test_log("testing iteration")
    tc = TestCase()
    lst = ArrayList()

    import random
    data = [random.randrange(1000) for _ in range(100)]
    lst.data = ConstrainedList.create(data)
    lst.len = len(lst.data)
    tc.assertEqual(data, [x for x in lst])

    it1 = iter(lst)
    it2 = iter(lst)
    for x in data:
        tc.assertEqual(next(it1), x)
        tc.assertEqual(next(it2), x)
    suc()

########################################
# success
def suc():
    print("  SUCCESS\n\n")

########################################
# test case output
def test_log(s):
    print(80 * "#" + "\n" + s + " ...")

########################################
# All tests
def main():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()

if __name__ == '__main__':
    main()
