

# DATE\_PART function
<a name="DATE_PART_function"></a>

DATE\_PART extracts date part values from an expression. DATE\_PART is a synonym of the PGDATE\_PART function. 

## Syntax
<a name="DATE_PART_function-synopsis"></a>

```
datepart(field, source) 
```

## Arguments
<a name="DATE_PART_function-arguments"></a>

 *field*   
Which part of the source should be extracted, and supported string values are the same as the fields of the equivalent function EXTRACT.

*source*  
A DATE or INTERVAL column from where field should be extracted.

## Return type
<a name="DATE_PART_function-return-type"></a>

If *field* is 'SECOND', a DECIMAL(8, 6). In all other cases, an INTEGER.

## Example
<a name="DATE_PART_function-examples"></a>

The following example extracts the day of the year (DOY) from a date value. The output shows that the day of the year for the date "2019-08-12" is `224`. This means that August 12, 2019 is the 224th day of the year 2019.

```
SELECT datepart('doy', DATE'2019-08-12');
 224
```