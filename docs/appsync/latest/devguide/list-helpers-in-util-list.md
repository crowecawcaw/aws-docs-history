# List helpers in $util.list

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$util.list` contains methods to help with common List operations such as
removing or retaining items from a list for filtering use cases.

## List utils

**`$util.list.copyAndRetainAll(List, List) : List`**

Makes a shallow copy of the supplied list in the first argument while
retaining only the items specified in the second argument, if they are
present. All other items will be removed from the copy.

**`$util.list.copyAndRemoveAll(List, List) : List`**

Makes a shallow copy of the supplied list in the first argument while
removing any items where the item is specified in the second argument, if
they are present. All other items will be retained in the copy.

**`$util.list.sortList(List, Boolean, String) : List`**

Sorts a list of objects, which is provided in the first argument. If the
second argument is true, the list is sorted in a descending manner; if the
second argument is false, the list is sorted in an ascending manner. The
third argument is the string name of the property used to sort a list of
custom objects. If it's a list of just Strings, Integers, Floats, or
Doubles, the third argument can be any random string. If all of the objects
are not from the same class, the original list is returned. Only lists
containing a maximum of 1000 objects are supported. The following is an
example of this utility's usage:

```

 INPUT:      $util.list.sortList([{"description":"youngest", "age":5},{"description":"middle", "age":45}, {"description":"oldest", "age":85}], false, "description")
 OUTPUT:     [{"description":"middle", "age":45}, {"description":"oldest", "age":85}, {"description":"youngest", "age":5}]
```
