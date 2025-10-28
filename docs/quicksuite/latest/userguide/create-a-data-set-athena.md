# Creating a dataset using Amazon Athena

data

Use the following procedure to create a new dataset that connects to Amazon Athena data or
to Athena Federated Query data.

###### To connect to Amazon Athena

1.  Begin by creating a new dataset. Choose **Data** from the
    navigation pane at left.
2.  Choose **Create**, then choose **New
    dataset**.
3.  1. To use an existing Athena connection profile (common), choose the card
       for the existing data source that you want to use. Choose
       **Select**.

    Cards are labeled with the Athena data source icon and the name
    provided by the person who created the connection. 2. To create a new Athena connection profile (less common), use the
    following steps:

        1. Choose **New data source**, then choose the
         **Athena** data source card.
        2. Choose **Next**.
        3. For **Data source name**, enter a descriptive
         name.
        4. For **Athena workgroup**, choose your
         workgroup.
        5. Choose **Validate connection** to test the
         connection.
        6. Choose **Create data source**.
        7. (Optional) Select an IAM role ARN for queries to run as.

4.  On the **Choose your table** screen, do the following:
    1.  For **Catalog**, choose one of the following:
        - If you are using Athena Federated Query, choose the catalog you
          want to use.
        - Otherwise, choose **AwsDataCatalog**.

    2.  Choose one of the following:

            * To write a SQL query, choose **Use custom
             SQL**.
            * To choose a database and table, choose your catalog that
             contains your databases from the dropdown under
             **Catalog**. Then, choose a database from
             the dropdown under **Database** and choose a
             table from the **Tables** list that appears for
             your database.If you don't have the right permissions, you receive the following error

        message: "You don't have sufficient permissions to connect to this dataset or
        run this query." Contact your Quick Suite administrator for assistance.
        For more information, see [Authorizing connections to Amazon Athena](athena.md "athena.md").

5.  Choose **Edit/preview data**.
6.  Create a dataset and analyze the data using the table by choosing
    **Visualize**. For more information, see [Analyses and reports: Visualizing data in
    Amazon Quick Sight](working-with-visuals.md "working-with-visuals.md").
