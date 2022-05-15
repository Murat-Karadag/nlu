import unittest
import tests.secrets as sct
import nlu
import nlu.pipe.pipe_component
from sparknlp.annotator import *


class AssertionTests(unittest.TestCase):

    def test_assertion_dl_model(self):
        SPARK_NLP_LICENSE = sct.SPARK_NLP_LICENSE
        AWS_ACCESS_KEY_ID = sct.AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY = sct.AWS_SECRET_ACCESS_KEY
        JSL_SECRET = sct.JSL_SECRET
        nlu.auth(SPARK_NLP_LICENSE, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, JSL_SECRET)

        data = 'Patient has a headache for the last 2 weeks and appears anxious when she walks fast. No alopecia noted. She denies pain'
        res = nlu.load('en.assert.healthcare', verbose=True).predict(data, metadata=True)  # .predict(data)

        print(res.columns)
        for c in res: print(res[c])
        print(res)



if __name__ == '__main__':
    AssertionTests().test_assertion_dl_model()
