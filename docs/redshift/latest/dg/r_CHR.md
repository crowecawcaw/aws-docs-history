

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CHR function
<a name="r_CHR"></a>

The CHR function returns the character that matches the ASCII code point value specified by the input parameter.

## Syntax
<a name="r_CHR-synopsis"></a>

```
CHR(number)
```

## Argument
<a name="r_CHR-argument"></a>

 *number*   
The input parameter is an `INTEGER` that represents an ASCII code point value.

## Return type
<a name="r_CHR-return-type"></a>

 CHAR   
The CHR function returns a `CHAR` string if an ASCII character matches the input value. If the input number has no ASCII match, the function returns `NULL`.

## Examples
<a name="r_CHR-example"></a>

To return the character that corresponds with ASCII code point 0, use the following example. Note that the CHR function returns `NULL` for the input `0`. 

```
SELECT CHR(0);

+-----+
| chr |
+-----+
|     |
+-----+
```

To return the character that corresponds with ASCII code point 65, use the following example.

```
SELECT CHR(65);

+-----+
| chr |
+-----+
| A   |
+-----+
```

To return distinct event names that begin with a capital A (ASCII code point 65), use the following example. The following example uses the EVENT table from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

```
SELECT DISTINCT eventname FROM event
WHERE SUBSTRING(eventname, 1, 1)=CHR(65) LIMIT 5;

+-----------------------+
|       eventname       |
+-----------------------+
| A Catered Affair      |
| As You Like It        |
| A Man For All Seasons |
| Alan Jackson          |
| Armando Manzanero     |
+-----------------------+
```