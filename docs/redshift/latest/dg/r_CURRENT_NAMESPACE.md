Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CURRENT_NAMESPACE

Returns the cluster namespace of the current Amazon Redshift cluster. Amazon Redshift cluster namespace is the unique ID of the Amazon Redshift cluster.

## Syntax

```
current_namespace
```

## Return type

Returns a CHAR or VARCHAR string.

## Example

The following query returns the name of the current namespace.

```
select user, current_namespace;
current_user | current_namespace
-------------+-------------------------------------
dwuser       | 86b5169f-01dc-4a6f-9fbb-e2e24359e9a8

(1 row)
```
