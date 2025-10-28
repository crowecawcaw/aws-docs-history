# CURRENT_DATE function

CURRENT_DATE returns a date in the current session time zone (UTC by default) in the
default format: YYYY-MM-DD.

###### Note

CURRENT_DATE returns the start date for the current transaction, not for the start of
the current statement. Consider the scenario where you start a transaction containing
multiple statements on 10/01/08 23:59, and the statement containing CURRENT_DATE runs at
10/02/08 00:00. CURRENT_DATE returns `10/01/08`, not
`10/02/08`.

## Syntax

```
CURRENT_DATE
```

## Return type

DATE

## Example

The following example returns the current date (in the AWS Region where the
function runs).

```
`select current_date;`
`date
------------
2008-10-01`
```
