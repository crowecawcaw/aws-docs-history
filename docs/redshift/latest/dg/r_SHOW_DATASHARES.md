Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW DATASHARES

Displays the inbound and outbound shares in a cluster either from the same account or
across accounts. If you don't specify a datashare name, then Amazon Redshift displays all
datashares in all databases in the cluster.
Users who have the
ALTER and SHARE privileges can see the shares that they have privileges for.

## Syntax

```
SHOW DATASHARES [ LIKE '*namepattern*' ]
```

## Parameters

LIKE

An optional clause that compares the specified name pattern to the
description of the datashare. When this clause is used, Amazon Redshift displays only
the datashares with names that match the specified name pattern.

_namepattern_

The name of the datashare requested or part of the name to be matched using
wildcard characters.

## Examples

The following example displays the inbound and outbound shares in a cluster.

```
SHOW DATASHARES;
SHOW DATASHARES LIKE 'sales%';

share_name   | share_owner | source_database | consumer_database | share_type | createdate          | is_publicaccessible | share_acl | producer_account |           producer_namespace
-------------+-------------+-----------------+-------------------+------------+---------------------+---------------------+-----------+------------------+---------------------------------------
'salesshare' | 100         | dev             |                   | outbound   | 2020-12-09 01:22:54.| False               |           |   123456789012   | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d
```
