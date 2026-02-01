Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with read-only data

sharing with the SQL interface

With Amazon Redshift, you can securely share data across Amazon Redshift clusters, enabling data consumers
to query and access live data without copying or replicating it. Data sharing lets you
create and configure datashares, which are producer-side objects that reference the
database objects you want to share.

You can share data for read purposes across different Amazon Redshift clusters within or across
AWS accounts, or across AWS Regions.

###### Topics

- [Sharing read access to data within an
  AWS account](within-account.md "within-account.md")
- [Working with views in Amazon Redshift data sharing](datashare-views.md "datashare-views.md")
- [Adding data lake tables to a
  datashare](create-datashare-external-views.md "create-datashare-external-views.md")
- [Sharing data across AWS accounts](across-account.md "across-account.md")
- [Sharing data across AWS Regions](across-region.md "across-region.md")
- [Sharing licensed Amazon Redshift data on AWS Data Exchange](adx-getting-started.md "adx-getting-started.md")
- [Getting started with AWS Lake Formation-managed
  datashares](lf-getting-started.md "lf-getting-started.md")
