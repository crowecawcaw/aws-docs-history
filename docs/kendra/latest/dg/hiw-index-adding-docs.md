

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Adding documents to an index in Amazon Kendra
<a name="hiw-index-adding-docs"></a>

The way you add documents to an index depends on how you store your documents.
+ If you store your documents in some kind of repository, such as an Amazon S3 bucket or a Microsoft SharePoint site, you use a [data source connector](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) to index your documents from your repository.
+ If you don't store your documents in a repository, you use the [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchPutDocument.html) API operation to directly index your documents. 
+ For FAQ questions and answers, which must be stored in an Amazon Kendra (Amazon S3) bucket, you upload them from the bucket.

You can create indexes with the Amazon Kendra console, the AWS CLI, or an AWS SDK. For information about the types of documents that can be indexed, see [Document types](https://docs.aws.amazon.com/kendra/latest/dg/index-document-types.html).