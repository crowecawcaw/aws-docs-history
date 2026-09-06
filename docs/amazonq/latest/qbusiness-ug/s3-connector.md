

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon S3 to Amazon Q Business
<a name="s3-connector"></a>

[Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (Amazon S3) is an object storage service that stores data as objects within storage buckets. You can connect an Amazon S3 instance to Amazon Q Business—using either the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API—and create an Amazon Q web experience.

After you integrate Amazon Q with Amazon S3, users can ask questions about the content stored in Amazon S3. For example, a user might ask about the main points discussed in a blog post on cloud security, the installation steps outlined in a user guide, findings from a case study on hybrid cloud usage, market trends noted in an analyst report, or key takeaways from a whitepaper on data encryption. This integration helps users to quickly find the specific information they need, improving their understanding and ability to make informed business decisions.

Amazon Q Business supports source attribution with citations. If you specify the `_source_uri` metadata field when you add metadata to your Amazon S3 bucket, the source attribution links returned by Amazon Q Business in the chat results will direct users to the configured URL. If you don't specify a `_source_uri`, users can still access the source documents through clickable citation links that will download the file at query time. This allows users to verify information even when no source URI is configured. To learn how to add metadata for your Amazon S3 connector, see [Adding document metadata in Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-metadata.html).

**Note**  
To learn how to create an Amazon S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon Simple Storage Service User Guide*.

**Topics**
+ [Connecting Amazon S3 to Amazon Q Business using the New connector](s3-v2-connector.md)
+ [Connecting Amazon S3 to Amazon Q Business (Old)](s3-v1-connector.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).