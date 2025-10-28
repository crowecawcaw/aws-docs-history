# Exporting data from a Neptune Analytics graph

Neptune Analytics provides export functionality to allow you to export your graph into columnar structured .csv and .parquet files that
are compatible with the [bulk import](bulk-import.md "bulk-import.md")
and [batch load](batch-load.md "batch-load.md") functionality.
This functionality facilitates workflows such as performing analytics on a Neptune Analytics graph, exporting the result for external
processing and transformation, and importing the results into Neptune Database, Neptune Analytics, or other software for further
analysis. Additionally, the export functionality allows you to specify a filter defining labels and properties of vertices and
edges to include in your export, or simply to export your entire graph. Using Neptune Analytics export with the import and export
features of Neptune Database also facilitates a round-tripping usecase from Neptune Database, allowing you to create
a temporary Neptune Analytics graph from your Neptune Database, run advanced analytics, and export the results back into Neptune Database.

## Relevant SDK/CLI commands

- `start-export-task` - This command starts an export task on an existing graph in Neptune Analytics. It allows
  you to export your graph into columnar structured .csv and .parquet files.
- `get-export-task` - This command queries the status of an export task that was started using the
  `start-export-task` command.
- `list-export-tasks` - This command lists all of the export tasks that have been ran on a specified
  Neptune Analytics graph.

## Permission setup

See [Import/export permissions](import-export-permissions.md "import-export-permissions.md") to learn more about setting up the
required permissions for exporting data from a Neptune Analytics graph.
