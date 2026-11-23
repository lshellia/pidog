import unittest

import numpy as np

from pidog.actions_dictionary import ActionDict
from pidog.pidog import compare_version, numpy_mat


class LibraryUnitTests(unittest.TestCase):
    def test_compare_numpy_versions(self):
        self.assertFalse(compare_version('1.26.4', '2.0.0'))
        self.assertTrue(compare_version('2.0.0', '2.0.0'))
        self.assertFalse(compare_version('2.0.0rc1', '2.0.0'))
        self.assertEqual(numpy_mat([1, 2]).shape, (1, 2))

    def test_actions_are_public_properties_only(self):
        actions = ActionDict()
        self.assertEqual(actions['lie'][1], 'legs')
        self.assertEqual(actions['lie with hands out'][1], 'legs')
        for name in ('__class__', 'set_height', 'missing', '__class__.__name__'):
            with self.subTest(name=name), self.assertRaises(KeyError):
                actions[name]


if __name__ == '__main__':
    unittest.main()