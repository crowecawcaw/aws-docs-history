

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using Amazon VPC with an Amazon S3 data source
<a name="s3-vpc-example-1"></a>

This topic describes the requirements for connecting Amazon Q Business to an Amazon Simple Storage Service through Amazon Virtual Private Cloud. It outlines the necessary prerequisites, including VPC configuration and S3 endpoint setup, to enable Amazon Q Business to access Amazon S3 buckets through a private connection.

**Important**  
So that an Amazon Q Business Amazon S3 connector can access your Amazon S3 bucket, make sure that you have assigned an Amazon S3 endpoint to your virtual private cloud (VPC). For more information about configuring an Amazon Q Business Amazon S3 connector with Amazon VPC, see [Using Amazon VPC with Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-connector.html#s3-vpc).

For Amazon Q Business to sync documents from your Amazon S3 bucket through Amazon VPC, you must complete the following steps:
+ Set up an Amazon S3 endpoint for Amazon VPC. For more information about how to set up an Amazon S3 endpoint, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the *AWS PrivateLink Guide*.
+ (Optional) Checked your Amazon S3 bucket policies to make sure that the Amazon S3 bucket is accessible from the virtual private cloud (VPC) that you assigned to Amazon Q Business. For more information, see [Controlling access from VPC endpoints with bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html) in the *Amazon S3 User Guide*.

For more information about how to configure Amazon VPC security groups, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.