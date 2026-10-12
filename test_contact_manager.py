import unittest
import contact_manager

class TestContactManager(unittest.TestCase):

    def setUp(self):
        contact_manager.contacts.clear()

    def test_add_contact(self):
        contact_manager.add_contact("Tae", "405-567-8907")
        self.assertEqual(contact_manager.contacts["Tae"], "405-567-8907")

    def test_find_contact(self):
        contact_manager.add_contact("Tae", "405-567-8907")
        result = contact_manager.find_contact("Tae")
        self.assertEqual(result, "405-567-8907")

    def test_delete_contact(self):
        contact_manager.add_contact("Tae", "405-567-8907")
        contact_manager.delete_contact("Tae")
        self.assertNotIn("Tae", contact_manager.contacts)

    def test_find_missing_contact(self):
        result = contact_manager.find_contact("Raychel")
        self.assertIsNone(result)

    def test_delete_missing_contact(self):
        contact_manager.delete_contact("Raychel")
        self.assertNotIn("Raychel", contact_manager.contacts)

    def test_duplicate_contact(self):
        contact_manager.add_contact("Tae", "405-567-8907")

        with self.assertRaises(contact_manager.DuplicateContactError):
            contact_manager.add_contact("Tae", "405-123-4567")
