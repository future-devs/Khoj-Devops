import json
import unittest
import sample_test_results
from core import stats

#hello world how are you?



class DjangoTestCases(unittest.TestCase):
    def test_lost_stats(self):
        self.lost_count_at_places = stats.lost_stats()
        self.assertNotEqual(self.lost_count_at_places, 0)
        self.assertNotEqual(self.lost_count_at_places, None)
        self.assertEqual(str(type(self.lost_count_at_places)), "<class 'dict'>")
        self.assertEqual(self.lost_count_at_places, sample_test_results.SAMPLE_TEST_LOST_STATS_RESULTS)

    def test_found_stats(self):
        self.found_count_at_places = stats.found_stats()
        self.assertNotEqual(self.found_count_at_places, 0)
        self.assertNotEqual(self.found_count_at_places, None)
        self.assertEqual(str(type(self.found_count_at_places)), "<class 'dict'>")
        self.assertEqual(self.found_count_at_places, sample_test_results.SAMPLE_TEST_FOUND_STATS_RESULTS)
    
    def test_lost_and_found_relation(self):
        self.relation_dict = stats.lost_and_found_relation()
        self.assertNotEqual(self.relation_dict, 0)
        self.assertNotEqual(self.relation_dict, None)
        self.assertEqual(str(type(self.relation_dict)), "<class 'dict'>")
        self.assertEqual(self.relation_dict, sample_test_results.SAMPLE_TEST_LOST_AND_FOUND_RELATION)
    
    
    



if __name__ == '__main__':
    unittest.main()
