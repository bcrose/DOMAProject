import unittest
import pygameFun


class TestGame(unittest.TestCase):
    def test_vel(self):
        self.assertGreater(pygameFun.buddha.vel, pygameFun.hand.vel)

    def test_size(self):
        self.assertGreater(pygameFun.buddha.width, pygameFun.hand.width)

    def test_errors(self):
        self.assertEqual(pygameFun.main(), None)


if __name__ == '__main__':
    unittest.main()
