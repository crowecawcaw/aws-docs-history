

# Track inference recommendation and benchmark results with MLflow
<a name="generative-ai-inference-recommendations-mlflow"></a>

You can track the results of your recommendation and benchmark jobs with fully managed MLflow on Amazon SageMaker AI. When you provide an MLflow configuration, SageMaker AI logs the performance metrics and artifacts that the job produces to an MLflow App. You can then use the MLflow UI to view individual runs, compare configurations across jobs, and share results with your team. For more information about MLflow on SageMaker AI, see [Accelerate generative AI development using managed MLflow on Amazon SageMaker AI](mlflow.md).

MLflow tracking is optional. To enable it, provide an MLflow configuration that references an MLflow App when you create the job.

## Prerequisites
<a name="generative-ai-inference-recommendations-mlflow-prereqs"></a>

Before you track results with MLflow, you need the following in addition to the [Prerequisites](generative-ai-inference-recommendations-get-started.md#generative-ai-inference-recommendations-get-started-prereqs) for a recommendation or benchmark job:
+ An MLflow App in an operational state, in the same AWS Region as your job. For information about creating an MLflow App, see [MLflow App Setup](mlflow-app-setup.md).
+ An IAM execution role (the `RoleArn` that you pass to the job) with permission to describe the MLflow App and call the MLflow REST APIs. Add the `sagemaker:DescribeMlflowApp` action and the `sagemaker-mlflow` actions that the job uses to log runs. For more information about MLflow permissions, see [MLflow App Setup](mlflow-app-setup.md).

## MLflow configuration parameters
<a name="generative-ai-inference-recommendations-mlflow-config"></a>

To track results, add an `MlflowConfig` object to the `OutputConfig` of your `CreateAIRecommendationJob` or `CreateAIBenchmarkJob` request. `MlflowConfig` contains the following fields:

`MlflowResourceArn`  
Required. The Amazon Resource Name (ARN) of the MLflow App to log results to, in the format `arn:aws:sagemaker:{{region}}:{{account-id}}:mlflow-app/{{app-id}}`.

`MlflowExperimentName`  
Optional. The name of the MLflow experiment to log the run under. If the experiment does not exist, SageMaker AI creates it; if it already exists, SageMaker AI reuses it, so you can group runs from multiple jobs under one experiment by passing the same name.

`MlflowRunName`  
Optional. The name of the top-level MLflow run that the job's results are nested under. To group the results of multiple jobs under one top-level run, pass the same `MlflowRunName` to each job.

Each job creates a top-level MLflow run, with nested child runs that break the results down by dimensions such as the benchmark target or instance type, the deployment configuration, and the concurrency level. This structure lets you drill into individual measurements and compare configurations in the MLflow UI.

The `MlflowConfig` that you supply on the create request is echoed back in the `OutputConfig` of the corresponding `Describe` response.

## Track a recommendation job
<a name="generative-ai-inference-recommendations-mlflow-recommendation"></a>

Add the `MlflowConfig` object to `OutputConfig` when you create a recommendation job.

**Python (boto3)**

```
response = client.create_ai_recommendation_job(
    AIRecommendationJobName="my-recommendation-job",
    ModelSource={
        "S3": {
            "S3Uri": "s3://DOC-EXAMPLE-BUCKET/models/my-model/",
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/recommendations/",
        "MlflowConfig": {
            "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:mlflow-app/app-EXAMPLE",
            "MlflowExperimentName": "my-recommendation-experiment",
            "MlflowRunName": "my-recommendation-job-run",
        },
    },
    PerformanceTarget={
        "Constraints": [
            {"Metric": "ttft-ms"}
        ]
    },
    AIWorkloadConfigIdentifier="my-recommendation-workload",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)
print(response["AIRecommendationJobArn"])
```

**AWS CLI**

```
aws sagemaker create-ai-recommendation-job \
  --ai-recommendation-job-name "my-recommendation-job" \
  --model-source '{"S3": {"S3Uri": "s3://DOC-EXAMPLE-BUCKET/models/my-model/"}}' \
  --output-config '{
    "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/recommendations/",
    "MlflowConfig": {
      "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:mlflow-app/app-EXAMPLE",
      "MlflowExperimentName": "my-recommendation-experiment",
      "MlflowRunName": "my-recommendation-job-run"
    }
  }' \
  --performance-target '{"Constraints": [{"Metric": "ttft-ms"}]}' \
  --ai-workload-config-identifier "my-recommendation-workload" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2
```

## Track a benchmark job
<a name="generative-ai-inference-recommendations-mlflow-benchmark"></a>

Add the `MlflowConfig` object to `OutputConfig` when you create a benchmark job.

**Python (boto3)**

```
response = client.create_ai_benchmark_job(
    AIBenchmarkJobName="my-benchmark-job",
    BenchmarkTarget={
        "Endpoint": {
            "Identifier": "my-sagemaker-endpoint"
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/",
        "MlflowConfig": {
            "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:mlflow-app/app-EXAMPLE",
            "MlflowExperimentName": "my-benchmark-experiment",
            "MlflowRunName": "my-benchmark-job-run",
        },
    },
    AIWorkloadConfigIdentifier="my-benchmark-config",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)
print(response["AIBenchmarkJobArn"])
```

**AWS CLI**

```
aws sagemaker create-ai-benchmark-job \
  --ai-benchmark-job-name "my-benchmark-job" \
  --benchmark-target '{"Endpoint": {"Identifier": "my-sagemaker-endpoint"}}' \
  --output-config '{
    "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/",
    "MlflowConfig": {
      "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:mlflow-app/app-EXAMPLE",
      "MlflowExperimentName": "my-benchmark-experiment",
      "MlflowRunName": "my-benchmark-job-run"
    }
  }' \
  --ai-workload-config-identifier "my-benchmark-config" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2
```

## View results in MLflow
<a name="generative-ai-inference-recommendations-mlflow-view"></a>

After the job reaches the `Completed` status, open the MLflow UI from the MLflow App to inspect the logged runs. For more information about launching the MLflow UI, see [Launch the MLflow UI using a presigned URL](mlflow-launch-ui.md).

On the **Experiments** page, select the experiment that you specified in `MlflowExperimentName`.

![The MLflow UI Experiments page showing a list of experiments with their names and creation times.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/inference-recommendations-mlflow-experiments.png)


The experiment's **Runs** view shows a top-level run that contains a per-job run, which expands into child runs for each instance type, deployment configuration, and concurrency level. Select a run to view its parameters, metrics, and artifacts.

![The MLflow UI Runs view showing a top-level run that expands into nested child runs for the per-job, instance type, image type, and concurrency levels.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/inference-recommendations-mlflow-runs.png)
