# ANY_VALUE function

The ANY_VALUE function returns any value from the input expression values
nondeterministically. This function can return NULL if the input expression doesn't result in any
rows being returned.

## Syntax

```
ANY_VALUE ( [ DISTINCT | ALL ] *expression* )

```

## Arguments

DISTINCT | ALL

Specify either DISTINCT or ALL to return any value from the input expression values. The
DISTINCT argument has no effect and is ignored.

_expression_

The target column or expression on which the function operates. The
_expression_ is one of the following data types:

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
- VARBYTE
- SUPER

## Returns

Returns the same data type as _expression_.

## Usage notes

If a statement that specifies the ANY_VALUE function for a column also includes a second
column reference, the second column must appear in a GROUP BY clause or be included in an
aggregate function.

## Examples

The following example returns an instance of any `dateid` where the
`eventname` is `Eagles`.

```
select any_value(dateid) as dateid, eventname from event where eventname ='Eagles' group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1878  | Eagles

```

The following example returns an instance of any `dateid` where the
`eventname` is `Eagles` or `Cold War Kids`.

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
