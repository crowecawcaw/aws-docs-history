

# Creating a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-eks-operate-cli-command-create-cluster"></a>

Learn how to create SageMaker HyperPod clusters orchestrated by Amazon EKS using the AWS CLI.

1. Before creating an SageMaker HyperPod cluster:

   1. Ensure that you have an existing Amazon EKS cluster up and running. For detailed instructions about how to set up an Amazon EKS cluster, see [Create an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) in the *Amazon EKS User Guide*.

   1. Install the Helm chart as instructed in [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md). If you create a [Amazon Nova SageMaker HyperPod cluster](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-cluster.html), you will need a separate Helm chart.

1. Prepare a lifecycle configuration script and upload to an Amazon S3 bucket, such as `s3://{{amzn-s3-demo-bucket}}/{{Lifecycle-scripts}}/{{base-config}}/`.

   For a quick start, download the sample script [`on_create.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts/base-config/on_create.sh) from the AWSome Distributed Training GitHub repository, and upload it to the S3 bucket. You can also include additional setup instructions, a series of setup scripts, or commands to be executed during the HyperPod cluster provisioning stage.
**Important**  
If you create an [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) attaching only the managed [`AmazonSageMakerClusterInstanceRolePolicy`](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html), your cluster has access to Amazon S3 buckets with the specific prefix `sagemaker-`.

   If you create a restricted instance group, you don't need to download and run the lifecycle script. Instead, you need to run `install_rig_dependencies.sh`. 

   The prerequisites to run the `install_rig_dependencies.sh` script include:
   + AWS Node (CNI) and CoreDNS should both be enabled. These are standard EKS add-ons that are not managed by the standard SageMaker HyperPod Helm, but can be easily enabled in the EKS console under Add-ons.
   +  The standard SageMaker HyperPod Helm chart should be installed before running this script.

   The `install_rig_dependencies.sh` script performs the following actions. 
   + `aws-node` (CNI): New `rig-aws-node` Daemonset created; existing `aws-node` patched to avoid RIG nodes.
   + `coredns`: Converted to Daemonset for RIGs to support multi-RIG use and prevent overloading.
   + training-operators: Updated with RIG Worker taint tolerations and nodeAffinity favoring non-RIG instances.
   + Elastic Fabric Adapter (EFA): Updated to tolerate RIG worker taint and use correct container images for each Region.

1. Prepare a [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) API request file in JSON format. For `ExecutionRole`, provide the ARN of the IAM role you created with the managed `AmazonSageMakerClusterInstanceRolePolicy` from the section [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod).
**Note**  
Ensure that your SageMaker HyperPod cluster is deployed within the same Virtual Private Cloud (VPC) as your Amazon EKS cluster. The subnets and security groups specified in the SageMaker HyperPod cluster configuration must allow network connectivity and communication with the Amazon EKS cluster's API server endpoint.

   ```
   // create_cluster.json
   {
       "ClusterName": {{"string"}},
       "InstanceGroups": [{
           "InstanceGroupName": {{"string"}},
           "InstanceType": {{"string"}},
           "InstanceCount": {{number}},
           "LifeCycleConfig": {
               "SourceS3Uri": {{"s3://amzn-s3-demo-bucket-sagemaker/lifecycle-script-directory/src/"}},
               "OnCreate": {{"on_create.sh"}}
           },
           "ExecutionRole": {{"string"}},
           "ThreadsPerCore": {{number}},
           "OnStartDeepHealthChecks": [
               {{"InstanceStress", "InstanceConnectivity"}}
           ]
       }],
       "RestrictedInstanceGroups": [ 
         { 
            "EnvironmentConfig": { 
               "FSxLustreConfig": { 
                  "PerUnitStorageThroughput": {{number}},
                  "SizeInGiB": {{number}}
               }
            },
            "ExecutionRole": {{"string"}},
            "InstanceCount": {{number}},
            "InstanceGroupName": {{"string"}},
            "InstanceStorageConfigs": [ 
               { ... }
            ],
            "InstanceType": {{"string"}},
            "OnStartDeepHealthChecks": [ {{"string"}} ],
            "OverrideVpcConfig": { 
               "SecurityGroupIds": [ {{"string"}} ],
               "Subnets": [ {{"string"}} ]
            },
            "ScheduledUpdateConfig": { 
               "DeploymentConfig": { 
                  "AutoRollbackConfiguration": [ 
                     { 
                        "AlarmName": {{"string"}}
                     }
                  ],
                  "RollingUpdatePolicy": { 
                     "MaximumBatchSize": { 
                        "Type": {{"string"}},
                        "Value": {{number}}
                     },
                     "RollbackMaximumBatchSize": { 
                        "Type": {{"string"}},
                        "Value": {{number}}
                     }
                  },
                  "WaitIntervalInSeconds": {{number}}
               },
               "ScheduleExpression": {{"string"}}
            },
            "ThreadsPerCore": {{number}},
            "TrainingPlanArn": {{"string"}}
         }
      ],
       "VpcConfig": {
           "SecurityGroupIds": [{{"string"}}],
           "Subnets": [{{"string"}}]
       },
       "Tags": [{
           "Key": {{"string"}},
           "Value": {{"string"}}
       }],
       "Orchestrator": {
           "Eks": {
               "ClusterArn": {{"string"}},
               "KubernetesConfig": {
                   "Labels": {
                       {{"nvidia.com/mig.config": "all-3g.40gb"}}
                   }
               }
           }
       },
       "NodeRecovery": "Automatic"
   }
   ```
**Flexible instance groups**  
Instead of specifying a single `InstanceType`, you can use the `InstanceRequirements` parameter to specify multiple instance types for an instance group. Note the following:  
`InstanceType` and `InstanceRequirements` are mutually exclusive. You must specify one or the other, but not both.
`InstanceRequirements.InstanceTypes` is an ordered list that determines provisioning priority. SageMaker HyperPod attempts to provision the first instance type in the list and falls back to subsequent types if capacity is unavailable. You can specify up to 20 instance types, and the list must not contain duplicates.
Flexible instance groups require continuous node provisioning mode.
The following example shows an instance group using `InstanceRequirements`:  

   ```
   {
       "InstanceGroupName": "flexible-ig",
       "InstanceRequirements": {
           "InstanceTypes": ["ml.p5.48xlarge", "ml.p4d.24xlarge", "ml.g6.48xlarge"]
       },
       "InstanceCount": 10,
       "LifeCycleConfig": {
           "SourceS3Uri": "s3://amzn-s3-demo-bucket-sagemaker/lifecycle-script-directory/src/",
           "OnCreate": "on_create.sh"
       },
       "ExecutionRole": "arn:aws:iam::111122223333:role/iam-role-for-cluster"
   }
   ```

   Note the following when configuring to create a new SageMaker HyperPod cluster associating with an EKS cluster.
   + You can configure up to 20 instance groups under the `InstanceGroups` parameter.
   + For `Orchestator.Eks.ClusterArn`, specify the ARN of the EKS cluster you want to use as the orchestrator.
   + For `OnStartDeepHealthChecks`, add `InstanceStress` and `InstanceConnectivity` to enable [Deep health checks](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md).
   + For `NodeRecovery`, specify `Automatic` to enable automatic node recovery. SageMaker HyperPod replaces or reboots instances (nodes) when issues are found by the health-monitoring agent.
   + For the `Tags` parameter, you can add custom tags for managing the SageMaker HyperPod cluster as an AWS resource. You can add tags to your cluster in the same way you add them in other AWS services that support tagging. To learn more about tagging AWS resources in general, see [Tagging AWS Resources User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).
   + For the `VpcConfig` parameter, specify the information of the VPC used in the EKS cluster. The subnets must be private.
   + For `Orchestrator.Eks.KubernetesConfig.Labels`, you can optionally specify Kubernetes labels to apply to the nodes. To enable GPU partitioning with Multi-Instance GPU (MIG), add the `nvidia.com/mig.config` label with the desired MIG profile. For example, `"nvidia.com/mig.config": "all-3g.40gb"` configures all GPUs with the 3g.40gb partition profile. For more information about GPU partitioning and available profiles, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md).

1. Run the [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-cluster.html) command as follows.
**Important**  
When running the `create-cluster` command with the `--cli-input-json` parameter, you must include the `file://` prefix before the complete path to the JSON file. This prefix is required to ensure that the AWS CLI recognizes the input as a file path. Omitting the `file://` prefix results in a parsing parameter error.

   ```
   aws sagemaker create-cluster \
       --cli-input-json {{file://complete/path/to/create_cluster.json}}
   ```

   This should return the ARN of the new cluster.
**Important**  
You can use the [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-cluster.html) operation to remove a restricted instance group (RIG). When a RIG is scaled down to 0, the FSx for Lustre file system won't be deleted. To completely remove the FSx for Lustre file system, you must remove the RIG entirely.   
Removing a RIG will not delete any artifacts stored in the service-managed Amazon S3 bucket. However, you should ensure all artifacts in the FSx for Lustre file system are fully synchronized to Amazon S3 before removal. We recommend waiting at least 30 minutes after job completion to ensure complete synchronization of all artifacts from the FSx for Lustre file system to the service-managed Amazon S3 bucket.
**Important**  
When using an onboarded On-Demand Capacity Reservation (ODCR), you must map your instance group to the same Availability Zone ID (AZ ID) as the ODCR by setting `OverrideVpcConfig` with a subnet in the matching AZ ID.  
CRITICAL: Verify `OverrideVpcConfig` configuration before deployment to avoid incurring duplicate charges for both ODCR and On-Demand Capacity.