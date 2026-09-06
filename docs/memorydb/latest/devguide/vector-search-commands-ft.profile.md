

# FT.PROFILE
<a name="vector-search-commands-ft.profile"></a>

Run a query and return profile information about that query.

**Syntax**

```
FT.PROFILE 

<index>
SEARCH | AGGREGATE 
[LIMITED]
QUERY <query ....>
```

**Return**

A two-element array. The first element is the result of the `FT.SEARCH` or `FT.AGGREGATE` command that was profiled. The second element is an array of performance and profiling information.