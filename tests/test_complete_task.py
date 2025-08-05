from command import Command
import unittest
import database


act = Command('test.db')
class MyTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        database.create_database('test.db')
    
    def test_complete_task(self):
        act.mark(1, 1)
        tasks = act.get_all()
        self.assertEqual(tasks[0][2], 1)