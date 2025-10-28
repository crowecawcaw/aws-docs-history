# Deploy MLflow models with `ModelBuilder`

You can deploy MLflow models to a SageMaker AI endpoint using Amazon SageMaker AI Model
Builder. For more information about Amazon SageMaker AI Model Builder, see [Create a model in Amazon SageMaker AI with ModelBuilder](how-it-works-modelbuilder-creation.md "how-it-works-modelbuilder-creation.md").

`ModelBuilder` is a Python class that takes a framework model or a
user-specified inference specification and converts it to a deployable model. For more
details about the `ModelBuilder` class, see [ModelBuilder](https://sagemaker.readthedocs.io/en/stable/api/inference/model_builder.html#sagemaker.serve.builder.model_builder.ModelBuilder "https://sagemaker.readthedocs.io/en/stable/api/inference/model_builder.html#sagemaker.serve.builder.model_builder.ModelBuilder").

To deploy your MLflow model using `ModelBuilder`, provide a path to your MLflow
artifacts in the `model_metadata["MLFLOW_MODEL_PATH"]` attribute. Read on for more
information about valid model path input formats:

###### Note

If you provide your model artifact path in the form of an MLflow run ID or MLflow model registry path, then you must also specify
your tracking server ARN through the `model_metadata["MLFLOW_TRACKING_ARN"]` attribute.

- [Model paths that require an ARN in the model_metadata](#mlflow-track-experiments-model-deployment-with-arn "#mlflow-track-experiments-model-deployment-with-arn")
- [Model paths that do not require an ARN in the model_metadata](#mlflow-track-experiments-model-deployment-without-arn "#mlflow-track-experiments-model-deployment-without-arn")

## Model paths that require an ARN in the `model_metadata`

The following model paths do require that you specify an ARN in the `model_metadata` for deployment:

- MLflow [run ID](https://mlflow.org/docs/latest/python_api/mlflow.entities.html?highlight=mlflow%20info#mlflow.entities.RunInfo.run_id "https://mlflow.org/docs/latest/python_api/mlflow.entities.html?highlight=mlflow%20info#mlflow.entities.RunInfo.run_id"):
  `runs:/aloy-run-id/run-relative/path/to/model`
- MLflow [model registry path](https://mlflow.org/docs/latest/model-registry.html#find-registered-models "https://mlflow.org/docs/latest/model-registry.html#find-registered-models"):
  `models:/model-name/model-version`

## Model paths that do not require an ARN in the `model_metadata`

The following model paths do not require that you specify an ARN in the `model_metadata` for deployment:

- Local model path: `/Users/me/path/to/local/model`
- Amazon S3 model path: `s3://amzn-s3-demo-bucket/path/to/model`
- Model package ARN:
  `arn:aws:sagemaker:region:account-id:mlflow-tracking-server/tracking-server-name`

For more information on how MLflow model deployment works with Amazon SageMaker AI, see [Deploy MLflow
Model to Amazon SageMaker AI](https://mlflow.org/docs/latest/deployment/deploy-model-to-sagemaker.html "https://mlflow.org/docs/latest/deployment/deploy-model-to-sagemaker.html") in the MLflow documentation.

If using an Amazon S3 path, you can find the path of your registered model with the following commands:

```
registered_model = client.get_registered_model(name=`'AutoRegisteredModel'`)
source_path = registered_model.latest_versions[0].source
```

The following sample is an overview of how to deploy your MLflow model using
`ModelBuilder` and an MLflow model registry path. Because this sample provides
the model artifact path in the form of an MLflow model registry path, the call to
`ModelBuilder` must also specify a tracking server ARN through the
`model_metadata["MLFLOW_TRACKING_ARN"]` attribute.

###### Important

You must use version [2.224.0](https://pypi.org/project/sagemaker/2.224.0/ "https://pypi.org/project/sagemaker/2.224.0/")
or later of the SageMaker Python SDK to use `ModelBuilder`.

###### Note

Use the following code example for reference. For end-to-end examples that show you how to
deploy registered MLflow models, see [MLflow tutorials using example Jupyter notebooks](mlflow-tutorials.md "mlflow-tutorials.md").

```
from sagemaker.serve import ModelBuilder
from sagemaker.serve.mode.function_pointers import Mode
from sagemaker.serve import SchemaBuilder

my_schema = SchemaBuilder(
    sample_input=`sample_input`,
    sample_output=`sample_output`
)

model_builder = ModelBuilder(
    mode=Mode.SAGEMAKER_ENDPOINT,
    schema_builder=my_schema,
    role_arn="`Your-service-role-ARN`",
    model_metadata={
        # both model path and tracking server ARN are required if you use an mlflow run ID or mlflow model registry path as input
        "MLFLOW_MODEL_PATH": "`models:/sklearn-model/1`"
        "MLFLOW_TRACKING_ARN": "`arn:aws:sagemaker:region:account-id:mlflow-tracking-server/tracking-server-name`"
    }
)
model = model_builder.build()
predictor = model.deploy( initial_instance_count=`1`, instance_type="`ml.c6i.xlarge`" )
```

To maintain [lineage
tracking](lineage-tracking.md "lineage-tracking.md") for MLflow models deployed using `ModelBuilder`, you must have
the following IAM permissions:

- `sagemaker:CreateArtifact`
- `sagemaker:ListArtifacts`
- `sagemaker:AddAssociation`
- `sagemaker:DescribeMLflowTrackingServer`

###### Important

Lineage tracking is optional. Deployment succeeds without the permissions related to
lineage tracking. If you do not have the permissions configured, you will see a lineage
tracking permissions error when calling `model.deploy()`. However, the endpoint
deployment still succeeds and you can directly interact with your model endpoint. If the
permissions above are configured, lineage tracking information is automatically created and
stored.

For more information and end-to-end examples, see [MLflow tutorials using example Jupyter notebooks](mlflow-tutorials.md "mlflow-tutorials.md").
