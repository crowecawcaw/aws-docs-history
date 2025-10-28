Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ANY_VALUE

function

The ANY_VALUE function returns any value from the input expression values
nondeterministically. This function returns `NULL` if the input expression
doesn't result in any rows being returned. The function can also return
`NULL` if there are `NULL` values in the input expression. If
the input contains `NULL` values mixed with non-`NULL` values,
`NULL` might be returned. If all values are `NULL`,
`NULL` is returned. If no rows match the condition, `NULL` is
returned.

## Syntax

```
ANY_VALUE( [ DISTINCT | ALL ] *expression* )

```

## Arguments

DISTINCT | ALL

Specify either DISTINCT or ALL
to return any value from the input expression values. The DISTINCT argument
has no effect and is ignored.

_expression_

The target column or expression on which the function operates. The _expression_ is one of the following data types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- REAL
- DOUBLE PRECISON
- BOOLEAN
- CHAR
- VARCHAR
- DATE
- TIMESTAMP
- TIMESTAMPTZ
- TIME
- TIMETZ
- INTERVAL YEAR TO MONTH
- INTERVAL DAY TO SECOND
- VARBYTE
- SUPER
- HLLSKETCH
- GEOMETRY
- GEOGRAPHY

## Returns

Returns the same data type as _expression_.

## Usage notes

If a statement that specifies the ANY_VALUE function for a column also includes a second column reference, the second column must appear in a GROUP BY clause or be included in an aggregate function.

## Examples

The examples use the event table that is created in [Step 4: Load sample data from Amazon S3](../gsg/rs-gsg-create-sample-db.md "../gsg/rs-gsg-create-sample-db.md") in the _Amazon Redshift Getting Started Guide_. The following example returns an instance of any dateid where the eventname is Eagles.

```
select any_value(dateid) as dateid, eventname from event where eventname ='Eagles' group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1878  | Eagles

```

The following example returns an instance of any dateid where the eventname is Eagles or Cold War Kids.

```
select any_value(dateid) as dateid, eventname from event where eventname in('Eagles', 'Cold War Kids') group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1922  | Cold War Kids
 1878  | Eagles

```
