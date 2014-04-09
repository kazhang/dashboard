from horizon.test import helpers as test


class CephTests(test.TestCase):
    # Unit tests for ceph.
    def test_me(self):
        self.assertTrue(1 + 1 == 2)
