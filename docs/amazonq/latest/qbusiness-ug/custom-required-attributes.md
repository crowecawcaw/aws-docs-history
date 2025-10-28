# Required attributes

When you submit a document to Amazon Q using the
`BatchPutDocument` API operation, you must provide the following two
attributes for each document:

- `_data_source_id` – The identifier of the data source. This
  is returned when you create the data source with either the console or the
  `CreateDataSource` API operation.
- `_data_source_sync_job_execution_id` – The identifier of the
  sync run. This is returned when you start the index synchronization with the
  `StartDataSourceSyncJob` operation.
  The following is the JSON required to index a document using a custom data
  source.

```
{
    "Documents": [
        {
            "Attributes": [
                {
                    "Key": "_data_source_id",
                    "Value": {
                        "StringValue": "`data source identifier`"
                    }
                },
                {
                    "Key": "_data_source_sync_job_execution_id",
                    "Value": {
                        "StringValue": "`sync job identifier`"
                    }
                }
            ],
            "Blob": "`document content`",
            "ContentType": "`content type`",
            "Id": "`document identifier`",
            "Title": "`document title`"
        }
    ],
    "IndexId": "`index identifier`",
    "RoleArn": "`IAM role ARN`"
}
```

When you remove a document from the index using the `BatchDeleteDocument`
API operation, you must specify the following two fields in the
`DataSourceSyncJobMetricTarget` parameter:

- `DataSourceId` – The identifier of the data source. This is
  returned when you create the data source with either the console or the
  `CreateDataSource` API operation.
- `DataSourceSyncJobId` – The identifier of the sync run. This
  is returned when you start the index synchronization with the
  `StartDataSourceSyncJob` operation.
  The following is the JSON required to delete a document from the index using the
  `BatchDeleteDocument` operation.

```
{
    "DataSourceSyncJobMetricTarget": {
        "DataSourceId": "`data source identifier`",
        "DataSourceSyncJobId": "`sync job identifier`"
    },
    "DocumentIdList": [
        "`document identifier`"
    ],
    "IndexId": "`index identifier`"
}
```
