# Amazon SageMaker Inference Recommender

Amazon SageMaker Inference Recommender is a capability of Amazon SageMaker AI. It reduces the time required to get machine
learning (ML) models in production by automating load testing and model tuning across SageMaker AI
ML instances. You can use Inference Recommender to deploy your model to a real-time or serverless inference
endpoint that delivers the best performance at the lowest cost. Inference Recommender helps you select the
best instance type and configuration for your ML models and workloads. It considers factors
like instance count, container parameters, model optimizations, max concurrency, and memory
size.

Amazon SageMaker Inference Recommender only charges you for the instances used while your jobs are executing.

## How it Works

To use Amazon SageMaker Inference Recommender, you can either [create a SageMaker AI model](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md")
or register a model to the SageMaker Model Registry with your model artifacts. Use the
AWS SDK for Python (Boto3) or the SageMaker AI console to run benchmarking jobs for different SageMaker AI endpoint
configurations. Inference Recommender jobs help you collect and visualize metrics across performance
and resource utilization to help you decide on which endpoint type and configuration to
choose.

## How to Get Started

If you are a first-time user of Amazon SageMaker Inference Recommender, we recommend that you do the
following:

1. Read through the [Prerequisites for using
   Amazon SageMaker Inference Recommender](inference-recommender-prerequisites.md "inference-recommender-prerequisites.md") section to make sure
   you have satisfied the requirements to use Amazon SageMaker Inference Recommender.
2. Read through the [Recommendation jobs with
   Amazon SageMaker Inference Recommender](inference-recommender-recommendation-jobs.md "inference-recommender-recommendation-jobs.md") section to
   launch your first Inference Recommender recommendation jobs.
3. Explore the introductory Amazon SageMaker Inference Recommender [Jupyter notebook](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-inference-recommender/inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-inference-recommender/inference-recommender.ipynb") example, or review the example notebooks in the
   following section.

## Example notebooks

The following example Jupyter notebooks can help you with the workflows for multiple use
cases in Inference Recommender:

- If you want an introductory notebook that benchmarks a TensorFlow model, see the
  [SageMaker Inference Recommender TensorFlow](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb") notebook.
- If you want to benchmark a HuggingFace model, see the [SageMaker Inference Recommender for HuggingFace](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/huggingface-inference-recommender/huggingface-inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/huggingface-inference-recommender/huggingface-inference-recommender.ipynb") notebook.
- If you want to benchmark an XGBoost model, see the [SageMaker Inference Recommender XGBoost](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/xgboost/xgboost-inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/xgboost/xgboost-inference-recommender.ipynb") notebook.
- If you want to review CloudWatch metrics for your Inference Recommender jobs, see the [SageMaker Inference Recommender CloudWatch metrics](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/tensorflow-cloudwatch/tf-cloudwatch-inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/tensorflow-cloudwatch/tf-cloudwatch-inference-recommender.ipynb") notebook.
