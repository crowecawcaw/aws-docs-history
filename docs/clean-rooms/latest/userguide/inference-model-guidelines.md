# Model authoring guidelines for the

inference container

This section details the guidelines that model providers should follow when
creating an inference algorithm for Clean Rooms ML.

- Use the appropriate SageMaker AI inference-supported container base image, as
  described in the [SageMaker AI Developer Guide](../../../sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../../../sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). The following code allows you to pull the
  supported container base images from public SageMaker AI endpoints.

```
`ecr_registry_endpoint='`763104351884`.dkr.ecr.$REGION.amazonaws.com'
base_image='pytorch-inference:2.3.0-cpu-py311-ubuntu20.04-sagemaker'
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ecr_registry_endpoint
docker pull $ecr_registry_endpoint/$base_image`
```

- When authoring the model locally, ensure the following so that you can
  test your model locally, on a development instance, on SageMaker AI Batch Transform
  in your AWS account, and on Clean Rooms ML.
  - Clean Rooms ML makes your model artifacts from inference available for
    use by your inference code via the `/opt/ml/model`
    directory in the docker container.
  - Clean Rooms ML splits input by line, uses a `MultiRecord`
    batch strategy, and adds a newline character at the end of every
    transformed record.
  - Ensure that you are able to generate a synthetic or test inference
    dataset based on the schema of the collaborators that will be used
    in your model code.
  - Ensure that you can run a SageMaker AI batch transform job on your own
    AWS account before you associate the model algorithm with a AWS Clean Rooms
    collaboration.

  The following code contains a sample Docker file that is
  compatible with local testing, SageMaker AI transform environment testing,
  and Clean Rooms ML

  ```
  `FROM `763104351884`.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.12.1-cpu-py38-ubuntu20.04-sagemaker

  ENV PYTHONUNBUFFERED=1

  COPY serve.py /opt/ml/code/serve.py
  COPY inference_handler.py /opt/ml/code/inference_handler.py
  COPY handler_service.py /opt/ml/code/handler_service.py
  COPY model.py /opt/ml/code/model.py

  RUN chmod +x /opt/ml/code/serve.py

  ENTRYPOINT ["/opt/ml/code/serve.py"]`
  ```

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

# Authenticate Docker
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Push To ECR Repository
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com$REPO_NAME:$REPO_TAG

# Create Sagemaker Model
# Configure the create_model.json with
# 1. Primary container -
 # a. ModelDataUrl - S3 Uri of the model.tar from your training job
aws sagemaker create-model --cli-input-json file://create_model.json --region $REGION

# Create Sagemaker Transform Job
# Configure the transform_job.json with
# 1. Model created in the step above
# 2. MultiRecord batch strategy
# 3. Line SplitType for TransformInput
# 4. AssembleWith Line for TransformOutput
aws sagemaker create-transform-job --cli-input-json file://transform_job.json --region $REGION`
```

After the SageMaker AI job is complete and you are satisfied with your batch
transform, you can register the Amazon ECR Registry with AWS Clean Rooms ML. Use the
`CreateConfiguredModelAlgorithm` action to register the model
algorithm and the `CreateConfiguredModelAlgorithmAssociation` to
associate it to a collaboration.
