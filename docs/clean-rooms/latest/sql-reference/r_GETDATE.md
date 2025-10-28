# GETDATE function

The GETDATE function returns the current date and time in the current
session time zone (UTC by default).

It returns the start date or time of the current statement, even when it is within a
transaction block.

## Syntax

```
GETDATE()
```

The parentheses are required.

## Return type

TIMESTAMP

## Example

The following example uses the GETDATE function to return the full
timestamp for the current date.

```
select getdate();
```
