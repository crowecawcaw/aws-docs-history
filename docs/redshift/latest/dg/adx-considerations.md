Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for data sharing with AWS Data Exchange in

Amazon Redshift

When using AWS Data Exchange for Amazon Redshift, consider the following:

- Both producers and consumers must use the RA3 instance types to use Amazon Redshift
  datashares. Producers must use the RA3 instance types with the latest Amazon Redshift cluster
  version.
- Both the producer and consumer clusters must be encrypted.
- You must be registered as an AWS Data Exchange provider to list products on AWS Data Exchange,
  including products that contain AWS Data Exchange datashares. For more information, see [Getting started as a provider](../../../data-exchange/latest/userguide/provider-getting-started.md "../../../data-exchange/latest/userguide/provider-getting-started.md").
- You don't need to be a registered AWS Data Exchange provider to find, subscribe to,
  and query Amazon Redshift data through AWS Data Exchange.
- To control access to your data, create AWS Data Exchange datashares with the publicly
  accessible setting turned on. To alter an AWS Data Exchange datashare to turn off the publicly
  accessible setting, set the session variable to allow ALTER DATASHARE SET
  PUBLICACCESSIBLE FALSE. For more information, see [ALTER DATASHARE usage notes](r_ALTER_DATASHARE.md#r_ALTER_DATASHARE_usage "r_ALTER_DATASHARE.md#r_ALTER_DATASHARE_usage").
- Producers can't manually add or remove consumers from AWS Data Exchange datashares
  because access to the datashares is granted based on having an active subscription
  to an AWS Data Exchange product that contains the AWS Data Exchange datashare.
- Producers can't view the SQL queries that consumers run. They can only
  view metadata, such as the number of queries or the objects consumers query,
  through Amazon Redshift tables that only the producer can access. For more information,
  see [Monitoring and auditing data sharing in Amazon Redshift](auditing.md "auditing.md").
- We recommend that you make your datashares publicly accessible. If you
  don't, subscribers on AWS Data Exchange with publicly accessible consumer clusters
  won't be able to use your datashare.
- We recommend that you don't delete an AWS Data Exchange datashare shared to other
  AWS accounts using the DROP DATASHARE statement. If you do, the AWS accounts
  that have access to the datashare will lose access. This action is irreversible.
  Performing this type of alteration can breach data product terms in AWS Data Exchange. If you
  want to delete an AWS Data Exchange datashare, see [DROP DATASHARE usage notes](r_DROP_DATASHARE.md#r_DROP_DATASHARE_usage "r_DROP_DATASHARE.md#r_DROP_DATASHARE_usage").
- For cross-Region data sharing, you can create AWS Data Exchange datashares to share
  licensed data.
- When consuming data from a different Region, the consumer pays the Cross-Region
  data transfer fee from the producer Region to the consumer Region.
