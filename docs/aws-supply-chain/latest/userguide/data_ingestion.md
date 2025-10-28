# Data lake dashboard

You can use AWS Supply Chain data lake to ingest your data from various data sources.
For information about supported data sources, see [Data lake](data-connections.md "data-connections.md").

![Data lake overview](images/data_lake_overvoew.png)

## Data Ingestion

You can view the current connections, source, and destination flows. To view the status of the ingested data, follow the procedure below.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data
   Lake** and then choose the **Data Ingestion** tab.

The **Data Ingestion** page appears.

![Data lake ingestion](images/data-lake-ingestion.png) 2. Choose the **Source Flows** tab.

    * Source Flows – Displays the file or folder structure of the dataset that was
     uploaded.
    * S3 Prefix – Displays the Amazon S3 path where the source files are uploaded.
    * Status – Displays the source files' upload status.
    * Last Sync – Displays when the files were last synced or updated.
    * Actions – You can view the following:




    	+ Manage Flow – You can update the data mapping.
    	+ Upload Files – You can add additional source files to your existing source flows.
    	+ Delete Flow – You can delete the source flow completely.

3. Choose the **Destination Flows** tab.
4. Under **Actions**, choose **Manage Flow** to view and update the data mappings.

The **Manage Destination Flows** page appears.

![Data lake workflow](images/data-lake-flow.png) 5. Move any unassociated source columns under **Source Columns** to **Destination Columns**. 6. Choose **Exit and Review Destination Flows** to go back to the **Destination Flows** page to review the destination flows. 7. Choose the **Connections** tab.

You can view all the existing connections.

## Datasets

You can view the status of the datasets ingested.

To view all the datasets uploaded to existing connections, follow the procedure below.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data
   Lake** and then choose the **Datasets** tab.

The **Datasets** page appears. 2. To view a dataset, choose **View**. 3. Under the **Dataset Fields** tab, you can view all the existing
dataset fields in the dataset. 4. Under the **Source Connections** tab, you can view the
connections that are feeding that dataset.
