# NTH_VALUE

```
NTH_VALUE(x, n) [ <from first or last> ] [ <null treatment> ] over w
```

Where:

<null treatment> := RESPECT NULLS | IGNORE NULL

<from first or last> := FROM FIRST | FROM LAST

NTH_VALUE returns the nth value of x from the first or last value in the window. Default is
first. If <null treatment> is set to IGNORE NULLS, then function will skip over nulls while
counting.

If there aren't enough rows in the window to reach nth value, the function returns NULL.
