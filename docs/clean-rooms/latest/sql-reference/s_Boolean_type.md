# Boolean type

Use the BOOLEAN data type to store true and false values in a single-byte column. The
following table describes the three possible states for a Boolean value and the literal
values that result in that state. Regardless of the input string, a Boolean column stores
and outputs "t" for true and "f" for false.

| State   | Valid literal values             | Storage |
| ------- | -------------------------------- | ------- |
| True    | `TRUE 't' 'true' 'y' 'yes' '1'`  | 1 byte  |
| False   | `FALSE 'f' 'false' 'n' 'no' '0'` | 1 byte  |
| Unknown | `NULL`                           | 1 byte  |

You can use an IS comparison to check a Boolean value only as a predicate in the WHERE
clause. You can't use the IS comparison with a Boolean value in the SELECT
list.

## Examples

You can use a BOOLEAN column to store an "Active/Inactive" state for each customer in
a CUSTOMER table.

```
select * from customer;
custid | active_flag
-------+--------------
   100 | t
```

In this example, the following query selects users from the USERS table who like
sports but do not like theatre:

```
select firstname, lastname, likesports, liketheatre
from users
where likesports is true and liketheatre is false
order by userid limit 10;

firstname |  lastname  | likesports | liketheatre
----------+------------+------------+-------------
Alejandro | Rosalez    | t          | f
Akua      | Mansa      | t          | f
Arnav     | Desai      | t          | f
Carlos    | Salazar    | t          | f
Diego     | Ramirez    | t          | f
Efua      | Owusu      | t          | f
John      | Stiles     | t          | f
Jorge     | Souza      | t          | f
Kwaku     | Mensah     | t          | f
Kwesi     | Manu       | t          | f
(10 rows)
```

The following example selects users from the USERS table for whom is it unknown
whether they like rock music.

```
select firstname, lastname, likerock
from users
where likerock is unknown
order by userid limit 10;

firstname | lastname | likerock
----------+----------+----------
Alejandro | Rosalez   |
Carlos    | Salazar   |
Diego     | Ramirez   |
John      | Stiles    |
Kwaku     | Mensah    |
Martha    | Rivera    |
Mateo     | Jackson   |
Paulo     | Santos    |
Richard   | Roe       |
Saanvi    | Sarkar    |
(10 rows)
```

The following example returns an error because it uses an IS comparison in the SELECT
list.

```
select firstname, lastname, likerock is true as "check"
from users
order by userid limit 10;

[Amazon](500310) Invalid operation: Not implemented
```

The following example succeeds because it uses an equal comparison ( = ) in the
SELECT list instead of the IS comparison.

```
select firstname, lastname, likerock = true as "check"
from users
order by userid limit 10;

firstname | lastname  | check
----------+-----------+------
Alejandro | Rosalez   |
Carlos    | Salazar   |
Diego     | Ramirez   | true
John      | Stiles    |
Kwaku     | Mensah    | true
Martha    | Rivera    | true
Mateo     | Jackson   |
Paulo     | Santos    | false
Richard   | Roe       |
Saanvi    | Sarkar    |
```
