Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATEFORMAT and TIMEFORMAT

strings

The COPY command uses the DATEFORMAT and TIMEFORMAT options to parse date and time values
in your source data. DATEFORMAT and TIMEFORMAT are formatted strings that must match the format of your
source data's date and time values. For example, a COPY command loading source data with the date value
`Jan-01-1999` must include the following DATEFORMAT string:

```
COPY ...
            DATEFORMAT AS 'MON-DD-YYYY'
```

For more information on managing COPY data conversions, see [Data conversion parameters](copy-parameters-data-conversion.md "copy-parameters-data-conversion.md").

DATEFORMAT and TIMEFORMAT strings can contain datetime separators (such as '`-`', '`/`', or
'`:`'), as well the datepart and timepart formats in the following table.

###### Note

If you can't match the format of your date or time values with the following dateparts
and timeparts, or if you have date and time values that use formats different from each other, use the
`'auto'` argument with the DATEFORMAT or TIMEFORMAT parameter. The
`'auto'` argument recognizes several formats that aren't supported
when using a DATEFORMAT or TIMEFORMAT string. For more information, see [Using automatic recognition with DATEFORMAT and
TIMEFORMAT](automatic-recognition.md "automatic-recognition.md").

| Datepart or timepart | Meaning                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| YY                   | Year without century                                                                                                                                                                 |
| YYYY                 | Year with century                                                                                                                                                                    |
| MM                   | Month as a number                                                                                                                                                                    |
| MON                  | Month as a name (abbreviated name or full name)                                                                                                                                      |
| DD                   | Day of month as a number                                                                                                                                                             |
| HH or HH24           | Hour (24-hour clock) NoteIn DATETIME format strings for SQL functions, HH is the same as<br>HH12. However, in DATEFORMAT and TIMEFORMAT strings for COPY, HH is<br>the same as HH24. |
| HH12                 | Hour (12-hour clock)                                                                                                                                                                 |
| MI                   | Minutes                                                                                                                                                                              |
| SS                   | Seconds                                                                                                                                                                              |
| AM or PM             | Meridian indicator (for 12-hour clock)                                                                                                                                               |

The default date format is YYYY-MM-DD. The default timestamp without time zone
(TIMESTAMP) format is YYYY-MM-DD HH:MI:SS. The default timestamp with time zone
(TIMESTAMPTZ) format is YYYY-MM-DD HH:MI:SSOF, where OF is the offset from UTC (for
example, -8:00. You can't include a time zone specifier (TZ, tz, or OF) in the
timeformat_string. The seconds (SS) field also supports fractional seconds up to a
microsecond level of detail. To load TIMESTAMPTZ data that is in a format different from
the default format, specify 'auto'.

Following are some sample dates or times you can encounter in your source data, and
the corresponding DATEFORMAT or TIMEFORMAT strings for them.

| Example of source data date or time               | DATEFORMAT or TIMEFORMAT Syntax     |
| ------------------------------------------------- | ----------------------------------- |
| 03/31/2003                                        | DATEFORMAT AS 'MM/DD/YYYY'          |
| March 31, 2003                                    | DATEFORMAT AS 'MON DD, YYYY'        |
| 03.31.2003 18:45:05 03.31.2003<br>18:45:05.123456 | TIMEFORMAT AS 'MM.DD.YYYY HH:MI:SS' |

## Example

For an example of using TIMEFORMAT, see [Load a timestamp or
datestamp](r_COPY_command_examples.md#r_COPY_command_examples-load-a-time-datestamp "r_COPY_command_examples.md#r_COPY_command_examples-load-a-time-datestamp").
