# Accessing Amazon S3 tables with Amazon Redshift

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple
and cost-effective to efficiently analyze all your data using your existing business
intelligence tools. Redshift Serverless lets you access and analyze data without all of the configurations
of a provisioned data warehouse. For more information, see [Get started with serverless data
warehouses](../../../redshift/latest/gsg/new-user-serverless.md "../../../redshift/latest/gsg/new-user-serverless.md") in the _Amazon Redshift Getting Started Guide_.

## Query Amazon S3 tables with Amazon Redshift

###### Prerequisites

- [Integrate your table buckets with
  AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
  - [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md").
  - [Create a table](s3-tables-create.md "s3-tables-create.md").

- [Managing access to a table or database with Lake Formation](grant-permissions-tables.md "grant-permissions-tables.md").

After you complete the prerequisites, you can begin using Amazon Redshift to query tables in one
of the following ways:

- [Using the Amazon Redshift query editor v2](../../../redshift/latest/mgmt/query-editor-v2.md "../../../redshift/latest/mgmt/query-editor-v2.md")
- [Connecting to an
  Amazon Redshift data warehouse using SQL client tools](../../../redshift/latest/mgmt/connecting-to-cluster.md "../../../redshift/latest/mgmt/connecting-to-cluster.md")
- [Using
  the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api.md "../../../redshift/latest/mgmt/data-api.md")
