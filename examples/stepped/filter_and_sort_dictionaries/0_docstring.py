"""This function filters a list of dicts by key, and alphabetizes the entries by value.

This function does not modify the argument list.

Parameters:
  list[dict[str, str]]: an array of dicts with string keys and string values
  str: the function will remove all dicts that don't have this key

Returns: a list of dicts where each dict contains the given key,
  and the dicts are sorted alphabetically by the value stored in the given key

>>> f([{'a':'z'},{'b':'y'},{'a':'x'}], 'a')
[{'a':'x'},{'a','z'}]


>>> f([{'a':'z','b':'j'},{'b':'y'},{'b':'i',a':'x'}], 'b')
[{'b':'i',a':'x'},{'a':'z','b':'j'},{'b':'y'}]

"""
