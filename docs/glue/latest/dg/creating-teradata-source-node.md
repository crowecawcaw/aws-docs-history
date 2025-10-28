# Creating a Teradata source node

## Prerequisites needed

- An AWS Glue Teradata Vantage connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a Teradata Vantage connection](creating-teradata-connection.md "creating-teradata-connection.md").
- Appropriate permissions on your job to read the secret used by the connection.
- A Teradata table you would like to read from, `tableName`, or query `targetQuery`.

## Adding a Teradata data source

###### To add a **Data source – Teradata** node:

1. Choose the connection for your Teradata data source. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create a new connection**. For more information see
   the previous section, [Creating a Teradata Vantage connection](creating-teradata-connection.md "creating-teradata-connection.md").

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Choose a **Teradata Source** option:

    * **Choose a single table** – access all data from a single table.
    * **Enter custom query**  – access a dataset from multiple
     tables based on your custom query.

3. If you chose a single table, enter `tableName`.

If you chose **Enter custom query**, enter a SQL SELECT query. 4. In **Custom Teradata properties**, enter parameters and values as needed.
