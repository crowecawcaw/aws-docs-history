

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Extracting content from visuals in a file
<a name="enable-semantic-meanining-file-upload"></a>

You can enable content extraction from a file with the Amazon Q Business console or API operations. Processing images and visuals takes more time than processing text-only for the documents.

## Console
<a name="enable-vrd-console"></a>

When you upload documents directly to an Amazon Q Business application environment, in the **Multi-media content configuration** section of **Select files**, choose the **Visual content in documents** option. For step by step instructions, see [Uploading files](upload-docs.md).

## APIs
<a name="enable-vrd-api"></a>

To enable content extraction from a file when you use the [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) API operation, in the `ImageExtractionConfiguration` you set the `imageExtractionStatus` to `ENABLED`. 

```
aws qbusiness batch-put-document \
--application-id {{app-12345abcde}} \
--index-id {{index-67890fghij}} \
--role-arn arn:aws:iam::{{123456789012}}:role/{{ServiceRoleName}} \
--documents '[{
    "Id": "doc1",
    "MediaExtractionConfiguration": {
        "ImageExtractionConfiguration": {
            "ImageExtractionStatus": "ENABLED"
        }
    }
}]' 
--data-source-sync-id {{sync-12345}}
```