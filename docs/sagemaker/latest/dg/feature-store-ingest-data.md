# Data sources and ingestion

Records are added to your feature groups through ingestion. Depending on your desired use
case, the ingested records may be kept within the feature group or not. This depends on the
storage configuration, if your feature group uses the offline or online store. The offline
store is used as a historical database, that is typically used for data exploration, machine
learning (ML) model training, and batch inference. The online store is used as a real-time
lookup of records, that is typically used for ML model serving. For more information on Feature Store
concepts and ingestion, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

There are multiple ways to bring your data into Amazon SageMaker Feature Store. Feature Store offers a single API call
for data ingestion called `PutRecord` that enables you to ingest data in batches
or from streaming sources. You can use Amazon SageMaker Data Wrangler to engineer features and then ingest your
features into your Feature Store. You can also use Amazon EMR for batch data ingestion through a Spark
connector.

In the following topics we will discuss the difference between

###### Topics

- [Stream ingestion](#feature-store-ingest-data-stream "#feature-store-ingest-data-stream")
- [Data Wrangler with Feature Store](#feature-store-data-wrangler-integration "#feature-store-data-wrangler-integration")
- [Batch ingestion with Amazon SageMaker Feature Store
  Spark](batch-ingestion-spark-connector-setup.md "batch-ingestion-spark-connector-setup.md")

## Stream ingestion

You can use streaming sources such as Kafka or Kinesis as a data source, where records
are extracted from, and directly feed records to the online store for training,
inference or feature creation. Records can be ingested into your feature group by using
the synchronous `PutRecord` API call. Since this is a synchronous API call it
allows small batches of updates to be pushed in a single API call. This enables you to
maintain high freshness of the feature values and publish values as soon an update is
detected. These are also called _streaming_ features.

## Data Wrangler with Feature Store

Data Wrangler is a feature of Studio Classic that provides an end-to-end solution to import,
prepare, transform, featurize, and analyze data. Data Wrangler enables you to engineer your
features and ingest them into your online or offline store feature groups.

The following instructions exports a Jupyter notebook that contains all of the source
code needed to create a Feature Store feature group that adds your features from Data Wrangler to an
online or offline store.

The instructions on exporting your Data Wrangler data flow to Feature Store on the console vary
depending on whether you enabled enabled [Amazon SageMaker Studio](studio-updated.md "studio-updated.md") or [Amazon SageMaker Studio Classic](studio.md "studio.md")
as your default experience.

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Data** from the left panel, to expand the
   dropdown list.
3. From the dropdown list, choose **Data
   Wrangler**.
4. If you have an instance of Amazon SageMaker Canvas already running, choose
   **Open Canvas**.

If you don't have an instance of SageMaker Canvas running, choose **Run
in Canvas**. 5. On the SageMaker Canvas console, choose **Data Wrangler** in the
left navigation pane. 6. Choose **Data flows** to view your data flows. 7. Choose **+** to expand the dropdown list. 8. Choose **Export data flow** to expand the dropdown
list. 9. Choose **Save to SageMaker Feature Store (via JupyterLab
Notebook)**. 10. **Under Export data flow as notebook**, choose one of
the following options:

    * **Download a local copy** to download the
     dataflow to your local machine.
    * **Export to S3 location** to download the
     dataflow to an Amazon Simple Storage Service location and enter the Amazon S3 location or
     choose **Browse** to find your Amazon S3
     location.

11. Choose **Export**.
1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
1. Choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ) in the left navigation pane.
1. Choose **Data**.
1. From the dropdown list, choose **Data
   Wrangler**.
1. Choose your workflow.
1. Choose the **Export** tab.
1. Choose **Export Step**.
1. Choose **Feature Store**.

After the feature group has been created, you can also select and join data across
multiple feature groups to create new engineered features in Data Wrangler and then export your
data set to an Amazon S3 bucket.

For more information on how to export to Feature Store, see [Export to SageMaker AI Feature Store](data-wrangler-data-export.md#data-wrangler-data-export-feature-store "data-wrangler-data-export.md#data-wrangler-data-export-feature-store").
