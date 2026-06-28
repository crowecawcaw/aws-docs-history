# NVL2 function

Returns one of two values based on whether a specified expression evaluates to NULL or
NOT NULL.

## Syntax

```
NVL2 ( *expression*, *not\_null\_return\_value*, *null\_return\_value* )
```

## Arguments

_expression_

An expression, such as a column name, to be evaluated for null
status.

_not\_null\_return\_value_

The value returned if _expression_ evaluates to NOT NULL.
The _not\_null\_return\_value_ value must either have the same
data type as _expression_ or be implicitly convertible to
that data type.

_null\_return\_value_

The value returned if _expression_ evaluates to NULL. The
_null\_return\_value_ value must either have the same data
type as _expression_ or be implicitly convertible to that
data type.

## Return type

The NVL2 return type is determined as follows:

- If either _not\_null\_return\_value_ or
  _null\_return\_value_ is null, the data type of the not-null
  expression is returned.

If both _not\_null\_return\_value_ and
_null\_return\_value_ are not null:

- If _not\_null\_return\_value_ and
  _null\_return\_value_ have the same data type, that data type
  is returned.
- If _not\_null\_return\_value_ and
  _null\_return\_value_ have different numeric data types, the
  smallest compatible numeric data type is returned.
- If _not\_null\_return\_value_ and
  _null\_return\_value_ have different datetime data types, a
  timestamp data type is returned.
- If _not\_null\_return\_value_ and
  _null\_return\_value_ have different character data types, the
  data type of _not\_null\_return\_value_ is returned.
- If _not\_null\_return\_value_ and
  _null\_return\_value_ have mixed numeric and non-numeric data
  types, the data type of _not\_null\_return\_value_ is
  returned.

###### Important

In the last two cases where the data type of
_not\_null\_return\_value_ is returned,
_null\_return\_value_ is implicitly cast to that data type. If
the data types are incompatible, the function fails.

## Usage notes

For NVL2, the return will have the value of either the
_not\_null\_return\_value_ or _null\_return\_value_
parameter, whichever is selected by the function, but will have the data type of
_not\_null\_return\_value_.

For example, assuming column1 is NULL, the following queries will return the same
value. However, the DECODE return value data type will be INTEGER and the NVL2 return
value data type will be VARCHAR.

```
select decode(column1, null, 1234, '2345');
select nvl2(column1, '2345', 1234);
```

## Example

The following example modifies some sample data, then evaluates two fields to provide
appropriate contact information for users:

```
update users set email = null where firstname = 'Aphrodite' and lastname = 'Acevedo';

select (firstname + ' ' + lastname) as name,
nvl2(email, email, phone) AS contact_info
from users
where state = 'WA'
and lastname  like 'A%'
order by lastname, firstname;

name			     contact_info
--------------------+-------------------------------------------
Aphrodite Acevedo	(555) 555-0100
Caldwell Acevedo 	Nunc.sollicitudin@example.ca
Quinn Adams		   vel@example.com
Kamal Aguilar		 quis@example.com
Samson Alexander	 hendrerit.neque@example.com
Hall Alford		   ac.mattis@example.com
Lane Allen		    et.netus@example.com
Xander Allison	   ac.facilisis.facilisis@example.com
Amaya Alvarado	   dui.nec.tempus@example.com
Vera Alvarez		  at.arcu.Vestibulum@example.com
Yetta Anthony		 enim.sit@example.com
Violet Arnold		 ad.litora@example.comm
August Ashley		 consectetuer.euismod@example.com
Karyn Austin		  ipsum.primis.in@example.com
Lucas Ayers		   at@example.com
```
