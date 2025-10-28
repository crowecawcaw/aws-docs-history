Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing a datashare in Amazon Redshift

You can view datashares from the console or with SQL.

Console
You can view datashares from the **Datashares** or
**Clusters** tab.

- Use the **Datashares** tab to list datashares
  in your account or from other accounts.
  - To view datashares created in your account, choose
    **In my account**, then choose the
    datashare you want to view.
  - To view datashares that are shared from other accounts,
    choose **From other accounts**, then choose
    the datashare you want to view.

- Use the **Clusters** tab to list datashares in
  your cluster or from other clusters.

First, connect to a database. Then, choose a datashare either
from the **Datashares from other clusters** or
**Datashares created in my cluster** section to
view its details.

SQL
You can list datashares created in the cluster and look into the
contents of the datashare.

The following example displays the information of a datashare named
`salesshare`.

```
DESC DATASHARE salesshare;

 producer_account  |          producer_namespace          | share_type | share_name | object_type |           object_name          |   include_new
-------------------+--------------------------------------+------------+------------+-------------+--------------------------------+-------------------
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_users_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_venue_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_category_redshift|
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_date_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_event_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_listing_redshift |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_sales_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | schema      | public                         |  t
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | view        | public.sales_data_summary_view |
```

The following example displays the outbound datashares in a producer
cluster.

```
SHOW DATASHARES LIKE 'sales%';
```

The output looks similar to the following.

```
share_name | share_owner  | source_database | consumer_database | share_type |     createdate      | is_publicaccessible  | share_acl | producer_account |          producer_namespace
-----------+--------------+-----------------+-------------------+------------+---------------------+----------------------+-----------+------------------+---------------------------------------
salesshare |    100       | dev             |                   |  OUTBOUND  | 2020-12-09 02:27:08 |          True        |           |   123456789012   | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d
```

For more information, see [DESC DATASHARE](r_DESC_DATASHARE.md "r_DESC_DATASHARE.md") and [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

You can also use [SVV_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md"), [SVV_DATASHARE_CONSUMERS](r_SVV_DATASHARE_CONSUMERS.md "r_SVV_DATASHARE_CONSUMERS.md"), and [SVV_DATASHARE_OBJECTS](r_SVV_DATASHARE_OBJECTS.md "r_SVV_DATASHARE_OBJECTS.md") to view the datashares, the
objects within the datashare, and the datashare consumers.
