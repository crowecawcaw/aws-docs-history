

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TRANSLATE function
<a name="r_TRANSLATE"></a>

For a given expression, replaces all occurrences of specified characters with specified substitutes. Existing characters are mapped to replacement characters by their positions in the *characters\_to\_replace* and *characters\_to\_substitute* arguments. If more characters are specified in the *characters\_to\_replace* argument than in the *characters\_to\_substitute* argument, the extra characters from the *characters\_to\_replace* argument are omitted in the return value.

TRANSLATE is similar to the [REPLACE function](r_REPLACE.md) and the [REGEXP\_REPLACE function](REGEXP_REPLACE.md), except that REPLACE substitutes one entire string with another string and with REGEXP\_REPLACE, you can search a string for a regular expression pattern, while TRANSLATE makes multiple single-character substitutions.

If any argument is null, the return is `NULL`.

## Syntax
<a name="r_TRANSLATE-synopsis"></a>

```
TRANSLATE( expression, characters_to_replace, characters_to_substitute )
```

## Arguments
<a name="r_TRANSLATE-arguments"></a>

 *expression*   
The expression to be translated.

 *characters\_to\_replace*   
A string containing the characters to be replaced.

 *characters\_to\_substitute*   
A string containing the characters to substitute.

## Return type
<a name="r_TRANSLATE-return-type"></a>

VARCHAR

## Examples
<a name="r_TRANSLATE-examples"></a>

To replace several characters in a string, use the following example. 

```
SELECT TRANSLATE('mint tea', 'inea', 'osin');

+-----------+
| translate |
+-----------+
| most tin  |
+-----------+
```

The following examples use data from the USERS table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To replace the at sign (@) with a period for all values in a column, use the following example. 

```
SELECT email, TRANSLATE(email, '@', '.') as obfuscated_email
FROM users LIMIT 10;

+---------------------------------------+---------------------------------------+
|                 email                 |           obfuscated_email            |
+---------------------------------------+---------------------------------------+
| Cum@accumsan.com                      | Cum.accumsan.com                      |
| lorem.ipsum@Vestibulumante.com        | lorem.ipsum.Vestibulumante.com        |
| non.justo.Proin@ametconsectetuer.edu  | non.justo.Proin.ametconsectetuer.edu  |
| non.ante.bibendum@porttitortellus.org | non.ante.bibendum.porttitortellus.org |
| eros@blanditatnisi.org                | eros.blanditatnisi.org                |
| augue@Donec.ca                        | augue.Donec.ca                        |
| cursus@pedeacurna.edu                 | cursus.pedeacurna.edu                 |
| at@Duis.com                           | at.Duis.com                           |
| quam@facilisisvitaeorci.ca            | quam.facilisisvitaeorci.ca            |
| mi.lorem@nunc.edu                     | mi.lorem.nunc.edu                     |
+---------------------------------------+---------------------------------------+
```

 To replace spaces with underscores and strips out periods for all values in a column, use the following example. 

```
SELECT city, TRANSLATE(city, ' .', '_') 
FROM users
WHERE city LIKE 'Sain%' OR city LIKE 'St%'
GROUP BY city
ORDER BY city;

+----------------+---------------+
|      city      |   translate   |
+----------------+---------------+
| Saint Albans   | Saint_Albans  |
| Saint Cloud    | Saint_Cloud   |
| Saint Joseph   | Saint_Joseph  |
| Saint Louis    | Saint_Louis   |
| Saint Paul     | Saint_Paul    |
| St. George     | St_George     |
| St. Marys      | St_Marys      |
| St. Petersburg | St_Petersburg |
| Stafford       | Stafford      |
| Stamford       | Stamford      |
| Stanton        | Stanton       |
| Starkville     | Starkville    |
| Statesboro     | Statesboro    |
| Staunton       | Staunton      |
| Steubenville   | Steubenville  |
| Stevens Point  | Stevens_Point |
| Stillwater     | Stillwater    |
| Stockton       | Stockton      |
| Sturgis        | Sturgis       |
+----------------+---------------+
```