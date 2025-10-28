# Combining multiple expressions

To combine multiple expressions together you use a pipe
separator (`|`). Use a combination of expressions when you want to use a single filter and filter on Items and Item interactions datasets,
or Action and Action interactions datasets.
Each expression is first evaluated independently and the
result is either the union or the intersection of the two results. The following examples show how to create expressions for Items and Item interactions datasets, but the same
rules apply when working with Actions and Action interactions.

**Matching expressions example**

If both expressions use `EXCLUDE`
or both expressions use `INCLUDE`, the result is the union of the two results as follows (A and B are different expressions):

- `Exclude A | Exclude B` is equal to `Exclude result from A or result from B`
- `Include A | Include B` is equal to `Include result from A or result from B`
  The following example shows how to combine two expressions that use `INCLUDE`.
  The first expression includes only items with a category or categories
  that you specify when you get recommendations using the `$CATEGORY` parameter.
  The second expression includes items the user has marked as a `favorite`.
  Recommendations will include only items with the category you specify along with items that the user has
  marked as a favorite.

```
INCLUDE ItemID WHERE Items.CATEGORY IN ($CATEGORY) | INCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ("favorite")
```

**INCLUDE and EXCLUDE example**

If one or more expression uses `INCLUDE` and one more expression uses
`EXCLUDE`, the result is the subtraction of the `EXCLUDE`
expression result from the `INCLUDE` expression result as follows (A, B, C, and
D are different expressions).

- `Include A | Exclude B` is equal to `Include result from A - result from B`
- `Include A | Include B | Exclude C | Exclude D` is equal to `Include (A or B) - (C or D)`
  Expression order does not matter: If the EXCLUDE expression comes before the INCLUDE expression, the result is the same.

The following example shows how to combine an `INCLUDE` expression and
a `EXCLUDE` expression. The first expression includes only items with a genre or genres
that you specify when you get recommendations using the `$GENRE` parameter.
The second expression excludes items that the user has clicked or streamed. Recommendations will
include only items with a genre that you specify that have not have been clicked or streamed.

```
INCLUDE ItemID WHERE Items.GENRE IN ($GENRE) | EXCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ("click", "stream")
```
