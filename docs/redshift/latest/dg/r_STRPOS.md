

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STRPOS function
<a name="r_STRPOS"></a>

Returns the position of a substring within a specified string. 

See [CHARINDEX function](r_CHARINDEX.md) and [POSITION function](r_POSITION.md) for similar functions.

## Syntax
<a name="r_STRPOS-synopsis"></a>

```
STRPOS(string, substring )
```

## Arguments
<a name="r_STRPOS-arguments"></a>

 *string*   
The first input parameter is the `CHAR` or `VARCHAR` string to be searched. 

 *substring*   
The second parameter is the substring to search for within the *string*. 

## Return type
<a name="r_STRPOS-return-type"></a>

INTEGER  
The STRPOS function returns an `INTEGER` corresponding to the position of the *substring* (one-based, not zero-based). The position is based on the number of characters, not bytes, so that multi-byte characters are counted as single characters.

## Usage notes
<a name="r_STRPOS_usage_notes"></a>

STRPOS returns `0` if the *substring* is not found within the *string*. 

```
SELECT STRPOS('dogfish', 'fist');

+--------+
| strpos |
+--------+
|      0 |
+--------+
```

## Examples
<a name="r_STRPOS-examples"></a>

To show the position of `fish` within `dogfish`, use the following example. 

```
SELECT STRPOS('dogfish', 'fish');

+--------+
| strpos |
+--------+
|      4 |
+--------+
```

The following example uses data from the SALES table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To return the number of sales transactions with a COMMISSION over 999.00 from the SALES table, use the following example. 

```
SELECT DISTINCT STRPOS(commission, '.'),
COUNT (STRPOS(commission, '.'))
FROM sales
WHERE STRPOS(commission, '.') > 4
GROUP BY STRPOS(commission, '.')
ORDER BY 1, 2;

+--------+-------+
| strpos | count |
+--------+-------+
|      5 |   629 |
+--------+-------+
```