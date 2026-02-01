Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Working with

Lake Formation-managed datashares as a producer

With Amazon Redshift, you can access and analyze data shared through AWS Lake Formation datashares.
AWS Lake Formation datashares enable secure data sharing across AWS accounts and Amazon Redshift
clusters without having to copy or move the underlying data.

Sharing data to AWS Lake Formation lets you centrally define AWS Lake Formation permissions of
Amazon Redshift datashares and restrict user access to objects within a datashare.

With Amazon Redshift, you can securely share live data across AWS accounts and Amazon Redshift
clusters using AWS Lake Formation-managed datashares as a producer. A Lake Formation-managed datashare
is an object that allows you to share live data from your Amazon Redshift cluster with other
AWS accounts and services.

As a producer cluster or workgroup administrator, follow these steps to share
datashares to Lake Formation:

1. Create datashares in your cluster and authorize AWS Lake Formation to access the
   datashares.

Only cluster superuser and database owners can create datashares. Each
datashare is associated with a database during creation. Only objects from
that database can be shared in that datashare. Multiple datashares can be
created on the same database with the same or different granularity of
objects. There is no limit on the number of datashares you can create on a
cluster.

```
CREATE DATASHARE salesshare;
```

2. Add objects to the datashare. The producer cluster or workgroup
   administrator continues to manage datashare objects that are available. To
   add objects to a datashare, add the schema before adding objects. When you
   add a schema, Amazon Redshift doesn't add all the objects under it. You must add
   them explicitly. For more information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

```
`ALTER DATASHARE salesshare ADD SCHEMA PUBLIC;
ALTER DATASHARE salesshare ADD TABLE public.tickit_sales_redshift;
ALTER DATASHARE salesshare ADD ALL TABLES IN SCHEMA PUBLIC;`

```

You can also add views to a datashare. Supported views are standard
views, late binding views, and materialized views.

```
`CREATE VIEW public.sales_data_summary_view AS SELECT * FROM public.tickit_sales_redshift;
ALTER DATASHARE salesshare ADD TABLE public.tickit_sales_redshift;`

```

Use ALTER DATASHARE to share schemas, tables, and views, in a given
schema. Superusers, datashare owners, or users who have ALTER or ALL
permissions on the datashare can alter the datashare to add objects to or
remove objects from it. Database users should be the owners of the objects
or have SELECT, USAGE, or ALL permissions on the objects.

Use the INCLUDENEW clause to add any new tables and views created in a
specified schema to the datashare. Only superusers can change this property
for each datashare-schema pair.

```
`ALTER DATASHARE salesshare ADD SCHEMA PUBLIC;
ALTER DATASHARE salesshare SET INCLUDENEW = TRUE FOR SCHEMA PUBLIC;`

```

3. Grant access of the datashare to a Lake Formation administrator account.

```
`GRANT USAGE ON DATASHARE salesshare TO ACCOUNT '012345678910' VIA DATA CATALOG;`
```

To revoke usage, use the following command.

```
`REVOKE USAGE ON DATASHARE salesshare FROM ACCOUNT '012345678910' VIA DATA CATALOG;`
```

4. Authorize access to the datashare for Lake Formation by using the `aws
redshift authorize-data-share` API operation. Doing so lets Lake Formation
   recognize the datashare in the service account and manage associating
   consumers to the datashare.

```
aws redshift authorize-data-share
--data-share-arn arn:aws:redshift:us-east-1:{PRODUCER_ACCOUNT}:datashare:{PRODUCER_CLUSTER_NAMESPACE}/salesshare
--consumer-identifier {"DataCatalog/<consumer-account-id>"}

```

To remove authorization from Lake Formation-managed datashares, use the `aws
 redshift deauthorize-data-share` API operation. By doing so, you
allow AWS Lake Formation to recognize the datashare in the service account and remove
authorization.

```
aws redshift deauthorize-data-share
--data-share-arn arn:aws:redshift:us-east-1:{PRODUCER_ACCOUNT}:datashare:{PRODUCER_CLUSTER_NAMESPACE}/salesshare
--consumer-identifier {"DataCatalog/<consumer-account-id>"}

```

At any time, if the producer cluster or workgroup administrator decides
that there is no longer a need to share data with the consumer cluster or
workgroup, they can use DROP DATASHARE to delete the datashare, deauthorize
the datashare, or revoke datashare permissions. The associated permissions
and objects in Lake Formation are not automatically deleted.

```
`DROP DATASHARE salesshare;`
```

After authorizing the Lake Formation account to manage the datashare, the Lake Formation
administrator can discover the shared datashare, associate the dateshare
with an Data Catalog ARN, and create a database in the AWS Glue Data Catalog linking to the
datashare. To associate datashares using the AWS CLI, use the command [associate-data-share-consumer](../../../cli/latest/reference/redshift/associate-data-share-consumer.md "../../../cli/latest/reference/redshift/associate-data-share-consumer.md"). To share a datashare across
AWS Regions, specify the `--region` parameter in the
`associate-data-share-consumer` command or use the AWS
console to choose your data consumers. The following example demonstrates
how to share a Lake Formation-managed datashare across Regions.

```
aws redshift associate-data-share-consumer --region <region-1>
--data-share-arn 'arn:aws:redshift:us-east-1:12345678912:datashare:035c45ea-61ce-86f0-8b75-19ac6102c3b7/sample_share'
--consumer-arn 'arn:aws:glue:<region-1>:111912345678:catalog'
```

The Lake Formation administrator must also create local resources that define how
objects within the datashare should map to objects within Lake Formation. For more
information about discovering datashares and creating local resources, see
[Managing
permissions for data in an Amazon Redshift datashare](../../../lake-formation/latest/dg/data-sharing-redshift.md "../../../lake-formation/latest/dg/data-sharing-redshift.md").
