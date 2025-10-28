# Updating

SageMaker HyperPod cluster configuration

Run [update-cluster](../../../cli/latest/reference/sagemaker/update-cluster.md "../../../cli/latest/reference/sagemaker/update-cluster.md")
to update the configuration of a cluster.

###### Note

Important considerations:

- You cannot change the EKS cluster information that your
  HyperPod cluster is associated after the cluster is created.
- If deep health checks are running on the cluster, this API will not
  function as expected. You might encounter an error message stating that
  deep health checks are in progress. To update the cluster, you should
  wait until the deep health checks finish.

1. Create an [`UpdateCluster`](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") API request file in JSON format.
   Make sure that you specify the right cluster name and instance group name to
   update. For each instance group, you can change the instance type, the
   number of instances, the lifecycle configuration entrypoint script, and the
   path to the script.

###### Note

You can use the `UpdateCluster` to scale down or remove
entire instance groups from your SageMaker HyperPod cluster. For additional
instructions on how to scale down or delete instance groups, see [Scaling down a SageMaker HyperPod cluster](smcluster-scale-down.md "smcluster-scale-down.md").

    1. For `ClusterName`, specify the name of the cluster you
     want to update.
    2. For `InstanceGroupName`




    	1. To update an existing instance group, specify the name of
    	 the instance group you want to update.
    	2. To add a new instance group, specify a new name not
    	 existing in your cluster.
    3. For `InstanceType`




    	1. To update an existing instance group, you must match the
    	 instance type you initially specified to the group.
    	2. To add a new instance group, specify an instance type you
    	 want to configure the group with.
    4. For `InstanceCount`




    	1. To update an existing instance group, specify an integer
    	 that corresponds to your desired number of instances. You
    	 can provide a higher or lower value (down to 0) to scale the
    	 instance group up or down.
    	2. To add a new instance group, specify an integer greater or
    	 equal to 1.
    5. For `LifeCycleConfig`, you can change the values for
     both `SourceS3Uri` and `OnCreate` as you want
     to update the instance group.
    6. For `ExecutionRole`




    	1. For updating an existing instance group, keep using the
    	 same IAM role you attached during cluster creation.
    	2. For adding a new instance group, specify an IAM role you
    	 want to attach.
    7. For `ThreadsPerCore`




    	1. For updating an existing instance group, keep using the
    	 same value you specified during cluster creation.
    	2. For adding a new instance group, you can choose any value
    	 from the allowed options per instance type. For more
    	 information, search the instance type and see the **Valid threads per core** column in
    	 the reference table at [CPU cores and threads per CPU core per instance
    	 type](../../../AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.md "../../../AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.md") in the *Amazon EC2 User
    	 Guide*.
    8. For `OnStartDeepHealthChecks`, add
     `InstanceStress` and
     `InstanceConnectivity` to enable [Deep health
     checks](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md "sagemaker-hyperpod-eks-resiliency-deep-health-checks.md").
    9. For `NodeRecovery`, specify `Automatic` to
     enable automatic node recovery. SageMaker HyperPod replaces or reboots
     instances (nodes) when issues are found by the health-monitoring
     agent.

The following code snippet is a JSON request file template you can use.
For more information about the request syntax and parameters of this API,
see the [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") API reference.

```
// update_cluster.json
{
    // Required
    "ClusterName": "`name-of-cluster-to-update`",
    // Required
    "InstanceGroups": [{
        "InstanceGroupName": `"string"`,
        "InstanceType": `"string"`,
        "InstanceCount": `number`,
        "LifeCycleConfig": {
            "SourceS3Uri": `"string"`,
            "OnCreate": `"string"`
        },
        "ExecutionRole": `"string"`,
        "ThreadsPerCore": `number`,
        "OnStartDeepHealthChecks": [
            `"InstanceStress", "InstanceConnectivity"`
        ]
    }],
    "NodeRecovery": "`Automatic`"
}
```

2. Run the following `update-cluster` command to submit the
   request.

```
aws sagemaker update-cluster \
    --cli-input-json `file://complete/path/to/update_cluster.json`
```
