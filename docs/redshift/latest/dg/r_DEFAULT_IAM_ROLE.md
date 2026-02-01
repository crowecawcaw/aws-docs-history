Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DEFAULT_IAM_ROLE

Returns the default IAM role currently associated with the Amazon Redshift cluster. The
function returns none if there isn't any default IAM role associated.

## Syntax

```
select default_iam_role();
```

## Return type

Returns a VARCHAR string.

## Example

The following example returns the default IAM role currently associated with the
specified Amazon Redshift cluster,

```
select default_iam_role();
              default_iam_role
-----------------------------------------------
 arn:aws:iam::123456789012:role/myRedshiftRole
(1 row)
```
