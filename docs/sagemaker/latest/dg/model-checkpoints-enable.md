

# Enable checkpointing
<a name="model-checkpoints-enable"></a>

After you enable checkpointing, SageMaker AI saves checkpoints to Amazon S3 and syncs your training job with the checkpoint S3 bucket. You can use either S3 general purpose or S3 directory buckets for your checkpoint S3 bucket. 

![Architecture diagram of writing checkpoints during training.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/checkpoints_write.png)


The following example shows how to configure checkpoint paths when you construct a SageMaker AI training object. 

To enable checkpointing, add the `checkpoint_config` parameter to your `ModelTrainer`. The following example template shows how to create a SageMaker AI `ModelTrainer` and enable checkpointing. You can use this template for any supported algorithm by specifying the `training_image` parameter. To find Docker image URIs for algorithms with checkpointing supported by SageMaker AI, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths). In V3, the unified `ModelTrainer` class replaces all framework-specific estimator classes (TensorFlow, PyTorch, HuggingFace, XGBoost, etc.).

```
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import Compute, CheckpointConfig
from sagemaker.core.helper.session_helper import Session

bucket = Session().default_bucket()
base_job_name = "{{sagemaker-checkpoint-test}}"
checkpoint_in_bucket = "{{checkpoints}}"

# The S3 URI to store the checkpoints
checkpoint_s3_bucket = "s3://{}/{}/{}".format(bucket, base_job_name, checkpoint_in_bucket)

model_trainer = ModelTrainer(
    training_image="{{<ecr_path>}}/{{<algorithm-name>}}:{{<tag>}}",
    role=role,
    compute=Compute(instance_type="ml.m5.xlarge", instance_count=1),
    base_job_name=base_job_name,
    checkpoint_config=CheckpointConfig(
        s3_uri=checkpoint_s3_bucket,
        local_path="/opt/ml/checkpoints"
    )
)
```

The `checkpoint_config` parameter accepts a `CheckpointConfig` object with the following fields:
+ `local_path` – The local path where the model saves the checkpoints periodically in a training container. The default path is set to `'/opt/ml/checkpoints'`. If you are using other frameworks or bringing your own training container, ensure that your training script's checkpoint configuration specifies the path to `'/opt/ml/checkpoints'`.
**Note**  
We recommend specifying the local paths as `'/opt/ml/checkpoints'` to be consistent with the default SageMaker AI checkpoint settings. If you prefer to specify your own local path, make sure you match the checkpoint saving path in your training script and the `local_path` in your `CheckpointConfig`.
+ `s3_uri` – The URI to an S3 bucket where the checkpoints are stored in real time. You can specify either an S3 general purpose or S3 directory bucket to store your checkpoints. For more information on S3 directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon Simple Storage Service User Guide*. 

To find a complete list of SageMaker AI `ModelTrainer` parameters, see the [ModelTrainer API](https://sagemaker.readthedocs.io/en/stable/) in the *[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) documentation*.