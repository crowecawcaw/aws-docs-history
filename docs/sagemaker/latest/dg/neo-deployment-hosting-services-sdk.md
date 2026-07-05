# Deploy a Compiled Model Using SageMaker SDK

You must satisfy the [prerequisites](neo-deployment-hosting-services-prerequisites.md "neo-deployment-hosting-services-prerequisites.md") section if the model was compiled using AWS SDK for Python (Boto3), AWS CLI,
or the Amazon SageMaker AI console. Follow one of the following use cases to deploy a model
compiled with SageMaker Neo based on how you compiled your model.

###### Topics

- [If you compiled your model using the SageMaker SDK](#neo-deployment-hosting-services-sdk-deploy-sm-sdk "#neo-deployment-hosting-services-sdk-deploy-sm-sdk")
- [If you compiled your model using MXNet or PyTorch](#neo-deployment-hosting-services-sdk-deploy-sm-boto3 "#neo-deployment-hosting-services-sdk-deploy-sm-boto3")
- [If you compiled your model using Boto3, SageMaker console, or the CLI for TensorFlow](#neo-deployment-hosting-services-sdk-deploy-sm-boto3-tensorflow "#neo-deployment-hosting-services-sdk-deploy-sm-boto3-tensorflow")

## If you compiled your model using the SageMaker SDK

The [sagemaker.Model](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html?highlight=sagemaker.Model "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html?highlight=sagemaker.Model") object handle for the compiled model supplies the
[deploy()](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html?highlight=sagemaker.Model#sagemaker.model.Model.deploy "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html?highlight=sagemaker.Model#sagemaker.model.Model.deploy") function, which enables you to create an endpoint to serve
inference requests. The function lets you set the number and type of instances that
are used for the endpoint. You must choose an instance for which you have compiled
your model. For example, in the job compiled in [Compile a Model
(Amazon SageMaker SDK)](neo-job-compilation-sagemaker-sdk.md "neo-job-compilation-sagemaker-sdk.md") section, this is `ml_c5`.

```
from sagemaker.serve import ModelBuilder

model_builder = ModelBuilder(
    model=compiled_model,
    role_arn=role,
    instance_type='ml.c5.4xlarge',
)
endpoint = model_builder.build().deploy(
    initial_instance_count=1,
    instance_type='ml.c5.4xlarge'
)

# Print the name of newly created endpoint
print(endpoint.endpoint_name)
```

## If you compiled your model using MXNet or PyTorch

Create and deploy the SageMaker AI model using `ModelBuilder`. Specify
the `s3_model_data_url` parameter as the S3 path to your compiled model
archive, the `role_arn` parameter as your execution role, and the
`instance_type` parameter for your target instance. You must also set
the `MMS_DEFAULT_RESPONSE_TIMEOUT` environment variable to
`500`.

The following example shows how to use these functions to deploy a compiled
model using the SageMaker AI SDK for Python:

```
from sagemaker.serve import ModelBuilder

# V3 uses a unified ModelBuilder approach for all frameworks
model_builder = ModelBuilder(
    s3_model_data_url='insert S3 path of compiled model archive',
    role_arn='AmazonSageMaker-ExecutionRole',
    instance_type='ml.p3.2xlarge',
    env={'MMS_DEFAULT_RESPONSE_TIMEOUT': '500'},
)
endpoint = model_builder.build().deploy(
    initial_instance_count=1,
    instance_type='ml.p3.2xlarge'
)

# Print the name of newly created endpoint
print(endpoint.endpoint_name)
```

###### Note

The `AmazonSageMakerFullAccess` and `AmazonS3ReadOnlyAccess` policies
must be attached to the `AmazonSageMaker-ExecutionRole` IAM
role.

## If you compiled your model using Boto3, SageMaker console, or the CLI for TensorFlow

Construct a model object, then call deploy:

```
from sagemaker.serve import ModelBuilder

model_builder = ModelBuilder(
    s3_model_data_url='S3 path for model file',
    role_arn=role,
    instance_type='ml.c5.xlarge',
)
endpoint = model_builder.build().deploy(
    initial_instance_count=1,
    instance_type='ml.c5.xlarge'
)
```

See [Deploying
directly from model artifacts](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#deploying-directly-from-model-artifacts "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#deploying-directly-from-model-artifacts") for more information.

You can select a Docker image Amazon ECR URI that meets your needs from [this list](neo-deployment-hosting-services-container-images.md "neo-deployment-hosting-services-container-images.md").

For more information on how to construct a `TensorFlowModel` object,
see the [SageMaker SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html").

###### Note

Your first inference request might have high latency if you deploy your model
on a GPU. This is because an optimized compute kernel is made on the first
inference request. We recommend that you make a warm-up file of inference
requests and store that alongside your model file before sending it off to a
TFX. This is known as “warming up” the model.

The following code snippet demonstrates how to produce the warm-up file for image
classification example in the [prerequisites](neo-deployment-hosting-services-prerequisites.md "neo-deployment-hosting-services-prerequisites.md") section:

```
import tensorflow as tf
from tensorflow_serving.apis import classification_pb2
from tensorflow_serving.apis import inference_pb2
from tensorflow_serving.apis import model_pb2
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_log_pb2
from tensorflow_serving.apis import regression_pb2
import numpy as np

with tf.python_io.TFRecordWriter("tf_serving_warmup_requests") as writer:
    img = np.random.uniform(0, 1, size=[224, 224, 3]).astype(np.float32)
    img = np.expand_dims(img, axis=0)
    test_data = np.repeat(img, 1, axis=0)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'compiled_models'
    request.model_spec.signature_name = 'serving_default'
    request.inputs['Placeholder:0'].CopyFrom(tf.compat.v1.make_tensor_proto(test_data, shape=test_data.shape, dtype=tf.float32))
    log = prediction_log_pb2.PredictionLog(
    predict_log=prediction_log_pb2.PredictLog(request=request))
    writer.write(log.SerializeToString())
```

For more information on how to “warm up” your model, see the [TensorFlow TFX
page](https://www.tensorflow.org/tfx/serving/saved_model_warmup "https://www.tensorflow.org/tfx/serving/saved_model_warmup").
