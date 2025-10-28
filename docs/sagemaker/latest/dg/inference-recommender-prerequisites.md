# Prerequisites for using

Amazon SageMaker Inference Recommender

Before you can use Amazon SageMaker Inference Recommender, you must complete the prerequisite steps. As an
example, we show how to use a PyTorch (v1.7.1) ResNet-18 pre-trained model for both
types of Amazon SageMaker Inference Recommender recommendation jobs. The examples shown use the
AWS SDK for Python (Boto3).

###### Note

- The following code examples use Python. Remove the `!` prefix
  character if you run any of the following code samples in your terminal or
  AWS CLI.
- You can run the following examples with the Python 3 (TensorFlow 2.6 Python 3.8
  CPU Optimized) kernel in an Amazon SageMaker Studio notebook. For more information
  about Studio, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

1. **Create an IAM role for Amazon SageMaker AI.**

Create an IAM role for Amazon SageMaker AI that has the
`AmazonSageMakerFullAccess` IAM managed policy attached. 2. **Set up your environment.**

Import dependencies and create variables for your AWS Region, your SageMaker AI
IAM role (from Step 1), and the SageMaker AI client.

```
!pip install --upgrade pip awscli botocore boto3  --quiet
from sagemaker import get_execution_role, Session, image_uris
import boto3

region = boto3.Session().region_name
role = get_execution_role()
sagemaker_client = boto3.client("sagemaker", region_name=region)
sagemaker_session = Session()
```

3. **(Optional) Review existing models benchmarked by
   Inference Recommender.**

Inference Recommender benchmarks models from popular model zoos. Inference Recommender supports your model
even if it is not already benchmarked.

Use `ListModelMetaData` to get a response object that lists the
domain, framework, task, and model name of machine learning models found in
common model zoos.

You use the domain, framework, framework version, task, and model name in
later steps to both select an inference Docker image and register your model
with SageMaker Model Registry. The following demonstrates how to list model metadata
with SDK for Python (Boto3):

```
list_model_metadata_response=sagemaker_client.list_model_metadata()
```

The output includes model summaries (`ModelMetadataSummaries`) and
response metadata (`ResponseMetadata`) similar to the following
example:

```
{
    'ModelMetadataSummaries': [{
            'Domain': 'NATURAL_LANGUAGE_PROCESSING',
            'Framework': 'PYTORCH:1.6.0',
             'Model': 'bert-base-cased',
             'Task': 'FILL_MASK'
             },
            {
             'Domain': 'NATURAL_LANGUAGE_PROCESSING',
             'Framework': 'PYTORCH:1.6.0',
             'Model': 'bert-base-uncased',
             'Task': 'FILL_MASK'
             },
            {
            'Domain': 'COMPUTER_VISION',
             'Framework': 'MXNET:1.8.0',
             'Model': 'resnet18v2-gluon',
             'Task': 'IMAGE_CLASSIFICATION'
             },
             {
             'Domain': 'COMPUTER_VISION',
             'Framework': 'PYTORCH:1.6.0',
             'Model': 'resnet152',
             'Task': 'IMAGE_CLASSIFICATION'
             }],
    'ResponseMetadata': {
                            'HTTPHeaders': {
                            'content-length': '2345',
                            'content-type': 'application/x-amz-json-1.1',
                            'date': 'Tue, 19 Oct 2021 20:52:03 GMT',
                            'x-amzn-requestid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
                          },
    'HTTPStatusCode': 200,
    'RequestId': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    'RetryAttempts': 0
    }
}
```

For this demo, we use a PyTorch (v1.7.1) ResNet-18 model to perform image
classification. The following Python code sample stores the framework, framework
version, domain, and task into variables for later use:

```
# ML framework details
framework = 'pytorch'
framework_version = '1.7.1'

# ML model details
ml_domain = 'COMPUTER_VISION'
ml_task = 'IMAGE_CLASSIFICATION'
```

4. **Upload your machine learning model to
   Amazon S3.**

Use this PyTorch (v1.7.1) ResNet-18 model if you do not have a pre-trained
machine learning model:

```
# Optional: Download a sample PyTorch model
import torch
from torchvision import models, transforms, datasets

# Create an example input for tracing
image = torch.zeros([1, 3, 256, 256], dtype=torch.float32)

# Load a pretrained resnet18 model from TorchHub
model = models.resnet18(pretrained=True)

# Tell the model we are using it for evaluation (not training). Note this is required for Inferentia compilation.
model.eval()
model_trace = torch.jit.trace(model, image)

# Save your traced model
model_trace.save('model.pth')
```

Download a sample inference script `inference.py`. Create a
`code` directory and move the inference script to the
`code` directory.

```
# Download the inference script
!wget https://aws-ml-blog-artifacts.s3.us-east-2.amazonaws.com/inference.py

# move it into a code/ directory
!mkdir code
!mv inference.py code/
```

Amazon SageMaker AI requires pre-trained machine learning models to be packaged as a
compressed TAR file (`*.tar.gz`). Compress your model and
inference script to satisfy this requirement:

```
!tar -czf test.tar.gz model.pth code/inference.py
```

When your endpoint is provisioned, the files in the archive are extracted to
`/opt/ml/model/` on the endpoint.

After you compress your model and model artifacts as a
`.tar.gz` file, upload them to your Amazon S3 bucket. The
following example demonstrates how to upload your model to Amazon S3 using the
AWS CLI:

```
!aws s3 cp test.tar.gz s3://`{your-bucket}`/models/
```

5. **Select a prebuilt Docker inference image or create your
   own Inference Docker Image.**

SageMaker AI provides containers for its built-in algorithms and prebuilt Docker
images for some of the most common machine learning frameworks, such as Apache
MXNet, TensorFlow, PyTorch, and Chainer. For a full list of the available SageMaker AI
images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

If none of the existing SageMaker AI containers meet your needs and you don't have an
existing container of your own, create a new Docker image. See [Containers with custom inference code](your-algorithms-inference-main.md "your-algorithms-inference-main.md") for information about how
to create your Docker image.

The following demonstrates how to retrieve a PyTorch version 1.7.1 inference
image using the SageMaker Python SDK:

```
from sagemaker import image_uris

## Uncomment and replace with your own values if you did not define
## these variables a previous step.
#framework = 'pytorch'
#framework_version = '1.7.1'

# Note: you can use any CPU-based instance here,
# this is just to set the arch as CPU for the Docker image
instance_type = 'ml.m5.2xlarge'

image_uri = image_uris.retrieve(framework,
                                region,
                                version=framework_version,
                                py_version='py3',
                                instance_type=instance_type,
                                image_scope='inference')

```

For a list of available SageMaker AI Instances, see [Amazon SageMaker AI
Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/"). 6. **Create a sample payload archive.**

Create an archive that contains individual files that the load testing tool
can send to your SageMaker AI endpoints. Your inference code must be able to read the
file formats from the sample payload.

The following downloads a .jpg image that this example uses in a later step
for the ResNet-18 model.

```
!wget https://cdn.pixabay.com/photo/2020/12/18/05/56/flowers-5841251_1280.jpg
```

Compress the sample payload as a tarball:

```
!tar -cvzf payload.tar.gz flowers-5841251_1280.jpg
```

Upload the sample payload to Amazon S3 and note the Amazon S3 URI:

```
!aws s3 cp payload.tar.gz s3://{bucket}/models/
```

You need the Amazon S3 URI in a later step, so store it in a variable:

```
bucket_prefix='models'
bucket = `'<your-bucket-name>'` # Provide the name of your S3 bucket
payload_s3_key = f"{bucket_prefix}/payload.tar.gz"
sample_payload_url= f"s3://{bucket}/{payload_s3_key}"
```

7. **Prepare your model input for the recommendations
   job**

For the last prerequisite, you have two options to prepare your model input.
You can either register your model with SageMaker Model Registry, which you can use
to catalog models for production, or you can create a SageMaker AI model and specify it
in the `ContainerConfig` field when creating a recommendations job.
The first option is best if you want to take advantage of the features that
[Model Registry](model-registry.md "model-registry.md") provides, such as managing model versions and
automating model deployment. The second option is ideal if you want to get
started quickly. For the first option, go to step 7. For the second option, skip
step 7 and go to step 8. 8. **Option 1: Register your model in the model
registry**

With SageMaker Model Registry, you can catalog models for production, manage model
versions, associate metadata (such as training metrics) with a model, manage the
approval status of a model, deploy models to production, and automate model
deployment with CI/CD.

When you use SageMaker Model Registry to track and manage your models, they are
represented as a versioned model package within model package groups.
Unversioned model packages are not part of a model group. Model package groups
hold multiple versions or iterations of a model. Though it is not required to
create them for every model in the registry, they help organize various models
that all have the same purpose and provide automatic versioning.

To use Amazon SageMaker Inference Recommender, you must have a versioned model package. You can create a
versioned model package programmatically with the AWS SDK for Python (Boto3) or with
Amazon SageMaker Studio Classic. To create a versioned model package programmatically, first
create a model package group with the `CreateModelPackageGroup` API.
Next, create a model package using the `CreateModelPackage` API.
Calling this method makes a versioned model package.

See [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md") and [Register a Model Version](model-registry-version.md "model-registry-version.md")
for detailed instructions about how to programmatically and interactively create
a model package group and how to create a versioned model package, respectively,
with the AWS SDK for Python (Boto3) and Amazon SageMaker Studio Classic.

The following code sample demonstrates how to create a versioned model package
using the AWS SDK for Python (Boto3).

###### Note

You do not need to approve the model package to create an Inference Recommender
job.

    1. **Create a model package group**


    Create a model package group with the
     `CreateModelPackageGroup` API. Provide a name to the
     model package group for the `ModelPackageGroupName` and
     optionally provide a description of the model package in the
     `ModelPackageGroupDescription` field.



    ```
    model_package_group_name = `'<INSERT>'`
    model_package_group_description = `'<INSERT>'`

    model_package_group_input_dict = {
     "ModelPackageGroupName" : model_package_group_name,
     "ModelPackageGroupDescription" : model_package_group_description,
    }

    model_package_group_response = sagemaker_client.create_model_package_group(**model_package_group_input_dict)
    ```

    See the [Amazon SageMaker API
     Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md") for a full list of optional and required
     arguments you can pass to [`CreateModelPackageGroup`](../APIReference/API_CreateModelPackageGroup.md "../APIReference/API_CreateModelPackageGroup.md").


    Create a model package by specifying a Docker image that runs your
     inference code and the Amazon S3 location of your model artifacts and provide
     values for `InferenceSpecification`.
     `InferenceSpecification` should contain information about
     inference jobs that can be run with models based on this model package,
     including the following:




    	* The Amazon ECR paths of images that run your inference code.
    	* (Optional) The instance types that the model package supports
    	 for transform jobs and real-time endpoints used for
    	 inference.
    	* The input and output content formats that the model package
    	 supports for inference.
    In addition, you must specify the following parameters when you create
     a model package:




    	* [Domain](../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Domain "../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Domain"): The machine learning domain of your model
    	 package and its components. Common machine learning domains
    	 include computer vision and natural language processing.
    	* [Task](../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Task "../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Task"): The machine learning task your model package
    	 accomplishes. Common machine learning tasks include object
    	 detection and image classification. Specify "OTHER" if none of
    	 the tasks listed in the [API
    	 Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md") satisfy your use case. See the
    	 [Task](../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Task "../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-Task") API field descriptions for a list of supported
    	 machine learning tasks.
    	* [SamplePayloadUrl](../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-SamplePayloadUrl "../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-SamplePayloadUrl"): The Amazon Simple Storage Service (Amazon S3) path where
    	 the sample payload are stored. This path must point to a single
    	 GZIP compressed TAR archive (.tar.gz suffix).
    	* [Framework](../APIReference/API_ModelPackageContainerDefinition.md#sagemaker-Type-ModelPackageContainerDefinition-Framework "../APIReference/API_ModelPackageContainerDefinition.md#sagemaker-Type-ModelPackageContainerDefinition-Framework"): The machine learning framework of the
    	 model package container image.
    	* [FrameworkVersion](../APIReference/API_ModelPackageContainerDefinition.md#sagemaker-Type-ModelPackageContainerDefinition-FrameworkVersion "../APIReference/API_ModelPackageContainerDefinition.md#sagemaker-Type-ModelPackageContainerDefinition-FrameworkVersion"): The framework version of the
    	 model package container image.
    If you provide an allow list of instance types to use to generate
     inferences in real-time for the [SupportedRealtimeInferenceInstanceTypes](../APIReference/API_InferenceSpecification.md#sagemaker-Type-InferenceSpecification-SupportedRealtimeInferenceInstanceTypes "../APIReference/API_InferenceSpecification.md#sagemaker-Type-InferenceSpecification-SupportedRealtimeInferenceInstanceTypes"), Inference Recommender limits the
     search space for instance types during a `Default` job. Use
     this parameter if you have budget constraints or know there's a specific
     set of instance types that can support your model and container
     image.


    In a previous step, we downloaded a pre-trained ResNet18 model and
     stored it in an Amazon S3 bucket in a directory called `models`.
     We retrieved a PyTorch (v1.7.1) Deep Learning Container inference image
     and stored the URI in a variable called `image_uri`. Use
     those variables in the following code sample to define a dictionary used
     as input to the [`CreateModelPackage`](../APIReference/API_CreateModelPackage.md "../APIReference/API_CreateModelPackage.md") API.



    ```
    # Provide the Amazon S3 URI of your compressed tarfile
    # so that Model Registry knows where to find your model artifacts
    bucket_prefix='models'
    bucket = `'<your-bucket-name>'` # Provide the name of your S3 bucket
    model_s3_key = f"{bucket_prefix}/test.tar.gz"
    model_url= f"s3://{bucket}/{model_s3_key}"

    # Similar open source model to the packaged model
    # The name of the ML model as standardized by common model zoos
    nearest_model_name = 'resnet18'

    # The supported MIME types for input and output data. In this example,
    # we are using images as input.
    input_content_type='image/jpeg'


    # Optional - provide a description of your model.
    model_package_description = `'<INSERT>'`

    ## Uncomment if you did not store the domain and task in an earlier
    ## step
    #ml_domain = 'COMPUTER_VISION'
    #ml_task = 'IMAGE_CLASSIFICATION'

    ## Uncomment if you did not store the framework and framework version
    ## in a previous step.
    #framework = 'PYTORCH'
    #framework_version = '1.7.1'

    # Optional: Used for optimizing your model using SageMaker Neo
    # PyTorch uses NCHW format for images
    data_input_configuration = "[[1,3,256,256]]"

    # Create a dictionary to use as input for creating a model pacakge group
    model_package_input_dict = {
            "ModelPackageGroupName" : model_package_group_name,
            "ModelPackageDescription" : model_package_description,
            "Domain": ml_domain,
            "Task": ml_task,
            "SamplePayloadUrl": sample_payload_url,
            "InferenceSpecification": {
                    "Containers": [
                        {
                            "Image": image_uri,
                            "ModelDataUrl": model_url,
                            "Framework": framework.upper(),
                            "FrameworkVersion": framework_version,
                            "NearestModelName": nearest_model_name,
                            "ModelInput": {"DataInputConfig": data_input_configuration}
                        }
                        ],
                    "SupportedContentTypes": [input_content_type]
            }
        }
    ```
    2. **Create a model package**


    Use the `CreateModelPackage` API to create a model package.
     Pass the input dictionary defined in the previous step:



    ```
    model_package_response = sagemaker_client.create_model_package(**model_package_input_dict)
    ```

    You need the model package ARN to use Amazon SageMaker Inference Recommender. Note the ARN of the
     model package or store it in a variable:



    ```
    model_package_arn = model_package_response["ModelPackageArn"]

    print('ModelPackage Version ARN : {}'.format(model_package_arn))
    ```

9. **Option 2: Create a model and configure the
   `ContainerConfig` field**

Use this option if you want to start an inference recommendations job and
don't need to register your model in the Model Registry. In the following steps,
you create a model in SageMaker AI and configure the `ContainerConfig` field
as input for the recommendations job.

    1. **Create a model**


    Create a model with the `CreateModel` API. For an example
     that calls this method when deploying a model to SageMaker AI Hosting, see
     [Create a Model (AWS SDK for Python (Boto3))](realtime-endpoints-deployment.md#realtime-endpoints-deployment-create-model "realtime-endpoints-deployment.md#realtime-endpoints-deployment-create-model").


    In a previous step, we downloaded a pre-trained ResNet18 model and
     stored it in an Amazon S3 bucket in a directory called `models`.
     We retrieved a PyTorch (v1.7.1) Deep Learning Container inference image
     and stored the URI in a variable called `image_uri`. We use
     those variables in the following code example where we define a
     dictionary used as input to the `CreateModel` API.



    ```

    model_name = '`<name_of_the_model>`'
    # Role to give SageMaker permission to access AWS services.
    sagemaker_role= "arn:aws:iam::`<region>`:`<account>`:role/*"

    # Provide the Amazon S3 URI of your compressed tarfile
    # so that Model Registry knows where to find your model artifacts
    bucket_prefix='models'
    bucket = '`<your-bucket-name>`' # Provide the name of your S3 bucket
    model_s3_key = f"{bucket_prefix}/test.tar.gz"
    model_url= f"s3://{bucket}/{model_s3_key}"

    #Create model
    create_model_response = sagemaker_client.create_model(
        ModelName = model_name,
        ExecutionRoleArn = sagemaker_role,
        PrimaryContainer = {
            'Image': image_uri,
            'ModelDataUrl': model_url,
        })

    ```
    2. **Configure the `ContainerConfig`
     field**


    Next, you must configure the [ContainerConfig](../APIReference/API_RecommendationJobInputConfig.md#sagemaker-Type-RecommendationJobInputConfig-ContainerConfig "../APIReference/API_RecommendationJobInputConfig.md#sagemaker-Type-RecommendationJobInputConfig-ContainerConfig") field with the model you just created and
     specify the following parameters in it:




    	* `Domain`: The machine learning domain of the model
    	 and its components, such as computer vision or natural language
    	 processing.
    	* `Task`: The machine learning task that the model
    	 accomplishes, such as image classification or object
    	 detection.
    	* `PayloadConfig`: The configuration for the payload
    	 for a recommendation job. For more information about the
    	 subfields, see `RecommendationJobPayloadConfig`.
    	* `Framework`: The machine learning framework of the
    	 container image, such as PyTorch.
    	* `FrameworkVersion`: The framework version of the
    	 container image.
    	* (Optional) `SupportedInstanceTypes`: A list of the
    	 instance types that are used to generate inferences in
    	 real-time.
    If you use the `SupportedInstanceTypes` parameter, Inference Recommender
     limits the search space for instance types during a `Default`
     job. Use this parameter if you have budget constraints or know there's a
     specific set of instance types that can support your model and container
     image.


    In the following code example, we use the previously defined
     parameters, along with `NearestModelName`, to define a
     dictionary used as input to the `CreateInferenceRecommendationsJob` API.



    ```
    ## Uncomment if you did not store the domain and task in a previous step
    #ml_domain = 'COMPUTER_VISION'
    #ml_task = 'IMAGE_CLASSIFICATION'

    ## Uncomment if you did not store the framework and framework version in a previous step
    #framework = 'PYTORCH'
    #framework_version = '1.7.1'

    # The name of the ML model as standardized by common model zoos
    nearest_model_name = 'resnet18'

    # The supported MIME types for input and output data. In this example,
    # we are using images as input
    input_content_type='image/jpeg'

    # Optional: Used for optimizing your model using SageMaker Neo
    # PyTorch uses NCHW format for images
    data_input_configuration = "[[1,3,256,256]]"

    # Create a dictionary to use as input for creating an inference recommendation job
    container_config = {
            "Domain": ml_domain,
            "Framework": framework.upper(),
            "FrameworkVersion": framework_version,
            "NearestModelName": nearest_model_name,
            "PayloadConfig": {
                "SamplePayloadUrl": sample_payload_url,
                "SupportedContentTypes": [ input_content_type ]
             },
            "DataInputConfig": data_input_configuration
            "Task": ml_task,
            }
    ```
