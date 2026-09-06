

# Using Amazon Timestream data with Amazon Quick Sight
<a name="using-data-from-timestream"></a>

Following, you can find how to connect to your Amazon Timestream data using Amazon Quick Sight. For a brief overview, see the [Getting started with Amazon Timestream and Amazon QuickSight](https://youtu.be/TzW4HWl-L8s) video tutorial on YouTube. 

## Creating a new Amazon Quick Sight data source connection for a Timestream database
<a name="create-connection-to-timestream"></a>

Following, you can find how to connect to Amazon Timestream from Amazon Quick Sight.

Before you can proceed, Amazon Quick Sight needs to be authorized to connect to Amazon Timestream. If connections aren't enabled, you get an error when you try to connect. A Quick Sight administrator can authorize connections to AWS resources. To authorize, open the menu by clicking on your profile icon at top right. Choose **Manage QuickSight**, **Security & permissions**, **Add or remove**. Then enable the check box for Amazon Timestream, then choose **Update** to confirm. For more information, see [Configuring Amazon Quick Sight access to AWS data sources](access-to-aws-resources.md).

**To connect to Amazon Timestream**

1. Begin by creating a new dataset. Choose **Data** from the navigation pane at left. 

1. Choose **Create** then **New Dataset**.

1. Choose the Timestream data source card.

1. For **Data source name**, enter a descriptive name for your Timestream data source connection, for example `US Timestream Data`. Because you can create many datasets from a connection to Timestream, it's best to keep the name simple.

1. Choose **Validate connection** to check that you can successfully connect to Timestream.

1. Choose **Create data source** to proceed.

1. For **Database**, choose **Select** to view the list of available options. 

1. Choose the one you want to use, then choose **Select** to continue. 

1. Do one of the following:
   + To import your data into Quick Sight's in-memory engine (called SPICE), choose **Import to SPICE for quicker analytics**. 
   + To allow Quick Sight to run a query against your data each time you refresh the dataset or use the analysis or dashboard, choose **Directly query your data**. 

   If you want to enable autorefresh on a published dashboard that uses Timestream data, the Timestream dataset needs to use a direct query.

1. Choose **Edit/Preview** and then **Save** to save your dataset and close it.

1. Repeat these steps for the number of concurrent direct connections to Timestream that you want to open in a dataset. For example, let's say you want to use four tables in a Quick Sight dataset. Currently, Quick Sight datasets connect to only one table at a time from a Timestream data source. To use four tables in the same dataset, you need to add four data source connections in Quick Sight. 

## Managing permissions for Timestream data
<a name="dataset-permissions-for-timestream"></a>

The following procedure describes how to view, add, and revoke permissions to allow access to the same Timestream data source. The people that you add need to be active users in Quick Sight before you can add them. 

**To edit permissions on a dataset**

1. Choose **Data** at left, then scroll down to find the dataset for your Timestream connection. An example might be `US Timestream Data`.

1. Choose the **Timestream** dataset to open it.

1. On the dataset details page that opens, choose the **Permissions**tab.

   A list of current permissions appears.

1. To add permissions, choose **Add users & groups**, then follow these steps:

   1. Add users or groups to allow them to use the same dataset.

   1. When you're finished adding everyone that you want to add, choose the **Permissions** that you want to apply to them.

1. (Optional) To edit permissions, you can choose **Viewer** or **Owner**. 
   + Choose **Viewer** to allow read access.
   + Choose **Owner** to allow that user to edit, share, or delete this Quick Sight data source. 

1. (Optional) To revoke permissions, choose **Revoke access**. After you revoke someone's access, they can't create edit, share, or delete the dataset.

1. When you are finished, choose **Close**.

## Adding a new Quick Sight dataset for Timestream
<a name="create-dataset-using-timestream"></a>

After you have an existing data source connection for Timestream data, you can create Timestream datasets to use for analysis. 

Currently, you can use a Timestream connection only for a single table in a dataset. To add data from multiple Timestream tables in a single dataset, create an additional Quick Sight data source connection for each table.

**To create a dataset using Amazon Timestream**

1. Choose **Data** at left, then scroll down to find the data source card for your Timestream connection. If you have many data sources, you can use the search bar at the top of the page to find your data source with a partial match on the name.

1. Choose the **Timestream** data source card, and then choose **Create data set**.

1. For **Database**, choose **Select** to view a list of available databases and choose the one that you want to use.

1. For **Tables**, choose the table that you want to use.

1. Choose **Edit/Preview**.

1. (Optional) To add more data, use the following steps: 

   1. Choose **Add data** at top right.

   1. To connect to different data, choose **Switch data source**, and choose a different dataset. 

   1. Follow the UI prompts to finish adding data. 

   1. After adding new data to the same dataset, choose **Configure this join **(the two red dots). Set up a join for each additional table. 

   1. If you want to add calculated fields, choose **Add calculated field**. 

   1. To add a model from SageMaker AI, choose **Augment with SageMaker**. This option is only available in Amazon Quick Enterprise edition.

   1. Clear the check box for any fields that you want to omit.

   1. Update any data types that you want to change.

1. When you are done, choose **Save** to save and close the dataset. 

## Adding Timestream data to an analysis
<a name="open-analysis-add-dataset-for-timestream"></a>

Following, you can find how to add an Amazon Timestream dataset to a Quick Sight analysis. Before you begin, make sure that you have an existing dataset that contains the Timestream data that you want to use.

**To add Amazon Timestream data to an analysis**

1. Choose **Analyses** at left.

1. Do one of the following:
   + To create a new analysis, choose **New analysis** at right. 
   + To add to an existing analysis, open the analysis that you want to edit. 
     + Choose the pencil icon near at top left.
     + Choose **Add data set**.

1. Choose the Timestream dataset that you want to add.

For more information, see [Working with analyses](https://docs.aws.amazon.com/quicksight/latest/user/working-with-analyses.html).