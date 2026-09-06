

# Getting Started
<a name="model-customize-evaluation-getting-started"></a>

## Submit an Evaluation Job Through SageMaker Studio
<a name="model-customize-evaluation-studio"></a>

### Step 1: Navigate to Evaluation From Your Model Card
<a name="model-customize-evaluation-studio-step1"></a>

After you customize your model, navigate to the evaluation page from your model card.

For information on open-weight custom model training: [https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-job.html](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-job.html)

SageMaker visualizes your customized model on the My Models tab:

![Registered model card page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-registered-model-card.png)


Choose View latest version, then choose Evaluate:

![Model customization page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-evaluate-from-model-card.png)


### Step 2: Submit Your Evaluation Job
<a name="model-customize-evaluation-studio-step2"></a>

Choose the Submit button and submit your evaluation job. This submits a minimal MMLU benchmark job.

For information on the supported evaluation job types, see [Evaluation types and Job Submission](model-customize-evaluation-types.md).

![Evaluation job submission page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-benchmark-submission.png)


### Step 3: Track Your Evaluation Job Progress
<a name="model-customize-evaluation-studio-step3"></a>

Your evaluation job progress is tracked in the Evaluation steps tab:

![Your evaluation job progress.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-benchmark-tracking.png)


### Step 4: View Your Evaluation Job Results
<a name="model-customize-evaluation-studio-step4"></a>

Your evaluation job results are visualized in the Evaluation results tab:

![Your evaluation job metrics.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-benchmark-results.png)


### Step 5: View Your Completed Evaluations
<a name="model-customize-evaluation-studio-step5"></a>

Your completed evaluation job is displayed in Evaluations of your model card:

![Your completed evaluation jobs.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/getting-started-benchmark-completed-model-card.png)


## Submit Your Evaluation Job Through SageMaker Python SDK
<a name="model-customize-evaluation-sdk"></a>

### Step 1: Create Your BenchMarkEvaluator
<a name="model-customize-evaluation-sdk-step1"></a>

Pass your registered trained model, AWS S3 output location, and MLFlow resource ARN to `BenchMarkEvaluator` and then initialize it.

```
from sagemaker.train.evaluate import BenchMarkEvaluator, Benchmark  
  
evaluator = BenchMarkEvaluator(  
    benchmark=Benchmark.MMLU,  
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",  
    s3_output_path="s3://<bucket-name>/<prefix>/eval/",  
    mlflow_resource_arn="arn:aws:sagemaker:<region>:<account-id>:mlflow-tracking-server/<tracking-server-name>",  
    evaluate_base_model=False  
)
```

### Step 2: Submit Your Evaluation Job
<a name="model-customize-evaluation-sdk-step2"></a>

Call the `evaluate()` method to submit the evaluation job.

```
execution = evaluator.evaluate()
```

### Step 3: Track Your Evaluation Job Progress
<a name="model-customize-evaluation-sdk-step3"></a>

Call the `wait()` method of the execution to get a live update of the evaluation job progress.

```
execution.wait(target_status="Succeeded", poll=5, timeout=3600)
```

### Step 4: View Your Evaluation Job Results
<a name="model-customize-evaluation-sdk-step4"></a>

Call the `show_results()` method to display your evaluation job results.

```
execution.show_results()
```