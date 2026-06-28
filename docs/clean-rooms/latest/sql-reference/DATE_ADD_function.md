# DATE\_ADD function

Returns the date that is num\_days after start\_date.

## Syntax

```
date_add(*start\_date*, *num\_days*)
```

## Arguments

_start\_date_

The starting date value.

_num\_days_

The number of days to add (integer). A positive number adds days, a negative
number subtracts days.

## Return type

DATE

## Examples

The following example adds one day to a date:

```
SELECT date_add('2016-07-30', 1);

Result:
2016-07-31

```

The following example adds multiple days.

```
SELECT date_add('2016-07-30', 5);

Result:
2016-08-04

```

## Usage notes

This documentation is for Spark SQL's DATE\_ADD function, which provides a simpler
interface for adding days to dates compared to some other SQL variants. For adding other
intervals like months or years, different functions may be required.
