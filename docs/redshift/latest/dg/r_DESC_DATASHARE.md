

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DESC DATASHARE
<a name="r_DESC_DATASHARE"></a>

Displays a list of the database objects within a datashare that are added to it using ALTER DATASHARE. Amazon Redshift displays the names, databases, schemas, and types of tables, views, and functions. 

Additional information about datashare objects can be found by using system views. For more information, see [SVV\_DATASHARE\_OBJECTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARE_OBJECTS.html) and [SVV\_DATASHARES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARES.html).

## Syntax
<a name="r_DESC_DATASHARE-synopsis"></a>

```
DESC DATASHARE datashare_name [ OF [ ACCOUNT account_id ] NAMESPACE namespace_guid ]
```

## Parameters
<a name="r_DESC_DATASHARE-parameters"></a>

 *datashare\_name*   
The name of the datashare . 

NAMESPACE *namespace\_guid*   
A value that specifies the namespace that the datashare uses. When you run DESC DATAHSARE as a consumer cluster administrator, specify the NAMESPACE parameter to view inbound datashares.

ACCOUNT *account\_id*  
A value that specifies the account that the datashare belongs to.

## Usage Notes
<a name="r_DESC_DATASHARE-usage"></a>

As a consumer account administrator, when you run DESC DATASHARE to see inbound datashares within the AWS account, specify the NAMESPACE option. When you run DESC DATASHARE to see inbound datashares across AWS accounts, specify the ACCOUNT and NAMESPACE options.

## Examples
<a name="r_DESC_DATASHARE-examples"></a>

The following example displays the information for outbound datashares on a producer cluster.

```
DESC DATASHARE salesshare;

producer_account |          producer_namespace           | share_type  | share_name   | object_type |        object_name           |  include_new
-----------------+---------------------------------------+-------------+--------------+-------------+------------------------------+--------------
 123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d  | OUTBOUND    |  salesshare  | TABLE       | public.tickit_sales_redshift |
 123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d  | OUTBOUND    |  salesshare  | SCHEMA      | public                       |   t
```

The following example displays the information for inbound datashares on a consumer cluster.

```
DESC DATASHARE salesshare of ACCOUNT '123456789012' NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';

 producer_account |          producer_namespace          | share_type | share_name | object_type |         object_name          |  include_new
------------------+--------------------------------------+------------+------------+-------------+------------------------------+--------------
 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_sales_redshift |
 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | schema      | public                       |
(2 rows)
```