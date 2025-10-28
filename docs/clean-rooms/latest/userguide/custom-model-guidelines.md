# Model authoring guidelines for the

training container

This section details the guidelines that model providers should follow when
creating a custom ML model algorithm for Clean Rooms ML.

- Use the appropriate SageMaker AI training-supported container base image, as
  described in the [SageMaker AI Developer Guide](../../../sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../../../sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). The following code allows you to pull the
  supported container base images from public SageMaker AI endpoints.

```
`ecr_registry_endpoint='`763104351884`.dkr.ecr.$REGION.amazonaws.com'
base_image='pytorch-training:2.3.0-cpu-py311-ubuntu20.04-sagemaker'
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ecr_registry_endpoint
docker pull $ecr_registry_endpoint/$base_image`
```

- When authoring the model locally, ensure the following so that you can
  test your model locally, on a development instance, on SageMaker AI Training in your
  AWS account, and on Clean Rooms ML.
  - We recommend writing a training script that accesses useful
    properties about the training environment through various
    environment variables. Clean Rooms ML uses the following arguments to
    invoke training on your model code: `SM_MODEL_DIR`,
    `SM_OUTPUT_DIR`, `SM_CHANNEL_TRAIN`, and
    `FILE_FORMAT`. These defaults are used by Clean Rooms ML to
    train your ML model in its own execution environment with the data
    from all parties.
  - Clean Rooms ML makes your training input channels available via the
    `/opt/ml/input/data/`channel-name``directories in the docker container. Each ML input channel is mapped
based on its corresponding`channel_name`provided in the`CreateTrainedModel` request.

  ```
  `parser = argparse.ArgumentParser()# Data, model, and output directories

  parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR', "/opt/ml/model"))
  parser.add_argument('--output_dir', type=str, default=os.environ.get('SM_OUTPUT_DIR', "/opt/ml/output/data"))
  parser.add_argument('--train_dir', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', "/opt/ml/input/data/train"))
  parser.add_argument('--train_file_format', type=str, default=os.environ.get('FILE_FORMAT', "csv"))`
  ```

  - Ensure that you are able to generate a synthetic or test dataset
    based on the schema of the collaborators that will be used in your
    model code.
  - Ensure that you can run a SageMaker AI training job on your own
    AWS account before you associate the model algorithm with a AWS Clean Rooms
    collaboration.

  The following code contains a sample Docker file that is
  compatible with local testing, SageMaker AI Training environment testing,
  and Clean Rooms ML

  ```
  `FROM `763104351884`.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:2.3.0-cpu-py311-ubuntu20.04-sagemaker
  MAINTAINER $author_name

  ENV PYTHONDONTWRITEBYTECODE=1 \
   PYTHONUNBUFFERED=1 \
   LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/lib"

  ENV PATH="/opt/ml/code:${PATH}"

  # this environment variable is used by the SageMaker PyTorch container to determine our user code directory
  ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/code

  # copy the training script inside the container
  COPY train.py /opt/ml/code/train.py
  # define train.py as the script entry point
  ENV SAGEMAKER_PROGRAM train.py
  ENTRYPOINT ["python", "/opt/ml/code/train.py"]`
  ```

- To
  best monitor container failures, we recommend exporting logs and debugging
  for failure reasons. In a `GetTrainedModel`
  response, Clean Rooms ML returns the first 1024 characters from this file under
  `StatusDetails`.
- After you have completed any model changes and you are ready to test it in
  the SageMaker AI environment, run the following commands in the order
  provided.

```
`export ACCOUNT_ID=xxx
export REPO_NAME=xxx
export REPO_TAG=xxx
export REGION=xxx

docker build -t $ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/$REPO_NAME:$REPO_TAG

# Sign into AWS $ACCOUNT_ID/ Run aws configure
# Check the account and make sure it is the correct role/credentials
aws sts get-caller-identity
aws ecr create-repository --repository-name $REPO_NAME --region $REGION
aws ecr describe-repositories --repository-name $REPO_NAME --region $REGION

# Authenticate Doker
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Push To ECR Images
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com$REPO_NAME:$REPO_TAG

# Create Sagemaker Training job
# Configure the training_job.json with
# 1. TrainingImage
# 2. Input DataConfig
# 3. Output DataConfig
aws sagemaker create-training-job --cli-input-json file://training_job.json --region $REGION`
```

After the SageMaker AI job is complete and you are satisfied with your model
algorithm, you can register the Amazon ECR Registry with AWS Clean Rooms ML. Use the
`CreateConfiguredModelAlgorithm` action to register the model
algorithm and the `CreateConfiguredModelAlgorithmAssociation` to
associate it to a collaboration.
