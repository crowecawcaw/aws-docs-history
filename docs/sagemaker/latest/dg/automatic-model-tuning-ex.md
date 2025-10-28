# Example: Hyperparameter Tuning Job

This
example shows how to create a new notebook for configuring and launching a hyperparameter
tuning job. The tuning job uses the [XGBoost algorithm with Amazon SageMaker AI](xgboost.md "xgboost.md") to train
a model to predict whether a customer will enroll for a term deposit at a bank after being
contacted by phone.

You use the low-level SDK for Python (Boto3) to configure and launch the hyperparameter tuning job, and
the AWS Management Console to monitor the status of hyperparameter tuning jobs. You can also use the
Amazon SageMaker AI high-level [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") to configure, run, monitor, and analyze
hyperparameter tuning jobs. For more information, see [https://github.com/aws/sagemaker-python-sdk](https://github.com/aws/sagemaker-python-sdk "https://github.com/aws/sagemaker-python-sdk").

## Prerequisites

To run the code in this example, you need

- [An AWS account and an administrator
  user](gs-set-up.md "gs-set-up.md")
- An Amazon S3 bucket for storing your training dataset and the model artifacts created
  during training
- [A running SageMaker AI notebook instance](gs-setup-working-env.md "gs-setup-working-env.md")

###### Topics

- [Create a Notebook Instance](automatic-model-tuning-ex-notebook.md "automatic-model-tuning-ex-notebook.md")
- [Get the Amazon SageMaker AI Boto 3 Client](automatic-model-tuning-ex-client.md "automatic-model-tuning-ex-client.md")
- [Get the SageMaker AI Execution Role](automatic-model-tuning-ex-role.md "automatic-model-tuning-ex-role.md")
- [Use an Amazon S3 bucket for input and
  output](automatic-model-tuning-ex-bucket.md "automatic-model-tuning-ex-bucket.md")
- [Download, Prepare, and Upload Training
  Data](automatic-model-tuning-ex-data.md "automatic-model-tuning-ex-data.md")
- [Configure and Launch a Hyperparameter
  Tuning Job](automatic-model-tuning-ex-tuning-job.md "automatic-model-tuning-ex-tuning-job.md")
- [Clean up](automatic-model-tuning-ex-cleanup.md "automatic-model-tuning-ex-cleanup.md")
