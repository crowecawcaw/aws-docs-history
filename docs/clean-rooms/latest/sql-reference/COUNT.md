# COUNT function

The COUNT function counts the rows defined by the expression.

The COUNT function has the following variations.

- COUNT ( \* ) counts all the rows in the target table whether they include nulls or
  not.
- COUNT ( _expression_ ) computes the number of rows with non-NULL values
  in a specific column or expression.
- COUNT ( DISTINCT _expression_ ) computes the number of distinct
  non-NULL values in a column or expression.

## Syntax

```
COUNT( * | *expression* )
```

```
COUNT ( [ DISTINCT | ALL ] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. The COUNT function
supports all argument data types.

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values from the
specified expression before doing the count. With the argument ALL, the function retains all
duplicate values from the expression for counting. ALL is the default.

## Return type

The COUNT function returns BIGINT.

## Examples

Count all of the users from the state of Florida:

```
`select count(*) from users where state='FL';`
`count
-------
510`
```

Count all of the event names from the EVENT table:

```
`select count(eventname) from event;`
`count
-------
8798`
```

Count all of the event names from the EVENT table:

```
`select count(all eventname) from event;`
`count
-------
8798`
```

Count all of the unique venue IDs from the EVENT table:

```
`select count(distinct venueid) as venues from event;`
`venues
--------
204`
```

Count the number of times each seller listed batches of more than four tickets for sale.
Group the results by seller ID:

```
`select count(*), sellerid from listing
where numtickets > 4
group by sellerid
order by 1 desc, 2;`
`count | sellerid
------+----------
12 | 6386
11 | 17304
11 | 20123
11 | 25428
...`
```
