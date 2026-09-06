

# Directly querying Amazon Security Lake data in OpenSearch Service
<a name="direct-query-security-lake-overview"></a>

This section will walk you through the process of creating and configuring a data source integration in Amazon OpenSearch Service, enabling you to efficiently query and analyze your data stored in Security Lake.

In the following pages, you'll learn how to set up a Security Lake direct-query data source, navigate the necessary prerequisites, and follow step-by-step procedures using the AWS Management Console. 

**Topics**
+ [Creating an Amazon Security Lake data source integration in OpenSearch Service](direct-query-security-lake-creating.md)
+ [Configuring and querying a Security Lake data source in OpenSearch Dashboards](direct-query-security-lake-configure.md)
+ [Pricing](#direct-query-security-lake-pricing)
+ [Limitations](#direct-query-security-lake-limitations)
+ [Recommendations](#direct-query-security-lake-recommendations)
+ [Quotas](#direct-query-security-lake-quotas)
+ [Supported AWS Regions](#direct-query-security-lake-regions)

## Pricing
<a name="direct-query-security-lake-pricing"></a>

Amazon OpenSearch Service offers OpenSearch Compute Unit (OCU) pricing for Security Lake direct queries. As you run direct queries, you incur charges for OCUs per hour, listed as DirectQuery OCU usage type on your bill. You will also incur separate charges from Amazon Security Lake.

Direct queries are of two types—interactive and indexed view queries.
+ *Interactive queries* are used to populate the data selector and perform analytics on your data in Security Lake. OpenSearch Service handles each query with a separate pre-warmed job, without maintaining an extended session.
+ *Indexed view queries* use compute to maintain indexed views in OpenSearch Service. These queries usually take longer because they ingest a varying amount of data into a named index. For Security Lake connected data sources, the indexed data is stored in an OpenSearch Serverless collection where you are charged for data indexed (IndexingOCU), data searched (SearchOCU), and data stored in GB.

For more information, see the Direct Query and Serverless sections within [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/).

## Limitations
<a name="direct-query-security-lake-limitations"></a>

The following limitations apply to direct queries in Security Lake:
+ The direct query integration with Security Lake is only available on OpenSearch Service collections and the OpenSearch user interface.
+ OpenSearch Serverless collections have networked payload limitations of 100 MiB. 
+ Table management for Security Lake is performed in Lake Formation.
+ Security Lake only supports materialized views as indexed views. Covering indexes are not supported.
+ AWS CloudFormation templates aren't supported yet.
+ OpenSearch SQL and OpenSearch PPL statements have different limitations when working with OpenSearch indexes compared to using direct query. Direct query supports advanced commands such as JOINs, subqueries, and lookups, while support for these commands on OpenSearch indexes is limited or nonexistent. For more information, see [Supported SQL and PPL commands](direct-query-supported-commands.md).

## Recommendations
<a name="direct-query-security-lake-recommendations"></a>

We recommend the following when using direct queries in Security Lake:
+ Check your Security Lake status and ensure that it's running smoothly without any problems. For detailed troubleshooting steps, see [Troubleshooting data lake status](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-data-lake-troubleshoot.html) in the Amazon Security Lake User Guide.
+ Verify your query access:
  + If you're querying Security Lake from a different account than the Security Lake delegated administrator account, [set up a subscriber with query access in Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-access.html). 
  + If you're querying Security Lake from the same account, check for any messages in Security Lake about registering your managed S3 buckets with LakeFormation.
+ Explore the query templates and pre-built dashboards to jumpstart your analysis.
+ Familiarize yourself with Open Cybersecurity Schema Framework (OCSF) and Security Lake:
  + Review schema mapping examples for AWS sources in the [OCSF GitHub repository](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/CloudTrail)
  + Learn how to query Security Lake effectively by visiting [Security Lake queries for AWS source version 2 (OCSF 1.1.0)](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-examples2.html)
  + Improve query performance by using partitions: `accountid`, `region`, and `time_dt`
+ Get comfortable with SQL syntax, which Security Lake supports for querying. For more information, see [Supported OpenSearch SQL commands and functions](supported-directquery-sql.md).
+ Use limits on your queries to make sure you aren't pulling too much data back.

## Quotas
<a name="direct-query-security-lake-quotas"></a>


| Description | Value | Soft limit? | Notes | 
| --- | --- | --- | --- | 
| Account-level TPS limit across direct query APIs | 3 TPS | Yes |  | 
| Maximum number of data sources | 20 | Yes | Limit is per AWS account. | 
| Maximum auto-refreshing indexes or materialized views | 30 | Yes | Limit applies per data source. <br />Only includes indices and materialized views (MVs) with auto-refresh set to true. | 
| Maximum concurrent queries | 30 | Yes | Limit applies to queries in pending or running state. <br />Includes interactive queries (for example, data retrieval commands like `SELECT`) and index queries (for example, operations like `CREATE`/`ALTER`/`DROP`).  | 
| Maximum concurrent OCU per query | 512 | Yes | OpenSearch Compute Units (OCU). Limit based on 15 executors and 1 driver, each with 16 vCPU and 32 GB memory. Represents concurrent processing power. | 
| Maximum query execution time in minutes | 30 | No | Applies only to interactive queries (for example, data retrieval commands like SELECT). For REFRESH queries, the limit is 6 hours. | 
| Period for purging stale query IDs | 90 days | Yes | This is the time period after which OpenSearch Service purges query metadata for older entries. For example, calling GetDirectQuery or GetDirectQueryResult fails for queries older than 90 days. | 

## Supported AWS Regions
<a name="direct-query-security-lake-regions"></a>

The following AWS Regions are supported for direct queries in Security Lake:
+ Asia Pacific (Mumbai)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+  Europe (Ireland)
+ Europe (Stockholm)
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Europe (Paris) 
+ Europe (London)
+ South America (Sao Paulo)