# MLPER-16: Establish an automated re-training framework

Monitor the data and the model predictions. Run analyses of
model performance against defined metrics to identify errors
due to data and concept drift. Automate model re-training to
mitigate these errors on fixed scheduled intervals, or when
model variance reaches a defined threshold. Automated model
retraining can also be started as enough new data becomes
available.

## Implementation plan

- **Identify retraining
  opportunities** - Monitor data statistics and
  ML inferences at production using Amazon SageMaker AI Model
  Monitor. If the data drifts beyond a defined threshold,
  then start retraining. Additionally, retraining can be
  initiated at defined scheduled intervals (to meet
  business requirements) or when additional training data
  is available. AWS supports mechanisms for automatically
  starting retraining based on a new data
  _PUT_ to an
  [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") bucket. Ensure model versioning is supported
  when incorporating additional data into your models.
  This enables re-creating an inadvertently deleted model
  artifact using the combined versions of components used
  to create the versioned artifact.
- **Use Amazon SageMaker AI
  Pipelines** - A retraining pipeline can be
  developed using
  [Amazon](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/")
  [SageMaker AI
  Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") that enables orchestration using step
  creation and management.
- **Use AWS Step Functions**- You can also use
  [AWS Step Functions Data Science SDK for Amazon](../../../step-functions/latest/dg/concepts-python-sdk.md "../../../step-functions/latest/dg/concepts-python-sdk.md")
  [SageMaker AI](../../../step-functions/latest/dg/concepts-python-sdk.md "../../../step-functions/latest/dg/concepts-python-sdk.md")
  to automate training of a machine learning model. Define
  all the steps in the workﬂow and set up alerts to start
  the ﬂow. To detect the presence of new training data in
  an S3 bucket,
  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
  combined with
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") Events allows you to start an AWS Step
  Function workflow to initiate retraining tasks in your
  training pipeline.
- **Use third-party tools**

* Use third-party deployment orchestration tools, such
  as
  [Jenkins](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/ "https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/"),
  that integrate with AWS service APIs to automate model
  retraining when new data is available.

## Documents

- [Amazon SageMaker AI Model Building Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [Retraining
  Models on New Data](../../../machine-learning/latest/dg/retraining-models-on-new-data.md "../../../machine-learning/latest/dg/retraining-models-on-new-data.md")
- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Train
  a Machine Learning Model (using AWS Step Functions)](../../../step-functions/latest/dg/sample-train-model.md "../../../step-functions/latest/dg/sample-train-model.md")
- [AWS Step Functions Data Science SDK for Python](../../../step-functions/latest/dg/concepts-python-sdk.md "../../../step-functions/latest/dg/concepts-python-sdk.md")

## Blogs

- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
- [Automating
  model retraining and deployment using the AWS Step Functions Data Science SDK for](https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/")
  [Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/")
- [Automating
  complex deep learning model training using Amazon SageMaker AI Debugger and AWS Step](https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/ "https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/")
  [Functions](https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/ "https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/")
- [Build
  a CI/CD pipeline for deploying custom machine learning
  models using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/ "https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/")
- [Create
  SageMaker AI Pipelines for training, consuming and
  monitoring your batch use cases](https://aws.amazon.com/blogs/machine-learning/create-sagemaker-pipelines-for-training-consuming-and-monitoring-your-batch-use-cases/ "https://aws.amazon.com/blogs/machine-learning/create-sagemaker-pipelines-for-training-consuming-and-monitoring-your-batch-use-cases/")

## Videos

- [How
  to create fully automated ML workﬂows with Amazon SageMaker AI Pipelines (29:23)](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/")
- [Machine
  Learning and Automated Model Retraining with
  SageMaker AI](https://www.youtube.com/watch?v=1kbWvlHBYLk "https://www.youtube.com/watch?v=1kbWvlHBYLk")

## Examples

- [Autopilot,
  Debugger and Model Monitor – Immersion Day](https://sagemaker-immersionday.workshop.aws/lab4.html "https://sagemaker-immersionday.workshop.aws/lab4.html")
- [Amazon SageMaker AI MLOps](https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml "https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml")
