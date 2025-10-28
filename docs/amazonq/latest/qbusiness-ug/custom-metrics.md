# Viewing metrics

After a sync job is finished, you can use the `DataSourceSyncJobMetrics`
API operation to get the metrics associated with the sync job. Use this API operation to
monitor your custom data source syncs.

You can submit the same document multiple times, either as part of the
`BatchPutDocument` operation, the `BatchDeleteDocument`
operation, or if the document is submitted for both addition and deletion, Regardless of
how you submit the document, it is only counted once in the metrics.

- `DocumentsAdded` – The number of documents submitted using
  the `BatchPutDocument` operation associated with this sync job that
  are added to the index for the first time. If a document is submitted for
  addition more than once in a sync, the document is only counted once in the
  metrics.
- `DocumentsDeleted` – The number of documents submitted using
  the `BatchDeleteDocument` operation associated with this sync job
  that are deleted from the index. If a document is submitted for deletion more
  than once in a sync, the document is only counted once in the metrics.
- `DocumentsFailed` – The number of documents associated with
  this sync job that failed indexing. These documents were accepted by Amazon Q for indexing but could not be indexed or deleted. If a document
  isn't accepted by Amazon Q, the identifier for the document is
  returned in the `FailedDocuments` response property of the
  `BatchPutDocument` and `BatchDeleteDocument`
  operations.
- `DocumentsModified` – The number of modified documents
  submitted using the `BatchPutDocument` operation associated with this
  sync job that were modified in the Amazon Q index.
  Amazon Q also emits Amazon CloudWatch metrics while indexing documents.
  For more information, see [Monitoring Amazon Q with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

Amazon Q doesn't return the `DocumentsScanned` metric for custom
data sources.
