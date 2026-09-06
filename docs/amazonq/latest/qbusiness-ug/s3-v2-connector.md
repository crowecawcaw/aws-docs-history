

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon S3 to Amazon Q Business using the New connector
<a name="s3-v2-connector"></a>

**Note**  
**Enhanced Version:** With the new connector, you can refresh your index significantly faster than before.

## Known limitations
<a name="s3-v2-limitations"></a>

The Amazon S3 connector has the following known limitations:
+ The [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket must be in the same AWS Region as your Amazon Q index, and your index must have permissions to access the bucket that contains your documents.
+ VPC connectivity not supported (use the old version if VPC support is required)
+ Custom field mappings not supported (use the old connector version if required)
+ Document enrichment is not supported. (use the old connector version if required)