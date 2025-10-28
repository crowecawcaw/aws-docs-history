# Creating a Vertica source node

## Prerequisites needed

- A Vertica type AWS Glue Data Catalog connection, `connectionName` and a
  temporary Amazon S3 location, `tempS3Path`, as described in the previous
  section, [Creating a Vertica connection](creating-vertica-connection.md "creating-vertica-connection.md").
- A Vertica table you would like to read from, `tableName`, or query `targetQuery`.

## Adding a Vertica data source

###### To add a **Data source – Vertica** node:

1. Choose the connection for your Vertica data source. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create Vertica connection**. For more information see
   the previous section, [Creating a Vertica connection](creating-vertica-connection.md "creating-vertica-connection.md").

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Choose the **Database** containing your table. 3. Choose the **Staging area in Amazon S3**, enter an S3A URI to `tempS3Path`. 4. Choose the **Vertica Source**.

    * **Choose a single table** – access all data from a single table.
    * **Enter custom query**  – access a dataset from multiple
     tables based on your custom query.

5. If you chose a single table, enter `tableName` and optionally select a **Schema**.

If you chose **Enter custom query**, enter a SQL SELECT query and optionally select a **Schema**. 6. In **Custom Vertica properties**, enter parameters and values as needed.
