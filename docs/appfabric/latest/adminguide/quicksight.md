

# Amazon Quick
<a name="quicksight"></a>

Amazon Quick powers data-driven organizations with unified business intelligence (BI) at hyperscale. With Quick, all users can meet varying analytic needs from the same source of truth through modern interactive dashboards, paginated reports, embedded analytics, and natural language queries. You can analyze AWS AppFabric audit log data in Quick, by choosing your Amazon Simple Storage Service (Amazon S3) bucket where your AppFabric for security logs are stored as your source.

## AppFabric audit log ingestion considerations
<a name="quicksight-audit-log-ingestion"></a>

The following sections describe the AppFabric output schema, output formats, and output destinations to use with Quick.

### Schema and formats
<a name="quicksight-schema-format"></a>

Quick supports the following AppFabric output schema and formats:
+ Raw - JSON
  + AppFabric outputs data in the original schema used by the source application in the JSON format.
+ OCSF - JSON
  + AppFabric normalizes the data using the Open Cybersecurity Schema Framework (OCSF) and outputs the data in the JSON format. 

### Output locations
<a name="quicksight-output-locations"></a>

Quick supports the following AppFabric output locations:
+ Amazon S3
  + You can ingest data from Amazon S3 directly into Quick by [Creating a dataset using Amazon S3 files](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html). To verify that your target file set doesn't exceed Quick data source quotas, see [Data source quotas](https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html) in the *Quick User Guide*.
  + If your file set exceeds Quick quotas for an Amazon S3 data source, you can ingest your data in Amazon S3 using Amazon Athena and AWS Glue tables. Using Athena in your Quick dataset will incur additional costs. For more information about Athena pricing, see the [Athena pricing page](https://aws.amazon.com/athena/pricing/).

    To use Athena:

    1. Follow the instructions in [Using AWS Glue to connect to data sources in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html) in the *Athena User Guide*.

    1. Follow the instructions in [Creating a dataset using Athena data](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html) in the *Quick User Guide*.