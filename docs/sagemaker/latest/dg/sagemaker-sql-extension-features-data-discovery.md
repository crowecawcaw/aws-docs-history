# Browse data using SQL extension

To open the SQL extension user interface (UI), choose the SQL extension icon
(
![Purple circular icon with a clock symbol representing time or scheduling.](images/studio/sqlexplorer/sqlexplorer-icon.png)
) in the navigation pane of your JupyterLab application in
Studio. The left panel data discovery view expands and displays all pre-configured data
store connections to Amazon Athena, Amazon Redshift, and Snowflake.

From there, you can:

- Expand a specific connection to explore its databases, schemas, tables or views, and
  columns.
- Search for a specific connection using the search box in the SQL extension UI. The
  search returns any databases, schemas, tables, or views that partially match the string
  you enter.

###### Note

If Athena is already set up in your AWS account, you can enable a
`default-athena-connection` in your JupyterLab application. This allows you to
run Athena queries without needing to manually create the connection. To enable the default
Athena connection:

1. Check with your administrator that your execution role has the required permissions
   to access Athena and the AWS Glue catalog. For details on the permissions required, see
   [Configure an
   AWS Glue connection for Athena](sagemaker-sql-extension-datasources-glue-connection.md#sagemaker-sql-extension-athena-glue-connection-config "sagemaker-sql-extension-datasources-glue-connection.md#sagemaker-sql-extension-athena-glue-connection-config")
2. In your JupyterLab application, navigate to the **Settings** menu
   in the top navigation bar and open the **Settings Editor** menu.
3. Choose **Data Discovery**.
4. Check the box for **Enable default Athena connection**.
5. You can update the default `primary` WorkGroup if needed.
   To query a database, schema, or table in a JupyterLab notebook, from a given connection
   in the SQL extension pane:

- Choose the three dots icon (
  ![SQL extension three dots icon.](images/studio/sqlexplorer/sqlexplorer-3dots-icon.png)
  ) on the right side of any database, schema, or table.
- Select **Query in notebook** from the menu.

This automatically populates a notebook cell in JupyterLab with the relevant
`%%sm_sql` magic command to connect to the data source. It also adds a sample
SQL statement to help you start querying right away. You can further refine the SQL query
using the auto-complete and highlighting features of the extension. See [SQL editor features of the
JupyterLab SQL extension](sagemaker-sql-extension-features-editor.md "sagemaker-sql-extension-features-editor.md") for more information on using the
SQL extension SQL editor.
At the table level, the three dots icon provides the additional option to choose to
**Preview** a table's metadata.

The JupyterLab notebook cell content below shows an example of what is automatically
generated when selecting the **Query in notebook** menu on a
`redshift-connection` data source in the SQL extension pane.

```
%%sm_sql --metastore-id redshift-connection --metastore-type GLUE_CONNECTION

-- Query to list tables from schema 'dev.public'
SHOW TABLES
FROM
  SCHEMA "dev"."public"
```

Use the _less than_ symbol (
![Icon to clear the SQL extension search box.](images/studio/sqlexplorer/sqlexplorer-search-clear.png)
) at the top of the SQL extension pane to clear the search box or return
to the list of your connections.

###### Note

The extension caches your exploration results for fast access. If the cached results are
outdated or a connection is missing from your list, you can manually refresh the cache by
choosing the **Refresh** button at the bottom of the SQL extension panel.
For more information on connection caching, see [SQL extension
connection caching](sagemaker-sql-extension-features-connection-caching.md "sagemaker-sql-extension-features-connection-caching.md").
