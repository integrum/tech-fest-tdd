from legacy import SuggestionEngine

s = SuggestionEngine()

# print s.suggest() exception
print s.suggest("","","","")
print s.suggest(None, None, None, None)
print s.suggest(0,1,2,3)
print s.suggest(9223372036854775808L,9223372036854775808L,9223372036854775808L,9223372036854775808L)
print s.suggest(-9223372036854775808L,-9223372036854775808L,-9223372036854775808L,-9223372036854775808L)
print s.suggest("Casino","","","")
print s.suggest("Casino","niro","","")
print s.suggest("Casino","Stone","","")
print s.suggest("Casino","Stone",9,"")
print s.suggest("Casino","Stone",3,"")
