Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Monitoring a query in a Multi-AZ

deployment

A Multi-AZ deployment uses compute resources that are deployed in both Availability
Zones and can continue operating in the event that the resources in a given Availability
Zone aren't available. All the compute resources will be used at all times. This
allows full operation across two Availability Zones in an active-active fashion for both
read and write operations.

You can query SYS\_ views in pg_catalog schema to monitor query runtime in a Multi-AZ
deployment. The SYS\_ views display query runtime activities or statistics from primary
and secondary clusters. For a list of monitoring views, see [Monitoring views](../dg/serverless-monitoring.md "../dg/serverless-monitoring.md").

Follow these steps to monitor query runtime for each Availability Zone within the
Multi-AZ deployment:

1. Navigate to the Amazon Redshift console and connect to the database in your Multi-AZ
   deployment and run queries through the query editor.
2. Run any sample query on the Multi-AZ Amazon Redshift deployment.
3. For a Multi-AZ deployment, you can identify a query and the Availability Zone
   where it is run by using the compute_type column in the SYS_QUERY_HISTORY table.
   _primary_ stands for queries run on the
   primary cluster in the Multi-AZ deployment, and _secondary_ stands for queries run on the secondary cluster in the
   Multi-AZ deployment.

The following query uses compute_type column to monitor a query.

```
select (compute_type) as compute_type, left(query_text, 50) query_text from sys_query_history order by start_time desc;

 compute_type | query_text
--------------+-------------------------
   secondary  | select count(*) from t1;
```
