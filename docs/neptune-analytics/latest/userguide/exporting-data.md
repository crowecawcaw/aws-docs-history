

# Exporting data from a Neptune Analytics graph
<a name="exporting-data"></a>

 Neptune Analytics provides export functionality to allow you to export your graph into columnar structured .csv and .parquet files that are compatible with the [bulk import](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import.html) and [batch load](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/batch-load.html) functionality. This functionality facilitates workflows such as performing analytics on a Neptune Analytics graph, exporting the result for external processing and transformation, and importing the results into Neptune Database, Neptune Analytics, or other software for further analysis. Additionally, the export functionality allows you to specify a filter defining labels and properties of vertices and edges to include in your export, or simply to export your entire graph. Using Neptune Analytics export with the import and export features of Neptune Database also facilitates a round-tripping use case from Neptune Database, allowing you to create a temporary Neptune Analytics graph from your Neptune Database, run advanced analytics, and export the results back into Neptune Database. 

## Limitations and unsupported features
<a name="exporting-data-limitations"></a>
+  If your graph data contains multi-line string values, exporting to CSV completes successfully, but the exported CSV files may not be re-importable into Neptune Analytics. This is because multi-line string values are not supported during CSV import into Neptune Analytics, and import behavior is undefined for datasets that contain them. Exporting to Parquet format is not affected by this limitation. Importing the exported CSV files into Neptune Database is also not affected. For more information, see [CSV limitations and unsupported features](using-CSV-data.md#using-CSV-data-limitations). 

## Relevant SDK/CLI commands
<a name="exporting-SDK-CLI-commands"></a>
+  `start-export-task` - This command starts an export task on an existing graph in Neptune Analytics. It allows you to export your graph into columnar structured .csv and .parquet files. 
+  `get-export-task` - This command queries the status of an export task that was started using the `start-export-task` command. 
+  `list-export-tasks` - This command lists all of the export tasks that have been run on a specified Neptune Analytics graph. 

## Permission setup
<a name="exporting-permission-setup"></a>

 See [Import/export permissions](import-export-permissions.md) to learn more about setting up the required permissions for exporting data from a Neptune Analytics graph. 