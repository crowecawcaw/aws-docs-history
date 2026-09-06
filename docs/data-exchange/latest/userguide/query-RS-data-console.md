

# Querying Worldwide Event Attendance (Test Product) data with an Amazon Redshift cluster (console)
<a name="query-RS-data-console"></a>

The following procedure shows how to set up and query the datashare using the Amazon Redshift console.

**To query Worldwide Event Attendance (Test Product) data on Amazon Redshift (console)**

1. Open and sign in to the Amazon Redshift console.

1. Choose **Clusters**, and choose your existing RA3 cluster.

1. Choose the **Datashares** tab.

1. Select the datashare you want to create the database from.

1. Under **Subscriptions to AWS Data Exchange datashares**, choose **Create database from datashare**.

1. In **Create database from datashare**, enter the **Database name** for your new database, and then choose **Create**. 

1. Choose the **Marketplace** icon on the navigation pane, and open the **Query editor**. 

1. Under **Resources**, select a database and a schema. 

1. Run the following SQL query. 

   `select * from database.schema.table`