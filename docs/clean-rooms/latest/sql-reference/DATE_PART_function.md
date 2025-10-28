# DATE_PART function

DATE_PART extracts date part values from an expression. DATE_PART is a synonym of the
PGDATE_PART function.

## Syntax

```
datepart(field, source)
```

## Arguments

_field_

Which part of the source should be extracted, and supported string values
are the same as the fields of the equivalent function EXTRACT.

_source_

A DATE or INTERVAL column from where field should be extracted.

## Return type

If _field_ is 'SECOND', a DECIMAL(8, 6). In all
other cases, an INTEGER.

## Example

The following example extracts the day of the year (DOY) from a date value. The
output shows that the day of the year for the date "2019-08-12" is `224`.
This means that August 12, 2019 is the 224th day of the year 2019.

```
SELECT datepart('doy', DATE'2019-08-12');
 224
```
