# Tutorial: Create an unmanaged compute

environment using Amazon EKS resources

Complete the following steps to create an unmanaged compute environment using Amazon Elastic Kubernetes Service
(Amazon EKS) resources.

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar on top of the page, select the AWS Region to use.
3. In the navigation pane, choose **Compute environments**.
4. Choose **Create**.
5. Configure the environment.
   1. For **Compute environment configuration**, choose
      **Amazon Elastic Kubernetes Service (Amazon EKS)**.
   2. For **Orchestration type**, choose
      **Unmanaged**.

6. For **Name**, specify a unique name for your compute environment. The
   name can be up to 128 characters in length. It can contain uppercase and lowercase
   letters, numbers, hyphens (-), and underscores (\_).
7. For **EKS cluster**, choose an existing Amazon EKS cluster. To create a new EKS cluster,
   follow the steps on [Create
   an Amazon EKS cluster page](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md").
8. For **Namespace**, enter a Kubernetes namespace to group your AWS Batch
   processes in the cluster.
9. (Optional) For **Maximum vCPUs**, specify the maximum number of vCPUs available
   for job scheduling from your provisioned capacity.
10. (Optional) Expand **Tags**. Choose **Add tag** and
    then enter a key-value pair.
11. Choose **Next page**.
12. For **Review**, review the configuration steps. If you
    need to make changes, choose **Edit**. When you're finished,
    choose **Create compute environment**.

###### Assigning Amazon EKS cluster nodes to unmanaged compute environment

After creating the unmanaged compute environment, you need to label your Amazon EKS nodes with the compute
environment UUID.

First, get the compute environment UUID from the `DescribeComputeEnvironments` API result:

```
`$` `aws batch describe-compute-environments \
 --compute-environments `unmanagedEksCE` \
 --query "computeEnvironments[].{name: computeEnvironmentName, uuid: uuid}"`
```

Get the node information:

```
kubectl get nodes -o name
```

Label the nodes with the AWS Batch compute environment UUID:

```
kubectl label `<node-name>` batch.amazonaws.com/compute-environment-uuid=`uuid`
```
