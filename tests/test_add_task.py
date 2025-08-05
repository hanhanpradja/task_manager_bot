from command import Command
import unittest
import database


act = Command('test.db')
class MyTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        database.create_database('test.db')
    
    def test_add_task(self):
        result = act.add("ujicoba aja")
        self.assertIn("ditambahkan", result)

        tasks = act.get_all()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "ujicoba aja")
        self.assertEqual(tasks[0][2], 0)
