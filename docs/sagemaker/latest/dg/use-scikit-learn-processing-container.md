# Run a Processing Job with scikit-learn

You can use Amazon SageMaker Processing to process data and evaluate models with scikit-learn scripts in a
Docker image provided by Amazon SageMaker AI. The following provides an example on how to run a
Amazon SageMaker Processing job using scikit-learn.

For a sample notebook that shows how to run scikit-learn scripts using a Docker image
provided and maintained by SageMaker AI to preprocess data and evaluate models, see [scikit-learn Processing](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation"). To use this notebook, you need to install the SageMaker AI
Python SDK for Processing.

This notebook runs a processing job using the SageMaker Python SDK to run a scikit-learn script that you provide. The script
preprocesses data, trains a model using a SageMaker training job, and then runs a processing
job to evaluate the trained model. The processing job estimates how the model is
expected to perform in production.

To learn more about using the SageMaker Python SDK with Processing containers, see the [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/"). For a complete list
of pre-built Docker images available for processing jobs, see
[Docker
Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md").

The following code example shows how to run a processing job using a scikit-learn
Docker image provided and maintained by SageMaker AI.

```
from sagemaker.core.resources import ProcessingJob

processing_job = ProcessingJob.create(
    processing_job_name="sklearn-processing",
    role_arn=role,
    app_specification={
        "image_uri": "sklearn-processing-image-uri",
        "container_entrypoint": ["python3", "/opt/ml/processing/input/code/preprocessing.py"]
    },
    processing_resources={
        "cluster_config": {
            "instance_count": 1,
            "instance_type": "ml.m5.xlarge",
            "volume_size_in_gb": 30
        }
    },
    processing_inputs=[
        {
            "input_name": "code",
            "s3_input": {
                "s3_uri": "s3://path/to/preprocessing.py",
                "local_path": "/opt/ml/processing/input/code",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        },
        {
            "input_name": "input-data",
            "s3_input": {
                "s3_uri": "s3://path/to/my/input-data.csv",
                "local_path": "/opt/ml/processing/input",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        }
    ],
    processing_output_config={
        "outputs": [
            {"output_name": "train", "s3_output": {"s3_uri": "s3://output/train", "local_path": "/opt/ml/processing/output/train", "s3_upload_mode": "EndOfJob"}},
            {"output_name": "validation", "s3_output": {"s3_uri": "s3://output/validation", "local_path": "/opt/ml/processing/output/validation", "s3_upload_mode": "EndOfJob"}},
            {"output_name": "test", "s3_output": {"s3_uri": "s3://output/test", "local_path": "/opt/ml/processing/output/test", "s3_upload_mode": "EndOfJob"}}
        ]
    }
)

```

To process data in parallel using Scikit-Learn on Amazon SageMaker Processing, you can shard
input objects by S3 key by setting `s3_data_distribution_type='ShardedByS3Key'` inside a
`ProcessingInput` so that each instance receives about the same number of input
objects.
