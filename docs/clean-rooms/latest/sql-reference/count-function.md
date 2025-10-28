# COUNT and COUNT DISTINCT

functions

The COUNT function counts the rows defined by the expression. The
COUNT DISTINCT function computes the number of distinct non-NULL values in a
column or expression. It eliminates all duplicate values from the specified expression before
doing the count.

## Syntax

```
COUNT (DISTINCT `column`)
```

## Arguments

`column`

The target column that the function operates on.

## Data types

The COUNT function and the COUNT DISTINCT function supports
all argument data types.

The COUNT DISTINCT function returns BIGINT.

## Examples

Count all of the users from the state of Florida.

```
select count (identifier) from users where state='FL';
```

Count all of the unique venue IDs from the EVENT table.

```
select count (distinct venueid) as venues from event;
```
