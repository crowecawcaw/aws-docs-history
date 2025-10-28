Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DESC DATASHARE

Displays a list of the database objects within a datashare that are added to it using
ALTER DATASHARE. Amazon Redshift displays the names, databases, schemas, and types of tables,
views, and functions.

Additional information about datashare objects can be found by using system views. For
more information, see [SVV_DATASHARE_OBJECTS](r_SVV_DATASHARE_OBJECTS.md "r_SVV_DATASHARE_OBJECTS.md") and [SVV_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md").

## Syntax

```
DESC DATASHARE *datashare\_name* [ OF [ ACCOUNT *account\_id* ] NAMESPACE *namespace\_guid* ]
```

## Parameters

_datashare_name_

The name of the datashare .

NAMESPACE _namespace_guid_

A value that specifies the namespace that the datashare uses. When you run
DESC DATAHSARE as a consumer cluster administrator, specify the NAMESPACE
parameter to view inbound datashares.

ACCOUNT _account_id_

A value that specifies the account that the datashare belongs to.

## Usage Notes

As a consumer account administrator, when you run DESC DATASHARE to see inbound
datashares within the AWS account, specify the NAMESPACE option. When you run DESC
DATASHARE to see inbound datashares across AWS accounts, specify the ACCOUNT and
NAMESPACE options.

## Examples

The following example displays the information for outbound datashares on a producer
cluster.

```
DESC DATASHARE salesshare;

producer_account |          producer_namespace           | share_type  | share_name   | object_type |        object_name           |  include_new
-----------------+---------------------------------------+-------------+--------------+-------------+------------------------------+--------------
 123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d  | OUTBOUND    |  salesshare  | TABLE       | public.tickit_sales_redshift |
 123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d  | OUTBOUND    |  salesshare  | SCHEMA      | public                       |   t
```

The following example displays the information for inbound datashares on a consumer
cluster.

```
DESC DATASHARE salesshare of ACCOUNT '123456789012' NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';

 producer_account |          producer_namespace          | share_type | share_name | object_type |         object_name          |  include_new
------------------+--------------------------------------+------------+------------+-------------+------------------------------+--------------
 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_sales_redshift |
 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | schema      | public                       |
(2 rows)
```
