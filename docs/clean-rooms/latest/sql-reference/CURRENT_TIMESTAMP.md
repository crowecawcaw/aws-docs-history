

# CURRENT\_TIMESTAMP function
<a name="CURRENT_TIMESTAMP"></a>

CURRENT\_TIMESTAMP returns the current date and time, including the date, time, and (optionally) the milliseconds or microseconds.

This function is useful when you need to get the current date and time, for example, to record the timestamp of an event, to perform time-based calculations, or to populate date/time columns.

## Syntax
<a name="CURRENT_TIMESTAMP-syntax"></a>

```
current_timestamp()
```

## Return type
<a name="CURRENT_TIMESTAMP-return-type"></a>

The CURRENT\_TIMESTAMP function returns a DATE.

## Example
<a name="CURRENT_TIMESTAMP-example"></a>

The following example returns current date and time at the moment the query is executed, which is April 25, 2020, at 15:49:11.914 (3:49:11.914 PM).

```
SELECT current_timestamp();
 2020-04-25 15:49:11.914
```

The following example retrieves the current date and time for each row in the `squirrels` table.

```
SELECT current_timestamp() FROM squirrels
```