# Query across regions

Athena supports the ability to query Amazon S3 data in an AWS Region that is different from
the Region in which you are using Athena. Querying across Regions can be an option when
moving the data is not practical or permissible, or if you want to query data across
multiple regions. Even if Athena is not available in a particular Region, data from that
Region can be queried from another Region in which Athena is available.

To query data in a Region, your account must be enabled in that Region even if the Amazon S3
data does not belong to your account. For some regions such as US East (Ohio), your
access to the Region is automatically enabled when your account is created. Other Regions
require that your account be "opted-in" to the Region before you can use it. For a list of
Regions that require opt-in, see [Available regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions") in the _Amazon EC2 User Guide_.
For specific instructions about opting-in to a Region, see [Managing AWS regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the
_Amazon Web Services General Reference_.

## Considerations and limitations

- Data access permissions – To
  successfully query Amazon S3 data from Athena across Regions, your account must have
  permissions to read the data. If the data that you want to query belongs to
  another account, the other account must grant you access to the Amazon S3 location
  that contains the data.
- Data transfer charges – Amazon S3 data
  transfer charges apply for cross-region queries. Running a query can result in
  more data transferred than the size of the dataset. We recommend that you start
  by testing your queries on a subset of data and reviewing the costs in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/").
- AWS Glue – You can use AWS Glue across
  Regions. Additional charges may apply for cross-region AWS Glue traffic. For more
  information, see [Create cross-account and cross-region AWS Glue connections](https://aws.amazon.com/blogs/big-data/create-cross-account-and-cross-region-aws-glue-connections/ "https://aws.amazon.com/blogs/big-data/create-cross-account-and-cross-region-aws-glue-connections/") in the
  _AWS Big Data Blog_.
- Amazon S3 encryption options – The SSE-S3 and
  SSE-KMS encryption options are supported for queries across Regions; CSE-KMS is
  not. For more information, see [Supported Amazon S3 encryption options](encryption.md#encryption-options-S3-and-Athena "encryption.md#encryption-options-S3-and-Athena").
- Federated queries – Using federated
  queries across AWS Regions is not supported.

Provided the above conditions are met, you can create an Athena table that points to
the `LOCATION` value that you specify and query the data transparently. No
special syntax is required. For information about creating Athena tables, see [Create tables in Athena](creating-tables.md "creating-tables.md").
