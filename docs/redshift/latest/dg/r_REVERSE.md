

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# REVERSE function
<a name="r_REVERSE"></a>

The REVERSE function operates on a string and returns the characters in reverse order. For example, `reverse('abcde')` returns `edcba`. This function works on numeric and date data types as well as character data types; however, in most cases it has practical value for character strings. 

## Syntax
<a name="r_REVERSE-synopsis"></a>

```
REVERSE( expression )
```

## Argument
<a name="r_REVERSE-argument"></a>

 *expression*   
An expression with a character, date, timestamp, or numeric data type that represents the target of the character reversal. All expressions are implicitly converted to `VARCHAR` strings. Trailing blanks in `CHAR` strings are ignored. 

## Return type
<a name="r_REVERSE-return-type"></a>

VARCHAR

## Examples
<a name="r_REVERSE-examples"></a>

The following examples use data from the USERS and SALES tables in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To select five distinct city names and their corresponding reversed names from the USERS table, use the following example. 

```
SELECT DISTINCT city AS cityname, REVERSE(cityname)
FROM users 
ORDER BY city LIMIT 5;

+----------+----------+
| cityname | reverse  |
+----------+----------+
| Aberdeen | needrebA |
| Abilene  | enelibA  |
| Ada      | adA      |
| Agat     | tagA     |
| Agawam   | mawagA   |
+----------+----------+
```

To select five sales IDs and their corresponding reversed IDs cast as character strings, use the following example. 

```
SELECT salesid, REVERSE(salesid)
FROM sales 
ORDER BY salesid DESC LIMIT 5;

+---------+---------+
| salesid | reverse |
+---------+---------+
|  172456 |  654271 |
|  172455 |  554271 |
|  172454 |  454271 |
|  172453 |  354271 |
|  172452 |  254271 |
+---------+---------+
```