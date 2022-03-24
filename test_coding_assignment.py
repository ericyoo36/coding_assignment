"""


Unit Testing for coding_assignment.py

Date: Mar, 2022
Author: Seongmok (Eric), Yoo 
"""


import unittest
import coding_assignment

class TestCodingAssignment(unittest.TestCase):

    #test update_dict
    #test if "abba", 1, 2 is added to the dictionary correctly
    def test_update_dict(self):
        testdict = {}
        result = coding_assignment.update_dict(testdict, "abba" ,1 ,2)
        dict = {"bb,1":2}
        self.assertEqual(result, dict)

    #test sorted_dict
    #test if {"aa,0":2, "bbb.1":3, "cccc,2":4} is sorted correctly by its value
    def test_sorted_dict(self):
        result = ""
        testcase1 = {"aa,0":2, "bbb.1":3, "cccc,2":4}
        for key, value in coding_assignment.sort_dict(testcase1):
            result += str(value)
        self.assertEqual(result, "432")
    
    #test find_palindromes (odd length)
    #test if "abba" ,0 ,3 is passed as a palindrome correctly
    def test_find_palindromes_odd(self):
        testdict = {}
        result = coding_assignment.find_palindromes(testdict, "abba" ,0 ,3)
        self.assertEqual(result, (-1,4))

    #test find_palindromes (even length)
    #test if "ababa" ,0 ,4 is passed as a palindrome correctly
    def test_find_palindromes_even(self):
        testdict = {}
        result = coding_assignment.find_palindromes(testdict, "ababa" ,0 ,4)
        self.assertEqual(result, (-1,5))

    #test solution
    #test if solution for "abacc" is generated correctly
    def test_solution(self):
        testdict = {}
        dict = {"aba,0":3, "cc,3":2}
        result = coding_assignment.solution(testdict, "abacc")
        self.assertEqual(result,dict)

if __name__ == '__main__':
    s = unittest.TestLoader().loadTestsFromTestCase(TestCodingAssignment)
    unittest.TextTestRunner().run(s)
