

# Data sources and ingestion
<a name="feature-store-ingest-data"></a>

Records are added to your feature groups through ingestion. Depending on your desired use case, the ingested records may be kept within the feature group or not. This depends on the storage configuration, if your feature group uses the offline or online store. The offline store is used as a historical database, that is typically used for data exploration, machine learning (ML) model training, and batch inference. The online store is used as a real-time lookup of records, that is typically used for ML model serving. For more information on Feature Store concepts and ingestion, see [Feature Store concepts](feature-store-concepts.md).

There are multiple ways to bring your data into Amazon SageMaker Feature Store. Feature Store offers a single API call for data ingestion called `PutRecord` that enables you to ingest data in batches or from streaming sources. You can use Amazon SageMaker Data Wrangler to engineer features and then ingest your features into your Feature Store. You can also use Amazon EMR for batch data ingestion through a Spark connector.

In the following topics we will discuss the difference between 

**Topics**
+ [Stream ingestion](#feature-store-ingest-data-stream)
+ [Data Wrangler with Feature Store](#feature-store-data-wrangler-integration)
+ [Batch ingestion with Amazon SageMaker Feature Store Spark](batch-ingestion-spark-connector-setup.md)

## Stream ingestion
<a name="feature-store-ingest-data-stream"></a>

You can use streaming sources such as Kafka or Kinesis as a data source, where records are extracted from, and directly feed records to the online store for training, inference or feature creation. Records can be ingested into your feature group by using the synchronous `PutRecord` API call. Since this is a synchronous API call it allows small batches of updates to be pushed in a single API call. This enables you to maintain high freshness of the feature values and publish values as soon an update is detected. These are also called *streaming* features. 

## Data Wrangler with Feature Store
<a name="feature-store-data-wrangler-integration"></a>

Data Wrangler is a feature of Studio Classic that provides an end-to-end solution to import, prepare, transform, featurize, and analyze data. Data Wrangler enables you to engineer your features and ingest them into your online or offline store feature groups.

The following instructions exports a Jupyter notebook that contains all of the source code needed to create a Feature Store feature group that adds your features from Data Wrangler to an online or offline store.

The instructions on exporting your Data Wrangler data flow to Feature Store on the console vary depending on whether you enabled enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### Export your Data Wrangler data flow to Feature Store if Studio is your default experience (console)
<a name="feature-store-ingest-data-wrangler-integration-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** from the left panel, to expand the dropdown list.

1. From the dropdown list, choose **Data Wrangler**.

1. If you have an instance of Amazon SageMaker Canvas already running, choose **Open Canvas**.

   If you don't have an instance of SageMaker Canvas running, choose **Run in Canvas**.

1. On the SageMaker Canvas console, choose **Data Wrangler** in the left navigation pane.

1. Choose **Data flows** to view your data flows.

1. Choose **\+** to expand the dropdown list.

1. Choose **Export data flow** to expand the dropdown list.

1. Choose **Save to SageMaker Feature Store (via JupyterLab Notebook)**.

1. **Under Export data flow as notebook**, choose one of the following options:
   + **Download a local copy** to download the dataflow to your local machine.
   + **Export to S3 location** to download the dataflow to an Amazon Simple Storage Service location and enter the Amazon S3 location or choose **Browse** to find your Amazon S3 location.

1. Choose **Export**.

### Export your Data Wrangler data flow to Feature Store if Studio Classic is your default experience (console)
<a name="feature-store-ingest-data-wrangler-integration-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Data Wrangler**.

1. Choose your workflow.

1. Choose the **Export** tab.

1. Choose **Export Step**.

1. Choose **Feature Store**.

 After the feature group has been created, you can also select and join data across multiple feature groups to create new engineered features in Data Wrangler and then export your data set to an Amazon S3 bucket. 

For more information on how to export to Feature Store, see [Export to SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-export.html#data-wrangler-data-export-feature-store). 