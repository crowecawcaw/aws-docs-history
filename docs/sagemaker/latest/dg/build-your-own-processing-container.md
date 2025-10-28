# How to Build Your Own Processing

Container (Advanced Scenario)

You can provide Amazon SageMaker Processing with a Docker image that has your own code and dependencies to
run your data processing, feature engineering, and model evaluation workloads. The
following provides information on how to build your own processing container.

The following example of a Dockerfile builds a container with the Python libraries
scikit-learn and pandas, which you can run as a processing job.

```
FROM python:3.7-slim-buster

# Install scikit-learn and pandas
RUN pip3 install pandas==0.25.3 scikit-learn==0.21.3

# Add a Python script and configure Docker to run it
ADD processing_script.py /
ENTRYPOINT ["python3", "/processing_script.py"]
```

For an example of a processing script, see [Get started with SageMaker Processing](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_processing/basic_sagemaker_data_processing/basic_sagemaker_processing.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_processing/basic_sagemaker_data_processing/basic_sagemaker_processing.ipynb").

Build and push this Docker image to an Amazon Elastic Container Registry (Amazon ECR) repository and ensure that
your SageMaker AI IAM role can pull the image from Amazon ECR. Then you can run this image on
Amazon SageMaker Processing.

## How Amazon SageMaker Processing Configures Your Processing Container

Amazon SageMaker Processing provides configuration information to your processing container through
environment variables and two JSON
files—`/opt/ml/config/processingjobconfig.json` and
`/opt/ml/config/resourceconfig.json`— at predefined locations
in the container.

When a processing job starts, it uses the environment variables that you specified
with the `Environment` map in the `CreateProcessingJob`
request. The `/opt/ml/config/processingjobconfig.json` file contains
information about the hostnames of your processing containers, and is also specified
in the `CreateProcessingJob` request.

The following example shows the format of the
`/opt/ml/config/processingjobconfig.json` file.

```
{
    "ProcessingJobArn": "<processing_job_arn>",
    "ProcessingJobName": "<processing_job_name>",
    "AppSpecification": {
        "ImageUri": "<image_uri>",
        "ContainerEntrypoint": null,
        "ContainerArguments": null
    },
    "Environment": {
        "KEY": "VALUE"
    },
    "ProcessingInputs": [
        {
            "InputName": "input-1",
            "S3Input": {
                "LocalPath": "/opt/ml/processing/input/dataset",
                "S3Uri": "<s3_uri>",
                "S3DataDistributionType": "FullyReplicated",
                "S3DataType": "S3Prefix",
                "S3InputMode": "File",
                "S3CompressionType": "None",
                "S3DownloadMode": "StartOfJob"
            }
        }
    ],
    "ProcessingOutputConfig": {
        "Outputs": [
            {
                "OutputName": "output-1",
                "S3Output": {
                    "LocalPath": "/opt/ml/processing/output/dataset",
                    "S3Uri": "<s3_uri>",
                    "S3UploadMode": "EndOfJob"
                }
            }
        ],
        "KmsKeyId": null
    },
    "ProcessingResources": {
        "ClusterConfig": {
            "InstanceCount": 1,
            "InstanceType": "ml.m5.xlarge",
            "VolumeSizeInGB": 30,
            "VolumeKmsKeyId": null
        }
    },
    "RoleArn": "<IAM role>",
    "StoppingCondition": {
        "MaxRuntimeInSeconds": 86400
    }
}
```

The `/opt/ml/config/resourceconfig.json` file contains information
about the hostnames of your processing containers. Use the following
hostnames
when creating or running distributed processing code.

```
{
  "current_host": "algo-1",
  "hosts": ["algo-1","algo-2","algo-3"]
}
```

Don't use the information about hostnames contained in
`/etc/hostname`
or `/etc/hosts` because it might be inaccurate.

Hostname information might not be immediately available to the processing
container. We recommend adding a retry policy on hostname resolution operations as
nodes become available in the cluster.
