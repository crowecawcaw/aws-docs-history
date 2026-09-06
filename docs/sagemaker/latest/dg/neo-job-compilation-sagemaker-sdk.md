# Compile a Model (Amazon SageMaker AI SDK)

You can use the [`compile_model`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") API in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") to
compile a trained model and optimize it for specific target hardware. The API should be
invoked on the estimator object used during model training.

###### Note

You must set `MMS_DEFAULT_RESPONSE_TIMEOUT`
environment variable to `500` when compiling the model with MXNet
or PyTorch. The environment variable is not needed for TensorFlow.

The following is an example of how you can
compile a model using the `trained_model_estimator` object:

```
# Neo compilation in V3 uses ModelBuilder.optimize() with compilation_config
from sagemaker.serve import ModelBuilder

# Replace the value of expected_trained_model_input below and
# specify the name & shape of the expected inputs for your trained model
# in json dictionary form
expected_trained_model_input = {'data':[1, 784]}

# Replace the example target_instance_family below to your preferred target_instance_family
model_builder = ModelBuilder(
    model=trained_model,
    role_arn=role,
    instance_type='ml.c5.xlarge',
)
optimized_model = model_builder.optimize(
    instance_type='ml.c5.xlarge',
    output_path='insert s3 output path',
    compilation_config={
        'OverrideEnvironment': {
            'OPTION_TARGET_INSTANCE_FAMILY': 'ml_c5',
            'MMS_DEFAULT_RESPONSE_TIMEOUT': '500',
        },
    },
)
```

The code compiles the model, saves the optimized model at `output_path`,
and creates a SageMaker AI model that can be deployed to an endpoint.
