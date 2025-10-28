Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# VERSION

The VERSION function returns details about the currently installed release, with
specific Amazon Redshift version information at the end.

###### Note

This is a leader-node function. This function returns an error if it references a
user-created table, an STL or STV system table, or an SVV or SVL system view.

## Syntax

```
VERSION()
```

## Return type

Returns a CHAR or VARCHAR string.

## Examples

The following example shows the cluster version information of the current cluster:

```
select version();
```

```
 version
 ------------------------------------------------------------------------------------------------------------------------
 PostgreSQL 8.0.2 on i686-pc-linux-gnu, compiled by GCC gcc (GCC) 3.4.2 20041017 (Red Hat 3.4.2-6.fc3), Redshift 1.0.12103
```

Where `1.0.12103` is the cluster version number.

###### Note

To force your cluster to update to the latest cluster version, adjust your [maintenance
window](../mgmt/working-with-clusters.md#rs-maintenance-windows "../mgmt/working-with-clusters.md#rs-maintenance-windows").
