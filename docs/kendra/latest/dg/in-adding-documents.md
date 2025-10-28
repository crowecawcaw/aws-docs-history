# Adding documents directly to an index with batch

upload

You can add documents directly to an index using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
API. You can't add documents directly using the console. If you use the console, you
connect to a data source to add documents to your index. Documents can be added from an
S3 bucket or supplied as binary data. For a list of document types supported by Amazon Kendra see [Types of documents](index-document-types.md "index-document-types.md").

Adding documents to an index using `BatchPutDocument` is an asynchronous
operation. After you call the `BatchPutDocument` API, you use the [BatchGetDocumentStatus](../APIReference/API_BatchGetDocumentStatus.md "../APIReference/API_BatchGetDocumentStatus.md") API to monitor the progress of indexing your
documents. When you call the `BatchGetDocumentStatus` API with a list of
document IDs, it returns the status of the document. When the status of the document is
`INDEXED` or `FAILED`, processing of the document is complete.
When the status is `FAILED`, the `BatchGetDocumentStatus` API
returns the reason that the document couldn't be indexed.

If you want to alter your content and document metadata fields or attributes during
the document ingestion process, see [Amazon Kendra Custom
Document Enrichment](custom-document-enrichment.md "custom-document-enrichment.md"). If you want to use a custom data source, each document
you submit using the `BatchPutDocument` API requires a data source ID and
execution ID as attributes or fields. For more information, see [Required
attributes for custom data sources](data-source-custom.md#custom-required-attributes "data-source-custom.md#custom-required-attributes").

###### Note

Each document ID must be unique per index. You cannot create a data source to
index your documents with their unique IDs and then use the
`BatchPutDocument` API to index the same documents, or vice versa.
You can delete a data source and then use the `BatchPutDocument` API to
index the same documents, or vice versa. Using the `BatchPutDocument` and
`BatchDeleteDocument` APIs in combination with an Amazon Kendra
data source connector for the same set of documents could cause inconsistencies with
your data. Instead, we recommend using the [Amazon Kendra custom data
source connector](data-source-custom.md "data-source-custom.md").

The following developer guide documents show how to add documents directly to an
index.

###### Topics

- [Adding documents with the BatchPutDocument
  API](#in-adding-binary-doc "#in-adding-binary-doc")
- [Adding documents from an S3 bucket](#in-adding-plain-text "#in-adding-plain-text")

## Adding documents with the BatchPutDocument

API

The following example adds a blob of text to an index by calling [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md").
You can use the `BatchPutDocument` API to add documents directly to your
index. For a list of document types supported by Amazon Kendra see [Types of
documents](index-document-types.md "index-document-types.md").

For an example of creating an index using the AWS CLI and SDKs, see
[Creating an
index](create-index.md "create-index.md"). To set up the CLI and SDKs, see [Setting up Amazon Kendra](setup.md "setup.md").

###### Note

Files added to the index must be in a UTF-8 encoded byte stream.

In the following examples, UTF-8 encoded text is added to the index.

CLI
In the AWS Command Line Interface, use the following command. The command
is formatted for Linux and macOS. If you are using Windows, replace the
Unix line continuation character (\) with a caret (^).

```
aws kendra batch-put-document \
   --index-id `index-id` \
   --documents '{"Id":"doc-id-1", "Blob":"Amazon.com is an online retailer.", "ContentType":"PLAIN_TEXT", "Title":"Information about Amazon.com"}'
```

Python

```
import boto3

kendra = boto3.client("kendra")

# Provide the index ID
index_id = "index-id"

# Provide the title and text
title = "Information about Amazon.com"
text = "Amazon.com is an online retailer."

document = {
    "Id": "1",
    "Blob": text,
    "ContentType": "PLAIN_TEXT",
    "Title": title
}

documents = [
    document
]

result = kendra.batch_put_document(
    IndexId = index_id,
    Documents = documents
)

print(result)
```

Java

```
package com.amazonaws.kendra;


import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.services.kendra.KendraClient;
import software.amazon.awssdk.services.kendra.model.BatchPutDocumentRequest;
import software.amazon.awssdk.services.kendra.model.BatchPutDocumentResponse;
import software.amazon.awssdk.services.kendra.model.ContentType;
import software.amazon.awssdk.services.kendra.model.Document;

public class AddDocumentsViaAPIExample {
    public static void main(String[] args) {
        KendraClient kendra = KendraClient.builder().build();

        String indexId = "yourIndexId";

        Document testDoc = Document
            .builder()
            .title("The title of your document")
            .id("a_doc_id")
            .blob(SdkBytes.fromUtf8String("your text content"))
            .contentType(ContentType.PLAIN_TEXT)
            .build();

        BatchPutDocumentRequest batchPutDocumentRequest = BatchPutDocumentRequest
            .builder()
            .indexId(indexId)
            .documents(testDoc)
            .build();

        BatchPutDocumentResponse result = kendra.batchPutDocument(batchPutDocumentRequest);

        System.out.println(String.format("BatchPutDocument Result: %s", result));
    }
}

```

## Adding documents from an S3 bucket

You can add documents directly to your index from an Amazon S3 bucket
using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
API. You can add up to 10 documents in the same call. When you use an S3 bucket, you
must provide an IAM role with permission to access the bucket that
contains your documents. You specify the role in the `RoleArn`
parameter.

Using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
API to add documents from an Amazon S3 bucket is a one-time operation. To
keep an index synchronized with the contents of a bucket, create an Amazon S3 data source. For more information, see [Amazon S3 data
source](data-source-s3.md "data-source-s3.md").

For an example of creating an index using the AWS CLI and SDKs, see
[Creating an
index](create-index.md "create-index.md"). To set up the CLI and SDKs, see [Setting up Amazon Kendra](setup.md "setup.md"). For
information on creating an S3 bucket, see [Amazon Simple Storage Service documentation](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").

In the following example, two Microsoft Word documents are added to the index
using the `BatchPutDocument` API.

Python

```
import boto3

kendra = boto3.client("kendra")

# Provide the index ID
index_id = "index-id"
# Provide the IAM role ARN required to index documents in an S3 bucket
role_arn = "arn:aws:iam::${acccountID}:policy/${roleName}"

doc1_s3_file_data = {
    "Bucket": "bucket-name",
    "Key": "document1.docx"
}

doc1_document = {
    "S3Path": doc1_s3_file_data,
    "Title": "Document 1 title",
    "Id": "doc_1"
}

doc2_s3_file_data = {
    "Bucket": "bucket-name",
    "Key": "document2.docx"
}

doc2_document = {
    "S3Path": doc2_s3_file_data,
    "Title": "Document 2 title",
    "Id": "doc_2"
}

documents = [
    doc1_document,
    doc2_document
]

result = kendra.batch_put_document(
    Documents = documents,
    IndexId = index_id,
    RoleArn = role_arn
)

print(result)
```

Java

```
package com.amazonaws.kendra;

import software.amazon.awssdk.services.kendra.KendraClient;
import software.amazon.awssdk.services.kendra.model.BatchPutDocumentRequest;
import software.amazon.awssdk.services.kendra.model.BatchPutDocumentResponse;
import software.amazon.awssdk.services.kendra.model.Document;
import software.amazon.awssdk.services.kendra.model.S3Path;

public class AddFilesFromS3Example {
    public static void main(String[] args) {
        KendraClient kendra = KendraClient.builder().build();

        String indexId = "yourIndexId";
        String roleArn = "yourIndexRoleArn";

        Document pollyDoc = Document
            .builder()
            .s3Path(
                S3Path.builder()
                .bucket("amzn-s3-demo-bucket")
                .key("What is Amazon Polly.docx")
                .build())
            .title("What is Amazon Polly")
            .id("polly_doc_1")
            .build();

        Document rekognitionDoc = Document
            .builder()
            .s3Path(
                S3Path.builder()
                .bucket("amzn-s3-demo-bucket")
                .key("What is Amazon Rekognition.docx")
                .build())
            .title("What is Amazon rekognition")
            .id("rekognition_doc_1")
            .build();

        BatchPutDocumentRequest batchPutDocumentRequest = BatchPutDocumentRequest
            .builder()
            .indexId(indexId)
            .roleArn(roleArn)
            .documents(pollyDoc, rekognitionDoc)
            .build();

        BatchPutDocumentResponse result = kendra.batchPutDocument(batchPutDocumentRequest);

        System.out.println(String.format("BatchPutDocument result: %s", result));
    }
}

```
