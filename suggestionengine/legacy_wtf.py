from legacy import SuggestionEngine
import unittest

engine = SuggestionEngine()

# print engine.suggest() exception
print engine.suggest("","","","")
print engine.suggest(None, None, None, None)
print engine.suggest(0,1,2,3)
print engine.suggest(9223372036854775808L,9223372036854775808L,9223372036854775808L,9223372036854775808L)
print engine.suggest(-9223372036854775808L,-9223372036854775808L,-9223372036854775808L,-9223372036854775808L)
print engine.suggest("Casino","","","")
print engine.suggest("Casino","niro","","")
print engine.suggest("Casino","Stone","","")
print engine.suggest("Casino","Stone",0,"")
print engine.suggest("Casino","Stone",1,"")
print engine.suggest("Casino","Stone",2,"")
print engine.suggest("Casino","Stone",3,"")
print engine.suggest("Casino","Stone",4,"")
# ...


class TestKnownKnowns(unittest.TestCase):

  def setUp(self):
    self.engine = SuggestionEngine()

  def test_casino_stone_3_blank(self):
    self.assertEqual(self.engine.suggest("Casino","Stone",3,""), "De Palma")

  # ...
