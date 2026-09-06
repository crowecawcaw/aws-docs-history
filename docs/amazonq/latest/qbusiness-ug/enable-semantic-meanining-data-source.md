

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Extracting content from visuals with data connectors
<a name="enable-semantic-meanining-data-source"></a>

You can enable content extraction when you add or update a data connector with the Amazon Q Business console or API operations. Processing images and visuals takes more time than processing text-only for the documents.

## Console
<a name="enable-vrd-console"></a>

When you add or update a data connector, in the **Multi-media content configuration** section of **Sync scope**, choose **Visual content in documents**. For more information, see the console procedure for your data connector. For example, for a console procedure for Amazon S3, see [Connecting Amazon Q Business to Amazon S3 using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-console.html).

## APIs
<a name="enable-vrd-api"></a>

To enable content extraction from images when you use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) API operations, for `mediaExtractionConfiguration` set `imageExtractionStatus` to ENABLED. The following example shows how to enable content extraction when you create a data source. After you turn on content extraction, you can view media extraction configuration for the data source with the GetDataSource API operation.

```
aws qbusiness create-data-source \
--application-id {{app-12345abcde}} \
--index-id {{index-67890fghij}}\
--display-name {{My New S3 Source}} \
--configuration '{
    "S3Configuration": {
      "BucketName": "{{my-s3-bucket}}",
      "DocumentsMetadataConfiguration": {
        "S3Prefix": "{{documents/}}"
      }
    }
}' \
--media-extraction-configuration '{
    "imageExtractionConfiguration": {
      "imageExtractionStatus": "ENABLED"
    }
}' \
--description {{Description of data source connector}} \
--role-arn arn:aws:iam::{{123456789012}}:role/{{AmazonQServiceRole}}
```