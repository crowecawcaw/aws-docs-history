# Direct query limitations

## General limitations

The following limitations apply to OpenSearch Service direct queries.

- Some data types aren't supported. Supported data types are limited to
  Parquet, CSV, and JSON.
- If the structure of your data changes over time, you will need to update
  your indexed views or out-of-the-box integrations to account for the data
  structure changes.
- AWS CloudFormation templates aren't supported yet.
- OpenSearch SQL and OpenSearch PPL statements have different limitations when
  working with OpenSearch indexes compared to using direct query. Direct query
  supports advanced commands such as JOINs, subqueries, and lookups, while
  support for these commands on OpenSearch indexes is limited or nonexistent.
  For more information, see [Supported SQL and PPL commands](direct-query-supported-commands.md "direct-query-supported-commands.md").

## Limitations for Amazon S3

If you’re direct querying data in Amazon S3, the following additional limitations
apply:

- Direct query for S3 is only available on OpenSearch Service domains running OpenSearch
  version 2.13 or later, and requires access to AWS Glue Data Catalog. Existing
  AWS Glue Data Catalog tables must be recreated using SQL in OpenSearch Query
  Workbench.
- Direct query for S3 requires you to specify a checkpoint bucket on Amazon S3.
  This bucket maintains the state of your indexed views, including the last
  refresh time and the most recently ingested data.
- Your OpenSearch domain and AWS Glue Data Catalog must be in the same AWS account.
  Your S3 bucket can be in a different account (requires condition to be added
  to your IAM policy), but must be in the same AWS Region as your
  domain.
- OpenSearch Service direct queries with S3 only support Spark tables generated from Query
  Workbench. Tables generated within AWS Glue Data Catalog or Athena are not supported
  by Spark streaming, which is needed to maintain indexed views.
- OpenSearch instance types have networked payload limitations of either 10
  MiB or 100 MiB, depending on the specific instance type you choose.

## Limitations for Amazon CloudWatch Logs

If you’re direct querying data in CloudWatch Logs, the following additional limitations
apply:

- The direct query integration with CloudWatch Logs is only available on OpenSearch Service
  collections and the OpenSearch user interface.
- OpenSearch Serverless collections have networked payload limitations of 100
  MiB.
- CloudWatch Logs supports VPC Flow, CloudTrail, and AWS WAF dashboard integrations installed
  from the console.

## Limitations for Amazon Security Lake

If you’re direct querying data in Security Lake, the following additional limitations
apply:

- The direct query integration with Security Lake is only available on OpenSearch Service
  collections and the OpenSearch user interface.
- OpenSearch Serverless collections have networked payload limitations of 100
  MiB.
- Table management for Security Lake is performed in Lake Formation.
- Security Lake only supports materialized views as indexed views. Covering indexes
  are not supported.
