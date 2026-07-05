# Deploy the model to Amazon EC2

To get predictions, deploy your model to Amazon EC2 using Amazon SageMaker AI.

###### Topics

- [Deploy the Model to SageMaker AI Hosting Services](#ex1-deploy-model "#ex1-deploy-model")
- [(Optional) Reuse or Invoke an Existing Endpoint](#ex1-deploy-model-sdk-use-endpoint "#ex1-deploy-model-sdk-use-endpoint")
- [(Optional) Make Prediction with Batch Transform](#ex1-batch-transform "#ex1-batch-transform")

## Deploy the Model to SageMaker AI Hosting Services

To host a model through Amazon EC2 using Amazon SageMaker AI, deploy the model that you trained in
[Create and Run a Training Job](ex1-train-model.md#ex1-train-model-sdk "ex1-train-model.md#ex1-train-model-sdk").

Use the `ModelBuilder` class to build and deploy your model.
`ModelBuilder` supports resource chaining,
so you can pass the trained `ModelTrainer` directly to build and deploy your model.

```
from sagemaker.serve import ModelBuilder

# Build and deploy using resource chaining from the trained model
model_builder = ModelBuilder(
    model=xgb_model_trainer,
    role_arn=role,
    instance_type='ml.t2.medium'
)

# Build creates a SageMaker Model resource
model = model_builder.build()

# Deploy creates a SageMaker Endpoint resource
endpoint = model_builder.deploy(endpoint_name="xgboost-endpoint")
```

- `model` – The trained `ModelTrainer` object.
  `ModelBuilder` automatically chains the training output to
  deployment.
- `instance_type` (str) – The type of instances that you
  want to operate your deployed model.

The `build()` method creates a SageMaker AI Model resource, and
`deploy()` creates a SageMaker AI Endpoint resource. For more
information, see the [SageMaker AI ModelBuilder](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
To retrieve the name of the endpoint, run
the following code:

```
endpoint.endpoint_name
```

This endpoint stays active in the ML instance, and you can make instantaneous
predictions at any time unless you shut it down later. Copy this endpoint name and
save it to reuse and make real-time predictions elsewhere in SageMaker Studio or SageMaker AI
notebook instances.

###### Tip

To learn more about compiling and optimizing your model for deployment to
Amazon EC2 instances or edge devices, see [Compile and Deploy Models with
Neo](neo.md "neo.md").

## (Optional) Reuse or Invoke an Existing Endpoint

After you deploy the model to an endpoint, you can invoke it from any other notebook
or application using the `Endpoint` class from sagemaker-core.
The following example code shows how to get an existing endpoint and make predictions.
Re-use the endpoint name from the deployment step above.

```
from sagemaker.core.resources import Endpoint

endpoint = Endpoint.get(endpoint_name="`xgboost-endpoint`")

# Make a prediction
response = endpoint.invoke(
    body=test_data,
    content_type="text/csv"
)
result = response.body.read().decode('utf-8')
```

## (Optional) Make Prediction with Batch Transform

Instead of hosting an endpoint in production, you can run a one-time batch inference
job to make predictions on a test dataset using the SageMaker AI batch transform. After your
model training has completed, you can use the batch transformer to read input
data from a specified S3 bucket and make predictions.

###### To run a batch transform job

1. Run the following code to convert the feature columns of the test dataset to a CSV
   file and uploads to the S3 bucket:

```
X_test.to_csv('test.csv', index=False, header=False)

boto3.Session().resource('s3').Bucket(bucket).Object(
os.path.join(prefix, 'test/test.csv')).upload_file('test.csv')
```

2. Specify S3 bucket URIs of input and output for the batch transform job as shown
   following:

```
# The location of the test dataset
batch_input = 's3://{}/{}/test'.format(bucket, prefix)

# The location to store the results of the batch transform job
batch_output = 's3://{}/{}/batch-prediction'.format(bucket, prefix)
```

3. Create and run a batch transform job.

```
# Build a model from the trained ModelTrainer
model_builder = ModelBuilder(model=xgb_model_trainer, role_arn=role)
model = model_builder.build(model_name="xgboost-batch-model")

# Create and run the batch transform job
from sagemaker.core.resources import TransformJob

transform_job = TransformJob.create(
    model_name=model.model_name,
    transform_input={
        "data_source": {
            "s3_data_source": {
                "s3_data_type": "S3Prefix",
                "s3_uri": batch_input
            }
        },
        "content_type": "text/csv",
        "split_type": "Line"
    },
    transform_output={
        "s3_output_path": batch_output
    },
    transform_resources={
        "instance_type": "ml.m4.xlarge",
        "instance_count": 1
    }
)

transform_job.wait()
```

4. When the batch transform job is complete, SageMaker AI creates the `test.csv.out`
   prediction data saved in the `batch_output` path, which should be in
   the following format:
   `s3://sagemaker-<region>-111122223333/demo-sagemaker-xgboost-adult-income-prediction/batch-prediction`.
   Run the following AWS CLI to download the output data of the batch transform
   job:

```
! aws s3 cp {batch_output} ./ --recursive
```

This should create the `test.csv.out` file under the current
working directory. You'll be able to see the float values that are predicted
based on the logistic regression of the XGBoost training job.
