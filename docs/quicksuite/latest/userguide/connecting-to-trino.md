# Using Trino with Amazon Quick Sight

Trino is a massively parallel processing (MPP) query engine built to quickly query
data lakes with petabytes of data. Use this section to learn how to connect from Amazon Quick Sight
to Trino. All traffic between Amazon Quick Sight and Trino is enabled by SSL. Amazon Quick Sight supports
basic username and password authentication to Trino.

## Creating a data source connection for

Trino

1. Begin by creating a new dataset. From the left navigation pane, choose
   **Data**. Choose **Create** then
   **New Dataset**.
2. Choose the **Trino** data source card.
3. For **Data source name**, enter a descriptive name for
   your Trino data source connection. Because you can create many datasets from
   a connection to Trino, it's best to keep the name simple.
4. For **Connection type**, select the type of network
   you're using. Choose **Public network** if your data is
   shared publicly. Choose **VPC** if your data is inside a
   VPC. To configure a VPC connection in Amazon Quick Sight, see [Configuring the VPC connection in Amazon Quick Sight](../../../quicksight/latest/user/vpc-creating-a-connection-in-quicksight.md "../../../quicksight/latest/user/vpc-creating-a-connection-in-quicksight.md").
5. For **Database server**, enter the hostname specified in
   your Trino connection details.
6. For **Catalog**, enter the catalog specified in your
   Trino connection details.
7. For **Port**, enter the port specified in your Trino
   connection details.
8. For **Username** and **Password**, enter
   your Trino connection credentials.
9. To verify the connection is working, choose **Validate
   connection**.
10. To finish and create the data source, choose **Create data
    source**.

## Adding a new Amazon Quick Sight dataset for

Trino

After you go through the [data source creation process](../../../create-connection-to-starburst.md "../../../create-connection-to-starburst.md")
for Trino, you can create Trino datasets to use for analysis. You can create new
datasets from a new or an existing Trino data source. When you are creating a new
data source, Amazon Quick Sight immediately takes you to creating a dataset, which is step 3
below. If you're using an existing data source to create a new dataset, start from
step 1 below.

To create a dataset using a Trino data source, see the following steps.

1. From the start page, choose **Data**. Choose
   **Create** then **New
   dataset**.
2. Choose the Trino data source you created.
3. Choose **Create data set**.
4. To specify the table you want to connect to, choose a schema. If you don't
   want to choose a schema, you can also use your own SQL statement.
5. To specify the table you want to connect to, first select the
   **Schema** you want to use. For
   **Tables**, choose the table that you want to use. If
   you prefer to use your own SQL statement, select **Use custom
   SQL**.
6. Choose **Edit/Preview**.
7. (Optional) To add more data, use the following steps:
8. Choose **Add data** in the top right.
9. To connect to different data, choose **Switch data
   source**, and choose a different dataset.
10. Follow the prompts to finish adding data.
11. After adding new data to the same dataset, choose **Configure this
    join** (the two red dots). Set up a join for each additional
    table.
12. If you want to add calculated fields, choose **Add calculated
    field**.
13. Clear the check box for any fields that you want to omit.
14. Update any data types that you want to change.
15. When you are done, choose **Save** to save and close the
    dataset.

###### Note

Connectivity between Quick Sight and Trino was validated using Trino version 410.
