# Querying Worldwide Event Attendance (Test

Product) data
with
an Amazon Redshift
cluster
(console)

The following procedure shows how to set up and query the datashare using the Amazon Redshift
console.

###### To query Worldwide Event Attendance (Test Product) data on Amazon Redshift (console)

1. Open and sign in to the Amazon Redshift console.
2. Choose **Clusters**, and choose your existing RA3
   cluster.
3. Choose the **Datashares** tab.
4. Select the datashare you want to create the database from.
5. Under **Subscriptions to AWS Data Exchange datashares**, choose
   **Create database from datashare**.
6. In **Create database from datashare**, enter the
   **Database name** for your new database, and then choose
   **Create**.
7. Choose the **Marketplace** icon on the navigation pane, and
   open the **Query editor**.
8. Under **Resources**, select a database and a schema.
9. Run the following SQL query.

`select * from database.schema.table`
