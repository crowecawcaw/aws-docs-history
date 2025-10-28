# Uncompressed model output

SageMaker AI stores your model in `/opt/ml/model` and your data in
`/opt/ml/output/data`. After the model and data are written to those locations,
they're uploaded to your Amazon S3 bucket as compressed files by default.

You can save time on large data file compression by uploading model and data outputs to
your S3 bucket as uncompressed files. To do this, create a training job in uncompressed upload
mode by using either the AWS Command Line Interface (AWS CLI) or the SageMaker Python SDK.

The following code example shows how to create a training job in uncompressed upload mode
when using the AWS CLI. To enable uncompressed upload mode, set `CompressionType`
field in the `OutputDataConfig` API to `NONE`.

```
{
   "TrainingJobName": "`uncompressed_model_upload`",
   ...
   "OutputDataConfig": {
      "S3OutputPath": "s3://amzn-s3-demo-bucket`/uncompressed_upload/output`",
      "CompressionType": "NONE"
   },
   ...
}
```

The following code example shows you how to create a training job in uncompressed upload
mode using the SageMaker Python SDK.

```
import sagemaker
from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri="`your-own-image-uri`",
    role=sagemaker.get_execution_role(),
    sagemaker_session=sagemaker.Session(),
    instance_count=1,
    instance_type='`ml.c4.xlarge`',
    disable_output_compression=True
)
```
