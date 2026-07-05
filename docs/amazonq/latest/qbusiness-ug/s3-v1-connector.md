Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Connecting Amazon S3 to Amazon Q Business (Old)

###### Note

For new implementations, we recommend using the new Amazon S3 connector which enables you
to refresh your index significantly faster than before. The new Amazon S3 connector doesn’t
support VPC, document enrichment, and custom metadata. If you need these features,
you can continue using the older Amazon S3 connector.

## Known limitations for the connector

The Amazon S3 connector has the following known limitations:

- The [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket must be in the same AWS Region as your Amazon Q index, and your index must have permissions to access the bucket
  that contains your documents.
