# Comparison conditions

Comparison conditions state logical relationships between two values. All comparison
conditions are binary operators with a Boolean return type.

AWS Clean Rooms SQL supports the comparison operators described in the following table.

| Operator | Syntax               | Description                                                                                                                                                                                         |
| -------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <        | `a < b`              | The less than comparison operator. Used to compare two values and<br>determine if the value on the left is less than the value on the right.                                                        |
| >        | `a > b`              | The greater than comparison operator. Used to compare two values and<br>determine if the value on the left is greater than the value on the right.                                                  |
| <=       | `a <= b`             | The less than or equal to comparison operator. Used to compare two values<br>and returns `true` if the value on the left is less than or equal to the value on<br>the right, and `false` otherwise. |
| >=       | `a >= b`             | The greater than or equal to comparison operator. Used to compare two<br>values and determine if the value on the left is greater than or equal to the value on the<br>right.                       |
| =        | `a = b`              | The equality comparison operator, which compares two values and returns<br>`true` if they're equal, and `false` otherwise.                                                                          |
| <> or != | `a <> b` or `a != b` | The not equal to comparison operator, which compares two values and<br>returns `true` if they're not equal, and `false` otherwise.                                                                  |

## Examples

Here are some simple examples of comparison conditions:

```
a = 5
a < b
min(x) >= 5
qtysold = any (select qtysold from sales where dateid = 1882
```

The following query returns the id values for all the squirrels that are not currently
foraging.

```
SELECT id FROM squirrels
WHERE !is_foraging
```

The following query returns venues with more than 10,000 seats from the VENUE table:

```
select venueid, venuename, venueseats from venue
where venueseats > 10000
order by venueseats desc;

venueid |           venuename            | venueseats
---------+--------------------------------+------------
83 | FedExField                     |      91704
 6 | New York Giants Stadium        |      80242
79 | Arrowhead Stadium              |      79451
78 | INVESCO Field                  |      76125
69 | Dolphin Stadium                |      74916
67 | Ralph Wilson Stadium           |      73967
76 | Jacksonville Municipal Stadium |      73800
89 | Bank of America Stadium        |      73298
72 | Cleveland Browns Stadium       |      73200
86 | Lambeau Field                  |      72922
...
(57 rows)
```

This example selects the users (USERID) from the USERS table who like rock music:

```
select userid from users where likerock = 't' order by 1 limit 5;

userid
--------
3
5
6
13
16
(5 rows)

```

This example selects the users (USERID) from the USERS table where it is unknown whether
they like rock music:

```
select firstname, lastname, likerock
from users
where likerock is unknown
order by userid limit 10;

firstname | lastname | likerock
----------+----------+----------
Rafael    | Taylor   |
Vladimir  | Humphrey |
Barry     | Roy      |
Tamekah   | Juarez   |
Mufutau   | Watkins  |
Naida     | Calderon |
Anika     | Huff     |
Bruce     | Beck     |
Mallory   | Farrell  |
Scarlett  | Mayer    |
(10 rows
```

## Examples with a TIME column

The following example table TIME_TEST has a column TIME_VAL (type TIME) with three values
inserted.

```
select time_val from time_test;

time_val
---------------------
20:00:00
00:00:00.5550
00:58:00
```

The following example extracts the hours from each timetz_val.

```
select time_val from time_test where time_val < '3:00';
   time_val
---------------
 00:00:00.5550
 00:58:00
```

The following example compares two time literals.

```
select time '18:25:33.123456' = time '18:25:33.123456';
 ?column?
----------
 t
```

## Examples with a TIMETZ column

The following example table TIMETZ_TEST has a column TIMETZ_VAL (type TIMETZ) with three
values inserted.

```
select timetz_val from timetz_test;

timetz_val
------------------
04:00:00+00
00:00:00.5550+00
05:58:00+00
```

The following example selects only the TIMETZ values less than `3:00:00 UTC`. The
comparison is made after converting the value to UTC.

```
select timetz_val from timetz_test where timetz_val < '3:00:00 UTC';

   timetz_val
---------------
 00:00:00.5550+00
```

The following example compares two TIMETZ literals. The time zone is ignored for the
comparison.

```
select time '18:25:33.123456 PST' < time '19:25:33.123456 EST';

 ?column?
----------
 t
```
