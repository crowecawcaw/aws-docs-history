# Deploy a pre-optimized model

Some models in JumpStart are pre-optimized by SageMaker AI, which means that you can deploy
optimized versions of these models without first creating an inference optimization job.

For the list of models with pre-optimized options, see [Pre-optimized JumpStart models](#pre-optimized-js "#pre-optimized-js").

Use the following procedure to deploy a pre-optimized JumpStart model using
Amazon SageMaker Studio.

###### To deploy a pre-optimized model

1. In Studio, in the navigation menu on the left, choose
   **JumpStart**.
2. On the **All public models** page, choose one of the
   models that are pre-optimized.
3. On the model details page, choose **Deploy**.
4. On the deployment page, some JumpStart models require you to sign an
   end-user license agreement (EULA) before you can proceed. If requested,
   review the license terms in the **License agreement**
   section. If the terms are acceptable for your use case, select the checkbox
   for **I accept the EULA, and read the terms and
   conditions.**

For more information, see [End-user license
agreements](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula"). 5. For **Endpoint name** and **Initial instance
count**, accept the default values or set custom ones. 6. For **Instance type**, keep the default value. Otherwise,
you can't deploy a pre-optimized configuration. 7. Under **Models**, expand the model configuration.
Studio shows a table that provides the pre-optimized configurations
that you can choose from. Each option has metrics for latency and
throughput. Choose the option that best suits your application needs. 8. Choose **Deploy**.
You can deploy a pre-optimized model by using the SageMaker AI Python SDK in your project.
First, you define a `Model` instance by using the
`ModelBuilder` class. Then, you use the
`set_deployment_config()` method to set the pre-optimized
configuration that you want to deploy. Then, you use the `build()` method
to build the model. Finally, you use the `deploy()` method to deploy it
to an inference endpoint.

For more information about the classes and methods used in the following examples,
see [APIs](https://sagemaker.readthedocs.io/en/stable/api/index.html "https://sagemaker.readthedocs.io/en/stable/api/index.html") in the SageMaker AI Python SDK documentation.

###### To set up your project

1. In your application code, import the necessary libraries. The following
   example imports the SDK for Python (Boto3). It also imports the modules from the SageMaker AI
   Python SDK that you use to define and work with models:

```
import boto3
from sagemaker.serve.builder.model_builder import ModelBuilder
from sagemaker.serve.builder.schema_builder import SchemaBuilder
from sagemaker.session import Session
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

###### To retrieve benchmark metrics

1. To determine which pre-optimized configuration you want to deploy, look up
   the options that SageMaker AI provides. The following example displays them:

```
model_builder.display_benchmark_metrics()
```

This `display_benchmark_metrics()` method prints a table like
the following:

```
| Instance Type   | Config Name   |   Concurrent Users |   Latency, TTFT (P50 in sec) |   Throughput (P50 in tokens/sec/user) |
|:----------------|:--------------|-------------------:|-----------------------------:|--------------------------------------:|
| ml.g5.48xlarge  | lmi-optimized |                  1 |                         2.25 |                                 49.70 |
| ml.g5.48xlarge  | lmi-optimized |                  2 |                         2.28 |                                 21.10 |
| ml.g5.48xlarge  | lmi-optimized |                  4 |                         2.37 |                                 14.10 |
. . .
| ml.p4d.24xlarge | lmi-optimized |                  1 |                         0.10 |                                137.40 |
| ml.p4d.24xlarge | lmi-optimized |                  2 |                         0.11 |                                109.20 |
| ml.p4d.24xlarge | lmi-optimized |                  4 |                         0.13 |                                 85.00 |
. . .
```

In the first column, the table lists potential instance types that you can
use to host your chosen JumpStart model. For each instance type, under
`Config Name`, it lists the names of the pre-optimized
configurations. The configurations that SageMaker AI provides are named
`lmi-optimized`. For each instance type and configuration,
the table provides benchmark metrics. These metrics indicate the throughput
and latency that your model will support for different numbers of concurrent
users. 2. Based on the benchmark metrics, pick the instance type and configuration
name that best supports your performance needs. You will use these values
when you create a deployment configuration.

###### To deploy a pre-optimized model

1. Create a deployment configuration. The following example uses a
   `ModelBuilder` instance. It passes an instance type and
   configuration name to the to the `set_deployment_config()`
   method:

```
model_builder.set_deployment_config(
    config_name="``config-name``",
    instance_type="``instance-type``",
)
```

Replace `config-name` with a
configuration name from the table, such as such as
`lmi-optimized`. Replace
`instance-type` with an
instance type from the table, such as `ml.p4d.24xlarge`. 2. Build your model. The following example uses the `.build()`
method of the `ModelBuilder` instance:

```
optimized_model = model_builder.build()
```

The `.build()` method returns a deployable `Model`
instance. 3. Deploy your model to an inference endpoint. The following example uses the
`.deploy()` method of the `Model` instance:

```
predictor = optimized_model.deploy(accept_eula=True)
```

The `deploy()` method returns a `Predictor`
instance, which you can use to send inference requests to the model.

###### To test your model with an inference request

- After you deploy your model to an inference endpoint, test the model's
  predictions. The following example sends an inference request by using the
  `Predictor` instance:

```
predictor.predict(sample_input)
```

The model returns the text that it generates with a response like the
following:

```
{'generated_text': ' Jupiter is the largest planet in the solar system. It is the fifth planet from the sun. It is a gas giant with . . .'}
```

## Pre-optimized JumpStart models

The following are the JumpStart models that have pre-optimized
configurations.

###### Meta

- Llama 3.1 70B Instruct
- Llama 3.1 70B
- Llama 3.1 405B Instruct FP8
- Llama 3.1 405B FP8
- Llama 3 8B Instruct
- Llama 3 8B
- Llama 3 70B Instruct
- Llama 3 70B
- Llama 2 70B Chat
- Llama 2 7B Chat
- Llama 2 13B Chat

###### HuggingFace

- Mixtral 8x7B Instruct
- Mixtral 8x7B
- Mistral 7B Instruct
- Mistral 7B

### Pre-compiled JumpStart models

For some models and configurations, SageMaker AI provides models that are pre-compiled for
specific AWS Inferentia and AWS Trainium instances. For these, if you create a
compilation optimization job, and you choose ml.inf2.48xlarge or ml.trn1.32xlarge as
the deployment instance type, SageMaker AI fetches the compiled artifacts. Because the job
uses a model that’s already compiled, it completes quickly without running the
compilation from scratch.

The following are the JumpStart models for which SageMaker AI has pre-compiled
models:

###### Meta

- Llama3 8B
- Llama3 70B
- Llama2 7B
- Llama2 70B
- Llama2 13B
- Code Llama 7B
- Code Llama 70B

###### HuggingFace

- Mistral 7B
