

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# \|\| (Concatenation) operator
<a name="r_concat_op"></a>

Concatenates two expressions on either side of the `||` symbol and returns the concatenated expression. 

Similar to [CONCAT function](r_CONCAT.md). 

**Note**  
If one or both of the expressions is null, the result of the concatenation is `NULL`. 

## Syntax
<a name="r_concat_op-synopsis"></a>

```
expression1 || expression2
```

## Arguments
<a name="r_concat_op-arguments"></a>

 *expression1*   
A `CHAR` string, a `VARCHAR` string, a binary expression, or an expression that evaluates to one of these types. 

 *expression2*   
A `CHAR` string, a `VARCHAR` string, a binary expression, or an expression that evaluates to one of these types. 

## Return type
<a name="r_concat_op-return-type"></a>

 The return type of the string is the same as the type of the input arguments. For example, concatenating two strings of type `VARCHAR` returns a string of type `VARCHAR`.

## Examples
<a name="r_concat_op-example"></a>

 The following examples use the USERS and VENUE tables from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To concatenate the FIRSTNAME and LASTNAME fields from the USERS table in the sample database, use the following example.

```
SELECT (firstname || ' ' || lastname) as fullname
FROM users
ORDER BY 1
LIMIT 10;

+-----------------+
|    fullname     |
+-----------------+
| Aaron Banks     |
| Aaron Booth     |
| Aaron Browning  |
| Aaron Burnett   |
| Aaron Casey     |
| Aaron Cash      |
| Aaron Castro    |
| Aaron Dickerson |
| Aaron Dixon     |
| Aaron Dotson    |
+-----------------+
```

 To concatenate columns that might contain nulls, use the [NVL and COALESCE functions](r_NVL_function.md) expression. The following example uses NVL to return a `0` whenever `NULL` is encountered. 

```
SELECT (venuename || ' seats ' || NVL(venueseats, 0)) as seating
FROM venue
WHERE venuestate = 'NV' or venuestate = 'NC'
ORDER BY 1
LIMIT 10;

+-------------------------------------+
|               seating               |
+-------------------------------------+
| Ballys Hotel seats 0                |
| Bank of America Stadium seats 73298 |
| Bellagio Hotel seats 0              |
| Caesars Palace seats 0              |
| Harrahs Hotel seats 0               |
| Hilton Hotel seats 0                |
| Luxor Hotel seats 0                 |
| Mandalay Bay Hotel seats 0          |
| Mirage Hotel seats 0                |
| New York New York seats 0           |
+-------------------------------------+
```