

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Step 4: Configure data and storage
<a name="create-cluster-step4"></a>

Choose data and storage configurations that will be used for the cluster. 

The parameters on this page are displayed according to the cluster type that you selected in *Step 1: Add cluster details*.

**Note**  
If you choose to add both the **Read data configuration** and **Savedown storage configuration**, the database name must be the same for both the configurations.

## For HDB cluster
<a name="create-cluster-step4-hdb"></a>

**Note**  
When you create a cluster with a database that has a changeset, it will autoload the database when you launch a cluster.

If you choose **Cluster type** as *HDB*, you can specify the database and cache configurations as following:

------
#### [ Scaling group cluster ]

1. Choose the name of the database.

1. Choose a dataview for the database you selected.
**Note**  
If a dataview is not available in the list, either choose **Create dataview** to create a new one for the database you selected or try changing the availability zone.

1. Choose **Next**. The **Review and create** page opens.

------
#### [ Dedicated clusters ]

1. Choose the name of the database. This database must have a changeset added to it.

1. Choose the changeset that you want to use. By default, this field displays the most recent changeset.

1. Choose whether you want to cache your data from your database to this cluster. If you choose to enable caching, provide the following information: 

   1. Choose the cache type, which is a type of read-only storage for storing a subset of your database content for faster read performance. You can choose from one of the following options:
      + **CACHE\_1000** – Provides a throughput of 1000 MB/s per unit storage (TiB).
      + **CACHE\_250** – Provides a throughput of 250 MB/s per unit storage (TiB).
      + **CACHE\_12** – Provides a throughput of 12 MB/s per unit storage (TiB).

   1. Choose the size of the cache. For cache type **CACHE\_1000** and **CACHE\_250** you can select cache size as 1200 GB or increments of 2400 GB. For cache type **CACHE\_12** you can select the cache size in increments of 6000 GB.

1. Choose **Next**. The **Review and create** page opens.

------

## For RDB cluster
<a name="create-cluster-step4-rdb"></a>

If you choose **Cluster type** as *RDB*, you can specify the savedown storage configurations for your cluster as following:

------
#### [ Scaling group cluster ]

1. **Savedown database configuration**

   Choose the name of the database where you want to save your data.

1. **(Optional) Savedown storage configuration**

   Choose the name of the storage volume for your savedown files that you created in advance. If a volume name is not available, choose **Create volume** to create it.

1. **(Optional) Tickerplant log configuration**

   Choose a **Volume name** to use the tickerplant logs from.

1. Choose **Next**. The **Review and create** page opens.

------
#### [ Dedicated clusters ]

1. **Savedown database configuration**

   Choose the name of the database where you want to save your data.

1. **(Optional) Savedown storage configuration**

   1. Choose the writeable storage space type for temporarily storing your savedown data. Currently, only the **SDS01** storage type is available. This type represents 3000 IOPS and the Amazon EBS volume type `io2`. 

   1. Enter the size of the savedown storage that will be available to the cluster in GiB.

1. **Tickerplant log configuration**

   Choose one or more volume names to use the tickerplant logs from.

1. Choose **Next**. The **Review and create** page opens.

------

## For Gateway cluster
<a name="create-cluster-step4-gw"></a>

If you choose **Cluster type** as **Gateway**, you do not need to attach databases, cache configurations, or local storage in this step.

## For General purpose cluster
<a name="create-cluster-step4-gp"></a>

If you choose **Cluster type** as *General purpose*, you can specify the database and cache configurations and savedown storage configurations as following:

------
#### [ Scaling group cluster ]

1. **(Optional) Read data configuration**

   1. Choose the name of the database.

   1. Choose a dataview for the database you selected.
**Note**  
If a dataview is not available in the list, either choose **Create dataview** to create a new one for the database you selected or try changing the availability zone.

1. **(Optional) Savedown database configuration**

   Choose the name of the database where you want to save your data.

1. **(Optional) Savedown storage configuration**

   Choose the name of the storage volume for your savedown files that you created in advance. If a volume name is not available, choose **Create volume** to create it.

1. **(Optional) Tickerplant log configuration**

   Choose a **Volume name** to use the tickerplant logs from.

1. Choose **Next**. The **Review and create** page opens.

------
#### [ Dedicated clusters ]

1. **(Optional) Read data configuration**

   1. Choose the name of the database. This database must have a changeset added to it.

   1. Choose the changeset that you want to use. By default, this field displays the most recent changeset.

   1. Choose whether you want to cache your data from your database to this cluster. If you choose to enable caching, provide the following information: 

      1. Specify paths within the database directory where you want to cache data.

      1. Choose the cache type, which is a type of read-only storage for storing a subset of your database content for faster read performance. You can choose from one of the following options:
         + **CACHE\_1000** – Provides a throughput of 1000 MB/s per unit storage (TiB).
         + **CACHE\_250** – Provides a throughput of 250 MB/s per unit storage (TiB).
         + **CACHE\_12** – Provides a throughput of 12 MB/s per unit storage (TiB).

      1. Choose the size of the cache. For cache type **CACHE\_1000** and **CACHE\_250** you can select cache size as 1200 GB or increments of 2400 GB. For cache type **CACHE\_12** you can select the cache size in increments of 6000 GB.

1. **(Optional) Savedown database configuration**

   Choose the name of the database where you want to save your data.

1. **(Optional) Savedown storage configuration**

   1. Choose the writeable storage space type for temporarily storing your savedown data. Currently, only the **SDS01** storage type is available. This type represents 3000 IOPS and the Amazon EBS volume type `io2`. 

   1. Enter the size of the savedown storage that will be available to the cluster in GiB.

1. **Tickerplant log configuration**

   Choose one or more volume names to use the tickerplant logs from.

1. Choose **Next**. The **Review and create** page opens.

------

## For Tickerplant cluster
<a name="create-cluster-step4-tp"></a>

For both scaling groups clusters and dedicated clusters, you can choose a volume where you want to store the tickerplant data.

1. **Tickerplant log configuration**

   Choose a **Volume name** to store the tickerplant logs.

1. Choose **Next**. The **Review and create** page opens.