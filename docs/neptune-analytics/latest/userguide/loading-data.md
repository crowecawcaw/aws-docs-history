# Loading data into a Neptune Analytics graph

Neptune Analytics provides several options for loading data into a graph, supporting both RDF (Resource Description Framework)
and LPG (Labeled Property Graph) models.

- **Bulk import**  –  
  Designed to handle large scale data ingestion and is the fastest way to load large volumes of data. Bulk import runs a
  task to load data from files in [Amazon S3](bulk-import-create-from-s3.md "bulk-import-create-from-s3.md"). This option
  **must** be done on an empty graph, either at creation time using the
  [CreateGraphUsingImportTask](../apiref/API_CreateGraphUsingImportTask.md "../apiref/API_CreateGraphUsingImportTask.md") action,
  or on an existing graph using the [StartImportTask](../apiref/API_StartImportTask.md "../apiref/API_StartImportTask.md") action.
- **Batch load**  –  
  Designed to handle incremental data ingestion to existing graphs using files in Amazon S3. This can be used to add more data
  or update single cardinality property values in existing graph data. The volume of data that can be ingested in a single
  request is lower than what bulk import can support.
- **openCypher queries**  –  
  Add more data through [queries](query.md "query.md"), if data is not available from files in Amazon S3 or the data
  volume is small. This is also a more generic approach for conditional inserts based on data already in the graph,
  and updating contents of the graph.

###### Warning

Be cautious while loading a file of edges. If the same edge file is loaded twice, duplicate edges will be inserted into
the graph which can lead to unintended results.

Also, while using the SDK/CLI command execute-query to run neptune.load(), it is recommended to increase the timeout window
and disable the retries for the SDK/CLI.

For more information about increasing the timeout and disabling retries, see
[ExecuteQuery](query-APIs-execute-query.md "query-APIs-execute-query.md").

###### Topics

- [Data format for loading from Amazon S3 into Neptune Analytics](loading-data-formats.md "loading-data-formats.md")
- [Batch load](batch-load.md "batch-load.md")
- [Bulk import data into a graph](bulk-import.md "bulk-import.md")
- [neptune.read()](neptune-read.md "neptune-read.md")
