# Date functions

###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/") 

Amazon S3 Select supports the following date functions.

###### Topics

* [DATE\_ADD](#s3-select-sql-reference-date-add "#s3-select-sql-reference-date-add")
* [DATE\_DIFF](#s3-select-sql-reference-date-diff "#s3-select-sql-reference-date-diff")
* [EXTRACT](#s3-select-sql-reference-extract "#s3-select-sql-reference-extract")
* [TO\_STRING](#s3-select-sql-reference-to-string "#s3-select-sql-reference-to-string")
* [TO\_TIMESTAMP](#s3-select-sql-reference-to-timestamp "#s3-select-sql-reference-to-timestamp")
* [UTCNOW](#s3-select-sql-reference-utcnow "#s3-select-sql-reference-utcnow")

## DATE\_ADD


Given a date part, a quantity, and a timestamp, `DATE_ADD` returns an updated
 timestamp by altering the date part by the quantity.


### Syntax



```
DATE_ADD( `date_part`, `quantity`, `timestamp` )
```

### Parameters




*``date_part``*


Specifies which part of the date to modify. This can be one of
 the following:



* year
* month
* day
* hour
* minute
* second



*``quantity``*


The value to apply to the updated timestamp. Positive values for
 ``quantity`` add to
 the timestamp's date\_part, and negative values subtract.




*``timestamp``*


The target timestamp that the function operates on.




### Examples



```
DATE_ADD(year, 5, `2010-01-01T`)                -- 2015-01-01 (equivalent to 2015-01-01T)
DATE_ADD(month, 1, `2010T`)                     -- 2010-02T (result will add precision as necessary)
DATE_ADD(month, 13, `2010T`)                    -- 2011-02T
DATE_ADD(day, -1, `2017-01-10T`)                -- 2017-01-09 (equivalent to 2017-01-09T)
DATE_ADD(hour, 1, `2017T`)                      -- 2017-01-01T01:00-00:00
DATE_ADD(hour, 1, `2017-01-02T03:04Z`)          -- 2017-01-02T04:04Z
DATE_ADD(minute, 1, `2017-01-02T03:04:05.006Z`) -- 2017-01-02T03:05:05.006Z
DATE_ADD(second, 1, `2017-01-02T03:04:05.006Z`) -- 2017-01-02T03:04:06.006Z
```

## DATE\_DIFF


Given a date part and two valid timestamps, `DATE_DIFF` returns the difference
 in date parts. The return value is a negative integer when the
 ``date_part`` value of
 ``timestamp1`` is greater than the
 ``date_part`` value of
 ``timestamp2``. The return value is
 a positive integer when the ``date_part``
 value of ``timestamp1`` is less than the
 ``date_part`` value of
 ``timestamp2``.


### Syntax



```
DATE_DIFF( `date_part`, `timestamp1`, `timestamp2` )
```

### Parameters





*``date_part``*


Specifies which part of the timestamps to compare. For the definition of
 `date_part`, see [DATE\_ADD](#s3-select-sql-reference-date-add "#s3-select-sql-reference-date-add").




*``timestamp1``*


The first timestamp to compare.




*``timestamp2``*


The second timestamp to compare.




### Examples



```
DATE_DIFF(year, `2010-01-01T`, `2011-01-01T`)            -- 1
DATE_DIFF(year, `2010T`, `2010-05T`)                     -- 4 (2010T is equivalent to 2010-01-01T00:00:00.000Z)
DATE_DIFF(month, `2010T`, `2011T`)                       -- 12
DATE_DIFF(month, `2011T`, `2010T`)                       -- -12
DATE_DIFF(day, `2010-01-01T23:00`, `2010-01-02T01:00`) -- 0 (need to be at least 24h apart to be 1 day apart)
```

## EXTRACT


Given a date part and a timestamp, `EXTRACT` returns the timestamp's date part
 value.


### Syntax



```
EXTRACT( `date_part` FROM `timestamp` )
```

### Parameters





*``date_part``*


Specifies which part of the timestamps to extract. This can be one of the
 following:



* `YEAR`
* `MONTH`
* `DAY`
* `HOUR`
* `MINUTE`
* `SECOND`
* `TIMEZONE_HOUR`
* `TIMEZONE_MINUTE`



*``timestamp``*


The target timestamp that the function operates on.




### Examples



```
EXTRACT(YEAR FROM `2010-01-01T`)                           -- 2010
EXTRACT(MONTH FROM `2010T`)                                -- 1 (equivalent to 2010-01-01T00:00:00.000Z)
EXTRACT(MONTH FROM `2010-10T`)                             -- 10
EXTRACT(HOUR FROM `2017-01-02T03:04:05+07:08`)             -- 3
EXTRACT(MINUTE FROM `2017-01-02T03:04:05+07:08`)           -- 4
EXTRACT(TIMEZONE_HOUR FROM `2017-01-02T03:04:05+07:08`)    -- 7
EXTRACT(TIMEZONE_MINUTE FROM `2017-01-02T03:04:05+07:08`)  -- 8
```

## TO\_STRING


Given a timestamp and a format pattern, `TO_STRING` returns a string
 representation of the timestamp in the given format.


### Syntax



```
TO_STRING ( `timestamp` `time_format_pattern` )
```

### Parameters





*``timestamp``*


The target timestamp that the function operates on.




*``time_format_pattern``*


A string that has the following special character interpretations:




|  Format  |  Example  |  Description  |
| --- | --- | --- |
| `yy` | `69` | 2-digit year |
| `y` | `1969` | 4-digit year |
| `yyyy` | `1969` | Zero-padded 4-digit year |
| `M` | `1` | Month of year |
| `MM` | `01` | Zero-padded month of
 year |
| `MMM` | `Jan` | Abbreviated month year
 name |
| `MMMM` | `January` | Full month of year name |
| `MMMMM` | `J` | Month of year first letter (NOTE: This format is not valid for use with the
 `TO_TIMESTAMP` function.) |
| `d` | `2` | Day of month (1-31) |
| `dd` | `02` | Zero-padded day of month
 (01-31) |
| `a` | `AM` | AM or PM of day |
| `h` | `3` | Hour of day (1-12) |
| `hh` | `03` | Zero-padded hour of day
 (01-12) |
| `H` | `3` | Hour of day (0-23) |
| `HH` | `03` | Zero-padded hour of day
 (00-23) |
| `m` | `4` | Minute of hour (0-59) |
| `mm` | `04` | Zero-padded minute of hour
 (00-59) |
| `s` | `5` | Second of minute (0-59) |
| `ss` | `05` | Zero-padded second of minute
 (00-59) |
| `S` | `0` | Fraction of a second (precision: 0.1, range: 0.0-0.9) |
| `SS` | `6` | Fraction of a second (precision: 0.01, range: 0.0-0.99) |
| `SSS` | `60` | Fraction of a second (precision: 0.001, range: 0.0-0.999) |
| `…` | `…` | … |
| `SSSSSSSSS` | `60000000` | Fraction of a second (maximum precision: 1 nanosecond, range: 0.0-0.999999999) |
| `n` | `60000000` | Nano of a second |
| `X` | `+07` or `Z` | Offset in hours, or `Z` if the offset is 0 |
| `XX` or `XXXX` | `+0700` or `Z` | Offset in hours and minutes, or `Z` if the offset is 0 |
| `XXX` or `XXXXX` | `+07:00` or `Z` | Offset in hours and minutes, or `Z` if the offset is 0 |
| `x` | `7` | Offset in hours |
| `xx` or `xxxx` | `700` | Offset in hours and
 minutes |
| `xxx` or `xxxxx` | `+07:00` | Offset in hours and
 minutes |




### Examples



```
TO_STRING(`1969-07-20T20:18Z`,  'MMMM d, y')                    -- "July 20, 1969"
TO_STRING(`1969-07-20T20:18Z`, 'MMM d, yyyy')                   -- "Jul 20, 1969"
TO_STRING(`1969-07-20T20:18Z`, 'M-d-yy')                        -- "7-20-69"
TO_STRING(`1969-07-20T20:18Z`, 'MM-d-y')                        -- "07-20-1969"
TO_STRING(`1969-07-20T20:18Z`, 'MMMM d, y h:m a')               -- "July 20, 1969 8:18 PM"
TO_STRING(`1969-07-20T20:18Z`, 'y-MM-dd''T''H:m:ssX')           -- "1969-07-20T20:18:00Z"
TO_STRING(`1969-07-20T20:18+08:00Z`, 'y-MM-dd''T''H:m:ssX')     -- "1969-07-20T20:18:00Z"
TO_STRING(`1969-07-20T20:18+08:00`, 'y-MM-dd''T''H:m:ssXXXX')   -- "1969-07-20T20:18:00+0800"
TO_STRING(`1969-07-20T20:18+08:00`, 'y-MM-dd''T''H:m:ssXXXXX')  -- "1969-07-20T20:18:00+08:00"
```

## TO\_TIMESTAMP


Given a string, `TO_TIMESTAMP` converts it to a timestamp.
 `TO_TIMESTAMP` is the inverse operation of
 `TO_STRING`.


### Syntax



```
TO_TIMESTAMP ( `string` )
```

### Parameters





*``string``*


The target string that the function operates on.




### Examples



```
TO_TIMESTAMP('2007T')                         -- `2007T`
TO_TIMESTAMP('2007-02-23T12:14:33.079-08:00') -- `2007-02-23T12:14:33.079-08:00`
```

## UTCNOW


`UTCNOW` returns the current time in UTC as a timestamp.


### Syntax



```
UTCNOW()
```

### Parameters


`UTCNOW` takes no parameters.


### Examples



```
UTCNOW() -- 2017-10-13T16:02:11.123Z
```
