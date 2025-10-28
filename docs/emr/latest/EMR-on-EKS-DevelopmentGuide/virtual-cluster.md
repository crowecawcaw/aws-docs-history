# Managing virtual clusters

A virtual cluster is a Kubernetes namespace that Amazon EMR is registered with. You can
create, describe, list, and delete virtual clusters. They do not consume any additional resource
in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this
relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet
your requirements. See possible use cases in the [Kubernetes
Concepts Overview](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/") documentation.

To register Amazon EMR with a Kubernetes namespace on an Amazon EKS cluster, you need the name of the
EKS cluster and the namespace that has been set up for running your workload. These registered
clusters in Amazon EMR are called virtual clusters because they do not manage physical compute or
storage but point to a Kubernetes namespace where your workload is scheduled.

###### Note

Before creating a virtual cluster, you must first complete the steps 1-8 in [Setting up Amazon EMR on EKS](setting-up.md "setting-up.md").

###### Topics

- [Create a virtual cluster](#create-virtul-cluster "#create-virtul-cluster")
- [List virtual clusters](#list-virtual-cluster "#list-virtual-cluster")
- [Describe a virtual cluster](#describe-virtual-cluster "#describe-virtual-cluster")
- [Delete a virtual cluster](#delete-virtual-cluster "#delete-virtual-cluster")
- [Virtual cluster states](#virtual-cluster-states "#virtual-cluster-states")

## Create a virtual cluster

Run the following command to create a virtual cluster by registering Amazon EMR with a namespace
on an EKS cluster. Replace `virtual_cluster_name` with a name that you
provide for your virtual cluster. Replace `eks_cluster_name` with the
name of the EKS cluster. Replace the `namespace_name` with the namespace
that you want to register Amazon EMR with.

```
aws emr-containers create-virtual-cluster \
--name `virtual_cluster_name` \
--container-provider '{
    "id": "`eks_cluster_name`",
    "type": "EKS",
    "info": {
        "eksInfo": {
            "namespace": "`namespace_name`"
        }
    }
}'
```

Alternatively, you can create a JSON file that includes the required parameters for the
virtual cluster, as the following example demonstrates.

```
{
    "name": "`virtual_cluster_name`",
    "containerProvider": {
        "type": "EKS",
        "id": "`eks_cluster_name`",
        "info": {
            "eksInfo": {
                "namespace": "`namespace_name`"
            }
        }
    }
}
```

Then run the following `create-virtual-cluster` command with the path to the JSON
file.

```
aws emr-containers create-virtual-cluster \
--cli-input-json `file://./create-virtual-cluster-request.json`

```

###### Note

To validate the successful creation of a virtual cluster, view the status of virtual
clusters by running the `list-virtual-clusters` command or by going to the
**Virtual clusters** page in the Amazon EMR console.

## List virtual clusters

Run the following command to view the status of virtual clusters.

```
aws emr-containers list-virtual-clusters
```

## Describe a virtual cluster

Run the following command to get more details about a virtual cluster, such as namespace,
status, and date registered. Replace `123456` with your virtual cluster
ID.

```
aws emr-containers describe-virtual-cluster --id `123456`
```

## Delete a virtual cluster

Run the following command to delete a virtual cluster. Replace
`123456` with your virtual cluster ID.

```
aws emr-containers delete-virtual-cluster --id `123456`
```

## Virtual cluster states

The following table describes the four possible states of a virtual cluster.

| `State`       | Description                                                           |
| ------------- | --------------------------------------------------------------------- |
| `RUNNING`     | Virtual cluster is in `RUNNING` state.                                |
| `TERMINATING` | The requested termination of the virtual cluster is in progress.      |
| `TERMINATED`  | The requested termination is complete.                                |
| `ARRESTED`    | The requested termination failed because of insufficient permissions. |
