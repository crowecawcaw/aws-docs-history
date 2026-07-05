# Batch transforms with inference pipelines

To get inferences on an entire dataset you run a batch transform on a trained model.
To run inferences on a full dataset, you can use the same inference pipeline model
created and deployed to an endpoint for real-time processing in a batch transform job.
To run a batch transform job in a pipeline, you download the input data from Amazon S3 and
send it in one or more HTTP requests to the inference pipeline model. For an example
that shows how to prepare data for a batch transform, see "Section 2 - Preprocess the raw housing data using Scikit Learn" of the [Amazon SageMaker Multi-Model Endpoints using Linear Learner sample
notebook](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/multi_model_linear_learner_home_value "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/multi_model_linear_learner_home_value"). For information about Amazon SageMaker AI batch transforms, see [Batch transform for inference with Amazon SageMaker AI](batch-transform.md "batch-transform.md").

###### Note

To use custom Docker images in a pipeline that includes [Amazon SageMaker AI built-in algorithms](sagemaker-algo-docker-registry-paths.md "sagemaker-algo-docker-registry-paths.md"), you need an [Amazon Elastic Container Registry
(ECR) policy](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md"). Your Amazon ECR repository must grant SageMaker AI permission to pull
the image. For more information, see [Troubleshoot Amazon ECR Permissions for Inference Pipelines](inference-pipeline-troubleshoot.md#inference-pipeline-troubleshoot-permissions "inference-pipeline-troubleshoot.md#inference-pipeline-troubleshoot-permissions").

The following example shows how to run a transform job using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
In this example, `model_name` is the inference pipeline that combines SparkML
and XGBoost models (created in previous examples). The Amazon S3 location specified by
`input_data_path` contains the input data, in CSV format, to be
downloaded and sent to the Spark ML model. After the transform job has finished, the
Amazon S3 location specified by `output_data_path` contains the output data
returned by the XGBoost model in CSV format.

```
from sagemaker.transform import TransformJob

input_data_path = 's3://{}/{}/{}'.format(default_bucket, 'key', 'file_name')
output_data_path = 's3://{}/{}'.format(default_bucket, 'key')
transform_job = TransformJob.create(
    model_name = model_name,
    transform_input = {
        'DataSource': {
            'S3DataSource': {
                'S3DataType': 'S3Prefix',
                'S3Uri': input_data_path
            }
        },
        'ContentType': CONTENT_TYPE_CSV,
        'SplitType': 'Line'
    },
    transform_output = {
        'S3OutputPath': output_data_path,
        'Accept': CONTENT_TYPE_CSV,
        'AssembleWith': 'Line'
    },
    transform_resources = {
        'InstanceType': 'ml.m4.xlarge',
        'InstanceCount': 1
    },
    transform_job_name = 'inference-pipelines-batch',
    batch_strategy = 'SingleRecord'
)
```
