# Use Amazon SageMaker AI Jobs

This section is based on the original version of [SageMaker AI Operators for
Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s "https://github.com/aws/amazon-sagemaker-operator-for-k8s").

###### Important

We are stopping the development and technical
support of the original version of [SageMaker Operators for Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master "https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master").

If you are currently using version `v1.2.2`
or below of [SageMaker Operators for Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master "https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master"), we recommend migrating your resources to the
[ACK service controller for Amazon SageMaker](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller").
The ACK service controller is a new generation of SageMaker Operators for Kubernetes based on
[AWS Controllers for Kubernetes (ACK)](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/").

For information on the migration steps, see [Migrate resources to the latest
Operators](kubernetes-sagemaker-operators-migrate.md "kubernetes-sagemaker-operators-migrate.md").

For answers to frequently asked
questions on the end of support of the original version of SageMaker Operators for
Kubernetes, see [Announcing the End of Support
of the Original Version of SageMaker AI
Operators for Kubernetes](kubernetes-sagemaker-operators-eos-announcement.md "kubernetes-sagemaker-operators-eos-announcement.md")

To run an Amazon SageMaker AI job using the Operators for Kubernetes, you can either apply a YAML file or
use the supplied Helm Charts.

All sample operator jobs in the following tutorials use sample data taken from a public
MNIST dataset. In order to run these samples, download the dataset into your Amazon S3 bucket. You
can find the dataset in [Download the MNIST Dataset.](ex1-preprocess-data-pull-data.md "ex1-preprocess-data-pull-data.md")

###### Contents

- [The TrainingJob operator](#trainingjob-operator "#trainingjob-operator")
- [The HyperParameterTuningJob
  operator](#hyperparametertuningjobs-operator "#hyperparametertuningjobs-operator")
- [The BatchTransformJob operator](#batchtransformjobs-operator "#batchtransformjobs-operator")
- [The HostingDeployment operator](#hosting-deployment-operator "#hosting-deployment-operator")
- [The ProcessingJob operator](#kubernetes-processing-job-operator "#kubernetes-processing-job-operator")
- [HostingAutoscalingPolicy (HAP)
  Operator](#kubernetes-hap-operator "#kubernetes-hap-operator")

## The TrainingJob operator

Training job operators reconcile your specified training job spec to SageMaker AI by launching it
for you in SageMaker AI. You can learn more about SageMaker training jobs in the SageMaker AI [CreateTrainingJob API documentation](API_CreateTrainingJob.md "API_CreateTrainingJob.md").

###### Topics

- [Create a TrainingJob using a
  YAML file](#create-a-trainingjob-using-a-simple-yaml-file "#create-a-trainingjob-using-a-simple-yaml-file")
- [Create a TrainingJob Using a Helm Chart](#create-a-trainingjob-using-a-helm-chart "#create-a-trainingjob-using-a-helm-chart")
- [List TrainingJobs](#list-training-jobs "#list-training-jobs")
- [Describe a TrainingJob](#describe-a-training-job "#describe-a-training-job")
- [View logs from TrainingJobs](#view-logs-from-training-jobs "#view-logs-from-training-jobs")
- [Delete TrainingJobs](#delete-training-jobs "#delete-training-jobs")

### Create a TrainingJob using a

YAML file

1. Download the sample YAML file for training using the following command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/xgboost-mnist-trainingjob.yaml
```

2. Edit the `xgboost-mnist-trainingjob.yaml` file to replace the
   `roleArn` parameter with your
   `<sagemaker-execution-role>`, and `outputPath` with your
   Amazon S3 bucket to which the SageMaker AI execution role has write access. The `roleArn`
   must have permissions so that SageMaker AI can access Amazon S3, Amazon CloudWatch, and other services on your
   behalf. For more information on creating an SageMaker AI ExecutionRole, see [SageMaker AI Roles](sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms "sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms"). Apply the YAML file using the following command:

```
kubectl apply -f xgboost-mnist-trainingjob.yaml
```

### Create a TrainingJob Using a Helm Chart

You can use Helm Charts to run TrainingJobs.

1. Clone the GitHub repository to get the source using the following command:

```
git clone https://github.com/aws/amazon-sagemaker-operator-for-k8s.git
```

2. Navigate to the
   `amazon-sagemaker-operator-for-k8s/hack/charts/training-jobs/` folder and
   edit the `values.yaml` file to replace values like `rolearn` and
   `outputpath` with values that correspond to your account. The RoleARN must
   have permissions so that SageMaker AI can access Amazon S3, Amazon CloudWatch, and other services on your
   behalf. For more information on creating an SageMaker AI ExecutionRole, see [SageMaker AI Roles](sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms "sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms").

#### Create the TrainingJob

With the roles and Amazon S3 buckets replaced with appropriate values in
`values.yaml`, you can create a training job using the following command:

```
helm install . --generate-name
```

Your output should look like the following:

```
NAME: chart-12345678
LAST DEPLOYED: Wed Nov 20 23:35:49 2019
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thanks for installing the sagemaker-k8s-trainingjob.
```

#### Verify your training Helm Chart

To verify that the Helm Chart was created successfully, run:

```
helm ls
```

Your output should look like the following:

```
NAME                    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                           APP VERSION
chart-12345678        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-trainingjob-0.1.0
rolebased-12345678    default         1               2019-11-20 23:14:59.6777082 +0000 UTC   deployed        sagemaker-k8s-operator-0.1.0
```

`helm install` creates a `TrainingJob` Kubernetes resource. The
operator launches the actual training job in SageMaker AI and updates the `TrainingJob`
Kubernetes resource to reflect the status of the job in SageMaker AI. You incur charges for SageMaker AI
resources used during the duration of your job. You do not incur any charges once your job
completes or stops.

**Note**: SageMaker AI does not allow you to update a running
training job. You cannot edit any parameter and re-apply the config file. Either change
the metadata name or delete the existing job and create a new one. Similar to existing
training job operators like TFJob in Kubeflow, `update` is not supported.

### List TrainingJobs

Use the following command to list all jobs created using the Kubernetes operator:

```
kubectl get TrainingJob
```

The output listing all jobs should look like the following:

```
kubectl get trainingjobs
NAME                        STATUS       SECONDARY-STATUS   CREATION-TIME          SAGEMAKER-JOB-NAME
xgboost-mnist-from-for-s3   InProgress   Starting           2019-11-20T23:42:35Z   xgboost-mnist-from-for-s3-examplef11eab94e0ed4671d5a8f
```

A training job continues to be listed after the job has completed or failed. You can
remove a `TrainingJob` job from the list by following the
[Delete TrainingJobs](#delete-training-jobs "#delete-training-jobs") steps.
Jobs that have completed or stopped do not incur
any charges for SageMaker AI resources.

#### TrainingJob status values

The `STATUS` field can be one of the following values:

- `Completed`
- `InProgress`
- `Failed`
- `Stopped`
- `Stopping`

These statuses come directly from the SageMaker AI official [API documentation](API_DescribeTrainingJob.md#SageMaker-DescribeTrainingJob-response-TrainingJobStatus "API_DescribeTrainingJob.md#SageMaker-DescribeTrainingJob-response-TrainingJobStatus").

In addition to the official SageMaker AI status, it is possible for `STATUS` to be
`SynchronizingK8sJobWithSageMaker`. This means that the operator has not yet
processed the job.

#### Secondary status values

The secondary statuses come directly from the SageMaker AI official [API documentation](API_DescribeTrainingJob.md#SageMaker-DescribeTrainingJob-response-SecondaryStatus "API_DescribeTrainingJob.md#SageMaker-DescribeTrainingJob-response-SecondaryStatus"). They contain more granular information about the status of
the job.

### Describe a TrainingJob

You can get more details about the training job by using the `describe`
`kubectl` command. This is typically used for debugging a problem or checking the
parameters of a training job. To get information about your training job, use the following
command:

```
kubectl describe trainingjob xgboost-mnist-from-for-s3
```

The output for your training job should look like the following:

```
Name:         xgboost-mnist-from-for-s3
Namespace:    default
Labels:       <none>
Annotations:  <none>
API Version:  sagemaker.aws.amazon.com/v1
Kind:         TrainingJob
Metadata:
  Creation Timestamp:  2019-11-20T23:42:35Z
  Finalizers:
    sagemaker-operator-finalizer
  Generation:        2
  Resource Version:  23119
  Self Link:         /apis/sagemaker.aws.amazon.com/v1/namespaces/default/trainingjobs/xgboost-mnist-from-for-s3
  UID:               6d7uiui-0bef-11ea-b94e-0ed467example
Spec:
  Algorithm Specification:
    Training Image:       8256416981234.dkr.ecr.us-east-2.amazonaws.com/xgboost:1
    Training Input Mode:  File
  Hyper Parameters:
    Name:   eta
    Value:  0.2
    Name:   gamma
    Value:  4
    Name:   max_depth
    Value:  5
    Name:   min_child_weight
    Value:  6
    Name:   num_class
    Value:  10
    Name:   num_round
    Value:  10
    Name:   objective
    Value:  multi:softmax
    Name:   silent
    Value:  0
  Input Data Config:
    Channel Name:      train
    Compression Type:  None
    Content Type:      text/csv
    Data Source:
      S 3 Data Source:
        S 3 Data Distribution Type:  FullyReplicated
        S 3 Data Type:               S3Prefix
        S 3 Uri:                     https://s3-us-east-2.amazonaws.com/amzn-s3-demo-bucket/sagemaker/xgboost-mnist/train/
    Channel Name:                    validation
    Compression Type:                None
    Content Type:                    text/csv
    Data Source:
      S 3 Data Source:
        S 3 Data Distribution Type:  FullyReplicated
        S 3 Data Type:               S3Prefix
        S 3 Uri:                     https://s3-us-east-2.amazonaws.com/amzn-s3-demo-bucket/sagemaker/xgboost-mnist/validation/
  Output Data Config:
    S 3 Output Path:  s3://amzn-s3-demo-bucket/sagemaker/xgboost-mnist/xgboost/
  Region:             us-east-2
  Resource Config:
    Instance Count:     1
    Instance Type:      ml.m4.xlarge
    Volume Size In GB:  5
  Role Arn:             arn:aws:iam::12345678910:role/service-role/AmazonSageMaker-ExecutionRole
  Stopping Condition:
    Max Runtime In Seconds:  86400
  Training Job Name:         xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0example
Status:
  Cloud Watch Log URL:           https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#logStream:group=/aws/sagemaker/TrainingJobs;prefix=<example>;streamFilter=typeLogStreamPrefix
  Last Check Time:               2019-11-20T23:44:29Z
  Sage Maker Training Job Name:  xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94eexample
  Secondary Status:              Downloading
  Training Job Status:           InProgress
Events:                          <none>
```

### View logs from TrainingJobs

Use the following command to see the logs from the `kmeans-mnist` training
job:

```
kubectl smlogs trainingjob xgboost-mnist-from-for-s3
```

Your output should look similar to the following. The logs from instances are ordered
chronologically.

```
"xgboost-mnist-from-for-s3" has SageMaker TrainingJobName "xgboost-mnist-from-for-s3-123456789" in region "us-east-2", status "InProgress" and secondary status "Starting"
xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0ed46example/algo-1-1574293123 2019-11-20 23:45:24.7 +0000 UTC Arguments: train
xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0ed46example/algo-1-1574293123 2019-11-20 23:45:24.7 +0000 UTC [2019-11-20:23:45:22:INFO] Running standalone xgboost training.
xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0ed46example/algo-1-1574293123 2019-11-20 23:45:24.7 +0000 UTC [2019-11-20:23:45:22:INFO] File size need to be processed in the node: 1122.95mb. Available memory size in the node: 8586.0mb
xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0ed46example/algo-1-1574293123 2019-11-20 23:45:24.7 +0000 UTC [2019-11-20:23:45:22:INFO] Determined delimiter of CSV input is ','
xgboost-mnist-from-for-s3-6d7fa0af0bef11eab94e0ed46example/algo-1-1574293123 2019-11-20 23:45:24.7 +0000 UTC [23:45:22] S3DistributionType set as FullyReplicated
```

### Delete TrainingJobs

Use the following command to stop a training job on Amazon SageMaker AI:

```
kubectl delete trainingjob xgboost-mnist-from-for-s3
```

This command removes the SageMaker training job from Kubernetes. This command returns the
following output:

```
trainingjob.sagemaker.aws.amazon.com "xgboost-mnist-from-for-s3" deleted
```

If the job is still in progress on SageMaker AI, the job stops. You do not incur any charges for
SageMaker AI resources after your job stops or completes.

**Note**: SageMaker AI does not delete training jobs. Stopped
jobs continue to show on the SageMaker AI console. The `delete` command takes about 2
minutes to clean up the resources from SageMaker AI.

## The HyperParameterTuningJob

operator

Hyperparameter tuning job operators reconcile your specified hyperparameter tuning job
spec to SageMaker AI by launching it in SageMaker AI. You can learn more about SageMaker AI hyperparameter tuning jobs
in the SageMaker AI [CreateHyperParameterTuningJob API documentation](API_CreateHyperParameterTuningJob.md "API_CreateHyperParameterTuningJob.md").

###### Topics

- [Create a
  HyperparameterTuningJob using a YAML file](#create-a-hyperparametertuningjob-using-a-simple-yaml-file "#create-a-hyperparametertuningjob-using-a-simple-yaml-file")
- [Create a
  HyperparameterTuningJob using a Helm Chart](#create-a-hyperparametertuningjob-using-a-helm-chart "#create-a-hyperparametertuningjob-using-a-helm-chart")
- [List HyperparameterTuningJobs](#list-hyperparameter-tuning-jobs "#list-hyperparameter-tuning-jobs")
- [Describe a HyperparameterTuningJob](#describe-a-hyperparameter-tuning-job "#describe-a-hyperparameter-tuning-job")
- [View logs from
  HyperparameterTuningJobs](#view-logs-from-hyperparametertuning-jobs "#view-logs-from-hyperparametertuning-jobs")
- [Delete a HyperparameterTuningJob](#delete-hyperparametertuning-jobs "#delete-hyperparametertuning-jobs")

### Create a

HyperparameterTuningJob using a YAML file

1. Download the sample YAML file for the hyperparameter tuning job using the following
   command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/xgboost-mnist-hpo.yaml
```

2. Edit the `xgboost-mnist-hpo.yaml` file to replace the
   `roleArn` parameter with your `sagemaker-execution-role`. For
   the hyperparameter tuning job to succeed, you must also change the
   `s3InputPath` and `s3OutputPath` to values that correspond to
   your account. Apply the updates YAML file using the following command:

```
kubectl apply -f xgboost-mnist-hpo.yaml
```

### Create a

HyperparameterTuningJob using a Helm Chart

You can use Helm Charts to run hyperparameter tuning jobs.

1. Clone the GitHub repository to get the source using the following command:

```
git clone https://github.com/aws/amazon-sagemaker-operator-for-k8s.git
```

2. Navigate to the
   `amazon-sagemaker-operator-for-k8s/hack/charts/hyperparameter-tuning-jobs/`
   folder.
3. Edit the `values.yaml` file to replace the `roleArn` parameter
   with your `sagemaker-execution-role`. For the hyperparameter tuning job to
   succeed, you must also change the `s3InputPath` and `s3OutputPath`
   to values that correspond to your account.

#### Create the HyperparameterTuningJob

With the roles and Amazon S3 paths replaced with appropriate values in
`values.yaml`, you can create a hyperparameter tuning job using the following
command:

```
helm install . --generate-name
```

Your output should look similar to the following:

```
NAME: chart-1574292948
LAST DEPLOYED: Wed Nov 20 23:35:49 2019
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thanks for installing the sagemaker-k8s-hyperparametertuningjob.
```

#### Verify chart installation

To verify that the Helm Chart was created successfully, run the following command:

```
helm ls
```

Your output should look like the following:

```
NAME                    NAMESPACE       REVISION        UPDATED
chart-1474292948        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-hyperparametertuningjob-0.1.0                               STATUS          CHART                           APP VERSION
chart-1574292948        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-trainingjob-0.1.0
rolebased-1574291698    default         1               2019-11-20 23:14:59.6777082 +0000 UTC   deployed        sagemaker-k8s-operator-0.1.0
```

`helm install` creates a `HyperParameterTuningJob` Kubernetes
resource. The operator launches the actual hyperparameter optimization job in SageMaker AI and
updates the `HyperParameterTuningJob` Kubernetes resource to reflect the status
of the job in SageMaker AI. You incur charges for SageMaker AI resources used during the duration of your
job. You do not incur any charges once your job completes or stops.

**Note**: SageMaker AI does not allow you to update a running
hyperparameter tuning job. You cannot edit any parameter and re-apply the config file.
You must either change the metadata name or delete the existing job and create a new one.
Similar to existing training job operators like `TFJob` in Kubeflow,
`update` is not supported.

### List HyperparameterTuningJobs

Use the following command to list all jobs created using the Kubernetes operator:

```
kubectl get hyperparametertuningjob
```

Your output should look like the following:

```
NAME         STATUS      CREATION-TIME          COMPLETED   INPROGRESS   ERRORS   STOPPED   BEST-TRAINING-JOB                               SAGEMAKER-JOB-NAME
xgboost-mnist-hpo   Completed   2019-10-17T01:15:52Z   10          0            0        0         xgboostha92f5e3cf07b11e9bf6c06d6-009-4c7a123   xgboostha92f5e3cf07b11e9bf6c123
```

A hyperparameter tuning job continues to be listed after the job has completed or
failed. You can remove a `hyperparametertuningjob` from the list by following the
steps in [Delete a HyperparameterTuningJob](#delete-hyperparametertuning-jobs "#delete-hyperparametertuning-jobs").
Jobs that have completed or stopped do not incur any charges for SageMaker AI resources.

#### Hyperparameter tuning job status

values

The `STATUS` field can be one of the following values:

- `Completed`
- `InProgress`
- `Failed`
- `Stopped`
- `Stopping`

These statuses come directly from the SageMaker AI official [API documentation](API_DescribeHyperParameterTuningJob.md#SageMaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus "API_DescribeHyperParameterTuningJob.md#SageMaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus").

In addition to the official SageMaker AI status, it is possible for `STATUS` to be
`SynchronizingK8sJobWithSageMaker`. This means that the operator has not yet
processed the job.

#### Status counters

The output has several counters, like `COMPLETED` and
`INPROGRESS`. These represent how many training jobs have completed and are
in progress, respectively. For more information about how these are determined, see [TrainingJobStatusCounters](API_TrainingJobStatusCounters.md "API_TrainingJobStatusCounters.md") in the SageMaker API documentation.

#### Best TrainingJob

This column contains the name of the `TrainingJob` that best optimized the
selected metric.

To see a summary of the tuned hyperparameters, run:

```
kubectl describe hyperparametertuningjob xgboost-mnist-hpo
```

To see detailed information about the `TrainingJob`, run:

```
kubectl describe trainingjobs `<job name>`
```

#### Spawned TrainingJobs

You can also track all 10 training jobs in Kubernetes launched by
`HyperparameterTuningJob` by running the following command:

```
kubectl get trainingjobs
```

### Describe a HyperparameterTuningJob

You can obtain debugging details using the `describe`
`kubectl` command.

```
kubectl describe hyperparametertuningjob xgboost-mnist-hpo
```

In addition to information about the tuning job, the SageMaker AI Operator for Kubernetes also
exposes the [best training job](automatic-model-tuning-monitor.md#automatic-model-tuning-best-training-job "automatic-model-tuning-monitor.md#automatic-model-tuning-best-training-job") found by the hyperparameter tuning job in the
`describe` output as follows:

```
Name:         xgboost-mnist-hpo
Namespace:    default
Labels:       <none>
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"sagemaker.aws.amazon.com/v1","kind":"HyperparameterTuningJob","metadata":{"annotations":{},"name":"xgboost-mnist-hpo","namespace":...
API Version:  sagemaker.aws.amazon.com/v1
Kind:         HyperparameterTuningJob
Metadata:
  Creation Timestamp:  2019-10-17T01:15:52Z
  Finalizers:
    sagemaker-operator-finalizer
  Generation:        2
  Resource Version:  8167
  Self Link:         /apis/sagemaker.aws.amazon.com/v1/namespaces/default/hyperparametertuningjobs/xgboost-mnist-hpo
  UID:               a92f5e3c-f07b-11e9-bf6c-06d6f303uidu
Spec:
  Hyper Parameter Tuning Job Config:
    Hyper Parameter Tuning Job Objective:
      Metric Name:  validation:error
      Type:         Minimize
    Parameter Ranges:
      Integer Parameter Ranges:
        Max Value:     20
        Min Value:     10
        Name:          num_round
        Scaling Type:  Linear
    Resource Limits:
      Max Number Of Training Jobs:     10
      Max Parallel Training Jobs:      10
    Strategy:                          Bayesian
    Training Job Early Stopping Type:  Off
  Hyper Parameter Tuning Job Name:     xgboostha92f5e3cf07b11e9bf6c06d6
  Region:                              us-east-2
  Training Job Definition:
    Algorithm Specification:
      Training Image:       12345678910.dkr.ecr.us-east-2.amazonaws.com/xgboost:1
      Training Input Mode:  File
    Input Data Config:
      Channel Name:  train
      Content Type:  text/csv
      Data Source:
        s3DataSource:
          s3DataDistributionType:  FullyReplicated
          s3DataType:              S3Prefix
          s3Uri:                   https://s3-us-east-2.amazonaws.com/amzn-s3-demo-bucket/sagemaker/xgboost-mnist/train/
      Channel Name:                validation
      Content Type:                text/csv
      Data Source:
        s3DataSource:
          s3DataDistributionType:  FullyReplicated
          s3DataType:              S3Prefix
          s3Uri:                   https://s3-us-east-2.amazonaws.com/amzn-s3-demo-bucket/sagemaker/xgboost-mnist/validation/
    Output Data Config:
      s3OutputPath:  https://s3-us-east-2.amazonaws.com/amzn-s3-demo-bucket/sagemaker/xgboost-mnist/xgboost
    Resource Config:
      Instance Count:     1
      Instance Type:      ml.m4.xlarge
      Volume Size In GB:  5
    Role Arn:             arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole
    Static Hyper Parameters:
      Name:   base_score
      Value:  0.5
      Name:   booster
      Value:  gbtree
      Name:   csv_weights
      Value:  0
      Name:   dsplit
      Value:  row
      Name:   grow_policy
      Value:  depthwise
      Name:   lambda_bias
      Value:  0.0
      Name:   max_bin
      Value:  256
      Name:   max_leaves
      Value:  0
      Name:   normalize_type
      Value:  tree
      Name:   objective
      Value:  reg:linear
      Name:   one_drop
      Value:  0
      Name:   prob_buffer_row
      Value:  1.0
      Name:   process_type
      Value:  default
      Name:   rate_drop
      Value:  0.0
      Name:   refresh_leaf
      Value:  1
      Name:   sample_type
      Value:  uniform
      Name:   scale_pos_weight
      Value:  1.0
      Name:   silent
      Value:  0
      Name:   sketch_eps
      Value:  0.03
      Name:   skip_drop
      Value:  0.0
      Name:   tree_method
      Value:  auto
      Name:   tweedie_variance_power
      Value:  1.5
    Stopping Condition:
      Max Runtime In Seconds:  86400
Status:
  Best Training Job:
    Creation Time:  2019-10-17T01:16:14Z
    Final Hyper Parameter Tuning Job Objective Metric:
      Metric Name:        validation:error
      Value:
    Objective Status:     Succeeded
    Training End Time:    2019-10-17T01:20:24Z
    Training Job Arn:     arn:aws:sagemaker:us-east-2:123456789012:training-job/xgboostha92f5e3cf07b11e9bf6c06d6-009-4sample
    Training Job Name:    xgboostha92f5e3cf07b11e9bf6c06d6-009-4c7a3059
    Training Job Status:  Completed
    Training Start Time:  2019-10-17T01:18:35Z
    Tuned Hyper Parameters:
      Name:                                    num_round
      Value:                                   18
  Hyper Parameter Tuning Job Status:           Completed
  Last Check Time:                             2019-10-17T01:21:01Z
  Sage Maker Hyper Parameter Tuning Job Name:  xgboostha92f5e3cf07b11e9bf6c06d6
  Training Job Status Counters:
    Completed:            10
    In Progress:          0
    Non Retryable Error:  0
    Retryable Error:      0
    Stopped:              0
    Total Error:          0
Events:                   <none>
```

### View logs from

HyperparameterTuningJobs

Hyperparameter tuning jobs do not have logs, but all training jobs launched by them do
have logs. These logs can be accessed as if they were a normal training job. For more
information, see [View logs from TrainingJobs](#view-logs-from-training-jobs "#view-logs-from-training-jobs").

### Delete a HyperparameterTuningJob

Use the following command to stop a hyperparameter job in SageMaker AI.

```
kubectl delete hyperparametertuningjob xgboost-mnist-hpo
```

This command removes the hyperparameter tuning job and associated training jobs from
your Kubernetes cluster and stops them in SageMaker AI. Jobs that have stopped or completed do not
incur any charges for SageMaker AI resources. SageMaker AI does not delete hyperparameter tuning jobs.
Stopped jobs continue to show on the SageMaker AI console.

Your output should look like the following:

```
hyperparametertuningjob.sagemaker.aws.amazon.com "xgboost-mnist-hpo" deleted
```

**Note**: The delete command takes about 2 minutes to
clean up the resources from SageMaker AI.

## The BatchTransformJob operator

Batch transform job operators reconcile your specified batch transform job spec to SageMaker AI by
launching it in SageMaker AI. You can learn more about SageMaker AI batch transform job in the SageMaker AI [CreateTransformJob API documentation](API_CreateTransformJob.md "API_CreateTransformJob.md").

###### Topics

- [Create a
  BatchTransformJob using a YAML File](#create-a-batchtransformjob-using-a-simple-yaml-file "#create-a-batchtransformjob-using-a-simple-yaml-file")
- [Create a BatchTransformJob
  using a Helm Chart](#create-a-batchtransformjob-using-a-helm-chart "#create-a-batchtransformjob-using-a-helm-chart")
- [List BatchTransformJobs](#list-batch-transform-jobs "#list-batch-transform-jobs")
- [Describe a BatchTransformJob](#describe-a-batch-transform-job "#describe-a-batch-transform-job")
- [View logs from
  BatchTransformJobs](#view-logs-from-batch-transform-jobs "#view-logs-from-batch-transform-jobs")
- [Delete a BatchTransformJob](#delete-a-batch-transform-job "#delete-a-batch-transform-job")

### Create a

BatchTransformJob using a YAML File

1. Download the sample YAML file for the batch transform job using the following command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/xgboost-mnist-batchtransform.yaml
```

2. Edit the file `xgboost-mnist-batchtransform.yaml` to change necessary
   parameters to replace the `inputdataconfig` with your input data and
   `s3OutputPath` with your Amazon S3 buckets that the SageMaker AI execution role has
   write access to.
3. Apply the YAML file using the following command:

```
kubectl apply -f xgboost-mnist-batchtransform.yaml
```

### Create a BatchTransformJob

using a Helm Chart

You can use Helm Charts to run batch transform jobs.

#### Get the Helm installer directory

Clone the GitHub repository to get the source using the following command:

```
git clone https://github.com/aws/amazon-sagemaker-operator-for-k8s.git
```

#### Configure the Helm Chart

Navigate to the
`amazon-sagemaker-operator-for-k8s/hack/charts/batch-transform-jobs/` folder.

Edit the `values.yaml` file to replace the `inputdataconfig`
with your input data and outputPath with your S3 buckets to which the SageMaker AI execution role
has write access.

#### Create a BatchTransformJob

1. Use the following command to create a batch transform job:

```
helm install . --generate-name
```

Your output should look like the following:

```
NAME: chart-1574292948
LAST DEPLOYED: Wed Nov 20 23:35:49 2019
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thanks for installing the sagemaker-k8s-batch-transform-job.
```

2. To verify that the Helm Chart was created successfully, run the following command:

```
helm ls
NAME                    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                           APP VERSION
chart-1474292948        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-batchtransformjob-0.1.0
chart-1474292948        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-hyperparametertuningjob-0.1.0
chart-1574292948        default         1               2019-11-20 23:35:49.9136092 +0000 UTC   deployed        sagemaker-k8s-trainingjob-0.1.0
rolebased-1574291698    default         1               2019-11-20 23:14:59.6777082 +0000 UTC   deployed        sagemaker-k8s-operator-0.1.0
```

This command creates a `BatchTransformJob` Kubernetes resource. The
operator launches the actual transform job in SageMaker AI and updates the
`BatchTransformJob` Kubernetes resource to reflect the status of the job
in SageMaker AI. You incur charges for SageMaker AI resources used during the duration of your job.
You do not incur any charges once your job completes or stops.

**Note**: SageMaker AI does not allow you to update a running
batch transform job. You cannot edit any parameter and re-apply the config file. You must
either change the metadata name or delete the existing job and create a new one. Similar
to existing training job operators like `TFJob` in Kubeflow,
`update` is not supported.

### List BatchTransformJobs

Use the following command to list all jobs created using the Kubernetes operator:

```
kubectl get batchtransformjob
```

Your output should look like the following:

```
NAME                                STATUS      CREATION-TIME          SAGEMAKER-JOB-NAME
xgboost-mnist-batch-transform       Completed   2019-11-18T03:44:00Z   xgboost-mnist-a88fb19809b511eaac440aa8axgboost
```

A batch transform job continues to be listed after the job has completed or failed. You
can remove a `hyperparametertuningjob` from the list by following the
[Delete a BatchTransformJob](#delete-a-batch-transform-job "#delete-a-batch-transform-job") steps. Jobs that
have completed or stopped do not incur any charges for SageMaker AI resources.

#### Batch transform status values

The `STATUS` field can be one of the following values:

- `Completed`
- `InProgress`
- `Failed`
- `Stopped`
- `Stopping`

These statuses come directly from the SageMaker AI official [API documentation](API_DescribeHyperParameterTuningJob.md#SageMaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus "API_DescribeHyperParameterTuningJob.md#SageMaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus").

In addition to the official SageMaker AI status, it is possible for `STATUS` to be
`SynchronizingK8sJobWithSageMaker`. This means that the operator has not yet
processed the job.

### Describe a BatchTransformJob

You can obtain debugging details using the `describe`
`kubectl` command.

```
kubectl describe batchtransformjob xgboost-mnist-batch-transform
```

Your output should look like the following:

```
Name:         xgboost-mnist-batch-transform
Namespace:    default
Labels:       <none>
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"sagemaker.aws.amazon.com/v1","kind":"BatchTransformJob","metadata":{"annotations":{},"name":"xgboost-mnist","namespace"...
API Version:  sagemaker.aws.amazon.com/v1
Kind:         BatchTransformJob
Metadata:
  Creation Timestamp:  2019-11-18T03:44:00Z
  Finalizers:
    sagemaker-operator-finalizer
  Generation:        2
  Resource Version:  21990924
  Self Link:         /apis/sagemaker.aws.amazon.com/v1/namespaces/default/batchtransformjobs/xgboost-mnist
  UID:               a88fb198-09b5-11ea-ac44-0aa8a9UIDNUM
Spec:
  Model Name:  TrainingJob-20190814SMJOb-IKEB
  Region:      us-east-1
  Transform Input:
    Content Type:  text/csv
    Data Source:
      S 3 Data Source:
        S 3 Data Type:  S3Prefix
        S 3 Uri:        s3://amzn-s3-demo-bucket/mnist_kmeans_example/input
  Transform Job Name:   xgboost-mnist-a88fb19809b511eaac440aa8a9SMJOB
  Transform Output:
    S 3 Output Path:  s3://amzn-s3-demo-bucket/mnist_kmeans_example/output
  Transform Resources:
    Instance Count:  1
    Instance Type:   ml.m4.xlarge
Status:
  Last Check Time:                2019-11-19T22:50:40Z
  Sage Maker Transform Job Name:  xgboost-mnist-a88fb19809b511eaac440aaSMJOB
  Transform Job Status:           Completed
Events:                           <none>
```

### View logs from

BatchTransformJobs

Use the following command to see the logs from the `xgboost-mnist` batch
transform job:

```
kubectl smlogs batchtransformjob xgboost-mnist-batch-transform
```

### Delete a BatchTransformJob

Use the following command to stop a batch transform job in SageMaker AI.

```
kubectl delete batchTransformJob xgboost-mnist-batch-transform
```

Your output should look like the following:

```
batchtransformjob.sagemaker.aws.amazon.com "xgboost-mnist" deleted
```

This command removes the batch transform job from your Kubernetes cluster, as well as
stops them in SageMaker AI. Jobs that have stopped or completed do not incur any charges for SageMaker AI
resources. Delete takes about 2 minutes to clean up the resources from SageMaker AI.

**Note**: SageMaker AI does not delete batch transform jobs.
Stopped jobs continue to show on the SageMaker AI console.

## The HostingDeployment operator

HostingDeployment operators support creating and deleting an endpoint, as well as updating an
existing endpoint, for real-time inference. The hosting deployment operator reconciles your specified hosting
deployment job spec to SageMaker AI by creating models, endpoint-configs and endpoints in SageMaker AI. You
can learn more about SageMaker AI inference in the SageMaker AI [CreateEndpoint
API documentation](API_CreateEndpoint.md "API_CreateEndpoint.md").

###### Topics

- [Configure a HostingDeployment
  resource](#configure-a-hostingdeployment-resource "#configure-a-hostingdeployment-resource")
- [Create a HostingDeployment](#create-a-hostingdeployment "#create-a-hostingdeployment")
- [List HostingDeployments](#list-hostingdeployments "#list-hostingdeployments")
- [Describe a HostingDeployment](#describe-a-hostingdeployment "#describe-a-hostingdeployment")
- [Invoking the endpoint](#invoking-the-endpoint "#invoking-the-endpoint")
- [Update HostingDeployment](#update-hostingdeployment "#update-hostingdeployment")
- [Delete the HostingDeployment](#delete-the-hostingdeployment "#delete-the-hostingdeployment")

### Configure a HostingDeployment

resource

Download the sample YAML file for the hosting deployment job using the following
command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/xgboost-mnist-hostingdeployment.yaml
```

The `xgboost-mnist-hostingdeployment.yaml` file has the following components
that can be edited as required:

- _ProductionVariants_. A production variant is a set
  of instances serving a single model. SageMaker AI load-balances between all production variants
  according to set weights.
- _Models_. A model is the containers and execution
  role ARN necessary to serve a model. It requires at least a single container.
- _Containers_. A container specifies the dataset and
  serving image. If you are using your own custom algorithm instead of an algorithm
  provided by SageMaker AI, the inference code must meet SageMaker AI requirements. For more information,
  see [Using Your Own Algorithms with SageMaker AI](your-algorithms.md "your-algorithms.md").

### Create a HostingDeployment

To create a HostingDeployment, use `kubectl` to apply the file
`hosting.yaml` with the following command:

```
kubectl apply -f hosting.yaml
```

SageMaker AI creates an endpoint with the specified configuration. You incur charges for SageMaker AI
resources used during the lifetime of your endpoint. You do not incur any charges once your
endpoint is deleted.

The creation process takes approximately 10 minutes.

### List HostingDeployments

To verify that the HostingDeployment was created, use the following command:

```
kubectl get hostingdeployments
```

Your output should look like the following:

```
NAME           STATUS     SAGEMAKER-ENDPOINT-NAME
host-xgboost   Creating   host-xgboost-def0e83e0d5f11eaaa450aSMLOGS
```

#### HostingDeployment status values

The status field can be one of several values:

- `SynchronizingK8sJobWithSageMaker`: The operator is preparing to create
  the endpoint.
- `ReconcilingEndpoint`: The operator is creating, updating, or deleting
  endpoint resources. If the HostingDeployment remains in this state, use `kubectl
describe` to see the reason in the `Additional` field.
- `OutOfService`: The endpoint is not available to take incoming
  requests.
- `Creating`: [CreateEndpoint](API_CreateEndpoint.md "API_CreateEndpoint.md") is running.
- `Updating`: [UpdateEndpoint](API_UpdateEndpoint.md "API_UpdateEndpoint.md") or [UpdateEndpointWeightsAndCapacities](API_UpdateEndpointWeightsAndCapacities.md "API_UpdateEndpointWeightsAndCapacities.md") is running.
- `SystemUpdating`: The endpoint is undergoing maintenance and cannot be
  updated or deleted or re-scaled until it has completed. This maintenance operation
  does not change any customer-specified values such as VPC config, AWS KMS encryption,
  model, instance type, or instance count.
- `RollingBack`: The endpoint fails to scale up or down or change its
  variant weight and is in the process of rolling back to its previous configuration.
  Once the rollback completes, the endpoint returns to an `InService` status.
  This transitional status only applies to an endpoint that has autoscaling turned on
  and is undergoing variant weight or capacity changes as part of an [UpdateEndpointWeightsAndCapacities](API_UpdateEndpointWeightsAndCapacities.md "API_UpdateEndpointWeightsAndCapacities.md") call or when the [UpdateEndpointWeightsAndCapacities](API_UpdateEndpointWeightsAndCapacities.md "API_UpdateEndpointWeightsAndCapacities.md") operation is called explicitly.
- `InService`: The endpoint is available to process incoming requests.
- `Deleting`: [DeleteEndpoint](API_DeleteEndpoint.md "API_DeleteEndpoint.md") is running.
- `Failed`: The endpoint could not be created, updated, or re-scaled. Use
  [DescribeEndpoint:FailureReason](API_DescribeEndpoint.md#SageMaker-DescribeEndpoint-response-FailureReason "API_DescribeEndpoint.md#SageMaker-DescribeEndpoint-response-FailureReason") for information about the failure. [DeleteEndpoint](API_DeleteEndpoint.md "API_DeleteEndpoint.md") is the only operation that can be performed on a failed
  endpoint.

### Describe a HostingDeployment

You can obtain debugging details using the `describe`
`kubectl` command.

```
kubectl describe hostingdeployment
```

Your output should look like the following:

```
Name:         host-xgboost
Namespace:    default
Labels:       <none>
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"sagemaker.aws.amazon.com/v1","kind":"HostingDeployment","metadata":{"annotations":{},"name":"host-xgboost","namespace":"def..."
API Version:  sagemaker.aws.amazon.com/v1
Kind:         HostingDeployment
Metadata:
  Creation Timestamp:  2019-11-22T19:40:00Z
  Finalizers:
    sagemaker-operator-finalizer
  Generation:        1
  Resource Version:  4258134
  Self Link:         /apis/sagemaker.aws.amazon.com/v1/namespaces/default/hostingdeployments/host-xgboost
  UID:               def0e83e-0d5f-11ea-aa45-0a3507uiduid
Spec:
  Containers:
    Container Hostname:  xgboost
    Image:               123456789012.dkr.ecr.us-east-2.amazonaws.com/xgboost:latest
    Model Data URL:      s3://amzn-s3-demo-bucket/inference/xgboost-mnist/model.tar.gz
  Models:
    Containers:
      xgboost
    Execution Role Arn:  arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole
    Name:                xgboost-model
    Primary Container:   xgboost
  Production Variants:
    Initial Instance Count:  1
    Instance Type:           ml.c5.large
    Model Name:              xgboost-model
    Variant Name:            all-traffic
  Region:                    us-east-2
Status:
  Creation Time:         2019-11-22T19:40:04Z
  Endpoint Arn:          arn:aws:sagemaker:us-east-2:123456789012:endpoint/host-xgboost-def0e83e0d5f11eaaaexample
  Endpoint Config Name:  host-xgboost-1-def0e83e0d5f11e-e08f6c510d5f11eaaa450aexample
  Endpoint Name:         host-xgboost-def0e83e0d5f11eaaa450a350733ba06
  Endpoint Status:       Creating
  Endpoint URL:          https://runtime.sagemaker.us-east-2.amazonaws.com/endpoints/host-xgboost-def0e83e0d5f11eaaaexample/invocations
  Last Check Time:       2019-11-22T19:43:57Z
  Last Modified Time:    2019-11-22T19:40:04Z
  Model Names:
    Name:   xgboost-model
    Value:  xgboost-model-1-def0e83e0d5f11-df5cc9fd0d5f11eaaa450aexample
Events:     <none>
```

The status field provides more information using the following fields:

- `Additional`: Additional information about the status of the hosting
  deployment. This field is optional and only gets populated in case of error.
- `Creation Time`: When the endpoint was created in SageMaker AI.
- `Endpoint ARN`: The SageMaker AI endpoint ARN.
- `Endpoint Config Name`: The SageMaker AI name of the endpoint configuration.
- `Endpoint Name`: The SageMaker AI name of the endpoint.
- `Endpoint Status`: The status of the endpoint.
- `Endpoint URL`: The HTTPS URL that can be used to access the endpoint.
  For more information, see [Deploy
  a Model on SageMaker AI Hosting Services](deploy-model.md "deploy-model.md").
- `FailureReason`: If a create, update, or delete command fails, the cause
  is shown here.
- `Last Check Time`: The last time the operator checked the status of the
  endpoint.
- `Last Modified Time`: The last time the endpoint was modified.
- `Model Names`: A key-value pair of HostingDeployment model names to SageMaker AI
  model names.

### Invoking the endpoint

Once the endpoint status is `InService`, you can invoke the endpoint in two
ways: using the AWS CLI, which does authentication and URL request signing, or using an HTTP
client like cURL. If you use your own client, you need to do AWS v4 URL signing and
authentication on your own.

To invoke the endpoint using the AWS CLI, run the following command. Make sure to
replace the Region and endpoint name with your endpoint's Region and SageMaker AI endpoint name.
This information can be obtained from the output of `kubectl describe`.

```
# Invoke the endpoint with mock input data.
aws sagemaker-runtime invoke-endpoint \
  --region us-east-2 \
  --endpoint-name `<endpoint name>` \
  --body $(seq 784 | xargs echo | sed 's/ /,/g') \
  >(cat) \
  --content-type text/csv > /dev/null
```

For example, if your Region is `us-east-2` and your endpoint config name is
`host-xgboost-f56b6b280d7511ea824b129926example`, then the following command
would invoke the endpoint:

```
aws sagemaker-runtime invoke-endpoint \
  --region us-east-2 \
  --endpoint-name host-xgboost-f56b6b280d7511ea824b1299example \
  --body $(seq 784 | xargs echo | sed 's/ /,/g') \
  >(cat) \
  --content-type text/csv > /dev/null
4.95847082138
```

Here, `4.95847082138` is the prediction from the model for the mock data.

### Update HostingDeployment

1. Once a HostingDeployment has a status of `InService`, it can be updated.
   It might take about 10 minutes for HostingDeployment to be in service. To verify that
   the status is `InService`, use the following command:

```
kubectl get hostingdeployments
```

2. The HostingDeployment can be updated before the status is `InService`.
   The operator waits until the SageMaker AI endpoint is `InService` before applying the
   update.

To apply an update, modify the `hosting.yaml` file. For example, change
the `initialInstanceCount` field from 1 to 2 as follows:

```
apiVersion: sagemaker.aws.amazon.com/v1
kind: HostingDeployment
metadata:
  name: host-xgboost
spec:
    region: us-east-2
    productionVariants:
        - variantName: all-traffic
          modelName: xgboost-model
          initialInstanceCount: 2
          instanceType: ml.c5.large
    models:
        - name: xgboost-model
          executionRoleArn: arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole
          primaryContainer: xgboost
          containers:
            - xgboost
    containers:
        - containerHostname: xgboost
          modelDataUrl: s3://amzn-s3-demo-bucket/inference/xgboost-mnist/model.tar.gz
          image: 123456789012.dkr.ecr.us-east-2.amazonaws.com/xgboost:latest
```

3. Save the file, then use `kubectl` to apply your update as follows. You
   should see the status change from `InService` to
   `ReconcilingEndpoint`, then `Updating`.

```
$ kubectl apply -f hosting.yaml
hostingdeployment.sagemaker.aws.amazon.com/host-xgboost configured

$ kubectl get hostingdeployments
NAME           STATUS                SAGEMAKER-ENDPOINT-NAME
host-xgboost   ReconcilingEndpoint   host-xgboost-def0e83e0d5f11eaaa450a350abcdef

$ kubectl get hostingdeployments
NAME           STATUS     SAGEMAKER-ENDPOINT-NAME
host-xgboost   Updating   host-xgboost-def0e83e0d5f11eaaa450a3507abcdef
```

SageMaker AI deploys a new set of instances with your models, switches traffic to use the new
instances, and drains the old instances. As soon as this process begins, the status becomes
`Updating`. After the update is complete, your endpoint becomes
`InService`. This process takes approximately 10 minutes.

### Delete the HostingDeployment

1. Use `kubectl` to delete a HostingDeployment with the following command:

```
kubectl delete hostingdeployments host-xgboost
```

Your output should look like the following:

```
hostingdeployment.sagemaker.aws.amazon.com "host-xgboost" deleted
```

2. To verify that the hosting deployment has been deleted, use the following command:

```
kubectl get hostingdeployments
No resources found.
```

Endpoints that have been deleted do not incur any charges for SageMaker AI resources.

## The ProcessingJob operator

ProcessingJob operators are used to launch Amazon SageMaker processing jobs. For more
information on SageMaker Processing jobs, see
[CreateProcessingJob](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md").

###### Topics

- [Create a ProcessingJob using a YAML
  file](#kubernetes-processing-job-yaml "#kubernetes-processing-job-yaml")
- [List ProcessingJobs](#kubernetes-processing-job-list "#kubernetes-processing-job-list")
- [Describe a ProcessingJob](#kubernetes-processing-job-description "#kubernetes-processing-job-description")
- [Delete a ProcessingJob](#kubernetes-processing-job-delete "#kubernetes-processing-job-delete")

### Create a ProcessingJob using a YAML

file

Follow these steps to create an Amazon SageMaker processing job by using a YAML file:

1. Download the `kmeans_preprocessing.py` pre-processing script.

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/kmeans_preprocessing.py
```

2. In one of your Amazon Simple Storage Service (Amazon S3) buckets, create a
   `mnist_kmeans_example/processing_code` folder and upload the script
   to the folder.
3. Download the `kmeans-mnist-processingjob.yaml` file.

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/kmeans-mnist-processingjob.yaml
```

4. Edit the YAML file to specify your `sagemaker-execution-role` and replace all
   instances of `amzn-s3-demo-bucket` with your S3 bucket.

```
...
metadata:
  name: kmeans-mnist-processing
...
  roleArn: arn:aws:iam::`<acct-id>`:role/service-role/`<sagemaker-execution-role>`
  ...
  processingOutputConfig:
    outputs:
      ...
          s3Output:
            s3Uri: s3://`<amzn-s3-demo-bucket>`/mnist_kmeans_example/output/
  ...
  processingInputs:
    ...
        s3Input:
          s3Uri: s3://`<amzn-s3-demo-bucket>`/mnist_kmeans_example/processing_code/kmeans_preprocessing.py

```

The `sagemaker-execution-role` must have permissions so that SageMaker AI can access your
S3 bucket, Amazon CloudWatch, and other services on your behalf. For more information on creating an
execution role, see [SageMaker AI
Roles](sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms "sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms"). 5. Apply the YAML file using one of the following commands.

For cluster-scoped installation:

```
kubectl apply -f kmeans-mnist-processingjob.yaml
```

For namespace-scoped installation:

```
kubectl apply -f kmeans-mnist-processingjob.yaml -n `<NAMESPACE>`
```

### List ProcessingJobs

Use one of the following commands to list all the jobs created using the ProcessingJob operator.
`SAGEMAKER-JOB-NAME` comes from the `metadata` section of the YAML
file.

For cluster-scoped installation:

```
kubectl get ProcessingJob kmeans-mnist-processing
```

For namespace-scoped installation:

```
kubectl get ProcessingJob -n `<NAMESPACE>` kmeans-mnist-processing
```

Your output should look similar to the following:

```
NAME                    STATUS     CREATION-TIME        SAGEMAKER-JOB-NAME
kmeans-mnist-processing InProgress 2020-09-22T21:13:25Z kmeans-mnist-processing-7410ed52fd1811eab19a165ae9f9e385
```

The output lists all jobs regardless of their status. To remove a job from the list, see
[Delete
a Processing Job](kubernetes-processing-job-operator.md#kubernetes-processing-job-delete "kubernetes-processing-job-operator.md#kubernetes-processing-job-delete").

###### ProcessingJob Status

- `SynchronizingK8sJobWithSageMaker` – The job is
  first submitted to the cluster. The operator has received the request
  and is preparing to create the processing job.
- `Reconciling` – The operator is initializing or recovering from transient
  errors, along with others. If the processing job remains in this state, use the
  `kubectl`
  `describe` command to see the reason in the `Additional` field.
- `InProgress | Completed | Failed | Stopping | Stopped`
  – Status of the SageMaker Processing job. For more information, see
  [DescribeProcessingJob](../APIReference/API_DescribeProcessingJob.md#sagemaker-DescribeProcessingJob-response-ProcessingJobStatus "../APIReference/API_DescribeProcessingJob.md#sagemaker-DescribeProcessingJob-response-ProcessingJobStatus").
- `Error` – The operator cannot recover by reconciling.

Jobs that have completed, stopped, or failed do not incur further charges for SageMaker AI
resources.

### Describe a ProcessingJob

Use one of the following commands to get more details about a processing job. These commands are
typically used for debugging a problem or checking the parameters of a processing job.

For cluster-scoped installation:

```
kubectl describe processingjob kmeans-mnist-processing
```

For namespace-scoped installation:

```
kubectl describe processingjob kmeans-mnist-processing -n `<NAMESPACE>`
```

The output for your processing job should look similar to the following.

```
$ kubectl describe ProcessingJob kmeans-mnist-processing
Name:         kmeans-mnist-processing
Namespace:    default
Labels:       <none>
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"sagemaker.aws.amazon.com/v1","kind":"ProcessingJob","metadata":{"annotations":{},"name":"kmeans-mnist-processing",...
API Version:  sagemaker.aws.amazon.com/v1
Kind:         ProcessingJob
Metadata:
  Creation Timestamp:  2020-09-22T21:13:25Z
  Finalizers:
    sagemaker-operator-finalizer
  Generation:        2
  Resource Version:  21746658
  Self Link:         /apis/sagemaker.aws.amazon.com/v1/namespaces/default/processingjobs/kmeans-mnist-processing
  UID:               7410ed52-fd18-11ea-b19a-165ae9f9e385
Spec:
  App Specification:
    Container Entrypoint:
      python
      /opt/ml/processing/code/kmeans_preprocessing.py
    Image Uri:  763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:1.5.0-cpu-py36-ubuntu16.04
  Environment:
    Name:   MYVAR
    Value:  my_value
    Name:   MYVAR2
    Value:  my_value2
  Network Config:
  Processing Inputs:
    Input Name:  mnist_tar
    s3Input:
      Local Path:   /opt/ml/processing/input
      s3DataType:   S3Prefix
      s3InputMode:  File
      s3Uri:        s3://<s3bucket>-us-west-2/algorithms/kmeans/mnist/mnist.pkl.gz
    Input Name:     source_code
    s3Input:
      Local Path:   /opt/ml/processing/code
      s3DataType:   S3Prefix
      s3InputMode:  File
      s3Uri:        s3://<s3bucket>/mnist_kmeans_example/processing_code/kmeans_preprocessing.py
  Processing Output Config:
    Outputs:
      Output Name:  train_data
      s3Output:
        Local Path:    /opt/ml/processing/output_train/
        s3UploadMode:  EndOfJob
        s3Uri:         s3://<s3bucket>/mnist_kmeans_example/output/
      Output Name:     test_data
      s3Output:
        Local Path:    /opt/ml/processing/output_test/
        s3UploadMode:  EndOfJob
        s3Uri:         s3://<s3bucket>/mnist_kmeans_example/output/
      Output Name:     valid_data
      s3Output:
        Local Path:    /opt/ml/processing/output_valid/
        s3UploadMode:  EndOfJob
        s3Uri:         s3://<s3bucket>/mnist_kmeans_example/output/
  Processing Resources:
    Cluster Config:
      Instance Count:     1
      Instance Type:      ml.m5.xlarge
      Volume Size In GB:  20
  Region:                 us-west-2
  Role Arn:               arn:aws:iam::<acct-id>:role/m-sagemaker-role
  Stopping Condition:
    Max Runtime In Seconds:  1800
  Tags:
    Key:    tagKey
    Value:  tagValue
Status:
  Cloud Watch Log URL:             https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=/aws/sagemaker/ProcessingJobs;prefix=kmeans-mnist-processing-7410ed52fd1811eab19a165ae9f9e385;streamFilter=typeLogStreamPrefix
  Last Check Time:                 2020-09-22T21:14:29Z
  Processing Job Status:           InProgress
  Sage Maker Processing Job Name:  kmeans-mnist-processing-7410ed52fd1811eab19a165ae9f9e385
Events:                            <none>
```

### Delete a ProcessingJob

When you delete a processing job, the SageMaker Processing job is removed from Kubernetes
but the job isn't deleted from SageMaker AI. If the job status in SageMaker AI is `InProgress`
the job is stopped. Processing jobs that are stopped do not incur any charges for SageMaker AI
resources. Use one of the following commands to delete a processing job.

For cluster-scoped installation:

```
kubectl delete processingjob kmeans-mnist-processing
```

For namespace-scoped installation:

```
kubectl delete processingjob kmeans-mnist-processing -n `<NAMESPACE>`
```

The output for your processing job should look similar to the following.

```
processingjob.sagemaker.aws.amazon.com "kmeans-mnist-processing" deleted
```

###### Note

SageMaker AI does not delete the processing job. Stopped jobs continue to show in the SageMaker AI console. The
`delete` command takes a few minutes to clean up the resources from SageMaker AI.

## HostingAutoscalingPolicy (HAP)

Operator

The HostingAutoscalingPolicy (HAP) operator takes a list of resource IDs as input and applies the
same policy to each of them. Each resource ID is a combination of an endpoint name and a variant name.
The HAP operator performs two steps: it registers the resource IDs and then applies the scaling policy
to each resource ID. `Delete` undoes both actions. You can apply the HAP to an existing SageMaker AI
endpoint or you can create a new SageMaker AI endpoint using the [HostingDeployment operator](hosting-deployment-operator.md#create-a-hostingdeployment "hosting-deployment-operator.md#create-a-hostingdeployment").
You can read more about SageMaker AI autoscaling in the [Application Autoscaling Policy documentation](endpoint-auto-scaling.md "endpoint-auto-scaling.md").

###### Note

In your `kubectl` commands, you can use the short form, `hap`, in place of
`hostingautoscalingpolicy`.

###### Topics

- [Create a HostingAutoscalingPolicy using a YAML
  file](#kubernetes-hap-job-yaml "#kubernetes-hap-job-yaml")
- [List HostingAutoscalingPolicies](#kubernetes-hap-list "#kubernetes-hap-list")
- [Describe a HostingAutoscalingPolicy](#kubernetes-hap-describe "#kubernetes-hap-describe")
- [Update a HostingAutoscalingPolicy](#kubernetes-hap-update "#kubernetes-hap-update")
- [Delete a HostingAutoscalingPolicy](#kubernetes-hap-delete "#kubernetes-hap-delete")
- [Update or delete an endpoint with a
  HostingAutoscalingPolicy](#kubernetes-hap-update-delete-endpoint "#kubernetes-hap-update-delete-endpoint")

### Create a HostingAutoscalingPolicy using a YAML

file

Use a YAML file to create a HostingAutoscalingPolicy (HAP) that applies a predefined or custom metric to one or multiple SageMaker AI endpoints.

Amazon SageMaker AI requires specific values in order to apply autoscaling to your variant. If these values
are not specified in the YAML spec, the HAP operator applies the following default values.

```
# Do not change
Namespace                    = "sagemaker"
# Do not change
ScalableDimension            = "sagemaker:variant:DesiredInstanceCount"
# Only one supported
PolicyType                   = "TargetTrackingScaling"
# This is the default policy name but can be changed to apply a custom policy
DefaultAutoscalingPolicyName = "SageMakerEndpointInvocationScalingPolicy"
```

Use the following samples to create a HAP that applies a predefined or custom metric to one or multiple endpoints.

#### Sample 1: Apply a predefined metric to a

single endpoint variant

1. Download the sample YAML file for a predefined metric using the following command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/hap-predefined-metric.yaml
```

2. Edit the YAML file to specify your `endpointName`, `variantName`,
   and `Region`.
3. Use one of the following commands to apply a predefined metric to a single resource ID (endpoint name and
   variant name combination).

For cluster-scoped installation:

```
kubectl apply -f hap-predefined-metric.yaml
```

For namespace-scoped installation:

```
kubectl apply -f hap-predefined-metric.yaml -n `<NAMESPACE>`
```

#### Sample 2: Apply a custom metric to a single

endpoint variant

1. Download the sample YAML file for a custom metric using the following command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/hap-custom-metric.yaml
```

2. Edit the YAML file to specify your `endpointName`, `variantName`,
   and `Region`.
3. Use one of the following commands to apply a custom metric to a single resource ID (endpoint name and
   variant name combination) in place of the recommended
   `SageMakerVariantInvocationsPerInstance`.

###### Note

Amazon SageMaker AI does not check the validity of your YAML spec.

For cluster-scoped installation:

```
kubectl apply -f hap-custom-metric.yaml
```

For namespace-scoped installation:

```
kubectl apply -f hap-custom-metric.yaml -n `<NAMESPACE>`
```

#### Sample 3: Apply a scaling policy to multiple

endpoints and variants

You can use the HAP operator to apply the same scaling policy to multiple resource IDs.
A separate `scaling_policy` request is created for each resource ID (endpoint name and variant name combination).

1. Download the sample YAML file for a predefined metric using the following command:

```
wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/samples/hap-predefined-metric.yaml
```

2. Edit the YAML file to specify your `Region` and multiple
   `endpointName` and `variantName` values.
3. Use one of the following commands to apply a predefined metric to multiple resource IDs (endpoint name and
   variant name combinations).

For cluster-scoped installation:

```
kubectl apply -f hap-predefined-metric.yaml
```

For namespace-scoped installation:

```
kubectl apply -f hap-predefined-metric.yaml -n `<NAMESPACE>`
```

#### Considerations for

HostingAutoscalingPolicies for multiple endpoints and variants

The following considerations apply when you use multiple resource IDs:

- If you apply a single policy across multiple resource IDs, one PolicyARN is created per
  resource ID. Five endpoints have five PolicyARNs. When you run the `describe` command
  on the policy, the responses show up as one job and include a single job status.
- If you apply a custom metric to multiple resource IDs, the same dimension or value is used for
  all the resource ID (variant) values. For example, if you apply a customer metric for instances
  1-5, and the endpoint variant dimension is mapped to variant 1, when variant 1 exceeds the
  metrics, all endpoints are scaled up or down.
- The HAP operator supports updating the list of resource IDs. If you modify, add, or delete
  resource IDs to the spec, the autoscaling policy is removed from the previous list of variants and
  applied to the newly specified resource ID combinations. Use the [`describe`](kubernetes-hap-operator.md#kubernetes-hap-describe "kubernetes-hap-operator.md#kubernetes-hap-describe") command to list the
  resource IDs to which the policy is currently applied.

### List HostingAutoscalingPolicies

Use one of the following commands to list all HostingAutoscalingPolicies (HAPs) created using the HAP operator.

For cluster-scoped installation:

```
kubectl get hap
```

For namespace-scoped installation:

```
kubectl get hap -n `<NAMESPACE>`
```

Your output should look similar to the following:

```
NAME             STATUS   CREATION-TIME
hap-predefined   Created  2021-07-13T21:32:21Z
```

Use the following command to check the status of your HostingAutoscalingPolicy (HAP).

```
kubectl get hap `<job-name>`
```

One of the following values is returned:

- `Reconciling` – Certain types of errors show the status as
  `Reconciling` instead of `Error`. Some examples are server-side errors and
  endpoints in the `Creating` or `Updating` state. Check the
  `Additional` field in status or operator logs for more details.
- `Created`
- `Error`

###### To view the autoscaling endpoint to which you applied the policy

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left side panel, expand **Inference**.
3. Choose **Endpoints**.
4. Select the name of the endpoint of interest.
5. Scroll to the **Endpoint runtime settings** section.

### Describe a HostingAutoscalingPolicy

Use the following command to get more details about a HostingAutoscalingPolicy (HAP).
These commands are typically used for debugging a problem or checking the resource IDs
(endpoint name and variant name combinations) of a HAP.

```
kubectl describe hap `<job-name>`
```

### Update a HostingAutoscalingPolicy

The HostingAutoscalingPolicy (HAP) operator supports updates. You can edit your YAML spec to
change the values and then reapply the policy. The HAP operator deletes the existing policy and
applies the new policy.

### Delete a HostingAutoscalingPolicy

Use one of the following commands to delete a HostingAutoscalingPolicy (HAP) policy.

For cluster-scoped installation:

```
kubectl delete hap hap-predefined
```

For namespace-scoped installation:

```
kubectl delete hap hap-predefined -n `<NAMESPACE>`
```

This command deletes the scaling policy and deregisters the scaling target from Kubernetes. This command returns the following output:

```
hostingautoscalingpolicies.sagemaker.aws.amazon.com "hap-predefined" deleted
```

### Update or delete an endpoint with a

HostingAutoscalingPolicy

To update an endpoint that has a HostingAutoscalingPolicy (HAP), use the `kubectl`
`delete` command to remove the HAP, update the endpoint, and then reapply the HAP.

To delete an endpoint that has a HAP, use the `kubectl`
`delete` command to remove the HAP before you delete the endpoint.
