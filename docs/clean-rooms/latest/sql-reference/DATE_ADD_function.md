

# DATE\_ADD function
<a name="DATE_ADD_function"></a>

Returns the date that is num\_days after start\_date. 

## Syntax
<a name="DATE_ADD_function-synopsis"></a>

```
date_add(start_date, num_days) 
```

## Arguments
<a name="DATE_ADD_function-arguments"></a>

 *start\_date*   
The starting date value.

 *num\_days*   
The number of days to add (integer). A positive number adds days, a negative number subtracts days.

## Return type
<a name="DATE_ADD_function-return-type"></a>

DATE

## Examples
<a name="DATE_ADD_function-examples"></a>

The following example adds one day to a date: 

```
SELECT date_add('2016-07-30', 1);

Result:
2016-07-31
```

The following example adds multiple days.

```
SELECT date_add('2016-07-30', 5);

Result:
2016-08-04
```

## Usage notes
<a name="DATE_ADD_usage_notes"></a>

This documentation is for Spark SQL's DATE\_ADD function, which provides a simpler interface for adding days to dates compared to some other SQL variants. For adding other intervals like months or years, different functions may be required.