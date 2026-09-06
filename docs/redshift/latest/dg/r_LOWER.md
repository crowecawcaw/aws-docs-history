

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# LOWER function
<a name="r_LOWER"></a>

Converts a string to lowercase. LOWER supports UTF-8 multibyte characters, up to a maximum of four bytes per character.

## Syntax
<a name="r_LOWER-synopsis"></a>

```
LOWER(string)
```

## Argument
<a name="r_LOWER-argument"></a>

 *string*   
A `VARCHAR` string or any expression that evaluates to the `VARCHAR` type.

## Return type
<a name="r_LOWER-return-type"></a>

 string   
The LOWER function returns a string that is the same data type as the input string. For example, if the input is a `CHAR` string, the function will return a `CHAR` string.

## Examples
<a name="r_LOWER-examples"></a>

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To convert the `VARCHAR` strings in the CATNAME column to lowercase, use the following example. 

```
SELECT catname, LOWER(catname) FROM category ORDER BY 1,2;

+-----------+-----------+
|  catname  |   lower   |
+-----------+-----------+
| Classical | classical |
| Jazz      | jazz      |
| MLB       | mlb       |
| MLS       | mls       |
| Musicals  | musicals  |
| NBA       | nba       |
| NFL       | nfl       |
| NHL       | nhl       |
| Opera     | opera     |
| Plays     | plays     |
| Pop       | pop       |
+-----------+-----------+
```