# Adding documents to an index in

Amazon Kendra

The way you add documents to an index depends on how you store your
documents.

- If you store your documents in some kind of repository, such as an Amazon S3 bucket or a Microsoft SharePoint site, you use a [data source
  connector](data-source.md "data-source.md") to index your documents from your repository.
- If you don't store your documents in a repository, you use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API operation to directly index your
  documents.
- For FAQ questions and answers, which must be stored in an Amazon Kendra (Amazon S3) bucket, you upload them from the bucket.
  You can create indexes with the Amazon Kendra console, the AWS CLI, or an AWS SDK. For information about the types of documents that
  can be indexed, see [Document types](index-document-types.md "index-document-types.md").
