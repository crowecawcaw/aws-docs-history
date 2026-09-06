

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# UPPER function
<a name="r_UPPER"></a>

Converts a string to uppercase. UPPER supports UTF-8 multibyte characters, up to a maximum of four bytes per character.

## Syntax
<a name="r_UPPER-synopsis"></a>

```
UPPER(string)
```

## Arguments
<a name="r_UPPER-arguments"></a>

 *string*   
The input parameter is a `VARCHAR` string or any other data type, such as `CHAR`, that can be implicitly converted to `VARCHAR`. 

## Return type
<a name="r_UPPER-return-type"></a>

The UPPER function returns a character string that is the same data type as the input string. For example, the function will return a `VARCHAR` string if the input is a `VARCHAR` string.

## Examples
<a name="r_UPPER-examples"></a>

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To convert the CATNAME field to uppercase, use the following. 

```
SELECT catname, UPPER(catname) 
FROM category 
ORDER BY 1,2;

+-----------+-----------+
|  catname  |   upper   |
+-----------+-----------+
| Classical | CLASSICAL |
| Jazz      | JAZZ      |
| MLB       | MLB       |
| MLS       | MLS       |
| Musicals  | MUSICALS  |
| NBA       | NBA       |
| NFL       | NFL       |
| NHL       | NHL       |
| Opera     | OPERA     |
| Plays     | PLAYS     |
| Pop       | POP       |
+-----------+-----------+
```