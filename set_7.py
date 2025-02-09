# sets are unordered..
#  "    "  unindexed...
empty=set() #empty set, don't use empty={} as it will create an empty dictionary
s={1,4,7,"apple",9,5,5,"rose",5,5}
print(s)

# methods of sets
s.add("banana")
print(s)

print(len(s))

s.remove("banana")
print(s)