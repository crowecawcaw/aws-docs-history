

# Create a SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI
<a name="use-training-plan-for-hyperpod-creation-using-api-cli-sdk"></a>

To use SageMaker training plans for your Amazon SageMaker HyperPod cluster, specify the ARN of the training plan you want to use in the [`TrainingPlanArn`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html#sagemaker-Type-ClusterInstanceGroupSpecification-TrainingPlanArn) parameter of the [`ClusterInstanceGroupSpecification`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html) when calling the [`CreateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) API operation. 

Ensure that the subnet associated with the designated AZ of your plan is included in the `VPCConfig` of your cluster configuration. You can retrieve the `AvailabilityZone` of a training plan in the response of a [``DescribeTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlan.html) API call.

The following sample illustrates how to create a new SageMaker HyperPod cluster and provide an instance group with a training plan in the `--instance-groups` attribute of the `create-cluster` AWS CLI command. 

```
# Create a cluster         
aws sagemaker create-cluster \
  --cluster-name {{cluster-name}} \
  --instance-groups '[ \
        { \
            "InstanceCount": {{1}},\
            "InstanceGroupName": "{{controller-nodes}}",\
            "InstanceType": "{{ml.t3.xlarge}}",\
            "LifeCycleConfig": {"SourceS3Uri": {{source_s3_uri}}, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::{{customer_account_id}}:role/{{execution_role}}",\
            "ThreadsPerCore": {{1}},\
        },\
        { \
            "InstanceCount": {{2}}, \
            "InstanceGroupName": "{{worker-nodes}}",\
            "InstanceType": "{{p4d.24xlarge}}",\
            "LifeCycleConfig": {"SourceS3Uri": {{source_s3_uri}}, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::{{customer_account_id}}}:role/{{execution_role}}}",\
            "ThreadsPerCore": {{1}},\
            "TrainingPlanArn": {{training_plan_arn}},\
        }]'
```

For information about how to create an HyperPod cluster using the AWS CLI, see [`create-cluster`](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-cluster.html).

After creating the cluster, you can verify that your instance group was properly assigned capacity from the training plan by calling the `DescribeCluster` API.

```
aws sagemaker describe-cluster --cluster-name {{cluster-name}}
```