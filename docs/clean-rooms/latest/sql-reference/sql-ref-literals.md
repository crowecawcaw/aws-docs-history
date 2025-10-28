# Literals

A literal or constant is a fixed data value, composed of a sequence of characters or a
numeric constant.

AWS Clean Rooms supports several types of literals, including:

- Numeric literals for integer, decimal, and floating-point numbers.
- Date, time, and timestamp literals, used with datetime data types. For more
  information, see [Date, time, and timestamp literals](r_Date_and_time_literals.md "r_Date_and_time_literals.md").
- Interval literals. For more information, see [Interval literals](r_interval_literals.md "r_interval_literals.md").
- Null literals, used to specify a null value.
- Only TAB, CARRIAGE RETURN (CR), and LINE
  FEED (LF) Unicode control characters from the Unicode general category (Cc)
  are supported.
  AWS Clean Rooms doesn't support direct references to string literals in the SELECT clause, but they
  can be used within functions such as CAST.

## + (Concatenation) operator

Concatenates numeric literals, string literals, and/or datetime and interval literals.
They are on either side of the + symbol and return different types based on the inputs on
either side of the + symbol.

### Syntax

```
``numeric` + `string``
```

```
`date` + `time`
```

```
`date` + `timetz`
```

The order of the arguments can be reversed.

### Arguments

`numeric literals`

Literals or constants that represent numbers can be integer or
floating-point.

`string literals`

Strings, character strings, or character constants

`date`

A DATE column or an expression that implicitly converts to a
DATE.

`time`

A TIME column or an expression that implicitly converts to a
TIME.

`timetz`

A TIMETZ column or an expression that implicitly converts to
a TIMETZ.

### Example

The following example table TIME_TEST has a column
TIME_VAL (type TIME) with three values inserted.

```
select date '2000-01-02' + time_val as ts from time_test;
```
