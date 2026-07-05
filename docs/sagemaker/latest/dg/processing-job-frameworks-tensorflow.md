# TensorFlow Framework Processor

TensorFlow is an open-source machine learning and artificial intelligence library. The `TensorFlowProcessor`
in the Amazon SageMaker Python SDK provides you with the ability to run processing jobs with TensorFlow scripts. When you use the
`TensorFlowProcessor`, you can leverage an Amazon-built Docker container with a managed TensorFlow environment
so that you don't need to bring your own container.

The following code example shows how you can run your Processing job using a Docker image
provided and maintained by SageMaker AI. Note that when you run the job, you can specify a directory containing your scripts and dependencies in the
`source_dir` argument, and you can have a `requirements.txt` file located inside your `source_dir`
directory that specifies the dependencies for your processing script(s). SageMaker Processing installs the dependencies in `requirements.txt`
in the container for you.

```
from sagemaker.core.resources import ProcessingJob
from sagemaker.core.helper.session_helper import get_execution_role

# Create a processing job with a TensorFlow container
processing_job = ProcessingJob.create(
    processing_job_name='frameworkprocessor-TF',
    role_arn=get_execution_role(),
    app_specification={
        "image_uri": "`tensorflow-processing-image-uri`",
        "container_entrypoint": ["python3", "/opt/ml/processing/input/code/`processing-script.py`"]
    },
    processing_resources={
        "cluster_config": {"instance_count": 1, "instance_type": "ml.m5.xlarge", "volume_size_in_gb": 30}
    },
    processing_inputs=[
        {"input_name": "data", "s3_input": {"s3_uri": f"`s3://{{BUCKET}}/{{S3_INPUT_PATH}}`", "local_path": "/opt/ml/processing/input/data", "s3_data_type": "S3Prefix", "s3_input_mode": "File"}},
        {"input_name": "model", "s3_input": {"s3_uri": f"`s3://{{BUCKET}}/{{S3_PATH_TO_MODEL}}`", "local_path": "/opt/ml/processing/input/model", "s3_data_type": "S3Prefix", "s3_input_mode": "File"}},
        {"input_name": "code", "s3_input": {"s3_uri": "`s3://path/to/scripts/`", "local_path": "/opt/ml/processing/input/code", "s3_data_type": "S3Prefix", "s3_input_mode": "File"}}
    ],
    processing_output_config={
        "outputs": [
            {"output_name": "predictions", "s3_output": {"s3_uri": f"`s3://{{BUCKET}}/{{S3_OUTPUT_PATH}}`", "local_path": "/opt/ml/processing/output", "s3_upload_mode": "EndOfJob"}}
        ]
    }
)
```

If you have a `requirements.txt` file, it should be a list of libraries you want
to install in the container. The path for `source_dir` can be a relative, absolute, or
Amazon S3 URI path. However, if you use an Amazon S3 URI, then it must point to a tar.gz file. You can have
multiple scripts in the directory you specify for `source_dir`. To learn more about
the `TensorFlowProcessor` class, see [TensorFlow Estimator](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") in the _Amazon SageMaker Python SDK_.
