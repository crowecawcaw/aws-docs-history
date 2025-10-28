# Create an inference optimization job

You can create an inference optimization job by using Studio or the SageMaker AI Python SDK.
The job optimizes your model by applying the techniques that you choose. For more
information, see [Optimization techniques](model-optimize.md#optimization-techniques "model-optimize.md#optimization-techniques").

###### Instance pricing for inference optimization jobs

When you create a inference optimization job that applies quantization or compilation,
SageMaker AI chooses which instance type to use to run the job. You are charged based on the
instance used.

For the possible instance types and their pricing details, see the inference
optimization pricing information on the [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") page.

You incur no additional costs for jobs that apply speculative decoding.

For the supported models that you can optimize, see [Supported models reference](optimization-supported-models.md "optimization-supported-models.md").

Complete the following steps to create an inference optimization job in
Studio.

###### To begin creating an optimization job

1. In SageMaker AI Studio, create an optimization job through any of the
   following paths:
   - To create a job for a JumpStart model, do the
     following:
     1. In the navigation menu, choose
        **JumpStart**.
     2. On the **All public models** page, choose
        a model provider, and then choose one of the models that
        supports optimization.
     3. On the model details page, choose
        **Optimize**. This button is enabled
        only for models that support optimization.
     4. On the **Create inference optimization
        job** page, some JumpStart models require
        you to sign an end-user license agreement (EULA) before you
        can proceed. If requested, review the license terms in the
        **License agreement** section. If the
        terms are acceptable for your use case, select the checkbox
        for **I accept the EULA, and read the terms and
        conditions.**

   - To create a job for a fine-tuned JumpStart model, do the
     following:
     1. In the navigation menu, under **Jobs**,
        choose **Training**.
     2. On the **Training Jobs** page, choose the
        name of a job that you used to fine tune a JumpStart
        model. These jobs have the type **JumpStart
        training** in the **Job type**
        column.
     3. On the details page for the training job, choose
        **Optimize**.

   - To create a job for a custom model, do the following:
     1. In the navigation menu, under **Jobs**,
        choose **Inference optimization**.
     2. Choose **Create new job**.
     3. On the **Create inference optimization
        job** page, choose **Add
        model**.
     4. In the **Add model** window, choose
        **Custom Model**.
     5. For **Custom model name**, enter a
        name.
     6. For **S3 URI**, enter the URI for the
        location in Amazon S3 where you've stored your model
        artifacts.

2. On the **Create inference optimization job** page, for
   **Job name**, you can accept the default name that SageMaker AI
   assigns. Or, to enter a custom job name, choose the **Job
   name** field, and choose **Enter job
   name**.

###### To set the optimization configurations

1. For **Deployment instance type**, choose the instance
   type that you want to optimize the model for.

The instance type affects what optimization techniques you can choose. For
most types that use GPU hardware, the supported techniques are
**Quantization** and **Speculative
decoding**. If you choose an instance that uses custom silicon,
like the AWS Inferentia instance ml.inf2.8xlarge, the supported technique
is **Compilation**, which you can use to compile the model
for that specific hardware type. 2. Select one or more of the optimization techniques that Studio
provides:

    * If you select **Quantization**, choose a data
     type for **Precision data type**.
    * If you select **Speculative decoding**, choose
     one of the following options:




    	+ **Use SageMaker AI draft model** – Choose
    	 to use the draft model that SageMaker AI provides.


    	###### Note

    	If you choose to use the SageMaker AI draft model, you must
    	 also enable network isolation. Studio provides this
    	 option under **Security**.
    	+ **Choose JumpStart draft model**
    	 – Choose to select a model from the JumpStart
    	 catalog to use as your draft model.
    	+ **Choose your own draft model** –
    	 Choose to use your own draft model, and provide the S3 URI
    	 that locates it.
    * If you choose **Fast model loading**, Studio
     shows the `OPTION_TENSOR_PARALLEL_DEGREE` environment
     variable. Use the **Value** field to set the degree
     of tensor parallelism. The value must evenly divide the number of
     GPUs in the instance you chose for **Deployment instance
     type**. For example, to shard your model while using an
     instance with 8 GPUs, use the values 2, 4, or 8.
    * If you set **Deployment instance type** to an
     AWS Inferentia or AWS Trainium instance, Studio might show
     that **Compilation** is the one supported option.
     In that case, Studio selects this option for you.

3. For **Output**, enter the URI of a location in Amazon S3.
   There, SageMaker AI stores the artifacts of the optimized model that your job
   creates.
4. (Optional) Expand **Advanced options** for more
   fine-grained control over settings such as the IAM role, VPC, and
   environment variables. For more information, see _Advanced options_ below.
5. When you're finished configuring the job, choose **Create
   job**.

Studio shows the job details page, which shows the job status and all
of its settings.

### Advanced options

You can set the following advanced options when you create an inference
optimization job.

Under **Configurations**, you can set the following
options:

**Tensor parallel degree**

A value for the degree of _tensor
parallelism_. Tensor parallelism is a type of model
parallelism in which specific model weights, gradients, and
optimizer states are split across devices. The value must evenly
divide the number of GPUs in your cluster.

**Maximum token length**

The limit for the number of tokens to be generated by the model.
Note that the model might not always generate the maximum number of
tokens.

**Concurrency**

The ability to run multiple instances of a model on the same
underlying hardware. Use concurrency to serve predictions to
multiple users and to maximize hardware
utilization.

**Batch size**

If your model does _batch
inferencing_, use this option to control the size of
the batches that your model processes.

Batch inferencing generates model predictions on a batch of
observations. It's a good option for large datasets or if you don't
need an immediate response to an inference request.

Under **Security**, you can set the following options:

**IAM Role**

An IAM role that enables SageMaker AI to perform tasks on your behalf.
During model optimization, SageMaker AI needs your permission to:

- Read input data from an S3 bucket
- Write model artifacts to an S3 bucket
- Write logs to Amazon CloudWatch Logs
- Publish metrics to Amazon CloudWatch

You grant permissions for all of these tasks to an IAM
role.

For more information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

**Encryption KMS key**

A key in AWS Key Management Service (AWS KMS). SageMaker AI uses they key to encrypt the
artifacts of the optimized model when SageMaker AI uploads the model to
Amazon S3.

**VPC**

SageMaker AI uses this information to create network interfaces and attach
them to your model containers. The network interfaces provide your
model containers with a network connection within your VPC that is
not connected to the internet. They also enable your model to
connect to resources in your private VPC.

For more information, see [Give SageMaker AI Hosted Endpoints Access to Resources in Your
Amazon VPC](host-vpc.md "host-vpc.md").

**Enable network isolation**

Activate this option if you want to restrict your container's
internet access. Containers that run with network isolation can’t
make any outbound network calls.

###### Note

You must activate this option when you optimize with
speculative decoding and you use the SageMaker AI draft model.

For more information about network isolation, see [Network Isolation](mkt-algo-model-internet-free.md#mkt-algo-model-internet-free-isolation "mkt-algo-model-internet-free.md#mkt-algo-model-internet-free-isolation").

Under **Advanced container definition**, you can set the
following options:

**Stopping condition**

Specifies a limit to how long a job can run. When the job reaches
the time limit, SageMaker AI ends the job. Use this option to cap
costs.

**Tags**

Key-value pairs associated with the optimization job.

For more information about tags, see [Tagging your
AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the _AWS General Reference_.

**Environment variables**

Key-value pairs that define the environment variables to set in
the model container.

You can create an inference optimization job by using the SageMaker AI Python SDK in your
project. First, you define a `Model` instance by using the
`ModelBuilder` class. Then, you use the `optimize()`
method to run a job that optimizes your model with quantization, speculative
decoding, or compilation. When the job completes, you deploy the model to an
inference endpoint by using the `deploy()` method.

For more information about the classes and methods used in the following examples,
see [APIs](https://sagemaker.readthedocs.io/en/stable/api/index.html "https://sagemaker.readthedocs.io/en/stable/api/index.html") in the SageMaker AI Python SDK documentation.

###### To set up your project

1. In your application code, import the necessary libraries. The following
   example imports the SDK for Python (Boto3). It also imports the classes from the SageMaker AI
   Python SDK that you use to define and work with models:

```
import boto3
from sagemaker.serve.builder.model_builder import ModelBuilder
from sagemaker.serve.builder.schema_builder import SchemaBuilder
from sagemaker.session import Session
from pathlib import Path
```

2. Initialize a SageMaker AI session. The following example uses the
   `Session()` class:

```
sagemaker_session = Session()
```

###### To define your model

1. Create a `SchemaBuilder` instance, and provide input and output
   samples. You supply this instance to the `ModelBuilder` class
   when you define a model. With it, SageMaker AI automatically generates the
   marshalling functions for serializing and deserializing the input and
   output.

For more information about using the `SchemaBuilder` and
`ModelBuilder` classes, see [Create a model in Amazon SageMaker AI with
ModelBuilder](how-it-works-modelbuilder-creation.md "how-it-works-modelbuilder-creation.md").

The following example provides sample input and output strings to the
`SchemaBuilder` class:

```
response = "Jupiter is the largest planet in the solar system. It is the fifth planet from the sun."
sample_input = {
    "inputs": "What is the largest planet in the solar system?",
    "parameters": {"max_new_tokens": 128, "top_p": 0.9, "temperature": 0.6},
}
sample_output = [{"generated_text": response}]
schema_builder = SchemaBuilder(sample_input, sample_output)
```

2. Define your model to SageMaker AI. The following example sets the parameters to
   initialize a `ModelBuilder` instance:

```
model_builder = ModelBuilder(
    model="`jumpstart-model-id`",
    schema_builder=schema_builder,
    sagemaker_session=sagemaker_session,
    role_arn=sagemaker_session.get_caller_identity_arn(),
)
```

This example uses a JumpStart model. Replace
`jumpstart-model-id` with the
ID of a JumpStart model, such as
`meta-textgeneration-llama-3-70b`.

###### Note

If you want to optimize with speculative decoding, and you want to use
the SageMaker AI draft, you must enable network isolation. To enable it, include
the following argument when you initialize a `ModelBuilder`
instance:

```
enable_network_isolation=True,
```

For more information about network isolation, see [Network Isolation](mkt-algo-model-internet-free.md#mkt-algo-model-internet-free-isolation "mkt-algo-model-internet-free.md#mkt-algo-model-internet-free-isolation").

###### To optimize with quantization

1. To run a quantization job, use the `optimize()` method, and set
   the `quantization_config` argument. The following example sets
   `OPTION_QUANTIZE` as an environment variable in the
   optimization container:

```
optimized_model = model_builder.optimize(
    instance_type="`instance-type`",
    accept_eula=True,
    quantization_config={
        "OverrideEnvironment": {
            "OPTION_QUANTIZE": "awq",
        },
    },
    output_path="`s3://output-path`",
)
```

In this example, replace
`instance-type` with an ML
instance, such as `ml.p4d.24xlarge`. Replace
`s3://output-path` with the
path to the S3 location where you store the optimized model that the job
creates.

The `optimize()` method returns a `Model` object,
which you can use to deploy your model to an endpoint. 2. When the job completes, deploy the model. The following example uses the
`deploy()` method:

```
predictor = optimized_model.deploy(
    instance_type="`instance-type`",
    accept_eula=True,
)
```

In this example, replace
`instance-type` with an ML
instance, such as `ml.p4d.24xlarge`.

The `deploy()` method returns a predictor object, which you can
use to send inference requests to the endpoint that hosts the model.

###### To optimize with speculative decoding using the SageMaker AI draft model

When you optimize your model with speculative decoding, you can choose to use
a draft model that SageMaker AI provides, or you can use your own. The following
examples use the SageMaker AI draft model.

###### Prerequisite

To optimize with speculative decoding and the SageMaker AI draft model, you must
enable network isolation when you define your model.

1. To run a speculative decoding job, use the `optimize()` method,
   and set the `speculative_decoding_config` argument. The following
   example sets the `ModelProvider` key to `SAGEMAKER` to
   use the draft model that SageMaker AI provides.

```
optimized_model = model_builder.optimize(
    instance_type="`instance-type`",
    accept_eula=True,
    speculative_decoding_config={
        "ModelProvider": "SAGEMAKER",
    },
)
```

In this example, replace
`instance-type` with an ML
instance, such as `ml.p4d.24xlarge`.

The `optimize()` method returns a `Model` object,
which you can use to deploy your model to an endpoint. 2. When the job completes, deploy the model. The following example uses the
`deploy()` method:

```
predictor = optimized_model.deploy(accept_eula=True)
```

The `deploy()` method returns a predictor object, which you can
use to send inference requests to the endpoint that hosts the model.

###### To optimize with speculative decoding using a custom draft model

Before you can provide your custom draft model to SageMaker AI, you must first upload
the model artifacts to Amazon S3.

The following examples demonstrate one possible way to provide a custom draft
model. The examples download the draft model from the Hugging Face Hub, upload
it to Amazon S3, and provide the S3 URI to the
`speculative_decoding_config` argument.

1. If you want to download a model from the Hugging Face Hub, add the
   `huggingface_hub` library to your project, and download a
   model with the `snapshot_download()` method. The following
   example downloads a model to a local directory:

```
import huggingface_hub

huggingface_hub.snapshot_download(
    repo_id="`model-id`",
    revision="main",
    local_dir=`download-dir`,
    token=`hf-access-token`,
)
```

In this example, replace `model-id`
with the ID of a model the Hugging Face Hub, such as
`meta-llama/Meta-Llama-3-8B`. Replace
`download-dir` with a local
directory. Replace `hf-access-token`
with your user access token. To learn how to get your access token, see
[User
access tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens") in the Hugging Face documentation.

For more information about the `huggingface_hub` library, see
[Hub
client library](https://huggingface.co/docs/huggingface_hub/en/index "https://huggingface.co/docs/huggingface_hub/en/index") in the Hugging Face documentation. 2. To make your downloaded model available to SageMaker AI, upload it to Amazon S3. The
following example uploads the model with the `sagemaker_session`
object:

```
custom_draft_model_uri = sagemaker_session.upload_data(
    path=hf_local_download_dir.as_posix(),
    bucket=sagemaker_session.default_bucket(),
    key_prefix="`prefix`",
)
```

In this example, replace `prefix`
with a qualifier that helps you distinguish the draft model in S3, such as
`spec-dec-custom-draft-model`.

The `upload_data()` method returns the S3 URI for the model
artifacts. 3. To run a speculative decoding job, use the `optimize()` method,
and set the `speculative_decoding_config` argument. The following
example sets the `ModelSource` key to the S3 URI of the custom
draft model:

```
optimized_model = model_builder.optimize(
    instance_type="`instance-type`",
    accept_eula=True,
    speculative_decoding_config={
        "ModelSource": custom_draft_model_uri + "/",
    },
)
```

In this example, replace
`instance-type` with an ML
instance, such as `ml.p4d.24xlarge`.

The `optimize()` method returns a `Model` object,
which you can use to deploy your model to an endpoint. 4. When the job completes, deploy the model. The following example uses the
`deploy()` method:

```
predictor = optimized_model.deploy(accept_eula=True)
```

The `deploy()` method returns a predictor object, which you can
use to send inference requests to the endpoint that hosts the model.

###### To optimize with compilation

1. To run a compilation job, use the `optimize()` method, and set
   the `compilation_config` argument. The following example uses the
   `OverrideEnvironment` key to set the necessary environment
   variables in the optimization container:

```
optimized_model = model_builder.optimize(
    instance_type="`instance-type`",
    accept_eula=True,
    compilation_config={
        "OverrideEnvironment": {
            "OPTION_TENSOR_PARALLEL_DEGREE": "24",
            "OPTION_N_POSITIONS": "8192",
            "OPTION_DTYPE": "fp16",
            "OPTION_ROLLING_BATCH": "auto",
            "OPTION_MAX_ROLLING_BATCH_SIZE": "4",
            "OPTION_NEURON_OPTIMIZE_LEVEL": "2",
        }
    },
    output_path="`s3://output-path`",
)
```

In this example, set `instance-type`
to an ML instance type with accelerated hardware. For example, for
accelerated inference with AWS Inferentia, you could set the type to an
Inf2 instance, such as `ml.inf2.48xlarge`. Replace
`s3://output-path` with the
path to the S3 location where you store the optimized model that the job
creates. 2. When the job completes, deploy the model. The following example uses the
`deploy()` method:

```
predictor = optimized_model.deploy(accept_eula=True)
```

The `deploy()` method returns a predictor object, which you can
use to send inference requests to the endpoint that hosts the model.

###### To test your model with an inference request

- To send a test inference request to your deployed model, use the
  `predict()` method of a predictor object. The following
  example passes the `sample_input` variable that was also passed
  to the `SchemaBuilder` class in the examples to define your
  model:

```
predictor.predict(sample_input)
```

The sample input has the prompt, `"What is the largest planet in the
 solar system?"`. The `predict()` method returns the
response that the model generated, as shown by the following example:

```
{'generated_text': ' Jupiter is the largest planet in the solar system. It is the fifth planet from the sun. It is a gas giant with . . .'}
```

## Limitations of the SageMaker AI draft model

For any model that you optimize with the SageMaker AI draft model, be aware of the
requirements, restrictions, and supported environment variables.

###### Requirements

You must do the following:

- Use a model that's provided by SageMaker JumpStart.
- Enable network isolation for the model deployment.
- If you deploy the model to a Large Model Inference (LMI) container, use a
  DJLServing container at version 0.28.0 or above.

For the available containers, see [Large Model Inference Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#large-model-inference-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#large-model-inference-containers") in the Deep Learning Containers
GitHub repository.

- If you fine tune the JumpStart model, use the safetensors format for the
  model weights.

For more information about this format, see [Safetensors](https://huggingface.co/docs/safetensors/en/index "https://huggingface.co/docs/safetensors/en/index")
in the Hugging Face documentation.

###### Restrictions

You can't do the following:

- Use the model in local test environments that you create with local mode.

For more information about local mode, see [Local Mode](https://sagemaker.readthedocs.io/en/stable/overview.html#local-mode "https://sagemaker.readthedocs.io/en/stable/overview.html#local-mode") in the SageMaker AI Python SDK documentation.

- Access the model container through the AWS Systems Manager Agent (SSM Agent). The SSM
  Agent provides shell-level access to your model container so that you can debug
  processes and log commands with Amazon CloudWatch.

For more information about this feature, see [Access containers through SSM](ssm-access.md "ssm-access.md").

- Configure the model container for a core dump that occurs if the process
  crashes.

For more information about core dumps from model containers, see [ProductionVariantCoreDumpConfig](sagemaker/latest/APIReference/API_ProductionVariantCoreDumpConfig.md "sagemaker/latest/APIReference/API_ProductionVariantCoreDumpConfig.md").

- Deploy the model to multi-model endpoints, multi-container endpoints, or
  endpoints that host inference components.

For more information about these endpoint types, see [Multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md"),
[Multi-container endpoints](multi-container-endpoints.md "multi-container-endpoints.md"), and [Inference components](realtime-endpoints-deploy-models.md#inference-components "realtime-endpoints-deploy-models.md#inference-components").

- Create a model package for the model. You use model packages to create
  deployable models that you publish on AWS Marketplace.

For more information about this feature, see [Create a Model Package
Resource](sagemaker-mkt-create-model-package.md "sagemaker-mkt-create-model-package.md").

- Use your own inference code in the model container.
- Use a `requirements.txt` file in the model container. This type of
  file lists package dependencies.
- Enable the Hugging Face parameter `trust_remote_code`.

###### Supported environment variables

You can configure the container only with the following environment
variables:

- Common environment variables for large model inference (LMI) containers.

For more information about these variables, see [Environment Variable Configurations](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/configurations.html#environment-variable-configurations "https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/configurations.html#environment-variable-configurations") in the LMI container
documentation.

- Common environment variables for packages that the Hugging Face Hub provides
  in its Git repositories.

For the repositories, see [Hugging
Face](https://github.com/huggingface "https://github.com/huggingface") on GitHub.

- Common PyTorch & CUDA environment variables.

For more information about these variables, see [Torch
Environment Variables](https://pytorch.org/docs/stable/torch_environment_variables.html "https://pytorch.org/docs/stable/torch_environment_variables.html") in the PyTorch documentation.
