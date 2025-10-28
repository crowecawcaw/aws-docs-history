# Prerequisites

To use the managed policies for Amazon Managed Grafana for Athena, complete the following
tasks before you configure the Athena data source:

- Tag your Athena work groups with `GrafanaDataSource: true`.
- Create an S3 bucket with a name that starts with
  `grafana-athena-query-results-`. This policy provides
  permissions for writing query results into an S3 bucket with that naming
  convention.
  The Amazon S3 permissions for accessing the underlying data source of an Athena
  query are not included in this managed policy. You must add the necessary
  permissions for the Amazon S3 buckets manually, on a case-by-case basis. For more
  information, see [Identity-based policy examples in Amazon Managed Grafana](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") in this guide.
