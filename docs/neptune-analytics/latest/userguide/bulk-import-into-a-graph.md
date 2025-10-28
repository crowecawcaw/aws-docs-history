# Create a graph from Amazon S3, a Neptune cluster, or a snapshot

You can create a Neptune Analytics graph directly from Amazon S3 or from Neptune using the
[CreateGraphUsingImportTask](../apiref/API_CreateGraphUsingImportTask.md "../apiref/API_CreateGraphUsingImportTask.md") API.
This is recommended for importing large graphs from files in Amazon S3 (>50GB of data), importing from existing Neptune
clusters, or importing from existing Neptune snapshots. This API automatically analyzes the data, provisions a new
graph based on the analysis, and imports data as one atomic operation using maximum available resources.

###### Note

The graph is made available for querying only after the data loading is completed successfully.

If errors are encountered during the import process, Neptune Analytics will automatically roll back the provisioned resources, and
perform the cleanup. No manual cleanup actions are needed. Error details are available in the CloudWatch logs. See
[troubleshooting](bulk-import-troubleshooting.md "bulk-import-troubleshooting.md") for more details.

###### Topics

- [Creating a Neptune Analytics graph from Amazon S3](bulk-import-create-from-s3.md "bulk-import-create-from-s3.md")
- [Creating a Neptune Analytics graph from Neptune cluster or snapshot](bulk-import-create-from-neptune.md "bulk-import-create-from-neptune.md")
