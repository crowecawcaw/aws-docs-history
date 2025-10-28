# SECOND function

The SECOND function is a time extraction function that takes a time or timestamp as
input and returns the second component (a value between 0 and 60).

## Syntax

```
second(timestamp)
```

## Arguments

_timestamp_

A TIMESTAMP expression.

## Returns

The SECOND function returns an INTEGER.

## Example

The following example extracts the second component (`59`) from the input
timestamp `'2009-07-30 12:58:59'`.

```
SELECT second('2009-07-30 12:58:59');
 59
```
