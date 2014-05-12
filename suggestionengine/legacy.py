import re

class SuggestionEngine(object):
  def suggest(self, k, c_name, lbl, d):
    _sg = ""

    c_name = str(c_name)
    k = str(k)

    if k == None:
      print "Missing title"
      return None
    else:
      if k == "Casino" and c_name == "Pesci":
        return "Goodfellas"
      elif k == "Casino" or k == "The Godfather" or re.search(r"II", k):
        if c_name == "De Niro" or re.search(r"niro",c_name):
          return "Goodfellas"
        elif c_name == "Stone":
          if lbl > 8:
            return "Scorsese"
          elif lbl < 4:
            return "De Palma"
          else:
            return "None"
        elif c_name == "Pacino":
          if d == 1995:
            return "Heat"
          elif  (d > 1992 and d < 1995) or d == 1993:
            return ("Carlito's Way", "Scent of a Woman")


