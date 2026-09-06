

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# REGEXP\_REPLACE function
<a name="REGEXP_REPLACE"></a>

Searches a string for a regular expression pattern and replaces every occurrence of the pattern with the specified string. REGEXP\_REPLACE is similar to the [REPLACE function](r_REPLACE.md), but with REGEXP\_REPLACE, you can search a string for a regular expression pattern. For more information about regular expressions, see [POSIX operators](pattern-matching-conditions-posix.md) and [Regular expression](https://en.wikipedia.org/wiki/Regular_expression) in Wikipedia.

REGEXP\_REPLACE is similar to the [TRANSLATE function](r_TRANSLATE.md) and the [REPLACE function](r_REPLACE.md), except that TRANSLATE makes multiple single-character substitutions and REPLACE substitutes one entire string with another string, while with REGEXP\_REPLACE, you can search a string for a regular expression pattern.

## Syntax
<a name="REGEXP_REPLACE-synopsis"></a>

```
REGEXP_REPLACE( source_string, pattern [, replace_string [ , position [, parameters ] ] ] )
```

## Arguments
<a name="REGEXP_REPLACE-arguments"></a>

 *source\_string*   
A `CHAR` or `VARCHAR` string expression, such as a column name, to be searched. 

 *pattern*   
A UTF-8 string literal that represents a regular expression pattern. For more information, see [POSIX operators](pattern-matching-conditions-posix.md).

*replace\_string*  
(Optional) A `CHAR` or `VARCHAR` string expression, such as a column name, that will replace each occurrence of pattern. The default is an empty string ( "" ). 

 *position*   
(Optional) A positive integer that indicates the position within *source\_string* to begin searching. The position is based on the number of characters, not bytes, so that multibyte characters are counted as single characters. The default is `1`. If *position* is less than `1`, the search begins at the first character of *source\_string*. If *position* is greater than the number of characters in *source\_string*, the result is *source\_string*.

 *parameters*   
(Optional) One or more string literals that indicate how the function matches the pattern. The possible values are the following:  
+ c – Perform case-sensitive matching. The default is to use case-sensitive matching.
+ i – Perform case-insensitive matching.
+ p – Interpret the pattern with Perl Compatible Regular Expression (PCRE) dialect. For more information about PCRE, see [Perl Compatible Regular Expressions](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) in Wikipedia.

## Return type
<a name="REGEXP_REPLACE-return-type"></a>

VARCHAR

If either *pattern* or *replace\_string* is `NULL`, the function returns `NULL`.

## Examples
<a name="REGEXP_REPLACE-examples"></a>

To replace all occurrences of the string `FOX` within the value `quick brown fox` using case-insensitive matching, use the following example.

```
SELECT REGEXP_REPLACE('the fox', 'FOX', 'quick brown fox', 1, 'i');

+---------------------+
|   regexp_replace    |
+---------------------+
| the quick brown fox |
+---------------------+
```

The following example uses a pattern written in the PCRE dialect to locate words containing at least one number and one lowercase letter. It uses the `?=` operator, which has a specific look-ahead connotation in PCRE. To replace each occurrence of such a word with the value `[hidden]`, use the following example.

```
SELECT REGEXP_REPLACE('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'p');

+-------------------------------+
|        regexp_replace         |
+-------------------------------+
| [hidden] plain A1234 [hidden] |
+-------------------------------+
```

The following example uses a pattern written in the PCRE dialect to locate words containing at least one number and one lowercase letter. It uses the `?=` operator, which has a specific look-ahead connotation in PCRE. To replace each occurrence of such a word with the value `[hidden]`, but differs from the previous example in that it uses case-insensitive matching, use the following example.

```
SELECT REGEXP_REPLACE('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'ip');

+----------------------------------+
|          regexp_replace          |
+----------------------------------+
| [hidden] plain [hidden] [hidden] |
+----------------------------------+
```

The following examples use data from the USERS table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To delete the `@` and domain name from email addresses, use the following example.

```
SELECT email, REGEXP_REPLACE(email, '@.*\\.(org|gov|com|edu|ca)$')
FROM users
ORDER BY userid LIMIT 4;

+-----------------------------------------------+-----------------------+
|                     email                     |    regexp_replace     |
+-----------------------------------------------+-----------------------+
| Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero  |
| Suspendisse.tristique@nonnisiAenean.edu       | Suspendisse.tristique |
| amet.faucibus.ut@condimentumegetvolutpat.ca   | amet.faucibus.ut      |
| sed@lacusUtnec.ca                             | sed                   |
+-----------------------------------------------+-----------------------+
```

To replace the domain names of email addresses with `internal.company.com`, use the following example.

```
SELECT email, REGEXP_REPLACE(email, '@.*\\.[[:alpha:]]{2,3}','@internal.company.com') 
FROM users
ORDER BY userid LIMIT 4;

+-----------------------------------------------+--------------------------------------------+
|                     email                     |               regexp_replace               |
+-----------------------------------------------+--------------------------------------------+
| Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero@internal.company.com  |
| Suspendisse.tristique@nonnisiAenean.edu       | Suspendisse.tristique@internal.company.com |
| amet.faucibus.ut@condimentumegetvolutpat.ca   | amet.faucibus.ut@internal.company.com      |
| sed@lacusUtnec.ca                             | sed@internal.company.com                   |
+-----------------------------------------------+--------------------------------------------+
```