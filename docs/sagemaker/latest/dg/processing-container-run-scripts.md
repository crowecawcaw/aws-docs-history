# Run Scripts with Your Own Processing Container

You can use scikit-learn scripts to preprocess data and evaluate your models. To see
how to run scikit-learn scripts to perform these tasks, see the [scikit-learn Processing](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation") sample notebook. This notebook uses the
`ScriptProcessor` class from the Amazon SageMaker Python SDK for Processing.

The following example shows a general workflow for using your own processing container. The workflow
shows how to create your own image, build your container, and run a Python preprocessing script with the
container. The processing job processes your input data and saves the processed data in
Amazon Simple Storage Service (Amazon S3).

Before using the following examples, you need to have your own input data and a Python
script prepared to process your data. For an end-to-end, guided example of this process,
refer back to the [scikit-learn Processing](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation") sample notebook.

1. Create a Docker directory and add the Dockerfile used to create the processing
   container. Install pandas and scikit-learn into it. (You could also install your
   own dependencies with a similar `RUN` command.)

```
mkdir docker

%%writefile docker/Dockerfile

FROM python:3.7-slim-buster

RUN pip3 install pandas==0.25.3 scikit-learn==0.21.3
ENV PYTHONUNBUFFERED=TRUE

ENTRYPOINT ["python3"]
```

2. Build the container using the docker command, create an Amazon Elastic
   Container Registry (Amazon ECR) repository, and push the image to Amazon
   ECR.

```
import boto3

account_id = boto3.client('sts').get_caller_identity().get('Account')
region = boto3.Session().region_name
ecr_repository = 'sagemaker-processing-container'
tag = ':latest'
processing_repository_uri = '{}.dkr.ecr.{}.amazonaws.com/{}'.format(account_id, region, ecr_repository + tag)

# Create ECR repository and push docker image
!docker build -t $ecr_repository docker
!aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {account_id}.dkr.ecr.{region}.amazonaws.com
!aws ecr create-repository --repository-name $ecr_repository
!docker tag {ecr_repository + tag} $processing_repository_uri
!docker push $processing_repository_uri
```

3. Set up and run the processing job. Replace `image_uri` with the URI for the image
   you created, and replace `role_arn` with the ARN for an
   AWS Identity and Access Management role that has access to your target Amazon S3
   bucket. Replace `preprocessing.py` with the
   name of your own Python processing script, and replace
   `s3://path/to/my/input-data.csv` with the
   Amazon S3 path to your input data.

```
from sagemaker.core.resources import ProcessingJob

processing_job = ProcessingJob.create(
    processing_job_name="my-processing-job",
    role_arn='`role_arn`',
    app_specification={
        "image_uri": '`image_uri`',
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
                "s3_uri": '`s3://path/to/preprocessing.py`',
                "local_path": "/opt/ml/processing/input/code",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        },
        {
            "input_name": "input-data",
            "s3_input": {
                "s3_uri": '`s3://path/to/my/input-data.csv`',
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

You can use the same procedure with any other library or system dependencies. You can
also use existing Docker images. This includes images that you run on other platforms
such as [Kubernetes](https://kubernetes.io/ "https://kubernetes.io/").
