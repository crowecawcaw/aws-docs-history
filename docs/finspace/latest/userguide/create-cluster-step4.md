After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 4: Configure data and storage

Choose data and storage configurations that will be used for the cluster.

The parameters on this page are displayed according to the cluster type that
you selected in _Step 1: Add cluster details_.

###### Note

If you choose to add both the **Read data
configuration** and **Savedown storage
configuration**, the database name must be the same for both
the configurations.

## For HDB cluster

###### Note

When you create a cluster with a database that has a changeset, it will autoload
the database when you launch a cluster.

If you choose **Cluster type** as _HDB_, you can specify the database and cache
configurations as following:

Scaling group cluster

1. Choose the name of the database.
2. Choose a dataview for the database you selected.

###### Note

If a dataview is not available in the list, either choose **Create dataview**
to create a new one for the database you selected or try changing the
availability zone. 3. Choose **Next**. The **Review and
create** page opens.

Dedicated clusters

1. Choose the name of the database. This database must have a
   changeset added to it.
2. Choose the changeset that you want to use. By default, this field
   displays the most recent changeset.
3. Choose whether you want to cache your data from your database to
   this cluster. If you choose to enable caching, provide the following
   information:
   1. Choose the cache type, which is a type of read-only storage
      for storing a subset of your database content for faster read
      performance. You can choose from one of the following options:
      - **CACHE_1000** – Provides a throughput of 1000 MB/s per unit storage (TiB).
      - **CACHE_250** – Provides a throughput of 250 MB/s per unit storage (TiB).
      - **CACHE_12** – Provides a throughput of 12 MB/s per unit storage (TiB).

   2. Choose the size of the cache. For cache type **CACHE_1000** and **CACHE_250** you can select cache size as 1200 GB or increments of 2400 GB. For cache type **CACHE_12** you can select the cache size in increments of 6000 GB.

4. Choose **Next**. The **Review and
   create** page opens.

## For RDB cluster

If you choose **Cluster type** as
_RDB_, you can specify the savedown storage
configurations for your cluster as following:

Scaling group cluster

1. **Savedown database configuration**

Choose the name of the database where you want to save your
data. 2. **(Optional) Savedown storage configuration**

Choose the name of the storage volume for your savedown files that you
created in advance. If a volume name is not available, choose
**Create volume** to create it. 3. **(Optional) Tickerplant log
configuration**

Choose a **Volume name** to use the tickerplant logs from. 4. Choose **Next**. The **Review and
create** page opens.

Dedicated clusters

1. **Savedown database configuration**

Choose the name of the database where you want to save your
data. 2. **(Optional) Savedown storage configuration**

    1. Choose the writeable storage space type for temporarily storing
     your savedown data. Currently, only the **SDS01**
     storage type is available. This type represents 3000 IOPS and the
     Amazon EBS volume type `io2`.
    2. Enter the size of the savedown storage that will be available to
     the cluster in GiB.

3. **Tickerplant log configuration**

Choose one or more volume names to use the tickerplant logs from. 4. Choose **Next**. The **Review and
create** page opens.

## For Gateway cluster

If you choose **Cluster type** as
**Gateway**, you do not need to attach databases, cache
configurations, or local storage in this step.

## For General purpose cluster

If you choose **Cluster type** as _General
purpose_, you can specify the database and cache configurations and
savedown storage configurations as following:

Scaling group cluster

1. **(Optional) Read data
   configuration**
   1. Choose the name of the database.
   2. Choose a dataview for the database you selected.

   ###### Note

   If a dataview is not available in the list, either choose
   **Create dataview** to create a new one for the
   database you selected or try changing the availability zone.

2. **(Optional) Savedown database
   configuration**

Choose the name of the database where you want to save your
data. 3. **(Optional) Savedown storage
configuration**

Choose the name of the storage volume for your savedown files that you
created in advance. If a volume name is not available, choose
**Create volume** to create it. 4. **(Optional) Tickerplant log
configuration**

Choose a **Volume name** to use the tickerplant logs
from. 5. Choose **Next**. The **Review and
create** page opens.

Dedicated clusters

1. **(Optional) Read data
   configuration**
   1. Choose the name of the database. This database must have a
      changeset added to it.
   2. Choose the changeset that you want to use. By default, this
      field displays the most recent changeset.
   3. Choose whether you want to cache your data from your database to
      this cluster. If you choose to enable caching, provide the
      following information:
      1. Specify paths within the database directory where you want
         to cache data.
      2. Choose the cache type, which is a type of read-only
         storage for storing a subset of your database content for
         faster read performance. You can choose from one of the
         following options:
         - **CACHE_1000** – Provides a
           throughput of 1000 MB/s per unit storage (TiB).
         - **CACHE_250** – Provides a
           throughput of 250 MB/s per unit storage (TiB).
         - **CACHE_12** – Provides a
           throughput of 12 MB/s per unit storage (TiB).

      3. Choose the size of the cache. For cache type
         **CACHE_1000** and
         **CACHE_250** you can select cache size
         as 1200 GB or increments of 2400 GB. For cache type
         **CACHE_12** you can select the cache
         size in increments of 6000 GB.

2. **(Optional) Savedown database configuration**

Choose the name of the database where you want to save your
data. 3. **(Optional) Savedown storage configuration**

    1. Choose the writeable storage space type for temporarily storing
     your savedown data. Currently, only the **SDS01**
     storage type is available. This type represents 3000 IOPS and the
     Amazon EBS volume type `io2`.
    2. Enter the size of the savedown storage that will be available to
     the cluster in GiB.

4. **Tickerplant log configuration**

Choose one or more volume names to use the tickerplant logs
from. 5. Choose **Next**. The **Review and
create** page opens.

## For Tickerplant cluster

For both scaling groups clusters and dedicated clusters, you can choose a volume
where you want to store the tickerplant data.

1. **Tickerplant log configuration**

Choose a **Volume name** to store the tickerplant logs. 2. Choose **Next**. The **Review and
create** page opens.
