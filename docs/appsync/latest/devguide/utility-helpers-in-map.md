

# Map helpers in $util.map
<a name="utility-helpers-in-map"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

 `$util.map` contains methods to help with common Map operations such as removing or retaining items from a Map for filtering use cases.

## Map utils
<a name="utility-helpers-in-map-list"></a>

** `$util.map.copyAndRetainAllKeys(Map, List) : Map` **  
Makes a shallow copy of the first map while retaining only the keys specified in the list, if they are present. All other keys will be removed from the copy.

** `$util.map.copyAndRemoveAllKeys(Map, List) : Map` **  
Makes a shallow copy of the first map while removing any entries where the key is specified in the list, if they are present. All other keys will be retained in the copy.