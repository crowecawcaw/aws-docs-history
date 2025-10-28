# Deploy models with DJL

Serving

DJL Serving is a high performance universal stand-alone model serving solution. It
takes a deep learning model, several models, or workflows and makes them available
through an HTTP endpoint.

You can use one of the DJL Serving [Deep Learning
Containers (DLCs)](../../../deep-learning-containers/latest/devguide/what-is-dlc.md "../../../deep-learning-containers/latest/devguide/what-is-dlc.md") to serve your models on AWS. To learn about the
supported model types and frameworks, see the [DJL Serving GitHub
repository](https://github.com/deepjavalibrary/djl-serving "https://github.com/deepjavalibrary/djl-serving").

DJL Serving offers many features that help you to deploy your models with high
performance:

- Ease of use – DJL Serving can serve most models without any
  modifications. You bring your model artifacts, and DJL Serving can host
  them.
- Multiple device and accelerator support – DJL Serving supports
  deploying models on CPUs, GPUs, and AWS Inferentia.
- Performance – DJL Serving runs multithreaded inference in a single Java
  virtual machine (JVM) to boost throughput.
- Dynamic batching – DJL Serving supports dynamic batching to increase
  throughput.
- Auto scaling – DJL Serving automatically scales workers up or down
  based on the traffic load.
- Multi-engine support – DJL Serving can simultaneously host models using
  different frameworks (for example, PyTorch and TensorFlow).
- Ensemble and workflow models – DJL Serving supports deploying complex
  workflows comprised of multiple models and can execute parts of the workflow on
  CPUs and other parts on GPUs. Models within a workflow can leverage different
  frameworks.
  The following sections describe how to set up an endpoint with DJL Serving on
  SageMaker AI.

## Getting started

To get started, ensure that you have the following prerequisites:

1. Ensure that you have access to an AWS account. Set up your environment
   so that the AWS CLI can access your account through either an AWS IAM user
   or an IAM role. We recommend using an IAM role. For the purposes of
   testing in your personal account, you can attach the following managed
   permissions policies to the IAM role:
   - [AmazonEC2ContainerRegistryFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess")
   - [AmazonEC2FullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEC2FullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEC2FullAccess")
   - [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess")
   - [AmazonS3FullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonS3FullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonS3FullAccess")

2. Ensure that you have the [docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") client set up on your system.
3. Log in to Amazon Elastic Container Registry and set the following environment variables:

```
export ACCOUNT_ID=`<your_account_id>`
export REGION=`<your_region>`
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
```

4. Pull the docker image.

```
docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.22.1-deepspeed0.9.2-cu118
```

For all of the available DJL Serving container images, see the [large model inference containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#large-model-inference-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#large-model-inference-containers") and the [DJL Serving CPU inference containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#djl-cpu-full-inference-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#djl-cpu-full-inference-containers"). When choosing an image
from the tables in the preceding links, replace the AWS region in the
example URL column with the region you are in. The DLCs are available in the
regions listed in the table at the top of the [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md") page.

## Customize your container

You can add packages to the base DLC images to customize your container. Suppose
you want to add a package to the
`763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.22.1-deepspeed0.9.2-cu118`
docker image. You must create a dockerfile with your desired image as the base
image, add the required packages, and push the image to Amazon ECR.

To add a package, complete the following steps:

1. Specify instructions for running your desired libraries or packages in the
   base image's dockerfile.

```
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.22.1-deepspeed0.9.2-cu118

## add custom packages/libraries
RUN git clone https://github.com/awslabs/amazon-sagemaker-examples
```

2. Build the Docker image from the dockerfile. Specify your Amazon ECR repository,
   the name of the base image, and a tag for the image. If you don't have an
   Amazon ECR repository, see [Using Amazon ECR
   with the AWS CLI](../../../AmazonECR/latest/userguide/getting-started-cli.md "../../../AmazonECR/latest/userguide/getting-started-cli.md") in the _Amazon ECR User
   Guide_ for instructions on how to create one.

```
docker build -f Dockerfile -t <registry>/<image_name>:<image_tag>
```

3. Push the Docker image to your Amazon ECR repository.

```
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<image_name>:<image_tag>
```

You should now have a customized container image that you can use for model
serving. For more examples of customizing your container, see [Building AWS Deep Learning Containers Custom Images](https://github.com/aws/deep-learning-containers/blob/master/custom_images.md "https://github.com/aws/deep-learning-containers/blob/master/custom_images.md").

## Prepare your model

artifacts

Before deploying your model on SageMaker AI, you must package your model artifacts in a
`.tar.gz` file. DJL Serving accepts the following artifacts in your
archive:

- Model checkpoint: Files that store your model weights.
- `serving.properties`: A configuration file that you can add for
  each model. Place `serving.properties` in the same directory as
  your model file.
- `model.py`: The inference handler code. This is only applicable
  when using Python mode. If you don't specify `model.py`,
  djl-serving uses one of the default handlers.

The following is an example of a `model.tar.gz` structure:

```
 - model_root_dir # root directory
    - serving.properties
    - model.py # your custom handler file for Python, if you choose not to use the default handlers provided by DJL Serving
    - model binary files # used for Java mode, or if you don't want to use option.model_id and option.s3_url for Python mode
```

DJL Serving supports Java engines powered by DJL or Python engines. Not all of the
preceding artifacts are required; the required artifacts vary based on the mode you
choose. For example, in Python mode, you only need to specify
`option.model_id` in the `serving.properties` file; you
don't need to specify the model checkpoint inside LMI containers. In Java mode, you
are required to package the model checkpoint. For more details on how to configure
`serving.properties` and operate with different engines, see [DJL Serving Operation Modes](https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md "https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md").

## Use single model

endpoints to deploy with DJL Serving

After preparing your model artifacts, you can deploy your model to a SageMaker AI
endpoint. This section describes how to deploy a single model to an endpoint with
DJL Serving. If you're deploying multiple models, skip this section and go to [Use multi-model endpoints to
deploy with DJL Serving](#deploy-models-frameworks-djl-mme "#deploy-models-frameworks-djl-mme").

The following example shows you a method to create a model object using the
Amazon SageMaker Python SDK. You'll need to specify the following fields:

- `image_uri`: You can either retrieve one of the base DJL
  Serving images as shown in this example, or you can specify a custom Docker
  image from your Amazon ECR repository, if you followed the instructions in [Customize your container](#deploy-models-frameworks-djl-byoc "#deploy-models-frameworks-djl-byoc").
- `model_s3_url`: This should an Amazon S3 URI that points to your
  `.tar.gz`file.
- `model_name`: Specify a name for the model object.

```
import boto3
 import sagemaker
from sagemaker.model import Model
from sagemaker import image_uris, get_execution_role

aws_region = "aws-region"
sagemaker_session = sagemaker.Session(boto_session=boto3.Session(region_name=aws_region))
role = get_execution_role()

def create_model(model_name, model_s3_url):
    # Get the DJL DeepSpeed image uri
    image_uri = image_uris.retrieve(
        framework="djl-deepspeed",
        region=sagemaker_session.boto_session.region_name,
        version="0.20.0"
    )
    model = Model(
        image_uri=image_uri,
        model_data=model_s3_url,
        role=role,
        name=model_name,
        sagemaker_session=sagemaker_session,
    )
    return model
```

## Use multi-model endpoints to

deploy with DJL Serving

If you want to deploy multiple models to an endpoint, SageMaker AI offers multi-model endpoints, which are
a scalable and cost-effective solution to deploying large numbers of models. DJL
Serving also supports loading multiple models simultaneously and running inference
on each of the models concurrently. DJL Serving containers adhere to the SageMaker AI multi-model endpoints
contracts and can be used to deploy multi-model endpoints.

Each individual model artifact needs to be packaged in the same way as described
in the previous section [Prepare your model
artifacts](#deploy-models-frameworks-djl-artifacts "#deploy-models-frameworks-djl-artifacts").
You can set model-specific configurations in the `serving.properties` file
and model-specific inference handler code in `model.py`. For a multi-model endpoint, models
need to be arranged in the following way:

````
 root_dir
|-- model_1.tar.gz
|-- model_2.tar.gz
|-- model_3.tar.gz . . . ``` The Amazon SageMaker Python SDK uses the [MultiDataModel](https://sagemaker.readthedocs.io/en/stable/api/inference/multi_data_model.html "https://sagemaker.readthedocs.io/en/stable/api/inference/multi_data_model.html") object to instantiate a multi-model endpoint. The Amazon S3 URI for the root directory should be passed as the `model_data_prefix` argument to the `MultiDataModel` constructor. DJL Serving also provides several configuration parameters to manage model memory requirements, such as `required_memory_mb` and `reserved_memory_mb`, that can be configured for each model in the [serving.properties](https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md#servingproperties "https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md#servingproperties") file. These parameters are useful to handle out of memory errors more gracefully. For all of the configurable parameters, see [OutofMemory handling in djl-serving](https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/out_of_memory_management.md "https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/out_of_memory_management.md"). The auto scaling feature of DJL Serving makes it easy to ensure that the models are scaled appropriately for incoming traffic. By default, DJL Serving determines the maximum number of workers for a model that can be supported based on the hardware available (such as CPU cores or GPU devices). You can set lower and upper bounds for each model to ensure that a minimum traffic level can always be served, and that a single model does not consume all available resources. You can set the following properties in the [serving.properties](https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md#servingproperties "https://github.com/deepjavalibrary/djl-serving/blob/master/serving/docs/modes.md#servingproperties") file: <br>• `gpu.minWorkers`: Minimum number of workers for GPUs. <br>• `gpu.maxWorkers`: Maximum number of workers for GPUs. <br>• `cpu.minWorkers`: Minimum number of workers for CPUs. <br>• `cpu.maxWorkers`: Maximum number of workers for CPUs. For an end-to-end example of how to deploy a multi-model endpoint on SageMaker AI using a DJL Serving container, see the example notebook [Multi-Model-Inference-Demo.ipynb](https://github.com/deepjavalibrary/djl-demo/blob/master/aws/sagemaker/Multi-Model-Inference-Demo.ipynb "https://github.com/deepjavalibrary/djl-demo/blob/master/aws/sagemaker/Multi-Model-Inference-Demo.ipynb").
````
