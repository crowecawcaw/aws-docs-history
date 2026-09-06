

# Debugger availability change
<a name="debugger-availability-change"></a>

**Note**  
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features.

## Replacing Amazon SageMaker Debugger
<a name="debugger-replacing"></a>

Follow this guide to transition to alternative services.

## Overview
<a name="debugger-migration-overview"></a>

Amazon SageMaker Debugger provided training observability, model debugging, and system profiling as a built-in SageMaker capability. These capabilities are now better served by a combination of Amazon SageMaker AI MLflow, TensorBoard on SageMaker, and Amazon CloudWatch for training observability, model debugging, and system performance monitoring. These tools provide flexible capabilities that adapt to your specific training workflow, whether you're fine-tuning foundation models, training custom architectures, or running distributed workloads.

## Capability mapping
<a name="debugger-capability-mapping"></a>


| Debugger capability | Replaced by | What it provides | 
| --- | --- | --- | 
| Training metric logging | MLflow / TensorBoard | Log, visualize, and compare metrics across training runs | 
| Model and parameter tracking | MLflow | Track hyperparameters, model versions, and artifacts with full reproducibility | 
| Gradient, activation, and weight analysis | TensorBoard | Histogram and distribution plugins for inspecting model internals across training steps | 
| System resource profiling (CPU, GPU, memory, disk) | Amazon CloudWatch | Real-time utilization metrics with configurable dashboards | 
| Automated training diagnostics | Amazon CloudWatch Alarms \+ MLflow | Monitor any logged metric such as loss convergence, gradient norms, resource utilization and alert on threshold breaches. MLflow run comparison identifies regressions across experiments | 

## Step 1: Removing Debugger configuration
<a name="debugger-step1-remove"></a>

### Remove DebuggerHookConfig from your estimator
<a name="debugger-remove-hook-config"></a>

If your training script or SageMaker estimator includes `DebuggerHookConfig`, Debugger-specific `TensorBoardOutputConfig`, or `rules` configurations, remove them. This disables automatic tensor capture and rule evaluation.

**Note**  
If you are using the SageMaker Python SDK v2 `Estimator` class, consider also transitioning to the newer [SageMaker Python SDK training APIs](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) or direct Boto3 `CreateTrainingJob` calls, as Estimators are a legacy construct.

### Delete Debugger output in Amazon S3
<a name="debugger-delete-s3-output"></a>

Debugger stored tensor data and profiling output in S3 under paths like:

```
s3://<bucket>/<training-job-name>/debug-output/
s3://<bucket>/<training-job-name>/profiler-output/
```

Delete these prefixes if you no longer need the historical data. Your training job logs and model artifacts in S3 remain unaffected.

### Delete custom Debugger rules (if used)
<a name="debugger-delete-custom-rules"></a>

If you defined custom rule containers:
+ Delete Amazon ECR images used for custom Debugger rule evaluation
+ Remove rule definition scripts or JSON configurations that are no longer needed

### Delete CloudWatch log groups (optional)
<a name="debugger-delete-cloudwatch-logs"></a>

Debugger created log groups under `/aws/sagemaker/TrainingJobs` for rule evaluation. Delete these if no longer needed to reduce log storage costs.

### Review IAM policies
<a name="debugger-review-iam"></a>

Remove IAM policies that granted access specifically for Debugger usage:
+ `s3:GetObject` / `s3:PutObject` scoped to Debugger output paths
+ `logs:PutLogEvents` for Debugger-specific log groups
+ Permissions for Debugger rule container execution

Retain any policies still needed for your training jobs, MLflow, or CloudWatch.

## Step 2: Configuring replacements
<a name="debugger-step2-configure"></a>

### Integrate MLflow for experiment tracking
<a name="debugger-integrate-mlflow"></a>

Amazon SageMaker AI offers a serverless MLflow capability that dynamically scales to support AI model development tasks at no additional cost. See the [launch blog](https://aws.amazon.com/blogs/aws/accelerate-ai-development-using-amazon-sagemaker-ai-with-serverless-mlflow/).

Use MLflow to:
+ Log hyperparameters, training metrics, and model artifacts
+ Compare runs side-by-side to identify regressions or improvements
+ Track model versions and lineage from experiment to production

**Get started:** [Machine learning experiments using Amazon SageMaker AI with MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments.html) – covers setup, creating a tracking server, and integrating with your training code.

### Use TensorBoard for model introspection
<a name="debugger-use-tensorboard"></a>

TensorBoard in Amazon SageMaker AI provides deep visibility into model internals during training:
+ Visualize gradient distributions and weight histograms across steps
+ Monitor activation patterns and layer behavior
+ Track scalar metrics, images, and custom visualizations

**When to use TensorBoard vs. MLflow:** MLflow tracks scalar metrics and supports basic visualization for run comparison. TensorBoard excels at multi-dimensional model introspection – gradient histograms, weight distributions, computational graphs, and embedding projections. Use both together: MLflow for experiment management, TensorBoard for deep debugging sessions.

**Get started:** [TensorBoard in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/tensorboard-on-sagemaker.html)

### Use Amazon CloudWatch for system monitoring and alerts
<a name="debugger-use-cloudwatch"></a>

Amazon CloudWatch captures resource utilization metrics for your training jobs and supports configurable alarms:
+ Monitor CPU, GPU, memory, and disk utilization in real time
+ Set alarms on any training metric to detect anomalies – loss plateaus, resource bottlenecks, or unexpected metric behavior
+ Build dashboards combining system metrics and training metrics for unified visibility

**Get started:** [Amazon CloudWatch Metrics for Monitoring and Analyzing Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html)

## What happens to your existing data
<a name="debugger-existing-data"></a>
+ **Training logs in S3:** Your training job output, model artifacts, and logs remain accessible. These are independent of Debugger.
+ **Debugger tensor data:** Historical tensor collections stored by Debugger remain in S3 at the paths listed above until you delete them. The [`smdebug` client library](https://github.com/awslabs/sagemaker-debugger) can still read this data for reference.
+ **CloudWatch metrics:** Historical training metrics already in CloudWatch are retained per your account's [log retention settings](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention).