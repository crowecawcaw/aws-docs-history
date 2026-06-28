Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DB\_COLLATION

Returns the collation setting of the current database.

## Syntax

```
db_collation()
```

## Return type

Returns a VARCHAR string representing the collation of the current database. Possible values are `case_sensitive` or `case_insensitive`.

## Example

The following example returns the collation of the current database.

```
select db_collation();

db_collation
----------------
case_sensitive
(1 row)
```
