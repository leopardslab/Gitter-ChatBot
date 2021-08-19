import os
import sys
import json
import unittest

current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import src.data_extraction as data_extraction

f = open('json_data/test-messages.json', )
data = json.load(f)


class Test_DataExtraction(unittest.TestCase):
    def test_MessageProcessing(self):
        TEST_RESPONSES = data['outcomes']
        for i in range(len(data['messages'])):
            __message__ = data['messages'][i]
            __res__ = data_extraction.process_message(__message__.lower(), 0)
            self.assertEqual(__res__, TEST_RESPONSES[i])


if __name__ == '__main__':
    unittest.main()
    