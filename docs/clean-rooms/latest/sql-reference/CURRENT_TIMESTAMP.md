# CURRENT_TIMESTAMP function

CURRENT_TIMESTAMP returns the current date and time, including the date, time, and
(optionally) the milliseconds or microseconds.

This function is useful when you need to get the current date and time, for example, to
record the timestamp of an event, to perform time-based calculations, or to populate
date/time columns.

## Syntax

```
current_timestamp()
```

## Return type

The CURRENT_TIMESTAMP function returns a DATE.

## Example

The following example returns current date and time at the moment the query is
executed, which is April 25, 2020, at 15:49:11.914 (3:49:11.914 PM).

```
SELECT current_timestamp();
 2020-04-25 15:49:11.914
```

The following example retrieves the current date and time for each row in the
`squirrels` table.

```
SELECT current_timestamp() FROM squirrels
```
