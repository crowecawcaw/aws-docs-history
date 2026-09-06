

# Using Amazon OpenSearch Service with Amazon Quick Sight
<a name="connecting-to-os"></a>

Following, you can find how to connect to your Amazon OpenSearch Service data using Amazon Quick Sight.

## Creating a new Quick Sight data source connection for OpenSearch Service
<a name="create-connection-to-es"></a>

Following, you can find how to connect to OpenSearch Service

Before you can proceed, Amazon Quick Sight needs to be authorized to connect to Amazon OpenSearch Service. If connections aren't enabled, you get an error when you try to connect. A Quick Sight administrator can authorize connections to AWS resources. 

**To authorize Quick Sight to initiate a connection to OpenSearch Service**

1. Open the menu by clicking on your profile icon at top right, then choose **Manage Quick**. If you don't see the **Manage Quick** option on your profile menu, ask your Amazon Quick administrator for assistance.

1. Choose **Security & permissions**, **Add or remove**.

1. Enable the option for **OpenSearch**.

1. Choose **Update**.

After OpenSearch Service is accessible, you create a data source so people can use the specified domains.

**To connect to OpenSearch Service**

1. Begin by creating a new dataset. Choose **Data** from the navigation pane at left, then choose **Create** and **New Dataset**.

1. Choose the **Amazon OpenSearch** data source card.

1. For **Data source name**, enter a descriptive name for your OpenSearch Service data source connection, for example `OpenSearch Service ML Data`. Because you can create many datasets from a connection to OpenSearch Service, it's best to keep the name simple.

1. For **Connection type**, choose the network you want to use. This can be a virtual private cloud (VPC) based on Amazon VPC or a public network. The list of VPCs contains the names of VPC connections, rather than VPC IDs. These names are defined by the Quick administrator. 

1. For **Domain**, choose the OpenSearch Service domain that you want to connect to. 

1. Choose **Validate connection** to check that you can successfully connect to OpenSearch Service.

1. Choose **Create data source** to proceed.

1. For **Tables**, choose the one you want to use, then choose **Select** to continue. 

1. Do one of the following:
   + To import your data into the Quick Sight in-memory engine (called SPICE), choose **Import to SPICE for quicker analytics**. For information about how to enable importing OpenSearch data, see [Authorizing connections to Amazon OpenSearch Service](opensearch.md).
   + To allow Quick Sight to run a query against your data each time you refresh the dataset or use the analysis or dashboard, choose **Directly query your data**. 

     To enable autorefresh on a published dashboard that uses OpenSearch Service data, the OpenSearch Service dataset needs to use a direct query.

1. Choose **Edit/Preview** and then **Save** to save your dataset and close it.

## Managing permissions for OpenSearch Service data
<a name="dataset-permissions-for-es"></a>

The following procedure describes how to view, add, and revoke permissions to allow access to the same OpenSearch Service data source. The people that you add need to be active users in Quick Sight before you can add them. 

**To edit permissions on a data source**

1. Choose **Data** at left, then scroll down to find the data source card for your Amazon OpenSearch Service connection. An example might be `US Amazon OpenSearch Service Data`.

1. Choose the **Amazon OpenSearch** dataset.

1. On the dataset details page that opens, choose the **Permissions** tab.

   A list of current permissions appears.

1. To add permissions, choose **Add users & groups**, then follow these steps:

   1. Add users or groups to allow them to use the same dataset.

   1. When you're finished adding everyone that you want to add, choose the **Permissions** that you want to apply to them.

1. (Optional) To edit permissions, you can choose **Viewer** or **Owner**. 
   + Choose **Viewer** to allow read access.
   + Choose **Owner** to allow that user to edit, share, or delete this Quick Sight dataset. 

1. (Optional) To revoke permissions, choose **Revoke access**. After you revoke someone's access, they can't create new datasets from this data source. However, their existing datasets still have access to this data source.

1. When you are finished, choose **Close**.

## Adding a new Quick Sight dataset for OpenSearch Service
<a name="create-dataset-using-es"></a>

After you have an existing data source connection for OpenSearch Service, you can create OpenSearch Service datasets to use for analysis. 

**To create a dataset using OpenSearch Service**

1. From the start page, choose **Data**, **Create**, **New dataset**.

1. Scroll down to the data source card for your OpenSearch Service connection. If you have many data sources, you can use the search bar at the top of the page to find your data source with a partial match on the name.

1. Choose the **Amazon OpenSearch** data source card, and then choose **Create data set**.

1. For **Tables**, choose the OpenSearch Service index that you want to use.

1. Choose **Edit/Preview**.

1. Choose **Save** to save and close the dataset. 

## Adding OpenSearch Service data to an analysis
<a name="open-analysis-add-dataset-for-es"></a>

After you have an OpenSearch Service dataset available, you can add it to a Quick Sight analysis. Before you begin, make sure that you have an existing dataset that contains the OpenSearch Service data that you want to use.

**To add OpenSearch Service data to an analysis**

1. Choose **Analyses** at left.

1. Do one of the following:
   + To create a new analysis, choose **New analysis** at right. 
   + To add to an existing analysis, open the analysis that you want to edit. 
     + Choose the pencil icon near at top left.
     + Choose **Add data set**.

1. Choose the OpenSearch Service dataset that you want to add. 

   For information on using OpenSearch Service in visualizations, see [Limitations for using OpenSearch Service](#limitations-for-es). 

1. For more information, see [Working with analyses](https://docs.aws.amazon.com/quicksight/latest/user/working-with-analyses.html).

## Limitations for using OpenSearch Service
<a name="limitations-for-es"></a>

The following limitations apply to using OpenSearch Service datasets:
+ OpenSearch Service datasets support a subset of the visual types, sort options, and filter options.
+ To enable autorefresh on a published dashboard that uses OpenSearch Service data, the OpenSearch Service dataset needs to use a direct query.
+ Multiple subquery operations aren't supported. To avoid errors during visualization, don't add multiple fields to a field well, use one or two fields per visualization, and avoid using the **Color** field well.
+ Custom SQL isn't supported.
+ Crossdataset joins and self joins aren't supported.
+ Calculated fields aren't supported. 
+ Text fields aren't supported. 
+ The "other" category isn't supported. If you use an OpenSearch Service dataset with a visualization that supports the "other" category, disable the "other" category by using the menu on the visual. 