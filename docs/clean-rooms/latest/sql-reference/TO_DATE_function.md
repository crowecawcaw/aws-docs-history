

# TO\_DATE function
<a name="TO_DATE_function"></a>

TO\_DATE converts a date represented by a character string to a DATE data type. 

## Syntax
<a name="TO_DATE_function-synopsis"></a>

```
TO_DATE (date_str)
```

```
TO_DATE (date_str, format)
```

## Arguments
<a name="TO_DATE_function-arguments"></a>

 *date\_str*   
A date string or a data type that can be cast into a date string. 

 *format*   
A string literal that matches Spark's datetime patterns. For valid datetime patterns, see [Datetime Patterns for Formatting and Parsing](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html). 

## Return type
<a name="TO_DATE_function-return-type"></a>

TO\_DATE returns a DATE, depending on the *format* value. 

If the conversion to *format* fails, then an error is returned. 

## Examples
<a name="TO_DATE_function-example"></a>

 The following SQL statement converts the date `02 Oct 2001` into a date data type.

```
select to_date('02 Oct 2001', 'dd MMM yyyy');

to_date
------------
2001-10-02
(1 row)
```

 The following SQL statement converts the string `20010631` to a date.

```
select to_date('20010631', 'yyyyMMdd');
```

 The following SQL statement converts the string `20010631` to a date: 

```
to_date('20010631', 'YYYYMMDD', TRUE);
```

The result is a null value because there are only 30 days in June.

```
to_date
------------
NULL
```