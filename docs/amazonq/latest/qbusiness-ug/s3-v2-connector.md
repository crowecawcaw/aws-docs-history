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
