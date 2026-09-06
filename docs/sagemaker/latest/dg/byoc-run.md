

# Run Your Processing Container Using the SageMaker AI Python SDK
<a name="byoc-run"></a>

You can use the SageMaker Python SDK to run your own processing image. The following example shows how to run your own processing container with one input from Amazon Simple Storage Service (Amazon S3) and one output to Amazon S3.

```
from sagemaker.core.resources import ProcessingJob

processing_job = ProcessingJob.create(
    processing_job_name="my-byoc-processing",
    role_arn=role,
    app_specification={
        "image_uri": '<your_ecr_image_uri>'
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
            "input_name": "input-data",
            "s3_input": {
                "s3_uri": '<s3_uri or local path>',
                "local_path": "/opt/ml/processing/input_data",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        }
    ],
    processing_output_config={
        "outputs": [
            {
                "output_name": "processed-data",
                "s3_output": {
                    "s3_uri": '<s3_uri>',
                    "local_path": "/opt/ml/processing/processed_data",
                    "s3_upload_mode": "EndOfJob"
                }
            }
        ]
    }
)
```

Instead of building your processing code into your processing image, you can provide a `ScriptProcessor` with your image and the command that you want to run, along with the code that you want to run inside that container. For an example, see [Run Scripts with Your Own Processing Container](processing-container-run-scripts.md).

You can also use the scikit-learn image that Amazon SageMaker Processing provides to run scikit-learn scripts. For an example, see [Run a Processing Job with scikit-learn](use-scikit-learn-processing-container.md). 