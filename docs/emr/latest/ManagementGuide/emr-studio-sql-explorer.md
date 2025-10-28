# Browse data with SQL Explorer for EMR Studio

###### Note

SQL Explorer for EMR Studio isn't supported with Amazon EMR Serverless
interactive applications or in a Studio with IAM Identity Center trusted identity propagation enabled.

This topic provides information to help you get started with SQL Explorer in
Amazon EMR Studio. SQL Explorer is a single-page tool in your Workspace that
helps you understand the data sources in your EMR cluster's data catalog. You can use
SQL Explorer to browse your data, run SQL queries to retrieve data, and download
query results.

SQL Explorer supports Presto. Before you use SQL Explorer, make sure you
have a cluster that uses Amazon EMR version 5.34.0 or later or version 6.4.0 or later with Presto
installed. The Amazon EMR Studio SQL Explorer doesn't support Presto clusters that you've
configured with in-transit encryption. This is because Presto runs in TLS mode on these
clusters.

## Browse your cluster's data catalog

SQL Explorer provides a catalog browser interface that you can use to explore
and understand how your data is organized. For example, you can use the data catalog browser
to verify table and column names before you write a SQL query.

###### To browse your data catalog

1. Open SQL Explorer in your Workspace.
2. Make sure your Workspace is attached to an EMR cluster running on EC2
   that uses Amazon EMR version 6.4.0 or later with Presto installed. You can choose an existing
   cluster, or create a new one. For more information, see [Attach a compute to an EMR Studio
   Workspace](emr-studio-create-use-clusters.md "emr-studio-create-use-clusters.md").
3. Select a **Database** from the dropdown list to browse.
4. Expand a table in your database to see the table's column names. You can also enter
   a keyword in the search bar to filter table results.

## Run a SQL query to retrieve data

###### To retrieve data with a SQL query and download the results

1. Open SQL Explorer in your Workspace.
2. Make sure your Workspace is attached to an EMR cluster running on EC2
   with Presto and Spark installed. You can choose an existing cluster, or create a new
   one. For more information, see [Attach a compute to an EMR Studio
   Workspace](emr-studio-create-use-clusters.md "emr-studio-create-use-clusters.md").
3. Select **Open editor** to open a new editor tab in your
   Workspace.
4. Compose your SQL query in the editor tab.
5. Choose **Run**.
6. View your query results under **Result preview**.
   SQL Explorer displays the first 100 results by default. You can choose a
   different number of results to display (up to 1000) using the **Preview first
   100 query results** drowdown.
7. Choose **Download results** to download your results in CSV format.
   You can download up to 1000 rows of results.
