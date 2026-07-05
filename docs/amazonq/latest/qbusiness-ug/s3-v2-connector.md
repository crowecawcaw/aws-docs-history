Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Connecting Amazon S3 to Amazon Q Business using the New connector

###### Note

**Enhanced Version:** With the new connector, you can
refresh your index significantly faster than before.

## Known limitations

The Amazon S3 connector has the following known limitations:

- The [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket must be in the same AWS Region as your Amazon Q index, and your index must have permissions to access the bucket
  that contains your documents.

- VPC connectivity not supported (use the old version if VPC support is
  required)
- Custom field mappings not supported (use the old connector version if
  required)
- Document enrichment is not supported. (use the old connector version if
  required)
