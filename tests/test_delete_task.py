from command import Command
import unittest
import database


act = Command('test1.db')
class MyTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        database.create_database('test1.db')
    
    def test_delete_task(self):
        act.add('ini untuk dihapus')
        result = act.delete(1)
        self.assertIn("dihapus", result)

        tasks = act.get_all()
        self.assertEqual(len(tasks), 0)
