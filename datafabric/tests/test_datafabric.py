import unittest

import distributed
import datafabric as df

class TestDataFabric(unittest.TestCase):
    def test_allocate(self):
        yp = df.YellowPages(distributed.Executor('127.0.0.1:8786'))
        yp.allocate(['block{}'.format(i) for i in range(10)], 100)

#        self.assert_equal(yp.size(), 10)

    def test_insert(self):
        yp = df.YellowPages(distributed.Executor('127.0.0.1:8786'))
        yp.allocate(['block{}'.format(i) for i in range(10)], 100)

        yp.insert('x', 10)

if __name__ == '__main__':
    unittest.main()
