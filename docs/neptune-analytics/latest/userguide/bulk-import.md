

# Bulk import data into a graph
<a name="bulk-import"></a>

 The task system in Neptune Analytics provides a powerful and flexible way to bulk import data into your graph. The `import` task is specifically designed to handle large-scale data ingestion from various data [formats](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data-formats.html). 

 To initiate a bulk data import, you would first create an import task by specifying the data source, the target graph, and any necessary configuration options. This can be done through the AWS console or programmatically via the API. 

 Throughout the import process, you can monitor the progress of the import task through the user interface or via API calls. Progress reports, and any potential errors or warnings will be accessible in your CloudWatch account, allowing for close monitoring and [troubleshooting](bulk-import-troubleshooting.md) if needed. 

 Importing of data through Import Task is supported in two ways: 
+  During graph creation: [Create a graph from Amazon S3, a Neptune cluster, or a snapshot](bulk-import-into-a-graph.md) 
+  On an existing empty graph: [Bulk import data into an existing Neptune Analytics graph](loading-data-existing-graph.md) 