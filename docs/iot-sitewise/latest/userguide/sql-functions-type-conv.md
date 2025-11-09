# Type conversion functions

Type conversion functions are used to change the data type of a value from one to
another. They are essential for ensuring data compatibility and performing operations
that require data in a specific format.

| **Function**   | **Signature**                                              | **Description**                                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `TO_DATE`      | • TO_DATE (integer)<br>• TO_DATE (expression, format)      | • Converts an epoch millisecond integer into a date value.<br>• Converts a character string representation into a date value.                                                                                                  |
| `TO_TIMESTAMP` | • TO_TIMESTAMP (double)<br>• TO_TIMESTAMP (string, format) | • Converts an epoch second integer into a timestamp data type.<br>• Converts a string representation of a date and time into a timestamp<br>data type.                                                                         |
| `TO_TIME`      | • TO_TIME (int)<br>• TO_TIME (string, format)              | • Converts an epoch millisecond integer into a time value.<br>• Converts a character string representation into a time value.                                                                                                  |
| `CAST`         | CAST (<expression> AS <data type>)                         | Converts an entity, or expression that evaluates to a single value, from<br>one type to another.<br>Supported data types are:<br>• BOOLEAN<br>• INTEGER<br>• INT<br>• TIMESTAMP<br>• DATE<br>• CHAR<br>• CHARACTER<br>• STRING |

###### Example of a SQL query using the listed functions:

```
SELECT TO_TIMESTAMP (100) AS timestamp_value,
  TO_DATE(r.event_timestamp) AS date_value,
  TO_TIME(r.event_timestamp) AS time_value
FROM raw_time_series AS r

```
