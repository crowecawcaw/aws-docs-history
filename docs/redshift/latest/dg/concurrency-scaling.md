Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Concurrency scaling

With the Concurrency Scaling feature, you can support thousands of concurrent
users and concurrent queries, with consistently fast query performance. When you turn on concurrency scaling, Amazon Redshift
automatically adds additional cluster
capacity to process an increase in both read and write queries. Users see the most
current data, whether the queries run on the main cluster or a concurrency-scaling cluster.

You can manage which queries are sent to the concurrency-scaling cluster by configuring WLM
queues. When you turn on concurrency scaling, eligible queries are sent to the
concurrency-scaling cluster instead of waiting in a queue.

You're charged for concurrency-scaling clusters only for the time they're
actively running queries. For more information about pricing, including how charges accrue and minimum charges, see [Concurrency Scaling pricing](https://aws.amazon.com/redshift/pricing/#Concurrency_Scaling_pricing "https://aws.amazon.com/redshift/pricing/#Concurrency_Scaling_pricing").

###### Topics

- [Concurrency scaling capabilities](#concurrency-scaling-capabilities "#concurrency-scaling-capabilities")
- [Limitations for concurrency scaling](#concurrency-scaling-limitations "#concurrency-scaling-limitations")
- [AWS Regions for concurrency
  scaling](#concurrency-scaling-regions "#concurrency-scaling-regions")
- [Concurrency scaling candidates](#concurrency-scaling-candidates "#concurrency-scaling-candidates")
- [Configuring concurrency scaling
  queues](#concurrency-scaling-queues "#concurrency-scaling-queues")
- [Monitoring concurrency scaling](#concurrency-scaling-monitoring "#concurrency-scaling-monitoring")
- [Concurrency scaling system
  views](#concurrency-scaling-monitoring-system-views "#concurrency-scaling-monitoring-system-views")

## Concurrency scaling capabilities

When you turn on concurrency scaling for a WLM queue, it works for read operations,
such as dashboard queries. It also works for commonly used write operations, such as
statements for data ingestion and processing.

### Concurrency scaling capabilities for write operations

Concurrency scaling supports frequently used write operations, such as extract, transform, and load (ETL) statements. Concurrency scaling for write operations is
especially useful when you want to maintain consistent response times when your cluster receives a large number of requests. It improves
throughput for write operations contending for resources on the main cluster.

Concurrency scaling supports COPY, INSERT, DELETE, UPDATE, CREATE TABLE AS
(CTAS), and VACUUM statements. Additionally, concurrency scaling supports manual refresh of
materialized views (MVs) and automatic vacuum operations. Other data-manipulation language (DML) statements and
data-definition language (DDL) statements aren't supported. When non-supported write
statements, such as CREATE without TABLE AS, are included in an explicit transaction
before the supported write statements, none of the write statements will run on
concurrency-scaling clusters.

When you accrue credit for concurrency scaling, this credit accrual applies to
both read and write operations.

## Limitations for concurrency scaling

The following are limitations for using Amazon Redshift concurrency scaling:

- It doesn't support queries on tables that use interleaved sort keys.
- It doesn't support queries on temporary tables.
- It doesn't support queries that access external resources that are
  protected by restrictive network or virtual private cloud (VPC)
  configurations.
- It doesn't support queries that contain Python user-defined functions
  (UDFs) and Lambda UDFs.
- It doesn't support queries that access system tables, PostgreSQL catalog
  tables, or no-backup tables.
- It doesn’t support COPY or UNLOAD queries that access an external resource when restrictive IAM policy permissions are in place. This includes permissions applied either to the
  resource, like an Amazon S3 bucket or DynamoDB table, or to the source. IAM sources can include the following:

      + `aws:sourceVpc` – A source VPC.
      + `aws:sourceVpce` – A source VPC endpoint.
      + `aws:sourceIp` – A source IP address.

  In some cases, you might need to remove permissions that restrict either the resource or the source, so that COPY and UNLOAD queries
  accessing the resource are sent to the concurrency-scaling cluster.

For more information about resource policies, see [Policy types](../../../IAM/latest/UserGuide/access_policies.md#access_policy-types "../../../IAM/latest/UserGuide/access_policies.md#access_policy-types") in the AWS Identity and Access Management user guide
and [Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md").

- Amazon Redshift concurrency scaling for write operations is not supported for most DDL operations, such as CREATE TABLE.
- It doesn't support ANALYZE for the COPY command.
- It doesn't support write operations on a target table where DISTSTYLE is set to ALL.
- It doesn't support COPY from the following file formats:
  - Parquet
  - ORC

- It doesn't support write operations on tables with identity columns.
- Amazon Redshift supports concurrency scaling for write operations on only Amazon Redshift RA3 nodes.
  Concurrency scaling for write operations isn't supported on other node types.

## AWS Regions for concurrency

scaling

With Amazon Redshift, you can use concurrency scaling to manage concurrent workload demands
across Redshift clusters. This topic details in which regions you can use concurrency
scaling with Amazon Redshift.

Concurrency scaling is available in these AWS Regions:

- US East (N. Virginia) Region (us-east-1)
- US East (Ohio) Region (us-east-2)
- US West (N. California) Region (us-west-1)
- US West (Oregon) Region (us-west-2)
- Africa (Cape Town) Region (af-south-1)
- Asia Pacific (Mumbai) Region (ap-south-1)
- Asia Pacific (Hyderabad) Region (ap-south-2)
- Asia Pacific (Seoul) Region (ap-northeast-2)
- Asia Pacific (Osaka) Region (ap-northeast-3)
- Asia Pacific (Singapore) Region (ap-southeast-1)
- Asia Pacific (Sydney) Region (ap-southeast-2)
- Asia Pacific (Jakarta) Region (ap-southeast-3)
- Asia Pacific (Malaysia) Region (ap-southeast-5)
- Asia Pacific (New Zealand) Region (ap-southeast-6)
- Asia Pacific (Thailand) Region (ap-southeast-7)
- Asia Pacific (Hong Kong) Region (ap-east-1)
- Asia Pacific (Taipei) Region (ap-east-2)
- Asia Pacific (Tokyo) Region (ap-northeast-1)
- Canada (Central) Region (ca-central-1)
- Canada West (Calgary) Region (ca-west-1)
- China (Beijing) Region (cn-north-1)
- China (Ningxia) Region (cn-northwest-1)
- Europe (Frankfurt) Region (eu-central-1)
- Europe (Ireland) Region (eu-west-1)
- Europe (London) Region (eu-west-2)
- Europe (Paris) Region (eu-west-3)
- Europe (Stockholm) Region (eu-north-1)
- Europe (Zurich) Region (eu-central-2)
- Europe (Milan) Region (eu-south-1)
- Europe (Spain) Region (eu-south-2)
- Israel (Tel Aviv) Region (il-central-1)
- Middle East (Bahrain) Region (me-south-1)
- Mexico (Central) Region (mx-central-1)
- South America (São Paulo) Region (sa-east-1)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)

## Concurrency scaling candidates

With Amazon Redshift, you can scale out query processing to accelerate execution of concurrent queries.
The following topic describes the criteria that Amazon Redshift uses to determine what queries to route to concurrency scaling.

Queries are routed to the concurrency scaling cluster only when the main cluster
meets the following requirements:

- EC2-VPC platform.
- Node type must be dc2.8xlarge, dc2.large, ra3.large, ra3.xlplus, ra3.4xlarge, or ra3.16xlarge. Concurrency scaling for write
  operations is supported on only Amazon Redshift RA3 nodes.
- Maximum of 32 compute nodes for clusters with ra3.xlplus, ra3.4xlarge, or ra3.16xlarge node types.
  In addition, the number of nodes of the main cluster can't be larger than 32 nodes when the cluster was originally created.
  For example, even if a cluster currently has 20 nodes, but was originally created with 40, it does not meet the requirements for concurrency scaling.
  Conversely, if a DC2 cluster currently has 40 nodes, but was originally created with 20, it does meet the requirements for concurrency scaling.
- Not a single-node cluster.

## Configuring concurrency scaling

queues

With Amazon Redshift, you can manage concurrency and system resources by configuring concurrency scaling.
Concurrency scaling queues allow you to set limits on the number of queries or user
sessions that can be executed concurrently. The following section provides instructions on
how to enable concurrency scaling queues in Amazon Redshift, enabling you to effectively handle concurrent
queries and user sessions.

You route queries to concurrency scaling clusters by enabling concurrency scaling in a workload manager
(WLM) queue. To turn on concurrency scaling for a queue, set the **Concurrency Scaling mode** value
to **auto**.

When the number of queries routed to a queue with concurrency scaling enabled exceeds the queue's
concurrency capacity, whether the capacity is configured manually or determined automatically, eligible queries
are sent to the concurrency scaling cluster. When queue slots become available on the main cluster, queries are routed to and
run on the main cluster. As with any WLM queue, you route queries to a concurrency scaling queue based on user groups, or by labeling
queries with query group labels, or according to matching conditions
defined in [Assigning queries to queues](cm-c-executing-queries.md "cm-c-executing-queries.md"). You can also
route queries by defining [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md"). For example, you might route all
queries that take longer than 5 seconds to a concurrency scaling queue. Keep in mind that queuing behavior can vary, depending on whether you're using automatic WLM or manual WLM. For more information,
see [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md") or [Implementing manual WLM](cm-c-defining-query-queues.md "cm-c-defining-query-queues.md").

The default number of concurrency scaling clusters is one.
The number of concurrency scaling clusters that can be used is controlled by
[max_concurrency_scaling_clusters](r_max_concurrency_scaling_clusters.md "r_max_concurrency_scaling_clusters.md").

## Monitoring concurrency scaling

With Amazon Redshift, you can monitor and manage concurrency scaling to optimize performance
and cost efficiency for your data warehousing workloads. Concurrency scaling allows
Amazon Redshift to automatically add additional cluster capacity when workload demands increase,
and remove that capacity when demands decrease. The following section provides
guidance on monitoring concurrency scaling for your Amazon Redshift clusters.

You can see whether a query is running on the main cluster or a concurrency scaling
cluster by navigating to **Cluster** in the Amazon Redshift console and
choosing a cluster. Then choose the **Query monitoring** tab and **Workload concurrency** to
view information about running queries and queued queries.

To find execution times, query the STL_QUERY table and filter on the
`concurrency_scaling_status` column. The following query compares the
queue time and execution time for queries run on the concurrency scaling cluster and
queries run on the main cluster.

```
SELECT w.service_class AS queue
, CASE WHEN q.concurrency_scaling_status = 1 THEN 'concurrency scaling cluster' ELSE 'main cluster' END as concurrency_scaling_status
, COUNT( * ) AS queries
, SUM( q.aborted ) AS aborted
, SUM( ROUND( total_queue_time::NUMERIC / 1000000,2) ) AS queue_secs
, SUM( ROUND( total_exec_time::NUMERIC / 1000000,2) ) AS exec_secs
FROM stl_query q
JOIN stl_wlm_query w
USING (userid,query)
WHERE q.userid > 1
AND q.starttime > '2019-01-04 16:38:00'
AND q.endtime < '2019-01-04 17:40:00'
GROUP BY 1,2
ORDER BY 1,2;
```

Adjust the `starttime` and `endtime` values according to
your requirements.

## Concurrency scaling system

views

With Amazon Redshift, you can use Concurrency scaling system views to monitor and manage
concurrency scaling activity in your cluster. The following section describes
querying these system views and interpreting the results to effectively leverage
concurrency scaling in your Amazon Redshift environment.

A set of system views with the prefix SVCS provides details from the system log
tables about queries on both the main and concurrency scaling clusters.

The following views have similar information as the corresponding STL views or SVL
views:

- [SVCS_ALERT_EVENT_LOG](r_SVCS_ALERT_EVENT_LOG.md "r_SVCS_ALERT_EVENT_LOG.md")
- [SVCS_COMPILE](r_SVCS_COMPILE.md "r_SVCS_COMPILE.md")
- [SVCS_EXPLAIN](r_SVCS_EXPLAIN.md "r_SVCS_EXPLAIN.md")
- [SVCS_PLAN_INFO](r_SVCS_PLAN_INFO.md "r_SVCS_PLAN_INFO.md")
- [SVCS_QUERY_SUMMARY](r_SVCS_QUERY_SUMMARY.md "r_SVCS_QUERY_SUMMARY.md")
- [SVCS_STREAM_SEGS](r_SVCS_STREAM_SEGS.md "r_SVCS_STREAM_SEGS.md")

The following views are specific to concurrency scaling.

- [SVCS_CONCURRENCY_SCALING_USAGE](r_SVCS_CONCURRENCY_SCALING_USAGE.md "r_SVCS_CONCURRENCY_SCALING_USAGE.md")

For more information about concurrency scaling, see the following topics in the
_Amazon Redshift Management Guide_.

- [Viewing Concurrency Scaling Data](../mgmt/performance-metrics-concurrency-scaling.md "../mgmt/performance-metrics-concurrency-scaling.md")
- [Viewing Cluster Performance During Query Execution](../mgmt/performance-metrics-query-cluster.md "../mgmt/performance-metrics-query-cluster.md")
- [Viewing Query Details](../mgmt/performance-metrics-query-execution-details.md "../mgmt/performance-metrics-query-execution-details.md")
