# Create a

simple magic command connection string

If your administrator has configured the connections to your data sources, follow these
steps to easily create a connection string in a notebook cell:

1. Open a notebook cell that uses `%%sm_sql`.
2. Select a pre-configured connection to your desired data source from the connection
   dropdown menu above the cell.
3. This will automatically populate the parameters needed to query that data
   source.
   Alternatively, you can specify connection properties inline in the cell.

Choosing a connection from the dropdown menu inserts the following two parameters into
the default magic command string. The parameters contain the connection information your
administrator configured.

- `--metastore-id`: The name of the connection object that holds your
  connection parameters.
- `--metastore-type`: The type of meta-store corresponding to
  `--metastore-id`. The SQL extension uses AWS Glue connections as a
  connection meta-store. This value is automatically set to
  `GLUE_CONNECTION`.
  For example, the connection string to a pre-configured Amazon Athena data store looks like
  the following:

```
%%sm_sql --metastore-id `athena-connection-name` --metastore-type GLUE_CONNECTION
```
