# Create a

SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI

To use SageMaker training plans for your Amazon SageMaker HyperPod cluster, specify the ARN of the training
plan you want to use in the [`TrainingPlanArn`](../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-TrainingPlanArn "../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-TrainingPlanArn") parameter of the [`ClusterInstanceGroupSpecification`](../APIReference/API_ClusterInstanceGroupSpecification.md "../APIReference/API_ClusterInstanceGroupSpecification.md") when calling the [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") API operation.

Ensure that the subnet associated with the designated AZ of your plan is included in the
`VPCConfig` of your cluster configuration. You can retrieve the
`AvailabilityZone` of a training plan in the response of a [DescribeTrainingPlan](../APIReference/API_DescribeTrainingPlan.md "../APIReference/API_DescribeTrainingPlan.md") API call.

The following sample illustrates how to create a new SageMaker HyperPod cluster and provide an
instance group with a training plan in the `--instance-groups` attribute of the
`create-cluster` AWS CLI command.

```
# Create a cluster
aws sagemaker create-cluster \
  --cluster-name `cluster-name` \
  --instance-groups '[ \
        { \
            "InstanceCount": `1`,\
            "InstanceGroupName": "`controller-nodes`",\
            "InstanceType": "`ml.t3.xlarge`",\
            "LifeCycleConfig": {"SourceS3Uri": `source_s3_uri`, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::`customer_account_id`:role/`execution_role`",\
            "ThreadsPerCore": `1`,\
        },\
        { \
            "InstanceCount": `2`, \
            "InstanceGroupName": "`worker-nodes`",\
            "InstanceType": "`p4d.24xlarge`",\
            "LifeCycleConfig": {"SourceS3Uri": `source_s3_uri`, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::`customer_account_id`}:role/`execution_role`}",\
            "ThreadsPerCore": `1`,\
            "TrainingPlanArn": `training_plan_arn`,\
        }]'
```

For information about how to create an HyperPod cluster using the AWS CLI, see
[`create-cluster`](../../../cli/latest/reference/sagemaker/create-cluster.md "../../../cli/latest/reference/sagemaker/create-cluster.md").

After creating the cluster, you can verify that your instance group was properly assigned
capacity from the training plan by calling the `DescribeCluster` API.

```
aws sagemaker describe-cluster --cluster-name `cluster-name`
```
