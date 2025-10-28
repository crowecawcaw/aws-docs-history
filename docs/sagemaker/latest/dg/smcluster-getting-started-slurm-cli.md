# Getting started with SageMaker HyperPod

using the AWS CLI

Create your first SageMaker HyperPod cluster using the AWS CLI commands for
HyperPod.

## Create your

first SageMaker HyperPod cluster with Slurm

The following tutorial demonstrates how to create a new SageMaker HyperPod cluster and
set it up with Slurm through the [AWS CLI
commands for SageMaker HyperPod](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-cli "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-cli"). Following the tutorial, you'll create a
HyperPod cluster with three Slurm nodes, `my-controller-group`,
`my-login-group`, and `worker-group-1`.

1. First, prepare and upload lifecycle scripts to an Amazon S3 bucket. During
   cluster creation, HyperPod runs them in each instance group. Upload
   lifecycle scripts to Amazon S3 using the following command.

```
aws s3 sync \
    ~/`local-dir-to-lifecycle-scripts`/* \
    s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`
```

###### Note

The S3 bucket path should start with a prefix `sagemaker-`,
because the [IAM role for
SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod")
with `AmazonSageMakerClusterInstanceRolePolicy` only allows
access to Amazon S3 buckets that starts with the specific prefix.

If you are starting from scratch, use sample lifecycle scripts provided in
the [Awsome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/"). The following
sub-steps show how to download, what to modify, and how to upload the sample
lifecycle scripts to an Amazon S3 bucket.

    1. Download a copy of the lifecycle script samples to a directory on
     your local computer.



    ```
    git clone https://github.com/aws-samples/awsome-distributed-training/
    ```
    2. Go into the directory [`1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config`](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config"),
     where you can find a set of lifecycle scripts.



    ```
    cd awsome-distributed-training/1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config
    ```

    To learn more about the lifecycle script samples, see [Customizing SageMaker HyperPod
     clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").
    3. Write a Slurm configuration file and save it as
     `provisioning_parameters.json`. In the file, specify
     basic Slurm configuration parameters to properly assign Slurm nodes
     to the SageMaker HyperPod cluster instance groups. In this tutorial, set
     up three Slurm nodes named `my-controller-group`,
     `my-login-group`, and `worker-group-1`, as
     shown in the following example configuration
     `provisioning_parameters.json`.



    ```
    {
        "version": "1.0.0",
        "workload_manager": "`slurm`",
        "controller_group": "`my-controller-group`",
        "login_group": "`my-login-group`",
        "worker_groups": [
            {
                "instance_group_name": "`worker-group-1`",
                "partition_name": "`partition-1`"
            }
        ]
    }
    ```
    4. Upload the scripts to
     `s3://sagemaker-`<unique-s3-bucket-name>`/`<lifecycle-script-directory>`/src`.
     You can do so by using the Amazon S3 console, or by running the following
     AWS CLI Amazon S3 command.



    ```
    aws s3 sync \
        ~/`local-dir-to-lifecycle-scripts`/* \
        s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`
    ```

2. Prepare a [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") request file in JSON format and save as
   `create_cluster.json`. The following request template aligns
   with the Slurm node configuration defined in the
   `provisioning_parameters.json` in Step 1.c. For
   `ExecutionRole`, provide the ARN of the IAM role you
   created with the managed
   `AmazonSageMakerClusterInstanceRolePolicy` in [Prerequisites for using
   SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md").

```
{
    `// Required: Specify the name of the cluster.`
    "ClusterName": "`my-hyperpod-cluster`",
    `// Required: Configure instance groups to be launched in the cluster`
    "InstanceGroups": [
        {
            `// Required: Specify the basic configurations to set up a controller node.`
            "InstanceGroupName": "`my-controller-group`",
            "InstanceType": "`ml.c5.xlarge`",
            "InstanceCount": `1`,
            "LifeCycleConfig": {
              "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
              "OnCreate": "`on_create.sh`"
            },
            "ExecutionRole": "`${ROLE}`",
            `// Optional: Configure an additional storage per instance group.`
            "InstanceStorageConfigs": [
                {
                   `// Attach an additional EBS volume to each instance within the instance group.`
                   `// The default mount path for the additional EBS volume is /opt/sagemaker.`
                   "EbsVolumeConfig":{
                      `// Specify an integer between 1 and 16384 in gigabytes (GB).`
                      "VolumeSizeInGB": `<integer>`
                   }
                }
            ]
        },
        {
            "InstanceGroupName": "`my-login-group`",
            "InstanceType": "`ml.m5.4xlarge`",
            "InstanceCount": `1`,
            "LifeCycleConfig": {
              "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
              "OnCreate": "`on_create.sh`"
            },
            "ExecutionRole": "`${ROLE}`"
        },
        {
            "InstanceGroupName": "`worker-group-1`",
            "InstanceType": "`ml.trn1.32xlarge`",
            "InstanceCount": `1`,
            "LifeCycleConfig": {
              "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
              "OnCreate": "`on_create.sh`"
            },
            "ExecutionRole": "`${ROLE}`"
        }
    ]
}
```

3. Run the following command to create the cluster.

```
aws sagemaker create-cluster --cli-input-json `file://complete/path/to/create_cluster.json`
```

This should return the ARN of the created cluster.

If you receive an error due to resource limits, ensure that you change the
instance type to one with sufficient quotas in your account, or request
additional quotas by following [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas"). 4. Run `describe-cluster` to check the status of the
cluster.

```
aws sagemaker describe-cluster --cluster-name `my-hyperpod-cluster`
```

After the status of the cluster turns to `InService`,
proceed to the next step. 5. Run `list-cluster-nodes` to check the details of the cluster
nodes.

```
aws sagemaker list-cluster-nodes --cluster-name `my-hyperpod-cluster`
```

This returns a response, and the `InstanceId` is what your
cluster users need for logging (`aws ssm`) into them. For more
information about logging into the cluster nodes and running ML workloads,
see [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md "sagemaker-hyperpod-run-jobs-slurm.md").

## Delete the cluster and clean resources

After you have successfully tested creating a SageMaker HyperPod cluster, it continues
running in the `InService` state until you delete the cluster. We
recommend that you delete any clusters created using on-demand SageMaker AI capacity when
not in use to avoid incurring continued service charges based on on-demand pricing.
In this tutorial, you have created a cluster that consists of two instance groups.
One of them uses a C5 instance, so make sure you delete the cluster by running the
following command.

```
aws sagemaker delete-cluster --cluster-name `my-hyperpod-cluster`
```

To clean up the lifecycle scripts from the Amazon S3 bucket used for this tutorial, go
to the Amazon S3 bucket you used during cluster creation and remove the files entirely.

If you have tested running any model training workloads on the cluster, also check
if you have uploaded any data or if your job has saved any artifacts to different
Amazon S3 buckets or file system services such as Amazon FSx for Lustre and Amazon Elastic File System. To
prevent incurring charges, delete all artifacts and data from the storage or file
system.
