Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data sharing in Amazon Redshift Serverless

With _data sharing_, you have live access to data so
that your users can see the most up-to-date and consistent information as it's updated
in Amazon Redshift Serverless.

You can share data for read purposes across different Amazon Redshift Serverless instances
within or across AWS accounts.

You can get started with data sharing by using either the SQL interface or the
Amazon Redshift console. For more information, see [Data sharing in Amazon Redshift](../dg/datashare-overview.md "../dg/datashare-overview.md") in the
_Amazon Redshift Database Developer Guide_.

With data sharing, Amazon Redshift Serverless namespaces and provisioned clusters can share
live data with each other, whether they are within an AWS account across
AWS accounts, or across AWS Regions. For more information, see [Regions
where data sharing is available](../dg/data_sharing_regions.md "../dg/data_sharing_regions.md").

To get started sharing data within an AWS account, open the AWS Management Console, and then
choose the Amazon Redshift console. Choose **Namespace configuration** and then
**Datashares**.

To start querying data in a datashare, create a database in a namespace that has a
workgroup associated with it. From a specified datashare, choose a namespace that has a
workgroup associated with it and create a database to query data.

## Considerations

Consider the following when working with data sharing in Amazon Redshift Serverless:

- Amazon Redshift only supports provisioned clusters of instance type ra3.16xlarge,
  ra3.4xlarge, and ra3.xlplus, and serverless endpoint as data sharing producers or
  consumers.
- Amazon Redshift Serverless is encrypted by default.

For a list of datasharing limitations, including database objects supported,
encryption requirements, and sort-key requirements, see [Considerations for data sharing in
Amazon Redshift](../dg/datashare-considerations.md "../dg/datashare-considerations.md") in the _Amazon Redshift Database Developer Guide_.
