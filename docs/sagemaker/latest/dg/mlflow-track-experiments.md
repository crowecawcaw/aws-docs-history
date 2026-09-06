

# Integrate MLflow with your environment
<a name="mlflow-track-experiments"></a>

The following page describes how to get started with the MLflow SDK and the AWS MLflow plugin within your development environment. This can include local IDEs or a Jupyter Notebook environment within Studio or Studio Classic.

Amazon SageMaker AI uses an MLflow plugin to customize the behavior of the MLflow Python client and integrate AWS tooling. The AWS MLflow plugin authenticates API calls made with MLflow using [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html). The AWS MLflow plugin allows you to connect to your MLflow tracking server using the tracking server ARN. For more information about plugins, see [AWS MLflow plugin](https://pypi.org/project/sagemaker-mlflow/) and [MLflow plugins](https://mlflow.org/docs/latest/plugins.html).

**Important**  
Your user IAM permissions within your development environment must have access to any relevant MLflow API actions to successfully run provided examples. For more information, see [Set up IAM permissions for MLflow](mlflow-create-tracking-server-iam.md).

For more information about using the MLflow SDK, see [Python API](https://mlflow.org/docs/2.13.2/python_api/index.html) in the MLflow documentation.

## Install MLflow and the AWS MLflow plugin
<a name="mlflow-track-experiments-install-plugin"></a>

Within your development environment, install both MLflow and the AWS MLflow plugin.

```
pip install sagemaker-mlflow
```

To ensure compatibility between your MLflow client and tracking server, use the corresponding MLflow version based on your tracking server version:
+ For tracking server 2.13.x, use `mlflow==2.13.2`
+ For tracking server 2.16.x, use `mlflow==2.16.2`
+ For tracking server 3.0.x, use `mlflow==3.0.0`

To see which versions of MLflow are available to use with SageMaker AI, see [Tracking server versions](mlflow.md#mlflow-create-tracking-server-versions).

## Connect to your MLflow Tracking Server
<a name="mlflow-track-experiments-tracking-server-connect"></a>

Use `[mlflow.set\_tracking\_uri](https://mlflow.org/docs/2.13.2/python_api/mlflow.html#mlflow.set_tracking_uri)` to connect to a your tracking server from your development environment using its ARN:

```
import mlflow

arn = {{"YOUR-TRACKING-SERVER-ARN"}}

mlflow.set_tracking_uri({{arn}})
```