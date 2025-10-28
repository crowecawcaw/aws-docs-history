After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Access datasets from a notebook

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

You can conveniently and securely access all datasets to prepare and analyze data from your Amazon FinSpace notebook. The following sections show how to access data from a FinSpace notebook.

###### Note

In order to use notebooks and Spark clusters, you must be a superuser or a member of a group with necessary permissions - **Access Notebooks, Manage Clusters**.

## Access data using a pre-populated notebook

###### To access data using a pre-populated notebook

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. Open a notebook by using one of the three methods listed in [Opening the notebook environment](opening-the-notebook-environment.md "opening-the-notebook-environment.md").

In the notebook, the dataset ID and data view ID are pre-populated. 3. Run all cells to print the schema and content of the data view.

## Access data using a newly created notebook

###### To access data using a newly created notebook

1. Run the following code from your notebook to instantiate a cluster and connect the FinSpace PySpark image to the cluster.

```
%local
from aws.finspace.cluster import FinSpaceClusterManager

finspace_clusters = FinSpaceClusterManager()
finspace_clusters.auto_connect()
```

The output should be similar to the following output

```
Cluster is starting. It will be operational in approximately 5 to 8 minutes
Started cluster with cluster ID: 8x6zd9cq and state: STARTING
......

cleared existing credential location
Persisted krb5.conf secret to /etc/krb5.conf
re-establishing connection...
Persisted keytab secret to /home/sagemaker-user/livy.keytab
Authenticated to Spark cluster
Persisted Sparkmagic config to /home/sagemaker-user/.Sparkmagic/config.json
Started Spark cluster with clusterId: 8x6zd9cq
finished reloading all magics & configurations
Persisted FinSpace cluster connection info to /home/sagemaker-user/.Sparkmagic/FinSpace_connection_info.json

SageMaker Studio Environment is now connected to your FinSpace Cluster: 8x6zd9cq at GMT: 2021-01-15 02:13:50.
```

###### Note

Without the `%local` at the beginning of the cell, your code will be executed on the Spark cluster. 2. To access the data view, you will need the dataset ID and data view ID. To get these IDs

    1. In the FinSpace web application, open the dataset details page of the dataset that you want to analyze.
    2. Under the **All Data Views** tab, find the data view that you want to analyze.
    3. Choose **Details**.
    4. Copy the **Data View ID** and **Dataset ID** to use in the notebook.

3. Initialize dataset ID and data view ID in the notebook.

```
dataset_id    = "rgg1hj1"
data_view_id  = "VrvKEKnA1El2nr821BaLTQ"
```

4. Instantiate FinSpace Analytics Manager to access the data and read into a Spark DataFrame.

```
from aws.finspace.analytics import FinSpaceAnalyticsManager
finspace_analytics = FinSpaceAnalyticsManager(Spark = Spark)

df = finspace_analytics.read_data_view(dataset_id = dataset_id, data_view_id = data_view_id)
```
