After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Working with Spark clusters in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Amazon FinSpace simplifies how to work with Spark clusters by offering easy to use cluster configuration templates that allow you to launch, connect, resize, and terminate without
worrying to manage the underlying infrastructure. Every user in FinSpace with **Access Notebooks** and **Manage Clusters** permission can instantiate one cluster.

###### Note

In order to use notebooks and Spark clusters, you must be a superuser or a member of a group with necessary permissions - **Access Notebooks, Manage Clusters**.

You can choose one of the following cluster configuration templates:

- Small
- Medium
- Large
- XLarge
- 2XLarge

###### Note

You are charged by the minute for using the Spark clusters. Terminate your Spark cluster when you are done using it.

## Import FinSpace cluster management library

Use the following code to import the cluster management library in a notebook.

```
%local
from aws.finspace.cluster import FinSpaceClusterManager
```

## Start a Spark cluster

Use the following code to start and connect your notebook to a Spark cluster.

```
%local
from aws.finspace.cluster import FinSpaceClusterManager

finspace_clusters = FinSpaceClusterManager()
finspace_clusters.auto_connect()
```

For a newly created cluster, the output should be similar to the following.

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

You can expect a startup time of about 5 to 8 minutes when instantiating a cluster for the first time.
Once a cluster is created, any newly created notebook will detect and connect to the running cluster when an `auto_connect()` call is issued and this operation is instantaneous.

## List details for Spark clusters

**Use the following code to list the Spark cluster name and details**

```
%local
finspace_clusters.list()
```

The output should be similar to the following output.

```
{'clusters': [{'clusterId': '8x6zd9cq',
   'clusterStatus': {'state': 'RUNNING',
    'reason': 'Started successfully',
    'details': ''},
   'name': 'hab-cluster-3e51',
   'currentTemplate': 'FinSpace-Small',
   'requestedTemplate': 'FinSpace-Small',
   'clusterTerminationTime': 1610676314,
   'createdTimestamp': 1610676374420,
   'modifiedTimestamp': 1610676823805},
  {'clusterId': '3ysaqx3g',
   'clusterStatus': {'state': 'TERMINATED',
    'reason': 'Initiated by user',
    'details': ''},
   'name': 'hab-cluster-c4f9',
   'currentTemplate': 'FinSpace-Small',
   'requestedTemplate': 'FinSpace-Small',
   'clusterTerminationTime': 1610478542,
   'createdTimestamp': 1610478602457,
   'modifiedTimestamp': 1610514182552}]}
```

In the output above, you can see the `clusterId`
**8x6zd9cq** is a small cluster with state equals to **RUNNING**, and the `clusterId` **3ysaqx3g** is a small cluster with state equals to **TERMINATED**.

## Resize Spark cluster

Scale your Spark cluster up or down based on your compute needs and the volume of data you need to analyze.

###### To resize clusters

1. Type the following code to update your cluster to a **Large** size.

```
%local
finspace_clusters.update('8x6zd9cq','Large')
```

The output will look like below

```
{'clusterId': '8x6zd9cq',
 'clusterStatus': {'state': 'UPDATING', 'reason': 'Initiated by user'}}
```

2. Note that the `update()` operation runs asynchronous so that you can continue to work on the cluster as the update operation completes.
3. Check the status of the update operation using the `list()` function.

```
{'clusters': [{'clusterId': '8x6zd9cq',
   'clusterStatus': {'state': 'UPDATING',
    'reason': 'Initiated by user',
    'details': ''},
   'name': 'hab-cluster-3e51',
   'currentTemplate': 'Small',
   'requestedTemplate': 'Large',
   'clusterTerminationTime': 1610676314,
   'createdTimestamp': 1610676374420,
   'modifiedTimestamp': 1610682765327}}
```

4. In the output above, the `clusterId` **8x6zd9cq** is being updated from **Small** to **Large**.

## Terminate Spark cluster

Terminate your Spark cluster once your work is done, so that you don't incur additional charges.

###### To terminate your Spark cluster

1. Type the following code to terminate a cluster.

```
%local
finspace_clusters.terminate('8x6zd9cq')
```

2. You can check the state of the cluster using the `list()` function.
