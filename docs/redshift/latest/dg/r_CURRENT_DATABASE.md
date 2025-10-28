Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CURRENT_DATABASE

Returns the name of the database where you are currently connected.

## Syntax

```
current_database()
```

## Return type

Returns a CHAR or VARCHAR string.

## Example

The following query returns the name of the current database.

```
select current_database();

current_database
------------------
tickit
(1 row)
```
