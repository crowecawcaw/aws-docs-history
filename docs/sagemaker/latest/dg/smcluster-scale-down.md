

# Scaling down a SageMaker HyperPod cluster
<a name="smcluster-scale-down"></a>

You can scale down the number of instances running on your Amazon SageMaker HyperPod cluster. You might want to scale down a cluster for various reasons, such as reduced resource utilization or cost optimization.

The following page outlines two main approaches to scaling down:
+ **Scale down at the instance group level:** This approach uses the `UpdateCluster` API, with which you can:
  + Scale down the instance counts for specific instance groups independently. SageMaker AI handles the termination of nodes in a way that reaches the new target instance counts you've set for each group. See [Scale down an instance group](#smcluster-scale-down-updatecluster).
  + Completely delete instance groups from your cluster. See [Delete instance groups](#smcluster-remove-instancegroup).
+ **Scale down at the instance level:** This approach uses the `BatchDeleteClusterNodes` API, with which you can specify the individual nodes you want to terminate. See [Scale down at the instance level](#smcluster-scale-down-batchdelete).

**Note**  
When scaling down at the instance level with `BatchDeleteCusterNodes`, you can only terminate a maximum of 99 instances at a time. `UpdateCluster` supports terminating any number of instances.

## Important considerations
<a name="smcluster-scale-down-considerations"></a>
+ When scaling down a cluster, you should ensure that the remaining resources are sufficient to handle your workload and that any necessary data migration or rebalancing is properly handled to avoid disruptions. 
+ Make sure to back up your data to Amazon S3 or an FSx for Lustre file system before invoking the API on a worker node group. This can help prevent any potential data loss from the instance root volume. For more information about backup, see [Use the backup script provided by SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup).
+ To invoke this API on an existing cluster, you must first patch the cluster by running the [ UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) API. For more information about patching a cluster, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software).
+ Metering/billing for on-demand instances will automatically be stopped after scale down. To stop metering for scaled-down reserved instances, you should reach out to your AWS account team for support.
+ You can use the released capacity from the scaled-down reserved instances to scale up another SageMaker HyperPod cluster.

## Scale down at the instance group level
<a name="smcluster-scale-down-or-delete"></a>

The [`UpdateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) operation allows you to make changes to the configuration of your SageMaker HyperPod cluster, such as scaling down the number of instances of an instance group or removing entire instance groups. This can be useful when you want to adjust the resources allocated to your cluster based on changes in your workload, optimize costs, or change the instance type of an instance group.

### Scale down an instance group
<a name="smcluster-scale-down-updatecluster"></a>

Use this approach when you have an instance group that is idle and it's safe to terminate any of the instances for scaling down. When you submit an `UpdateCluster` request to scale down, HyperPod randomly chooses instances for termination and scales down to the specified number of nodes for the instance group.

**Scale-down behavior with flexible instance groups**  
For instance groups that use `InstanceRequirements` with multiple instance types, HyperPod terminates the lowest-priority instance types first during scale-down. The priority is determined by the order of instance types in the `InstanceTypes` list, where the first type has the highest priority. This protects higher-priority instances, which are typically higher-performance, during scale-down operations.

**Note**  
When you scale the number of instances in an instance group down to 0, all the instances within that group will be terminated. However, the instance group itself will still exist as part of the SageMaker HyperPod cluster. You can scale the instance group back up at a later time, using the same instance group configuration.   
Alternatively, you can choose to remove an instance group permanently. For more information, see [Delete instance groups](#smcluster-remove-instancegroup).

**To scale down with `UpdateCluster`**

1. Follow the steps outlined in [Updating SageMaker HyperPod cluster configuration](sagemaker-hyperpod-eks-operate-cli-command-update-cluster.md). When you reach step **1.d** where you specify the **InstanceCount** field, enter a number that is smaller than the current number of instances to scale down the cluster.

1. Run the [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) AWS CLI command to submit your request.

The following is an example of an `UpdateCluster` JSON object. Consider the case where your instance group currently has 2 running instances. If you set the **InstanceCount** field to 1, as shown in the example, then HyperPod randomly selects one of the instances and terminates it.

```
{
  "ClusterName": {{"name-of-cluster-to-update"}},
  "InstanceGroups": [
    {
      "InstanceGroupName": {{"training-instances"}},
      "InstanceType": {{"instance-type"}},
      "InstanceCount": {{1}},
      "LifeCycleConfig": {
        "SourceS3Uri": {{"s3://amzn-s3-demo-bucket/training-script.py"}},
        "OnCreate": {{"s3://amzn-s3-demo-bucket/setup-script.sh"}}
      },
      "ExecutionRole": {{"arn:aws:iam::123456789012:role/SageMakerRole"}},
      "ThreadsPerCore": {{number-of-threads}},
      "OnStartDeepHealthChecks": [
        "InstanceStress",
        "InstanceConnectivity"
      ]
    }
  ],
  "NodeRecovery": {{"Automatic"}}
}
```

### Delete instance groups
<a name="smcluster-remove-instancegroup"></a>

You can use the [`UpdateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) operation to remove entire instance groups from your SageMaker HyperPod cluster when they are no longer needed. This goes beyond simple scaling down, allowing you to completely eliminate specific instance groups from your cluster's configuration. 

**Note**  
When removing an instance group:  
All instances within the targeted group are terminated.
The entire group configuration is deleted from the cluster.
Any workloads running on that instance group are stopped.

**To delete instance groups with `UpdateCluster`**

1. When following the steps outlined in [Updating SageMaker HyperPod cluster configuration](sagemaker-hyperpod-eks-operate-cli-command-update-cluster.md):

   1. Set the optional `InstanceGroupsToDelete` parameter in your `UpdateCluster` JSON and pass the comma-separated list of instance group names that you want to delete.

   1.  When you specify the `InstanceGroups` list, ensure that the specifications of the instance groups you are removing are no longer listed in the `InstanceGroups` list.

1. Run the [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) AWS CLI command to submit your request.

**Important**  
Your SageMaker HyperPod cluster must always maintain at least one instance group.
Ensure all critical data is backed up before removal.
The removal process cannot be undone.

The following is an example of an `UpdateCluster` JSON object. Consider the case where a cluster currently has 3 instance groups, a *training*, a *prototype-training*, and an *inference-serving* group. You want to delete the *prototype-training* group.

```
{
  "ClusterName": {{"name-of-cluster-to-update"}},
  "InstanceGroups": [
    {
      "InstanceGroupName": {{"training"}},
      "InstanceType": {{"instance-type"}},
      "InstanceCount": {{}},
      "LifeCycleConfig": {
        "SourceS3Uri": {{"s3://amzn-s3-demo-bucket/training-script.py"}},
        "OnCreate": {{"s3://amzn-s3-demo-bucket/setup-script.sh"}}
      },
      "ExecutionRole": {{"arn:aws:iam::123456789012:role/SageMakerRole"}},
      "ThreadsPerCore": {{number-of-threads}},
      "OnStartDeepHealthChecks": [
        "InstanceStress",
        "InstanceConnectivity"
      ]
    },
    {
      "InstanceGroupName": {{"inference-serving"}},
      "InstanceType": {{"instance-type"}},
      "InstanceCount": {{2}},
      [...]
    },
  ],
  "InstanceGroupsToDelete": [ {{"prototype-training"}} ],
  "NodeRecovery": {{"Automatic"}}
}
```

## Scale down at the instance level
<a name="smcluster-scale-down-batchdelete"></a>

The `BatchDeleteClusterNodes` operation allows you to scale down a SageMaker HyperPod cluster by specifying the individual nodes you want to terminate. `BatchDeleteClusterNodes` provides more granular control for targeted node removal and cluster optimization. For example, you might use `BatchDeleteClusterNodes` to delete targeted nodes for maintenance, rolling upgrades, or rebalancing resources geographically.

**API request and response**

When you submit a `BatchDeleteClusterNodes` request, SageMaker HyperPod deletes nodes by their instance IDs. The API accepts a request with the cluster name and a list of node IDs to be deleted. 

The response includes two sections: 
+  `Failed`: A list of errors of type `[ BatchDeleteClusterNodesError ](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodesError.html)` - one per instance ID.
+  `Successful`: The list of instance IDs successfully terminated. 

**Validation and error handling**

The API performs various validations, such as:
+ Verifying the node ID format (prefix of `i-` and Amazon EC2 instance ID structure). 
+ Checking the node list length, with a limit of 99 or fewer node IDs in a single `BatchDeleteClusterNodes` request.
+ Ensuring a valid SageMaker HyperPod cluster with the input cluster-name is present and that no cluster-level operations (update, system update, patching, or deletion) are in progress.
+ Handling cases where instances are not found, have invalid status, or are in use.

**API Response Codes**
+  The API returns a `200` status code for successful (e.g., all input nodes succeeded validation) or partially successful requests (e.g., some input nodes fail validation). 
+  If all of these validations fail (e.g., all input nodes fail validation), the API will return a `400` Bad Request response with the appropriate error messages and error codes. 

**Example**

The following is an example of **scaling down a cluster at the instance level** using the AWS CLI:

```
aws sagemaker batch-delete-cluster-nodes --cluster-name {{"cluster-name"}} --node-ids {{'["i-111112222233333", "i-111112222233333"]'}}
```