import unittest

def increment_dictionary_values(d,i):
    return {k:d[k]+i for k in d}
    #This signle line have fixed the issue


class TestIncrementDictionaryValues(unittest.TestCase):

    def test_increment_dictionayry_values(self):
        d = {'a':1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEquals(dd['a'],2)
        self.assertEquals(ddd['a'],0)

if __name__ == '__main__':
    unittest.main()