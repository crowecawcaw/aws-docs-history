# TIMESTAMP

Use the TIMESTAMP data type to store complete timestamp values that include the date
and the time of day.

TIMESTAMP columns store values with up to a maximum of six digits of precision for
fractional seconds.

If you insert a date into a TIMESTAMP column, or a date with a partial timestamp
value, the value is implicitly converted into a full timestamp value. This full
timestamp value has default values (00) for missing hours, minutes, and seconds. Time
zone values in input strings are ignored.

By default, TIMESTAMP values are UTC in both user tables and AWS Clean Rooms system
tables.
