# This programs works in O(n)
# for better performance improvement consider using golang
import unittest

def max_loss(n,vector):
    #checks on the input before evaluations
    if n<2 or len(vector)<2: return 0
    for c in vector:
        if c<=0: return -1

    post_frontier_reverse_sorted = sorted(vector[1:],reverse=True)
    max_pre_frontier = vector[0]
    max_loss_value = max(0,max_pre_frontier - post_frontier_reverse_sorted[-1])
    for i in xrange(1,n-1):
        value = vector[i]
        max_pre_frontier = max(max_pre_frontier, value)
        if post_frontier_reverse_sorted[-1] == value: post_frontier_reverse_sorted.pop()
        max_loss_value = max(max_loss_value, max_pre_frontier - post_frontier_reverse_sorted[-1])
    return max_loss_value


class TestIncrementDictionaryValues(unittest.TestCase):

    def test_max_loss_less_than_two_values(self):
        self.assertEquals(max_loss(1, [1]),0)
        self.assertEquals(max_loss(2, [1,1]), 0)

    def test_max_loss_negative_values(self):
        self.assertEquals(max_loss(2, [1, -1]), -1)

    def test_max_valid_short_ordered_sequence(self):
        self.assertEquals(max_loss(5, [1, 2, 3,4,5]), 0)

    def test_max_valid_long_sequence_single_value(self):
        self.assertEquals(max_loss(10**6, [1]*10**6), 0)

    def test_max_valid_long_sequence_psuedo_rand_values(self):
        self.assertEquals(max_loss(6*10**6, [1,5,2,3,6,10]*10**6), 9)


if __name__ == '__main__':
    unittest.main()