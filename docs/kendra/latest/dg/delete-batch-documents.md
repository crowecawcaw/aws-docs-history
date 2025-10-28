# Deleting batch uploaded documents

You can delete documents directly from an index using the [BatchDeleteDocument](../APIReference/API_BatchDeleteDocument.md "../APIReference/API_BatchDeleteDocument.md") API.
You can't delete documents directly using the console. If you use the console, you can either
delete specific documents from your data source repository and re-sync with your index or
delete the entire data source connector.

Deleting documents from an index using `BatchDeleteDocument` is an asynchronous
operation. After you call the `BatchDeleteDocument` API, you use the
[BatchGetDocumentStatus](../APIReference/API_BatchGetDocumentStatus.md "../APIReference/API_BatchGetDocumentStatus.md") API to monitor the progress of deleting your documents.
When a document is deleted from the index, Amazon Kendra returns `NOT_FOUND`
as the status.

###### Note

Deleting documents from an index using `BatchDeleteDocument` could take up
to an hour or more, depending on the number of documents you want to delete.

###### To delete batch uploaded documents from an index (CLI)

- In the AWS Command Line Interface, use the following command. The command is
  formatted for Linux and macOS. If you are using Windows, replace the Unix line
  continuation character (\) with a caret (^).

```
aws kendra batch-delete-document \
   --index-id `index-id` \
   --document-id-list 'doc-id-1' 'doc-id-2'
```
