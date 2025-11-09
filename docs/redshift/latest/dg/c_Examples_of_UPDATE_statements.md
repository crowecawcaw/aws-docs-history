Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Examples of UPDATE statements

For more information about the tables used in the following examples, see [Sample database](c_sampledb.md "c_sampledb.md").

The CATEGORY table in the TICKIT database contains the following rows:

```
+-------+----------+-----------+--------------------------------------------+
| catid | catgroup |  catname  |                  catdesc                   |
+-------+----------+-----------+--------------------------------------------+
| 5     | Sports   | MLS       | Major League Soccer                        |
| 11    | Concerts | Classical | All symphony, concerto, and choir concerts |
| 1     | Sports   | MLB       | Major League Baseball                      |
| 6     | Shows    | Musicals  | Musical theatre                            |
| 3     | Sports   | NFL       | National Football League                   |
| 8     | Shows    | Opera     | All opera and light opera                  |
| 2     | Sports   | NHL       | National Hockey League                     |
| 9     | Concerts | Pop       | All rock and pop music concerts            |
| 4     | Sports   | NBA       | National Basketball Association            |
| 7     | Shows    | Plays     | All non-musical theatre                    |
| 10    | Concerts | Jazz      | All jazz singers and bands                 |
+-------+----------+-----------+--------------------------------------------+
```

**Updating a table based on a range of values**

Update the CATGROUP column based on a range of values in the CATID column.

```
`UPDATE category
SET catgroup='Theatre'
WHERE catid BETWEEN 6 AND 8;

SELECT * FROM category
WHERE catid BETWEEN 6 AND 8;`

`+-------+----------+----------+---------------------------+
| catid | catgroup | catname | catdesc |
+-------+----------+----------+---------------------------+
| 6 | Theatre | Musicals | Musical theatre |
| 7 | Theatre | Plays | All non-musical theatre |
| 8 | Theatre | Opera | All opera and light opera |
+-------+----------+----------+---------------------------+`
```

**Updating a table based on a current value**

Update the CATNAME and CATDESC columns based on their current CATGROUP value:

```
`UPDATE category
SET catdesc=default, catname='Shows'
WHERE catgroup='Theatre';

SELECT * FROM category
WHERE catname='Shows';`

`+-------+----------+---------+---------+
| catid | catgroup | catname | catdesc |
+-------+----------+---------+---------+
| 6 | Theatre | Shows | NULL |
| 7 | Theatre | Shows | NULL |
| 8 | Theatre | Shows | NULL |
+-------+----------+---------+---------+)`
```

In this case, the CATDESC column was set to null because no default value was defined
when the table was created.

Run the following commands to set the CATEGORY table data back to the original
values:

```
`TRUNCATE category;

COPY category
FROM 's3://redshift-downloads/tickit/category_pipe.txt'
DELIMITER '|'
IGNOREHEADER 1
REGION 'us-east-1'
IAM_ROLE default;`
```

**Updating a table based on the result of a WHERE clause
subquery**

Update the CATEGORY table based on the result of a subquery in the WHERE clause:

```
UPDATE category
SET catdesc='Broadway Musical'
WHERE category.catid IN
(SELECT category.catid FROM category
JOIN event ON category.catid = event.catid
JOIN venue ON venue.venueid = event.venueid
JOIN sales ON sales.eventid = event.eventid
WHERE venuecity='New York City' AND catname='Musicals');
```

View the updated table:

```
`SELECT * FROM category ORDER BY catid;`

`+-------+----------+-----------+--------------------------------------------+
| catid | catgroup | catname | catdesc |
+-------+----------+-----------+--------------------------------------------+
| 2 | Sports | NHL | National Hockey League |
| 3 | Sports | NFL | National Football League |
| 4 | Sports | NBA | National Basketball Association |
| 5 | Sports | MLS | Major League Soccer |
| 6 | Shows | Musicals | Broadway Musical |
| 7 | Shows | Plays | All non-musical theatre |
| 8 | Shows | Opera | All opera and light opera |
| 9 | Concerts | Pop | All rock and pop music concerts |
| 10 | Concerts | Jazz | All jazz singers and bands |
| 11 | Concerts | Classical | All symphony, concerto, and choir concerts |
+-------+----------+-----------+--------------------------------------------+`
```

**Updating a table based on the result of a WITH clause
subquery**

To update the CATEGORY table based on the result of a subquery using the WITH clause,
use the following example.

```
`WITH u1 as (SELECT catid FROM event ORDER BY catid DESC LIMIT 1)
UPDATE category SET catid='200' FROM u1 WHERE u1.catid=category.catid;

SELECT * FROM category ORDER BY catid DESC LIMIT 1;`

`+-------+----------+---------+---------------------------------+
| catid | catgroup | catname | catdesc |
+-------+----------+---------+---------------------------------+
| 200 | Concerts | Pop | All rock and pop music concerts |
+-------+----------+---------+---------------------------------+`
```

## Updating a table based on the result of a join condition

Update the original 11 rows in the CATEGORY table based on matching CATID rows in
the EVENT table:

```
`UPDATE category SET catid=100
FROM event
WHERE event.catid=category.catid;

SELECT * FROM category ORDER BY catid;`

`+-------+----------+-----------+--------------------------------------------+
| catid | catgroup | catname | catdesc |
+-------+----------+-----------+--------------------------------------------+
| 2 | Sports | NHL | National Hockey League |
| 3 | Sports | NFL | National Football League |
| 4 | Sports | NBA | National Basketball Association |
| 5 | Sports | MLS | Major League Soccer |
| 10 | Concerts | Jazz | All jazz singers and bands |
| 11 | Concerts | Classical | All symphony, concerto, and choir concerts |
| 100 | Concerts | Pop | All rock and pop music concerts |
| 100 | Shows | Plays | All non-musical theatre |
| 100 | Shows | Opera | All opera and light opera |
| 100 | Shows | Musicals | Broadway Musical |
+-------+----------+-----------+--------------------------------------------+`
```

Note that the EVENT table is listed in the FROM clause and the join condition to
the target table is defined in the WHERE clause. Only four rows qualified for the
update. These four rows are the rows whose CATID values were originally 6, 7, 8, and
9; only those four categories are represented in the EVENT table:

```
`SELECT DISTINCT catid FROM event;`

`+-------+
| catid |
+-------+
| 6 |
| 7 |
| 8 |
| 9 |
+-------+`
```

Update the original 11 rows in the CATEGORY table by extending the previous
example and adding another condition to the WHERE clause. Because of the restriction
on the CATGROUP column, only one row qualifies for the update (although four rows
qualify for the join).

```
`UPDATE category SET catid=100
FROM event
WHERE event.catid=category.catid
AND catgroup='Concerts';

SELECT * FROM category WHERE catid=100;`

`+-------+----------+---------+---------------------------------+
| catid | catgroup | catname | catdesc |
+-------+----------+---------+---------------------------------+
| 100 | Concerts | Pop | All rock and pop music concerts |
+-------+----------+---------+---------------------------------+`
```

An alternative way to write this example is as follows:

```
UPDATE category SET catid=100
FROM event JOIN category cat ON event.catid=cat.catid
WHERE cat.catgroup='Concerts';
```

The advantage to this approach is that the join criteria are clearly separated
from any other criteria that qualify rows for the update. Note the use of the alias
CAT for the CATEGORY table in the FROM clause.

## Updates with outer joins in the FROM clause

The previous example showed an inner join specified in the FROM clause of an
UPDATE statement. The following example returns an error because the FROM clause does
not support outer joins to the target table:

```
UPDATE category SET catid=100
FROM event LEFT JOIN category cat ON event.catid=cat.catid
WHERE cat.catgroup='Concerts';
ERROR:  Target table must be part of an equijoin predicate
```

If the outer join is required for the UPDATE statement, you can move the outer
join syntax into a subquery:

```
UPDATE category SET catid=100
FROM
(SELECT event.catid FROM event LEFT JOIN category cat ON event.catid=cat.catid) eventcat
WHERE category.catid=eventcat.catid
AND catgroup='Concerts';
```

## Updates with columns from another table in the SET clause

To update the listing table in the TICKIT sample database with
values from the sales table, use the following example.

```
`SELECT listid, numtickets FROM listing WHERE sellerid = 1 ORDER BY 1 ASC LIMIT 5;`

`+--------+------------+
| listid | numtickets |
+--------+------------+
| 100423 | 4 |
| 108334 | 24 |
| 117150 | 4 |
| 135915 | 20 |
| 205927 | 6 |
+--------+------------+`

`UPDATE listing
SET numtickets = sales.sellerid
FROM sales
WHERE sales.sellerid = 1 AND listing.sellerid = sales.sellerid;

SELECT listid, numtickets FROM listing WHERE sellerid = 1 ORDER BY 1 ASC LIMIT 5;`

`+--------+------------+
| listid | numtickets |
+--------+------------+
| 100423 | 1 |
| 108334 | 1 |
| 117150 | 1 |
| 135915 | 1 |
| 205927 | 1 |
+--------+------------+`
```
