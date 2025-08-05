from command import Command
import unittest

act = Command('test.db')
class MyTest(unittest.TestCase):
   
    def test_show_task(self):

        tasks = act.get_all()
        self.assertNotEqual(len(tasks), 0)