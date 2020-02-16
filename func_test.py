import unittest
import asg3

class TestMyModule(unittest.TestCase):
    
    def setUp(self):
        return

    def test_clean_text_normal(self):
        rawtext = "RT @whoisthat: this is! @a, test? https://ajkslf.dakl"
        
        result = asg3.clean_text(rawtext)

        expected_result = "this is! test?"
        self.assertEqual(result, expected_result)

    def test_clean_text_normal_1(self):
        rawtext = "RT @Apex_sH: My niece has her bird trained to attack anyone she screams at ???????????? https://t.co/ea0JoWMNrT"
        
        result = asg3.clean_text(rawtext)

        expected_result = "My niece has her bird trained to attack anyone she screams at ????????????"
        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):

        twt_str = "this is! test?"

        result = asg3.tokenize_text(twt_str)

        expected_result = ['this', 'is', '!', 'test', '?']
        self.assertEqual(result, expected_result)

    def test_replace_token_with_index(self):

        tkn_twt = ['this', 'is', '!', 'test', '?']
        max_len = 3000000

        result = asg3.replace_token_with_index(tkn_twt,max_len)

        expected_result = [53, 32, 9, 1155, 14]
        self.assertEqual(result, expected_result)

        tkn_twt = ['this', 'slkdfhgueywqiofjp', '!', 'test', '?']
        max_len = 3000000

        result = asg3.replace_token_with_index(tkn_twt,max_len)

        expected_result = [53, 1193514, 9, 1155, 14]
        self.assertEqual(result, expected_result)

    def test_pad_sequence(self):

        arr = [53, 32, 9, 1155, 14]
        max_len = 10

        result = asg3.pad_sequence(arr, max_len)

        expected_result = [53, 32, 9, 1155, 14, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected_result)

"""    def test_preprocess(self):

        max_len_twt = 50
        max_len_dict = 50

        result = class_example.preprocess(max_len_twt,max_len_dict)

        expected_result = ""
        self.assertEqual(result, expected_result)"""