# HOUR function

The HOUR function is a time extraction function that takes a time or timestamp as input
and returns the hour component (a value between 0 and 23).

This time extraction function is useful when you need to work with specific components
of a time or timestamp, such as when performing time-based calculations, filtering data, or
formatting time values.

## Syntax

```
hour(timestamp)
```

## Arguments

_timestamp_

A TIMESTAMP expression.

## Returns

The HOUR function returns an INTEGER.

## Example

The following example extracts the hour component (`12`) from the input
timestamp `'2009-07-30 12:58:59'`.

```
SELECT hour('2009-07-30 12:58:59');
 12
```
