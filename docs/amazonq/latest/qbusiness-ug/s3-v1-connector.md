

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon S3 to Amazon Q Business (Old)
<a name="s3-v1-connector"></a>

**Note**  
For new implementations, we recommend using the new Amazon S3 connector which enables you to refresh your index significantly faster than before. The new Amazon S3 connector doesn’t support VPC, document enrichment, and custom metadata. If you need these features, you can continue using the older Amazon S3 connector.

## Known limitations for the connector
<a name="s3-v1-limitations"></a>

The Amazon S3 connector has the following known limitations:
+ The [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket must be in the same AWS Region as your Amazon Q index, and your index must have permissions to access the bucket that contains your documents.