

# Directly querying Amazon CloudWatch Logs data in OpenSearch Service
<a name="direct-query-cloudwatch-logs-overview"></a>

This section will walk you through the process of creating and configuring a data source integration in Amazon OpenSearch Service, enabling you to efficiently query and analyze your data stored in CloudWatch Logs.

In the following pages, you'll learn how to set up a CloudWatch Logs direct-query data source, navigate the necessary prerequisites, and follow step-by-step procedures using the AWS Management Console. 

**Topics**
+ [Creating an Amazon CloudWatch Logs data source integration in OpenSearch Service](direct-query-cloudwatch-logs-creating.md)
+ [Configuring and querying a CloudWatch Logs data source in OpenSearch Dashboards](direct-query-cloudwatch-logs-configure.md)
+ [Pricing](#direct-query-cloudwatch-logs-pricing)
+ [Limitations](#direct-query-cloudwatch-logs-limitations)
+ [Recommendations](#direct-query-cloudwatch-logs-recommendations)
+ [Quotas](#direct-query-cloudwatch-logs-quotas)
+ [Supported AWS Regions](#direct-query-cloudwatch-logs-regions)

## Pricing
<a name="direct-query-cloudwatch-logs-pricing"></a>

Amazon OpenSearch Service offers OpenSearch Compute Unit (OCU) pricing for CloudWatch Logs direct queries. As you run direct queries, you incur charges for OCUs per hour, listed as DirectQuery OCU usage type on your bill. You will also incur separate charges from Amazon CloudWatch Logs.

Direct queries are of two types—interactive and indexed view queries.
+ *Interactive queries* are used to populate the data selector and perform analytics on your data in CloudWatch Logs. OpenSearch Service handles each query with a separate pre-warmed job, without maintaining an extended session.
+ *Indexed view queries* use compute to maintain indexed views in OpenSearch Service. These queries usually take longer because they ingest a varying amount of data into a named index. For CloudWatch Logs connected data sources, the indexed data is stored in an OpenSearch Serverless collection where you are charged for data indexed (IndexingOCU), data searched (SearchOCU), and data stored in GB.

For more information, see the Direct Query and Serverless sections within [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/).

## Limitations
<a name="direct-query-cloudwatch-logs-limitations"></a>

The following limitations apply to direct queries in CloudWatch Logs:
+ The direct query integration with CloudWatch Logs is only available on OpenSearch Service collections and the OpenSearch user interface.
+ OpenSearch Serverless collections have networked payload limitations of 100 MiB. 
+ CloudWatch Logs supports VPC Flow, CloudTrail, and AWS WAF dashboard integrations installed from the console. 
+ AWS CloudFormation templates aren't supported yet.
+ OpenSearch SQL and OpenSearch PPL statements have different limitations when working with OpenSearch indexes compared to using direct query. Direct query supports advanced commands such as JOINs, subqueries, and lookups, while support for these commands on OpenSearch indexes is limited or nonexistent. For more information, see [Supported SQL and PPL commands](direct-query-supported-commands.md).

## Recommendations
<a name="direct-query-cloudwatch-logs-recommendations"></a>

We recommend the following when using direct queries in CloudWatch Logs:
+ When searching multiple log groups in one query, use the appropriate syntax. For more information, see [Multi-log group functions](supported-directquery-sql.md#multi-log-queries).
+ When using SQL or PPL commands, enclose certain fields in backticks to successfully query them. Backticks are needed for fields with special characters (non-alphabetic and non-numeric). For example, enclose `@message`, `Operation.Export,` and `Test::Field` in backticks. You don't need to enclose columns with purely alphabetic names in backticks.

  Example query with simple fields:

  ```
  SELECT SessionToken, Operation, StartTime  FROM `LogGroup-A`
  LIMIT 1000;
  ```

  Similar query with backticks appended:

  ```
  SELECT `@SessionToken`, `@Operation`, `@StartTime` FROM `LogGroup-A`
  LIMIT 1000;
  ```
+ Use limits on your queries to make sure you aren't pulling too much data back.
+ Queries containing field names that are identical but differ only in case (such as `field1` and `FIELD1`) are not supported.

  For example, the following queries are not supported:

  ```
  Select AWSAccountId, AwsAccountId from LogGroup
  Select a.@LogStream, b.@logStream from Table A INNER Join Table B ona.id = b.id
  ```

  However, the following query is supported because the field name (@logStream) is identical in both log groups:

  ```
  Select a.@logStream, b.@logStream from Table A INNER Join Table B on a.id = b.id
  ```
+ Functions and expressions must operate on field names and be part of a `SELECT` statement with a log group specified in the `FROM` clause.

  For example, this query is not supported:

  ```
  SELECT cos(10) FROM LogGroup
  ```

  This query is supported:

  ```
  SELECT cos(field1) FROM LogGroup
  ```

## Quotas
<a name="direct-query-cloudwatch-logs-quotas"></a>

**Note**  
If you're looking to perform direct queries using CloudWatch Logs Insights, make sure that you refer to [Additional information for CloudWatch Logs Insights users using OpenSearch SQL](supported-directquery-sql.md#supported-sql-for-multi-log-queries).


| Description | Value | Soft limit? | Notes | 
| --- | --- | --- | --- | 
| Account-level TPS limit across direct query APIs | 3 TPS | Yes |  | 
| Maximum number of data sources | 20 | Yes | Limit is per AWS account. | 
| Maximum auto-refreshing indexes or materialized views | 30 | Yes | Limit is per data source. | 
| Maximum concurrent queries | 30 | Yes | Limit is per data source and applies to queries in pending or running state. <br />Includes interactive queries (for example, data retrieval commands like `SELECT`) and index queries (for example, operations like `CREATE`/`ALTER`).  | 
| Maximum concurrent OCU per query | 512 | Yes | OpenSearch Compute Units (OCU). Limit based on 15 executors and 1 driver, each with 16 vCPU and 32 GB memory. Represents concurrent processing power. | 
| Maximum query execution time in minutes | 60 | No | Limit applies to OpenSearch PPL/SQL queries in CloudWatch Logs Insights. | 
| Period for purging stale query IDs | 90 days | Yes | This is the time period after which OpenSearch Service purges query metadata for older entries. For example, calling GetDirectQuery or GetDirectQueryResult fails for queries older than 90 days. | 

## Supported AWS Regions
<a name="direct-query-cloudwatch-logs-regions"></a>

The following AWS Regions are supported for direct queries in CloudWatch Logs:
+ Asia Pacific (Mumbai) 
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+  Europe (Ireland)
+ Europe (Stockholm)
+ Europe (Milan)
+ Europe (Spain)
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ US West (N. California)
+ Europe (Paris) 
+ Europe (London)
+ South America (Sao Paulo)