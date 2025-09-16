from semanticanalyser.analyser import *
from semanticanalyser.analyser import SemanticAnalyser

analyser = SemanticAnalyser()
match_types = analyser.getMatchTypes()
match_properties = analyser.getMatchProperties()
match_categories = analyser.get_categories()
categories_list = [category['name'] for category in match_categories]
match_vocabularies = analyser.get_vocabularies(categories_list[1])

print("Match Types:")
if match_types:
  for mt in match_types:
    print(mt.get_type())
else:
  print("Could not retrieve match types.")
print()

if match_properties and len(match_properties) > 0:
  print("Match Properties:")
  for mp in match_properties:
    print(mp.get_property())
else:
  print("Could not retrieve match properties or the list is empty.")
print()
if match_categories:
  print("Categories:")
  for category in match_categories:
    print(category)
else:
  print("Could not retrieve categories.")

print()

if match_vocabularies:
  print("Vocabularies:")
  for vocabulary in match_vocabularies:
    print(vocabulary)
else:
  print("Could not retrieve vocabularies.")