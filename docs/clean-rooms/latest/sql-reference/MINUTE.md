# MINUTE function

The MINUTE function is a time extraction function that takes a time or timestamp as
input and returns the minute component (a value between 0 and 60).

## Syntax

```
minute(timestamp)
```

## Arguments

_timestamp_

A TIMESTAMP expression or a STRING of a valid timestamp format.

## Returns

The MINUTE function returns an INTEGER.

## Example

The following example extracts the minute component (`58`) from the input
timestamp `'2009-07-30 12:58:59'`.

```
SELECT minute('2009-07-30 12:58:59');
 58
```
