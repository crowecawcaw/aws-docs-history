Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# OBJECT function

Creates an object of the SUPER data type.

## Syntax

```
OBJECT ( [ key1, value1 ], [ key2, value2 ...] )
```

## Arguments

_key1, key2_

Expressions that evaluate to VARCHAR type strings.

_value1, value2_

Expressions of any Amazon Redshift data type except datetime types, since
Amazon Redshift doesn't cast datetime types to the SUPER data type. For more
information on datetime types, see [Datetime types](r_Datetime_types.md "r_Datetime_types.md").

`value` expressions in an object don't need to be of the same
data type.

## Return type

`SUPER`

## Example

```
-- Creates an empty object.
select object();

`object
--------
{}
(1 row)`

-- Creates objects with different keys and values.
select object('a', 1, 'b', true, 'c', 3.14);

`object
---------------------------
{"a":1,"b":true,"c":3.14}
(1 row)`

select object('a', object('aa', 1), 'b', array(2,3), 'c', json_parse('{}'));

`object
---------------------------------
{"a":{"aa":1},"b":[2,3],"c":{}}
(1 row)`

-- Creates objects using columns from a table.
create table bar (k varchar, v super);
insert into bar values ('k1', json_parse('[1]')), ('k2', json_parse('{}'));
select object(k, v) from bar;

`object
------------
{"k1":[1]}
{"k2":{}}
(2 rows)`

-- Errors out because DATE type values can't be converted to SUPER type.
select object('k', '2008-12-31'::date);

`ERROR: OBJECT could not convert type date to super`
```
