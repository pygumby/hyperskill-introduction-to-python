# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
print({w.upper(): w.lower() for w in some_iterable})
