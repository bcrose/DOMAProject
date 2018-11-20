import unittest
import pygameFun


class TestGame(unittest.TestCase):
    def test_vel(self):
        self.assertGreater(pygameFun.sprite1.vel, pygameFun.sprite2.vel)

    def test_size(self):
        self.assertGreater(pygameFun.sprite1.width, pygameFun.sprite2.width)

    def test_errors(self):
        self.assertEqual(pygameFun.main(), None)


if __name__ == '__main__':
    unittest.main()
