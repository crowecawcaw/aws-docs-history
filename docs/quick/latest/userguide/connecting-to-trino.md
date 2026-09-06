

# Using Trino with Amazon Quick Sight
<a name="connecting-to-trino"></a>

Trino is a massively parallel processing (MPP) query engine built to quickly query data lakes with petabytes of data. Use this section to learn how to connect from Amazon Quick Sight to Trino. All traffic between Amazon Quick Sight and Trino is enabled by SSL. Amazon Quick Sight supports basic username and password authentication to Trino.

## Creating a data source connection for Trino
<a name="create-connection-to-trino"></a>

1. Begin by creating a new dataset. From the left navigation pane, choose **Data**. Choose **Create** then **New Dataset**.

1. Choose the **Trino** data source card.

1. For **Data source name**, enter a descriptive name for your Trino data source connection. Because you can create many datasets from a connection to Trino, it's best to keep the name simple.

1. For **Connection type**, select the type of network you're using. Choose **Public network** if your data is shared publicly. Choose **VPC** if your data is inside a VPC. To configure a VPC connection in Amazon Quick Sight, see [ Configuring the VPC connection in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/vpc-creating-a-connection-in-quicksight.html).

1. For **Database server**, enter the hostname specified in your Trino connection details.

1. For **Catalog**, enter the catalog specified in your Trino connection details.

1. For **Port**, enter the port specified in your Trino connection details.

1. For **Username** and **Password**, enter your Trino connection credentials.

1. To verify the connection is working, choose **Validate connection**.

1. To finish and create the data source, choose **Create data source**.

## Adding a new Amazon Quick Sight dataset for Trino
<a name="create-dataset-using-trino"></a>

After you go through the [ data source creation process](https://docs.aws.amazon.com/create-connection-to-starburst.html) for Trino, you can create Trino datasets to use for analysis. You can create new datasets from a new or an existing Trino data source. When you are creating a new data source, Amazon Quick Sight immediately takes you to creating a dataset, which is step 3 below. If you're using an existing data source to create a new dataset, start from step 1 below.

To create a dataset using a Trino data source, see the following steps.

1. From the start page, choose **Data**. Choose **Create** then **New dataset**.

1. Choose the Trino data source you created.

1. Choose **Create data set**.

1. To specify the table you want to connect to, choose a schema. If you don't want to choose a schema, you can also use your own SQL statement.

1. To specify the table you want to connect to, first select the **Schema** you want to use. For **Tables**, choose the table that you want to use. If you prefer to use your own SQL statement, select **Use custom SQL**.

1. Choose **Edit/Preview**.

1. (Optional) To add more data, use the following steps:

1. Choose **Add data** in the top right.

1. To connect to different data, choose **Switch data source**, and choose a different dataset.

1. Follow the prompts to finish adding data.

1. After adding new data to the same dataset, choose **Configure this join** (the two red dots). Set up a join for each additional table.

1. If you want to add calculated fields, choose **Add calculated field**.

1. Clear the check box for any fields that you want to omit.

1. Update any data types that you want to change.

1. When you are done, choose **Save** to save and close the dataset.

**Note**  
Connectivity between Quick Sight and Trino was validated using Trino version 410.