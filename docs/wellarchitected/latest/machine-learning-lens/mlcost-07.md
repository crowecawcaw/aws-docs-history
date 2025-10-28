# MLCOST-07: Use managed data processing capabilities

With managed data processing, you can use a simplified, managed
experience to run your data processing workloads, such as
feature engineering, data validation, model evaluation, and
model interpretation. 

## Implementation plan

- **Use Amazon SageMaker AI Processing
  –** With Amazon SageMaker AI Processing, you can run
  processing jobs for data processing steps in your machine
  learning pipeline. Processing jobs accept data from Amazon S3 as input and store data into Amazon S3 as output. The
  processing container image can either be an Amazon SageMaker AI built-in image or a custom image that you
  provide. The underlying infrastructure for a Processing
  job is fully managed by Amazon SageMaker AI. Cluster
  resources are provisioned for the duration of your job,
  and cleaned up when a job completes. SageMaker AI Processing
  has simplified running machine learning preprocessing and
  postprocessing tasks with popular frameworks such as
  scikit-learn, Apache Spark, PyTorch, TensorFlow, Hugging
  Face, MXNet, and XGBoost.

## Documents

- [Process
  Data with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")

## Blogs

- [Amazon SageMaker AI Processing – Fully Managed Data Processing and
  Model Evaluation](https://aws.amazon.com/blogs/aws/amazon-sagemaker-processing-fully-managed-data-processing-and-model-evaluation/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-processing-fully-managed-data-processing-and-model-evaluation/")
- [Use
  deep learning frameworks natively in Amazon SageMaker AI
  Processing](https://aws.amazon.com/blogs/machine-learning/use-deep-learning-frameworks-natively-in-amazon-sagemaker-processing/ "https://aws.amazon.com/blogs/machine-learning/use-deep-learning-frameworks-natively-in-amazon-sagemaker-processing/")
- [Building
  machine learning workflows with Amazon SageMaker AI Processing jobs and AWS Step Functions](https://aws.amazon.com/blogs/machine-learning/building-machine-learning-workflows-with-amazon-sagemaker-processing-jobs-and-aws-step-functions/ "https://aws.amazon.com/blogs/machine-learning/building-machine-learning-workflows-with-amazon-sagemaker-processing-jobs-and-aws-step-functions/")
- [Process
  Amazon Redshift data and schedule a training pipeline with Amazon SageMaker AI Processing and Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/process-amazon-redshift-data-and-schedule-a-training-pipeline-with-amazon-sagemaker-processing-and-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/process-amazon-redshift-data-and-schedule-a-training-pipeline-with-amazon-sagemaker-processing-and-amazon-sagemaker-pipelines/")

## Examples

- [Amazon SageMaker AI Processing jobs](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html")
