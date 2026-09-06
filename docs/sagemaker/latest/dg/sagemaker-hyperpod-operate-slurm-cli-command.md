

# Managing SageMaker HyperPod Slurm clusters using the AWS CLI
<a name="sagemaker-hyperpod-operate-slurm-cli-command"></a>

The following topics provide guidance on writing SageMaker HyperPod API request files in JSON format and run them using the AWS CLI commands.

**Topics**
+ [Create a new cluster](#sagemaker-hyperpod-operate-slurm-cli-command-create-cluster)
+ [Describe a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-describe-cluster)
+ [List details of cluster nodes](#sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes)
+ [Describe details of a cluster node](#sagemaker-hyperpod-operate-slurm-cli-command-describe-cluster-node)
+ [List clusters](#sagemaker-hyperpod-operate-slurm-cli-command-list-clusters)
+ [Update cluster configuration](#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster)
+ [Update the SageMaker HyperPod platform software of a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software)
+ [Scale down a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-scale-down)
+ [Delete a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-delete-cluster)

## Create a new cluster
<a name="sagemaker-hyperpod-operate-slurm-cli-command-create-cluster"></a>

1. Prepare lifecycle configuration scripts and upload them to an S3 bucket, such as `s3://sagemaker-{{amzn-s3-demo-bucket}}/{{lifecycle-script-directory/src/}}`. The following step 2 assumes that there’s an entry point script named `on_create.sh` in the specified S3 bucket.
**Important**  
Make sure that you set the S3 path to start with `s3://sagemaker-`. The [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed [`AmazonSageMakerClusterInstanceRolePolicy`](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html) attached, which allows access to S3 buckets with the specific prefix `sagemaker-`.

1. Prepare a [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) API request file in JSON format. You should configure instance groups to match with the Slurm cluster you design in the `provisioning_parameters.json` file that'll be used during cluster creating as part of running a set of lifecycle scripts. To learn more, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md). The following template has two instance groups to meet the minimum requirement for a Slurm cluster: one controller (head) node and one compute (worker) node. For `ExecutionRole`, provide the ARN of the IAM role you created with the managed `AmazonSageMakerClusterInstanceRolePolicy` from the section [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod).

   ```
   // create_cluster.json
   {
       "ClusterName": "{{your-hyperpod-cluster}}",
       "InstanceGroups": [
           {
               "InstanceGroupName": "{{controller-group}}",
               "InstanceType": "{{ml.m5.xlarge}}",
               "InstanceCount": {{1}},
               "LifeCycleConfig": {
                   "SourceS3Uri": "s3://{{amzn-s3-demo-bucket}}-sagemaker/{{lifecycle-script-directory/src/}}",
                   "OnCreate": "{{on_create.sh}}"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{iam-role-for-cluster}}",
               // Optional: Configure an additional storage per instance group.
               "InstanceStorageConfigs": [
                   {
                      // Attach an additional EBS volume to each instance within the instance group.
                      // The default mount path for the additional EBS volume is /opt/sagemaker.
                      "EbsVolumeConfig":{
                         // Specify an integer between 1 and 16384 in gigabytes (GB).
                         "VolumeSizeInGB": {{integer}},
                      }
                   }
               ]
           }, 
           {
               "InstanceGroupName": "{{worker-group-1}}",
               "InstanceType": "{{ml.p4d.xlarge}}",
               "InstanceCount": {{1}},
               "LifeCycleConfig": {
                   "SourceS3Uri": "s3://{{amzn-s3-demo-bucket}}-sagemaker/{{lifecycle-script-directory/src/}}",
                   "OnCreate": "{{on_create.sh}}"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{iam-role-for-cluster}}"
           }
       ],
       // Optional
       "Tags": [ 
           { 
              "Key": "{{string}}",
              "Value": "{{string}}"
           }
       ],
       // Optional
       "VpcConfig": { 
           "SecurityGroupIds": [ "{{string}}" ],
           "Subnets": [ "{{string}}" ]
       }
   }
   ```

   Depending on how you design the cluster structure through your lifecycle scripts, you can configure up to 20 instance groups under the `InstanceGroups` parameter.

   For the `Tags` request parameter, you can add custom tags for managing the SageMaker HyperPod cluster as an AWS resource. You can add tags to your cluster in the same way you add them in other AWS services that support tagging. To learn more about tagging AWS resources in general, see [Tagging AWS Resources User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

   For the `VpcConfig` request parameter, specify the information of a VPC you want to use. For more information, see [Setting up SageMaker HyperPod with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc).

1. Run the [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-cluster.html) command as follows.

   ```
   aws sagemaker create-cluster \
       --cli-input-json {{file://complete/path/to/create_cluster.json}}
   ```

   This should return the ARN of the new cluster.

## Describe a cluster
<a name="sagemaker-hyperpod-operate-slurm-cli-command-describe-cluster"></a>

Run [describe-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster.html) to check the status of the cluster. You can specify either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster --cluster-name {{your-hyperpod-cluster}}
```

After the status of the cluster turns to **InService**, proceed to the next step. Using this API, you can also retrieve failure messages from running other HyperPod API operations.

## List details of cluster nodes
<a name="sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes"></a>

Run [list-cluster-nodes](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-cluster-nodes.html) to check the key information of the cluster nodes.

```
aws sagemaker list-cluster-nodes --cluster-name {{your-hyperpod-cluster}}
```

This returns a response, and the `InstanceId` is what you need to use for logging (using `aws ssm`) into them.

## Describe details of a cluster node
<a name="sagemaker-hyperpod-operate-slurm-cli-command-describe-cluster-node"></a>

Run [describe-cluster-node](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster-node.html) to retrieve details of a cluster node. You can get the cluster node ID from list-cluster-nodes output. You can specify either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster-node \
    --cluster-name {{your-hyperpod-cluster}} \
    --node-id {{i-111222333444555aa}}
```

## List clusters
<a name="sagemaker-hyperpod-operate-slurm-cli-command-list-clusters"></a>

Run [list-clusters](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-clusters.html) to list all clusters in your account.

```
aws sagemaker list-clusters
```

You can also add additional flags to filter the list of clusters down. To learn more about what this command runs at low level and additional flags for filtering, see the [ListClusters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusters.html) API reference.

## Update cluster configuration
<a name="sagemaker-hyperpod-operate-slurm-cli-command-update-cluster"></a>

Run [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) to update the configuration of a cluster.

**Note**  
You can use the `UpdateCluster` API to scale down or remove entire instance groups from your SageMaker HyperPod cluster. For additional instructions on how to scale down or delete instance groups, see [Scale down a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-scale-down).

1. Create an `UpdateCluster` request file in JSON format. Make sure that you specify the right cluster name and instance group name to update. You can change the instance type, the number of instances, the lifecycle configuration entrypoint script, and the path to the script.

   1. For `ClusterName`, specify the name of the cluster you want to update.

   1. For `InstanceGroupName`

      1. To update an existing instance group, specify the name of the instance group you want to update.

      1. To add a new instance group, specify a new name not existing in your cluster.

   1. For `InstanceType`

      1. To update an existing instance group, you must match the instance type you initially specified to the group.

      1. To add a new instance group, specify an instance type you want to configure the group with.

   1. For `InstanceCount`

      1. To update an existing instance group, specify an integer that corresponds to your desired number of instances. You can provide a higher or lower value (down to 0) to scale the instance group up or down.

      1. To add a new instance group, specify an integer greater or equal to 1. 

   1. For `LifeCycleConfig`, you can change both `SourceS3Uri` and `OnCreate` values as you want to update the instance group.

   1. For `ExecutionRole`

      1. For updating an existing instance group, keep using the same IAM role you attached during cluster creation.

      1. For adding a new instance group, specify an IAM role you want to attach.

   1. For `ThreadsPerCore`

      1. For updating an existing instance group, keep using the same value you specified during cluster creation.

      1. For adding a new instance group, you can choose any value from the allowed options per instance type. For more information, search the instance type and see the **Valid threads per core** column in the reference table at [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon EC2 User Guide*.

   The following code snippet is a JSON request file template you can use. For more information about the request syntax and parameters of this API, see the [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) API reference.

   ```
   // update_cluster.json
   {
       // Required
       "ClusterName": "{{name-of-cluster-to-update}}",
       // Required
       "InstanceGroups": [
           {
               "InstanceGroupName": "{{name-of-instance-group-to-update}}",
               "InstanceType": "{{ml.m5.xlarge}}",
               "InstanceCount": {{1}},
               "LifeCycleConfig": {
                   "SourceS3Uri": "s3://{{amzn-s3-demo-bucket}}-sagemaker/{{lifecycle-script-directory/src/}}",
                   "OnCreate": "{{on_create.sh}}"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{iam-role-for-cluster}}",
               // Optional: Configure an additional storage per instance group.
               "InstanceStorageConfigs": [
                   {
                      // Attach an additional EBS volume to each instance within the instance group.
                      // The default mount path for the additional EBS volume is /opt/sagemaker.
                      "EbsVolumeConfig":{
                         // Specify an integer between 1 and 16384 in gigabytes (GB).
                         "VolumeSizeInGB": {{integer}},
                      }
                   }
               ]
           },
           // add more blocks of instance groups as needed
           { ... }
       ]
   }
   ```

1. Run the following `update-cluster` command to submit the request. 

   ```
   aws sagemaker update-cluster \
       --cli-input-json {{file://complete/path/to/update_cluster.json}}
   ```

## Update the SageMaker HyperPod platform software of a cluster
<a name="sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software"></a>

Run [update-cluster-software](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster-software.html) to update existing clusters with software and security patches provided by the SageMaker HyperPod service. For `--cluster-name`, specify either the name or the ARN of the cluster to update.

**Important**  
Note that you must back up your work before running this API. The patching process replaces the root volume with the updated AMI, which means that your previous data stored in the instance root volume will be lost. Make sure that you back up your data from the instance root volume to Amazon S3 or Amazon FSx for Lustre. For more information, see [Use the backup script provided by SageMaker HyperPod](#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup).

```
aws sagemaker update-cluster-software --cluster-name {{your-hyperpod-cluster}}
```

This command calls the [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) API. After the API call, SageMaker HyperPod checks if there's a newer DLAMI available for the cluster instances. If a DLAMI update is required, SageMaker HyperPod will update the cluster instances to use the latest [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami) and run your lifecycle scripts in the Amazon S3 bucket that you specified during cluster creation or update. If the cluster is already using the latest DLAMI, SageMaker HyperPod will not make any changes to the cluster or run the lifecycle scripts again. The SageMaker HyperPod service team regularly rolls out new [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami)s for enhancing security and improving user experiences. We recommend that you always keep updating to the latest SageMaker HyperPod DLAMI. For future SageMaker HyperPod DLAMI updates for security patching, follow up with [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md).

**Tip**  
If the security patch fails, you can retrieve failure messages by running the [`DescribeCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCluster.html) API as instructed at [Describe a cluster](#sagemaker-hyperpod-operate-slurm-cli-command-describe-cluster).

**Note**  
You can only run this API programatically. The patching functionality is not implemented in the SageMaker HyperPod console UI.

### Use the backup script provided by SageMaker HyperPod
<a name="sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup"></a>

SageMaker HyperPod provides a script to back up and restore your data at [`1.architectures/5.sagemaker-hyperpod/patching-backup.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/patching-backup.sh) in the *Awsome Distributed Training GitHub repository*. The script provides the following two functions.

**To back up data to an S3 bucket before patching**

```
sudo bash patching-backup.sh --create {{<s3-buckup-bucket-path>}}
```

After you run the command, the script checks `squeue` if there are queued jobs, stops Slurm if there's no job in the queue, backs up `mariadb`, and copies local items on disc defined under `LOCAL_ITEMS`. You can add more files and directories to `LOCAL_ITEMS`.

```
# Define files and directories to back up.
LOCAL_ITEMS=(
    "/var/spool/slurmd"
    "/var/spool/slurmctld"
    "/etc/systemd/system/slurmctld.service"
    "/home/ubuntu/backup_slurm_acct_db.sql"
    # ... Add more items as needed
)
```

Also, you can add custom code to the provided script to back up any applications for your use case.

**To restore data from an S3 bucket after patching**

```
sudo bash patching-backup.sh --restore {{<s3-buckup-bucket-path>}}
```

## Scale down a cluster
<a name="sagemaker-hyperpod-operate-slurm-cli-command-scale-down"></a>

You can scale down the number of instances or delete instance groups in your SageMaker HyperPod cluster to optimize resource allocation or reduce costs.

You scale down by either using the `UpdateCluster` API operation to randomly terminate instances from your instance group down to a specified number, or by terminating specific instances using the `BatchDeleteClusterNodes` API operation. You can also completely remove entire instance groups using the `UpdateCluster` API. For more information about how to scale down using these methods, see [Scaling down a SageMaker HyperPod cluster](smcluster-scale-down.md).

**Note**  
You cannot remove instances that are configured as Slurm controller nodes. Attempting to delete a Slurm controller node results in a validation error with the error code `NODE_ID_IN_USE`.

## Delete a cluster
<a name="sagemaker-hyperpod-operate-slurm-cli-command-delete-cluster"></a>

Run [delete-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/delete-cluster.html) to delete a cluster. You can specify either the name or the ARN of the cluster.

```
aws sagemaker delete-cluster --cluster-name {{your-hyperpod-cluster}}
```