# Amazon Quick Suite

Amazon Quick Suite powers data-driven organizations with unified business intelligence (BI) at
hyperscale. With Quick Suite, all users can meet varying analytic needs from the same source
of truth through modern interactive dashboards, paginated reports, embedded analytics, and
natural language queries. You can analyze AWS AppFabric audit log data in Quick Suite, by choosing
your Amazon Simple Storage Service (Amazon S3) bucket where your AppFabric for security logs are stored as your source.

## AppFabric audit log ingestion

considerations

The following sections describe the AppFabric output schema, output formats, and output
destinations to use with Quick Suite.

### Schema and formats

Quick Suite supports the following AppFabric output schema and formats:

- Raw - JSON
  - AppFabric outputs data in the original schema used by the source
    application in the JSON format.

- OCSF - JSON
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in the JSON format.

### Output locations

Quick Suite supports the following AppFabric output locations:

- Amazon S3
  - You can ingest data from Amazon S3 directly into Quick Suite by [Creating
    a dataset using Amazon S3 files](../../../quicksight/latest/user/create-a-data-set-s3.md "../../../quicksight/latest/user/create-a-data-set-s3.md"). To verify that your target
    file set doesn't exceed Quick Suite data source quotas, see [Data source
    quotas](../../../quicksight/latest/user/data-source-limits.md "../../../quicksight/latest/user/data-source-limits.md") in the _Quick Suite User
    Guide_.
  - If your file set exceeds Quick Suite quotas for an Amazon S3 data source,
    you can ingest your data in Amazon S3 using Amazon Athena and AWS Glue tables.
    Using Athena in your Quick Suite dataset will incur additional costs.
    For more information about Athena pricing, see the [Athena pricing
    page](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").

  To use Athena:

      1. Follow the instructions in [Using
       AWS Glue to connect to data sources in Amazon S3](../../../athena/latest/ug/data-sources-glue.md "../../../athena/latest/ug/data-sources-glue.md") in the
       *Athena User Guide*.
      2. Follow the instructions in [Creating a dataset using Athena data](../../../quicksight/latest/user/create-a-data-set-athena.md "../../../quicksight/latest/user/create-a-data-set-athena.md") in the
       *Quick Suite User Guide*.
