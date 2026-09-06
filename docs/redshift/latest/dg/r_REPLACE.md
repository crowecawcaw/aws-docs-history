

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# REPLACE function
<a name="r_REPLACE"></a>

Replaces all occurrences of a set of characters within an existing string with other specified characters. 

REPLACE is similar to the [TRANSLATE function](r_TRANSLATE.md) and the [REGEXP\_REPLACE function](REGEXP_REPLACE.md), except that TRANSLATE makes multiple single-character substitutions and with REGEXP\_REPLACE, you can search a string for a regular expression pattern, while REPLACE substitutes one entire string with another string.

## Syntax
<a name="r_REPLACE-synopsis"></a>

```
REPLACE(string, old_chars, new_chars)
```

## Arguments
<a name="r_REPLACE-arguments"></a>

 *string*   
`CHAR` or `VARCHAR` string to be searched search 

 *old\_chars*   
`CHAR` or `VARCHAR` string to replace. 

 *new\_chars*   
New `CHAR` or `VARCHAR` string replacing the *old\_string*. 

## Return type
<a name="r_REPLACE-return-type"></a>

VARCHAR  
If either *old\_chars* or *new\_chars* is `NULL`, the return is `NULL`. 

## Examples
<a name="r_REPLACE-examples"></a>

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To convert the string `Shows` to `Theatre` in the CATGROUP field, use the following example. 

```
SELECT catid, catgroup, REPLACE(catgroup, 'Shows', 'Theatre')
FROM category
ORDER BY 1,2,3;

+-------+----------+----------+
| catid | catgroup | replace  |
+-------+----------+----------+
|     1 | Sports   | Sports   |
|     2 | Sports   | Sports   |
|     3 | Sports   | Sports   |
|     4 | Sports   | Sports   |
|     5 | Sports   | Sports   |
|     6 | Shows    | Theatre  |
|     7 | Shows    | Theatre  |
|     8 | Shows    | Theatre  |
|     9 | Concerts | Concerts |
|    10 | Concerts | Concerts |
|    11 | Concerts | Concerts |
+-------+----------+----------+
```