# Update a

SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI

You can add, update, or remove a training plan by updating the instance group of an
existing cluster using the `update-cluster` AWS CLI command. The following sample
illustrates how to update a SageMaker HyperPod cluster and provide an instance group with a new
training plan.

```
# Update a cluster
aws sagemaker update-cluster \
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
        },\
        {\
            "InstanceCount": `1`,\
            "InstanceGroupName": "`worker-nodes-2`",\
            "InstanceType": "`p4d.24xlarge`",\
            "LifeCycleConfig": {"SourceS3Uri": `source_s3_uri`, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::`customer_account_id`:role/`execution_role`",\
            "ThreadsPerCore": `1`,\
            "TrainingPlanArn": `training_plan_arn`,\
        }\
    ]'
```
