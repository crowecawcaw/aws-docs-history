# Extracting content from visuals in a file

You can enable content extraction from a file with the Amazon Q Business console or API
operations. Processing images and visuals takes more time than processing text-only for
the documents.

When you upload documents directly to an Amazon Q Business application environment,
in the **Multi-media content configuration** section of
**Select files**, choose the **Visual content in
documents** option. For step by step instructions, see [Uploading files](upload-docs.md "upload-docs.md").

To enable content extraction from a file when you use the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation, in the
`ImageExtractionConfiguration` you set the
`imageExtractionStatus` to `ENABLED`.

```
aws qbusiness batch-put-document \
--application-id `app-12345abcde` \
--index-id `index-67890fghij` \
--role-arn arn:aws:iam::`123456789012`:role/`ServiceRoleName` \
--documents '[{
    "Id": "doc1",
    "MediaExtractionConfiguration": {
        "ImageExtractionConfiguration": {
            "ImageExtractionStatus": "ENABLED"
        }
    }
}]'
--data-source-sync-id `sync-12345`

```
