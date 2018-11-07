import unittest
import verify

class TestOrder(unittest.TestCase):
    def test_order_status(self):
        order_id=2
        self.assertEqual(verify.check_order_status(order_id),True)
    
    def test_order_status_pending(self):
        self.assertEqual(verify.check_order_status_pending(20), False)

    def test_id_is_integer(self):
        self.assertFalse(verify.check_order_status(32))
    
    def test_id_exists(self):
        self.assertFalse(verify.check_order_status_pending(20))
        self.assertTrue(verify.check_order_status_pending(2))
    
    def test_orders_in_list(self):
        self.assertTrue(len(verify.pending)>0)
        self.assertFalse(len(verify.pending)==0)
    
    def test_add_new_order(self):
        self.assertFalse(verify.add_new_order(2))
        self.assertTrue(verify.add_new_order(31))
    
    def test_mark_as_delivered(self):
        self.assertEqual(verify.add_to_delivered(2),'Already Delivered')
        self.assertEqual(verify.add_to_delivered(32),'Non existent')
        self.assertTrue(verify.add_to_delivered(6))
        self.assertFalse(verify.check_order_status_pending(6))
    
    
    