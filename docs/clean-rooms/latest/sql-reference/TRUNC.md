

# TRUNC function

The TRUNC function truncates a date to the first day of the date part that you specify, such as the month or year, and returns a value of type DATE.

**Note**  
TRUNC is different from [DATE\_TRUNC](DATE_TRUNC.md). TRUNC takes the date first and the format second and returns a DATE. DATE\_TRUNC takes the format first and a datetime value second and returns a timestamp.

## Syntax
<a name="TRUNC-synopsis"></a>

```
TRUNC(date, format)
```

## Arguments
<a name="TRUNC-arguments"></a>

 *date*   
A DATE or TIMESTAMP column, or a string that represents a date, such as `'2024-03-15'`. TRUNC truncates a TIMESTAMP to a DATE.

 *format*   
A string that specifies the date part to truncate to. AWS Clean Rooms Spark SQL supports the following formats:  
+ `YEAR` (also `YYYY` or `YY`) - the first day of the year
+ `QUARTER` - the first day of the quarter
+ `MONTH` (also `MM` or `MON`) - the first day of the month
+ `WEEK` - the Monday of the week

## Return type
<a name="TRUNC-return-type"></a>

TRUNC returns a DATE.

## Usage notes
<a name="TRUNC-usage-notes"></a>

TRUNC requires both a date and a format. The numeric form `TRUNC(number, decimal_places)` returns the error `An argument passed to function 'trunc' has an unsupported data type`. The single-argument form `TRUNC(date)` returns the error `Invalid number of arguments`.

TRUNC supports only the WEEK, MONTH, QUARTER, and YEAR formats and their aliases. With any other format, such as `DAY` or `HOUR`, TRUNC returns NULL instead of an error.

## Examples
<a name="TRUNC-examples"></a>

The `impressions` table has `event_date` values of `2024-03-01`, `2024-03-15`, and `2024-03-20`. The following example truncates each date to the first day of its month.

```
SELECT TRUNC(event_date, 'MONTH') AS month_start
FROM impressions;

month_start
-----------
2024-03-01
2024-03-01
2024-03-01
```

The following example truncates the same dates to the first day of their year.

```
SELECT TRUNC(event_date, 'YEAR') AS year_start
FROM impressions;

year_start
----------
2024-01-01
2024-01-01
2024-01-01
```