

# WHERE clause

The WHERE clause filters the rows that a query returns by applying one or more conditions to columns in the configured tables that the query reads. A condition is an expression that evaluates to a Boolean result, such as a comparison or a combination of comparisons joined by `AND`, `OR`, and `NOT`.

## Syntax
<a name="WHERE_clause-synopsis"></a>

```
[ WHERE condition ]
```

## *condition*
<a name="WHERE_clause-synopsis-condition"></a>

Any search condition that returns a Boolean result, such as a predicate on a table column. The following examples are valid conditions:

```
region = 'west'
spend > 100
campaign_id IN ('c-1', 'c-2')
region LIKE 'w%'
```

You can combine conditions with `AND`, `OR`, and `NOT`, and you can use parentheses to group them. In the following example, parentheses group two conditions:

```
WHERE region = 'west'
    AND (spend > 100 OR campaign_id = 'c-1')
```

## Usage notes
<a name="WHERE_clause_usage_notes"></a>

You can't use aggregate functions in the WHERE clause. To filter on the result of an aggregate function, use the HAVING clause instead.

Columns that you reference in the WHERE clause must come from the tables in the FROM clause.

## Examples
<a name="SELECT_synopsis-example"></a>

The following example returns the rows of the `impressions` table where `region` is `west` and `spend` is greater than `100`. For input rows `(u-100, west, 150)`, `(u-101, east, 90)`, and `(u-103, west, 220)`, the query returns two rows.

```
SELECT user_id,
    region,
    spend
FROM impressions
WHERE region = 'west'
    AND spend > 100;

user_id | region | spend
--------+--------+------
u-100   | west   |   150
u-103   | west   |   220
```

The following example joins the `impressions` and `purchases` tables by putting the join condition in the WHERE clause, and keeps only purchases over `50`. For impressions rows `(u-100, c-1)` and `(u-103, c-2)` and purchases rows `(u-100, 80)`, `(u-103, 120)`, and `(u-101, 40)`, the query returns two rows.

```
SELECT i.user_id,
    i.campaign_id,
    p.amount
FROM impressions i, purchases p
WHERE i.user_id = p.user_id
    AND p.amount > 50;

user_id | campaign_id | amount
--------+-------------+-------
u-100   | c-1         |     80
u-103   | c-2         |    120
```