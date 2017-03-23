import local_settings

from store import TripleStore, E, BasePredicate
from enum import Enum

P = BasePredicate("P", "name is_a has made_of weighs is_edible")
T = Enum("tissue" "muscle nerve connective cartilage gland")

body = TripleStore()
body.add({P.name:"Torso", P.has:{E("HEAD")}}, s=E("TORSO"))