# countFrequent

Use the `countFrequent` command (also available as
`count_frequent`) to compute an approximate count of each unique
field-value combination, sorted in descending order. The command emits an
`_approxcount` field.

###### Syntax

```
| countFrequent `field`[, `field` ...]
```

The command uses the following arguments:

- `field` – One or more
  fields to count frequencies for.

###### Example

The following query counts the frequency of method and status
combinations.

```
fields method, status
| countFrequent method, status
```
