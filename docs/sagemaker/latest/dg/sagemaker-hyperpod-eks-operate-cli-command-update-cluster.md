

# Updating SageMaker HyperPod cluster configuration
<a name="sagemaker-hyperpod-eks-operate-cli-command-update-cluster"></a>

Run [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) to update the configuration of a cluster.

**Note**  
Important considerations:  
You cannot change the EKS cluster information that your HyperPod cluster is associated after the cluster is created. 
If deep health checks are running on the cluster, this API will not function as expected. You might encounter an error message stating that deep health checks are in progress. To update the cluster, you should wait until the deep health checks finish.

1. Create an [`UpdateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) API request file in JSON format. Make sure that you specify the right cluster name and instance group name to update. For each instance group, you can change the instance type, the number of instances, the lifecycle configuration entrypoint script, and the path to the script.
**Note**  
You can use the `UpdateCluster` to scale down or remove entire instance groups from your SageMaker HyperPod cluster. For additional instructions on how to scale down or delete instance groups, see [Scaling down a SageMaker HyperPod cluster](smcluster-scale-down.md).

   1. For `ClusterName`, specify the name of the cluster you want to update.

   1. For `InstanceGroupName`

      1. To update an existing instance group, specify the name of the instance group you want to update.

      1. To add a new instance group, specify a new name not existing in your cluster.

   1. For `InstanceType`

      1. To update an existing instance group, you must match the instance type you initially specified to the group.

      1. To add a new instance group, specify an instance type you want to configure the group with.

      For instance groups that use `InstanceRequirements` instead of `InstanceType`, you can add or remove instance types from the `InstanceTypes` list. However, you cannot remove an instance type that has active nodes running on it. You also cannot switch between `InstanceType` and `InstanceRequirements` when updating an existing instance group. `InstanceType` and `InstanceRequirements` are mutually exclusive.

   1. For `InstanceCount`

      1. To update an existing instance group, specify an integer that corresponds to your desired number of instances. You can provide a higher or lower value (down to 0) to scale the instance group up or down.

      1. To add a new instance group, specify an integer greater or equal to 1. 

   1. For `LifeCycleConfig`, you can change the values for both `SourceS3Uri` and `OnCreate` as you want to update the instance group.

   1. For `ExecutionRole`

      1. For updating an existing instance group, keep using the same IAM role you attached during cluster creation.

      1. For adding a new instance group, specify an IAM role you want to attach.

   1. For `ThreadsPerCore`

      1. For updating an existing instance group, keep using the same value you specified during cluster creation.

      1. For adding a new instance group, you can choose any value from the allowed options per instance type. For more information, search the instance type and see the **Valid threads per core** column in the reference table at [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon EC2 User Guide*.

   1. For `OnStartDeepHealthChecks`, add `InstanceStress` and `InstanceConnectivity` to enable [Deep health checks](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md).

   1. For `NodeRecovery`, specify `Automatic` to enable automatic node recovery. SageMaker HyperPod replaces or reboots instances (nodes) when issues are found by the health-monitoring agent.

   The following code snippet is a JSON request file template you can use. For more information about the request syntax and parameters of this API, see the [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) API reference.

   ```
   // update_cluster.json
   {
       // Required
       "ClusterName": "{{name-of-cluster-to-update}}",
       // Required
       "InstanceGroups": [{
           "InstanceGroupName": {{"string"}},
           "InstanceType": {{"string"}},
           "InstanceCount": {{number}},
           "LifeCycleConfig": {
               "SourceS3Uri": {{"string"}},
               "OnCreate": {{"string"}}
           },
           "ExecutionRole": {{"string"}},
           "ThreadsPerCore": {{number}},
           "OnStartDeepHealthChecks": [
               {{"InstanceStress", "InstanceConnectivity"}}
           ]
       }],
       "NodeRecovery": "{{Automatic}}"
   }
   ```

1. Run the following `update-cluster` command to submit the request. 

   ```
   aws sagemaker update-cluster \
       --cli-input-json {{file://complete/path/to/update_cluster.json}}
   ```