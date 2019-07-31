tabby_cat = "\tI'm tabled in."
persian_cat = "T'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fish food
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Use triple-single-quote instead.
fat_cat = '''
I'll do a list:
\t* jay
\t* wu
'''
print(fat_cat)

# Combine escape sequences and format strings to create a more complex format
# can't use f and format both
# comple_cat = f"This is a {}. \n And This is a persian {}".format('\t (tabby cat)', '\ncat')
comple_cat = "This is a {}. \n And This is a persian {}".format('\t (tabby cat)', '\ncat')
print(comple_cat)
