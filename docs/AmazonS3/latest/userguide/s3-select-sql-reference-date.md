

# Date functions
<a name="s3-select-sql-reference-date"></a>

**Important**  
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/) 

Amazon S3 Select supports the following date functions.

**Topics**
+ [DATE\_ADD](#s3-select-sql-reference-date-add)
+ [DATE\_DIFF](#s3-select-sql-reference-date-diff)
+ [EXTRACT](#s3-select-sql-reference-extract)
+ [TO\_STRING](#s3-select-sql-reference-to-string)
+ [TO\_TIMESTAMP](#s3-select-sql-reference-to-timestamp)
+ [UTCNOW](#s3-select-sql-reference-utcnow)

## DATE\_ADD
<a name="s3-select-sql-reference-date-add"></a>

Given a date part, a quantity, and a timestamp, `DATE_ADD` returns an updated timestamp by altering the date part by the quantity.

### Syntax
<a name="s3-select-sql-reference-date-add-syntax"></a>

```
DATE_ADD( {{date_part}}, {{quantity}}, {{timestamp}} )
```

### Parameters
<a name="s3-select-sql-reference-date-add-parameters"></a>

*`{{date_part}}`*   
Specifies which part of the date to modify. This can be one of the following:  
+ year
+ month
+ day
+ hour
+ minute
+ second

 *`{{quantity}}`*   
The value to apply to the updated timestamp. Positive values for `{{quantity}}` add to the timestamp's date\_part, and negative values subtract.

 *`{{timestamp}}`*   
The target timestamp that the function operates on.

### Examples
<a name="s3-select-sql-reference-date-add-examples"></a>

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
<a name="s3-select-sql-reference-date-diff"></a>

Given a date part and two valid timestamps, `DATE_DIFF` returns the difference in date parts. The return value is a negative integer when the `{{date_part}}` value of `{{timestamp1}}` is greater than the `{{date_part}}` value of `{{timestamp2}}`. The return value is a positive integer when the `{{date_part}}` value of `{{timestamp1}}` is less than the `{{date_part}}` value of `{{timestamp2}}`.

### Syntax
<a name="s3-select-sql-reference-date-diff-syntax"></a>

```
DATE_DIFF( {{date_part}}, {{timestamp1}}, {{timestamp2}} )
```

### Parameters
<a name="s3-select-sql-reference-date-diff-parameters"></a>

 *{{`date_part`}}*   
Specifies which part of the timestamps to compare. For the definition of `date_part`, see [DATE\_ADD](#s3-select-sql-reference-date-add).

 *{{`timestamp1`}}*   
The first timestamp to compare.

 *{{`timestamp2`}}*   
The second timestamp to compare.

### Examples
<a name="s3-select-sql-reference-date-diff-examples"></a>

```
DATE_DIFF(year, `2010-01-01T`, `2011-01-01T`)            -- 1
DATE_DIFF(year, `2010T`, `2010-05T`)                     -- 4 (2010T is equivalent to 2010-01-01T00:00:00.000Z)
DATE_DIFF(month, `2010T`, `2011T`)                       -- 12
DATE_DIFF(month, `2011T`, `2010T`)                       -- -12
DATE_DIFF(day, `2010-01-01T23:00`, `2010-01-02T01:00`) -- 0 (need to be at least 24h apart to be 1 day apart)
```

## EXTRACT
<a name="s3-select-sql-reference-extract"></a>

Given a date part and a timestamp, `EXTRACT` returns the timestamp's date part value.

### Syntax
<a name="s3-select-sql-reference-extract-syntax"></a>

```
EXTRACT( {{date_part}} FROM {{timestamp}} )
```

### Parameters
<a name="s3-select-sql-reference-extract-parameters"></a>

 *{{`date_part`}}*   
Specifies which part of the timestamps to extract. This can be one of the following:  
+ `YEAR`
+ `MONTH`
+ `DAY`
+ `HOUR`
+ `MINUTE`
+ `SECOND`
+ `TIMEZONE_HOUR`
+ `TIMEZONE_MINUTE`

 *{{`timestamp`}}*   
The target timestamp that the function operates on.

### Examples
<a name="s3-select-sql-reference-extract-examples"></a>

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
<a name="s3-select-sql-reference-to-string"></a>

Given a timestamp and a format pattern, `TO_STRING` returns a string representation of the timestamp in the given format.

### Syntax
<a name="s3-select-sql-reference-size-syntax"></a>

```
TO_STRING ( {{timestamp}} {{time_format_pattern}} )
```

### Parameters
<a name="s3-select-sql-reference-size-parameters"></a>

 *`{{timestamp}}`*   
The target timestamp that the function operates on.

 *`{{time_format_pattern}}`*   
A string that has the following special character interpretations:  


<table>
<thead>
  <tr><th> Format </th><th> Example </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td><code>yy</code></td><td><code>69</code></td><td>2-digit year</td></tr>
  <tr><td><code>y</code></td><td><code>1969</code></td><td>4-digit year</td></tr>
  <tr><td><code>yyyy</code></td><td><code>1969</code></td><td>Zero-padded 4-digit year</td></tr>
  <tr><td><code>M</code></td><td><code>1</code></td><td>Month of year</td></tr>
  <tr><td><code>MM</code></td><td><code>01</code></td><td>Zero-padded month of year</td></tr>
  <tr><td><code>MMM</code></td><td><code>Jan</code></td><td>Abbreviated month year name</td></tr>
  <tr><td><code>MMMM</code></td><td><code>January</code></td><td>Full month of year name</td></tr>
  <tr><td><code>MMMMM</code></td><td><code>J</code></td><td>Month of year first letter (NOTE: This format is not valid for use with the <code>TO_TIMESTAMP</code> function.)</td></tr>
  <tr><td><code>d</code></td><td><code>2</code></td><td>Day of month (1-31)</td></tr>
  <tr><td><code>dd</code></td><td><code>02</code></td><td>Zero-padded day of month (01-31)</td></tr>
  <tr><td><code>a</code></td><td><code>AM</code></td><td>AM or PM of day</td></tr>
  <tr><td><code>h</code></td><td><code>3</code></td><td>Hour of day (1-12)</td></tr>
  <tr><td><code>hh</code></td><td><code>03</code></td><td>Zero-padded hour of day (01-12)</td></tr>
  <tr><td><code>H</code></td><td><code>3</code></td><td>Hour of day (0-23)</td></tr>
  <tr><td><code>HH</code></td><td><code>03</code></td><td>Zero-padded hour of day (00-23)</td></tr>
  <tr><td><code>m</code></td><td><code>4</code></td><td>Minute of hour (0-59)</td></tr>
  <tr><td><code>mm</code></td><td><code>04</code></td><td>Zero-padded minute of hour (00-59)</td></tr>
  <tr><td><code>s</code></td><td><code>5</code></td><td>Second of minute (0-59)</td></tr>
  <tr><td><code>ss</code></td><td><code>05</code></td><td>Zero-padded second of minute (00-59)</td></tr>
  <tr><td><code>S</code></td><td><code>0</code></td><td>Fraction of a second (precision: 0.1, range: 0.0-0.9)</td></tr>
  <tr><td><code>SS</code></td><td><code>6</code></td><td>Fraction of a second (precision: 0.01, range: 0.0-0.99)</td></tr>
  <tr><td><code>SSS</code></td><td><code>60</code></td><td>Fraction of a second (precision: 0.001, range: 0.0-0.999)</td></tr>
  <tr><td><code>…</code></td><td><code>…</code></td><td>…</td></tr>
  <tr><td><code>SSSSSSSSS</code></td><td><code>60000000</code></td><td>Fraction of a second (maximum precision: 1 nanosecond, range: 0.0-0.999999999)</td></tr>
  <tr><td><code>n</code></td><td><code>60000000</code></td><td>Nano of a second</td></tr>
  <tr><td><code>X</code></td><td><code>+07</code> or <code>Z</code></td><td>Offset in hours, or <code>Z</code> if the offset is 0</td></tr>
  <tr><td><code>XX</code> or <code>XXXX</code></td><td><code>+0700</code> or <code>Z</code></td><td>Offset in hours and minutes, or <code>Z</code> if the offset is 0</td></tr>
  <tr><td><code>XXX</code> or <code>XXXXX</code></td><td><code>+07:00</code> or <code>Z</code></td><td>Offset in hours and minutes, or <code>Z</code> if the offset is 0</td></tr>
  <tr><td><code>x</code></td><td><code>7</code></td><td>Offset in hours</td></tr>
  <tr><td><code>xx</code> or <code>xxxx</code></td><td><code>700</code></td><td>Offset in hours and minutes</td></tr>
  <tr><td><code>xxx</code> or <code>xxxxx</code></td><td><code>+07:00</code></td><td>Offset in hours and minutes</td></tr>
</tbody>
</table>


### Examples
<a name="s3-select-sql-reference-size-examples"></a>

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
<a name="s3-select-sql-reference-to-timestamp"></a>

Given a string, `TO_TIMESTAMP` converts it to a timestamp. `TO_TIMESTAMP` is the inverse operation of `TO_STRING`.

### Syntax
<a name="s3-select-sql-reference-to-timestamp-syntax"></a>

```
TO_TIMESTAMP ( {{string}} )
```

### Parameters
<a name="s3-select-sql-reference-to-timestamp-parameters"></a>

 *`{{string}}`*   
The target string that the function operates on.

### Examples
<a name="s3-select-sql-reference-to-timestamp-examples"></a>

```
TO_TIMESTAMP('2007T')                         -- `2007T`
TO_TIMESTAMP('2007-02-23T12:14:33.079-08:00') -- `2007-02-23T12:14:33.079-08:00`
```

## UTCNOW
<a name="s3-select-sql-reference-utcnow"></a>

`UTCNOW` returns the current time in UTC as a timestamp.

### Syntax
<a name="s3-select-sql-reference-utcnow-syntax"></a>

```
UTCNOW()
```

### Parameters
<a name="s3-select-sql-reference-utcnow-parameters"></a>

`UTCNOW` takes no parameters.

### Examples
<a name="s3-select-sql-reference-utcnow-examples"></a>

```
UTCNOW() -- 2017-10-13T16:02:11.123Z
```