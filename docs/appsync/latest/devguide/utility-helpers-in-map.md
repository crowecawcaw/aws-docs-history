# Map helpers in $util.map

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$util.map` contains methods to help with common Map operations such as removing
or retaining items from a Map for filtering use cases.

## Map utils

**`$util.map.copyAndRetainAllKeys(Map, List) : Map`**

Makes a shallow copy of the first map while retaining only the keys
specified in the list, if they are present. All other keys will be removed
from the copy.

**`$util.map.copyAndRemoveAllKeys(Map, List) : Map`**

Makes a shallow copy of the first map while removing any entries where
the key is specified in the list, if they are present. All other keys will
be retained in the copy.
