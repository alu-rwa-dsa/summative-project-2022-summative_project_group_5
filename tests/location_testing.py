import unittest
from unittest.mock import patch
from module.location import *


class Testmethods(unittest.TestCase):
    def test_upper(self):
        # checking locations names
        self.assertEqual('Kibagabaga'.upper(), 'KIBAGABAGA')
        self.assertEqual('Nyarutarama'.upper(), 'NYARUTARAMA')
        self.assertEqual('Kimironko'.upper(), 'KIMIRONKO')
        self.assertEqual('Gishushu'.upper(), 'GISHUSHU')
        self.assertEqual('Kacyiru'.upper(), 'KACYIRU')

    # testing if user's location's type matches with ours on the location list
    def test_locationlist(self):
        print('1.Kibagabaga\n2. Nyarutarama\n3. Kimironko\n4. Gishushu\n5. Kacyiru')
        choice = int(input('choose your Location: '))
        if choice == 1:
            self.assertTrue(choice, 1)
        elif choice == 2:
            self.assertTrue(choice, 2)
        elif choice == 3:
            self.assertTrue(choice, 3)
        elif choice == 4:
            self.assertTrue(choice, 4)
        elif choice == 5:
            self.assertTrue(choice, 5)
        else:
            self.assertFalse(choice, 1) or (choice, 2) or (choice, 2) or (choice, 3) or (choice, 4) or (choice, 5)


if __name__ == '__main__':
    unittest.main()
