# RAND function

The RAND function generates a random floating-point number between 0 and 1. The RAND
function generates a new random number each time it's called.

## Syntax

```
RAND()
```

## Return type

RANDOM returns a DOUBLE.

## Example

The following example generates a column of random floating-point numbers between 0
and 1 for each row in the `squirrels` table. The resulting output would be a
single column containing a list of random decimal values, with one value for each row in
the squirrels table.

```
SELECT rand() FROM squirrels
```

This type of query is useful when you need to generate random numbers, for example,
to simulate random events or to introduce randomness into your data analysis. In the
context of the `squirrels` table, it might be used to assign random values to
each squirrel, which could then be used for further processing or analysis.
