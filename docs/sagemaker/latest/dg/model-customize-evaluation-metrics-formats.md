

# Evaluation Metrics Formats
<a name="model-customize-evaluation-metrics-formats"></a>

Evaluating the quality of your model across these metric formats:
+ Model Evaluation Summary
+ MLFlow
+ TensorBoard

## Model Evaluation Summary
<a name="model-customize-evaluation-metrics-summary"></a>

When you submit your evaluation job you specify an AWS S3 output location. SageMaker automatically uploads the evaluation summary .json file to the location. The benchmark summary S3 path is the following:

```
s3://<your-provide-s3-location>/<training-job-name>/output/output/<evaluation-job-name>/eval_results/
```

**Pass the AWS S3 location**

------
#### [ SageMaker Studio ]

![Pass into output artifact location (AWS S3 URI).](http://docs.aws.amazon.com/sagemaker/latest/dg/images/s3-output-path-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
evaluator = BenchMarkEvaluator(
    benchmark=Benchmark.MMLU,
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    s3_output_path="s3://<bucket-name>/<prefix>/eval/",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

------

Read it directly as a `.json` from the AWS S3 location or visualized automatically in the UI:

```
{
  "results": {
    "custom|gen_qa_gen_qa|0": {
      "rouge1": 0.9152812653966208,
      "rouge1_stderr": 0.003536439199232507,
      "rouge2": 0.774569918517409,
      "rouge2_stderr": 0.006368825746765958,
      "rougeL": 0.9111255645823356,
      "rougeL_stderr": 0.003603841524881021,
      "em": 0.6562150055991042,
      "em_stderr": 0.007948251702846893,
      "qem": 0.7522396416573348,
      "qem_stderr": 0.007224355240883467,
      "f1": 0.8428757602152095,
      "f1_stderr": 0.005186300690881584,
      "f1_score_quasi": 0.9156170336744968,
      "f1_score_quasi_stderr": 0.003667700152375464,
      "bleu": 100.00000000000004,
      "bleu_stderr": 1.464411857851008
    },
    "all": {
      "rouge1": 0.9152812653966208,
      "rouge1_stderr": 0.003536439199232507,
      "rouge2": 0.774569918517409,
      "rouge2_stderr": 0.006368825746765958,
      "rougeL": 0.9111255645823356,
      "rougeL_stderr": 0.003603841524881021,
      "em": 0.6562150055991042,
      "em_stderr": 0.007948251702846893,
      "qem": 0.7522396416573348,
      "qem_stderr": 0.007224355240883467,
      "f1": 0.8428757602152095,
      "f1_stderr": 0.005186300690881584,
      "f1_score_quasi": 0.9156170336744968,
      "f1_score_quasi_stderr": 0.003667700152375464,
      "bleu": 100.00000000000004,
      "bleu_stderr": 1.464411857851008
    }
  }
}
```

![Sample performance metrics for custom gen-qa benchmark visualized in SageMaker Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/gen-qa-metrics-visualization-sagemaker-studio.png)


## MLFlow logging
<a name="model-customize-evaluation-metrics-mlflow"></a>

**Provide your SageMaker MLFlow resource ARN**

SageMaker Studio uses the default MLFlow app that gets provisioned on each Studio domain when you use the model customization capability for the first time. SageMaker Studio uses the default MLflow app associated ARN in evaluation job submission.

You can also submit your evaluation job and explicitly provide an MLFlow Resource ARN to stream metrics to said associated tracking server/app for real time analysis.

**SageMaker Python SDK**

```
evaluator = BenchMarkEvaluator(
    benchmark=Benchmark.MMLU,
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    s3_output_path="s3://<bucket-name>/<prefix>/eval/",
    mlflow_resource_arn="arn:aws:sagemaker:<region>:<account-id>:mlflow-tracking-server/<tracking-server-name>",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

Model level and system level metric visualization:

![Sample model level error and accuracy for MMLU benchmarking task.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model-metrics-mlflow.png)


![Sample built-in metrics for LLMAJ benchmarking task.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/llmaj-metrics-mlflow.png)


![Sample system level metrics for MMLU benchmarking task.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/system-metrics-mlflow.png)


## TensorBoard
<a name="model-customize-evaluation-metrics-tensorboard"></a>

Submit your evaluation job with an AWS S3 output location. SageMaker automatically uploads a TensorBoard file to the location.

SageMaker uploads the TensorBoard file to AWS S3 in the following location:

```
s3://<your-provide-s3-location>/<training-job-name>/output/output/<evaluation-job-name>/tensorboard_results/eval/
```

**Pass the AWS S3 location as follows**

------
#### [ SageMaker Studio ]

![Pass into output artifact location (AWS S3 URI).](http://docs.aws.amazon.com/sagemaker/latest/dg/images/s3-output-path-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
evaluator = BenchMarkEvaluator(
    benchmark=Benchmark.MMLU,
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    s3_output_path="s3://<bucket-name>/<prefix>/eval/",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

------

**Sample model level metrics**

![SageMaker TensorBoard displaying results of a benchmarking job.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/metrics-in-tensorboard.png)
