# Deploying uncompressed models

When deploying ML models, one option is to archive and compress the model artifacts into a `tar.gz`
format. Although this method works well for small models, compressing a large model artifact with hundreds of
billions of parameters and then decompressing it on an endpoint can take a significant amount of time. For large
model inference, we recommend that you deploy uncompressed ML model. This guide shows how you can deploy
uncompressed ML model.

To deploy uncompressed ML models, upload all model artifacts to Amazon S3 and organize them under a common Amazon S3
prefix. A Amazon S3 prefix is a string of characters at the beginning of an Amazon S3 object key name, separated from the
rest of the name by a delimiter. For more information on Amazon S3 prefix, see [Organizing objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md").

For deploying with SageMaker AI, you must use slash (/) as the delimiter. You have to ensure that only artifacts
associated with your ML model are organized with the prefix. For ML models with a single uncompressed artifact,
the prefix will be identical to the key name. You can check which objects are associated with your prefix with
the AWS CLI:

```
aws s3 ls --recursive s3://`bucket`/`prefix`
```

After uploading the model artifacts to Amazon S3 and organizing them under a common prefix, you can specify their
location as part of the [ModelDataSource](../APIReference/API_ModelDataSource.md "../APIReference/API_ModelDataSource.md") field when you invoke the
[CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md")
request. SageMaker AI will automatically download the uncompressed model artifacts to `/opt/ml/model` for
inference. For more information about the rules that SageMaker AI uses when downloading the artifacts, see [S3ModelDataSource](../APIReference/API_S3ModelDataSource.md "../APIReference/API_S3ModelDataSource.md").

The following code snippet shows how you can invoke the `CreateModel` API when deploying an
uncompressed model. Replace the `italicized user text` with your own information.

```
model_name = "`model-name`"
sagemaker_role = "arn:aws:iam::`123456789012:role/SageMakerExecutionRole`"
container = "`123456789012.dkr.ecr.us-west-2.amazonaws.com/inference-image:latest`"

create_model_response = sagemaker_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    PrimaryContainer = {
        "Image": container,
        "ModelDataSource": {
            "S3DataSource": {
                "S3Uri": "`s3://amzn-s3-demo-bucket/prefix/to/model/data/`",
                "S3DataType": "S3Prefix",
                "CompressionType": "None",
            },
        },
    },
)

```

The aforementioned example assumes that your model artifacts are organized under a common prefix. If instead
your model artifact is a single uncompressed Amazon S3 object, then change `"S3Uri"` to point to the Amazon S3
object, and change `"S3DataType"` to `"S3Object"`.

###### Note

Currently you cannot use `ModelDataSource` with AWS Marketplace, SageMaker AI batch transform, SageMaker Serverless Inference
endpoints, and SageMaker multi-model endpoints.
