# Blueprints and workflows in Lake Formation

A workflow encapsulates a complex multi-job extract, transform, and load (ETL) activity.
Workflows generate AWS Glue crawlers, jobs, and triggers to orchestrate the loading and
update of data. Lake Formation executes and tracks a workflow as a single entity. You can configure a
workflow to run on demand or on a schedule.

###### Note

Spark parquet writer doesn't support special characters in column names. This is a technical limitation of the writer itself, not a configuration issue.

Workflows that you create in Lake Formation are visible in the AWS Glue console as a directed acyclic
graph (DAG). Each DAG node is a job, crawler, or trigger. To monitor progress and
troubleshoot, you can track the status of each node in the workflow.

When a Lake Formation workflow has completed, the user who ran the workflow is granted the Lake Formation
`SELECT` permission on the Data Catalog tables that the workflow creates.

You can also create workflows in AWS Glue. However, because Lake Formation enables you to create a
workflow from a blueprint, creating workflows is much simpler and more automated in Lake Formation. Lake Formation
provides the following types of blueprints:

- **Database snapshot** – Loads or reloads data from all tables
  into the data lake from a JDBC source. You can exclude some data from the source based on
  an exclude pattern.
- **Incremental database** – Loads only new data into the data
  lake from a JDBC source, based on previously set bookmarks. You specify the individual
  tables in the JDBC source database to include. For each table, you choose the bookmark
  columns and bookmark sort order to keep track of data that has previously been loaded. The
  first time that you run an incremental database blueprint against a set of tables, the
  workflow loads all data from the tables and sets bookmarks for the next incremental
  database blueprint run. You can therefore use an incremental database blueprint instead of
  the database snapshot blueprint to load all data, provided that you specify each table in
  the data source as a parameter.
- **Log file** – bulk loads data from log file sources,
  including AWS CloudTrail, Elastic Load Balancing logs, and Application Load Balancer logs.
  Use the following table to help decide whether to use a database snapshot or incremental
  database blueprint.

| Use database snapshot when...                                                                                                                                                                                     | Use incremental database when...                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Schema evolution is flexible. (Columns are re-named, previous columns are<br>deleted, and new columns are added in their place.)<br>• Complete consistency is needed between the source and the<br>destination. | • Schema evolution is incremental. (There is only successive addition of<br>columns.)<br>• Only new rows are added; previous rows are not updated. |

###### Note

Users cannot edit blue prints and workflows created by Lake Formation.
