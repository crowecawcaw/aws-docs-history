# Checkpoints in Amazon SageMaker AI

Use checkpoints in Amazon SageMaker AI to save the state of machine learning (ML) models during
training. Checkpoints are snapshots of the model and can be configured by the callback
functions of ML frameworks. You can use the saved checkpoints to restart a training job from
the last saved checkpoint.

Using checkpoints, you can do the following:

- Save your model snapshots under training due to an unexpected interruption to the
  training job or instance.
- Resume training the model in the future from a checkpoint.
- Analyze the model at intermediate stages of training.
- Use checkpoints with S3 Express One Zone for increased access speeds.
- Use checkpoints with SageMaker AI managed spot training to save on training costs.
  The SageMaker training mechanism uses training containers on Amazon EC2 instances, and the
  checkpoint files are saved under a local directory of the containers (the default is
  `/opt/ml/checkpoints`). SageMaker AI provides the functionality to copy the
  checkpoints from the local path to Amazon S3 and automatically syncs the checkpoints in that
  directory with S3. Existing checkpoints in S3 are written to the SageMaker AI
  container at the start of the job, enabling jobs to resume from a checkpoint. Checkpoints
  added to the S3 folder after the job has started are not copied to the training
  container. SageMaker AI also writes new checkpoints from the container to S3 during training.
  If a checkpoint is deleted in the SageMaker AI container, it will also be deleted in the S3
  folder.

You can use checkpoints in Amazon SageMaker AI with the Amazon S3 Express One Zone storage class (S3 Express One Zone) for faster
access to checkpoints. When you enable checkpointing and specify the S3 URI for your
checkpoint storage destination, you can provide an S3 URI for a folder in either an
S3 general purpose bucket or an S3 directory bucket. S3 directory buckets
that are integrated with SageMaker AI can only be encrypted with server-side encryption with Amazon S3 managed
keys (SSE-S3). Server-side encryption with AWS KMS keys (SSE-KMS) is not currently supported.
For more information on
S3 Express One Zone and S3 directory buckets, see [What is S3 Express One Zone](../../../AmazonS3/latest/userguide/s3-express-one-zone.md "../../../AmazonS3/latest/userguide/s3-express-one-zone.md").

If you are using checkpoints with SageMaker AI managed spot training, SageMaker AI manages checkpointing
your model training on a spot instance and resuming the training job on the next spot
instance. With SageMaker AI managed spot training, you can significantly reduce the billable time
for training ML models. For more information, see [Managed Spot Training in Amazon SageMaker AI](model-managed-spot-training.md "model-managed-spot-training.md").

###### Topics

- [Checkpoints for frameworks and
  algorithms in SageMaker AI](#model-checkpoints-whats-supported "#model-checkpoints-whats-supported")
- [Considerations for
  checkpointing](#model-checkpoints-considerations "#model-checkpoints-considerations")
- [Enable checkpointing](model-checkpoints-enable.md "model-checkpoints-enable.md")
- [Browse checkpoint files](model-checkpoints-saved-file.md "model-checkpoints-saved-file.md")
- [Resume training from a checkpoint](model-checkpoints-resume.md "model-checkpoints-resume.md")
- [Cluster repairs for GPU errors](model-checkpoints-cluster-repair.md "model-checkpoints-cluster-repair.md")

## Checkpoints for frameworks and

algorithms in SageMaker AI

Use checkpoints to save snapshots of ML models built on your preferred frameworks
within SageMaker AI.

**SageMaker AI frameworks and algorithms that support checkpointing**

SageMaker AI supports checkpointing for AWS Deep Learning Containers and a subset of
built-in algorithms without requiring training script changes. SageMaker AI saves the
checkpoints to the default local path `'/opt/ml/checkpoints'` and copies them
to Amazon S3.

- Deep Learning Containers: [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html"), [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html"), [MXNet](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/sagemaker.mxnet.html "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/sagemaker.mxnet.html"), and [HuggingFace](https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/sagemaker.huggingface.html "https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/sagemaker.huggingface.html")

###### Note

If you are using the HuggingFace framework estimator, you need to specify
a checkpoint output path through hyperparameters. For more information, see
[Run training on Amazon SageMaker AI](https://huggingface.co/docs/sagemaker/train "https://huggingface.co/docs/sagemaker/train") in the _HuggingFace
documentation_.

- Built-in algorithms: [Image
  Classification](image-classification.md "image-classification.md"), [Object Detection](object-detection.md "object-detection.md"),
  [Semantic
  Segmentation](semantic-segmentation.md "semantic-segmentation.md"), and [XGBoost](xgboost.md "xgboost.md") (0.90-1 or
  later)

###### Note

If you are using the XGBoost algorithm in framework mode (script mode),
you need to bring an XGBoost training script with checkpointing that's
manually configured. For more information about the XGBoost training methods
to save model snapshots, see [Training XGBoost](https://xgboost.readthedocs.io/en/latest/python/python_intro.html#training "https://xgboost.readthedocs.io/en/latest/python/python_intro.html#training") in _the XGBoost Python SDK
documentation_.

If a pre-built algorithm that does not support checkpointing is used in a managed spot
training job, SageMaker AI does not allow a maximum wait time greater than an hour for the job
in order to limit wasted training time from interrupts.

**For custom training containers and other frameworks**

If you are using your own training containers, training scripts, or other frameworks
not listed in the previous section, you must properly set up your training script using
callbacks or training APIs to save checkpoints to the local path
(`'/opt/ml/checkpoints'`) and load from the local path in your training
script. SageMaker AI estimators can sync up with the local path and save the checkpoints to
Amazon S3.

## Considerations for

checkpointing

Consider the following when using checkpoints in SageMaker AI.

- To avoid overwrites in distributed training with multiple instances, you must
  manually configure the checkpoint file names and paths in your training script.
  The high-level SageMaker AI checkpoint configuration specifies a single Amazon S3 location
  without additional suffixes or prefixes to tag checkpoints from multiple
  instances.
- The SageMaker Python SDK does not support high-level configuration for
  checkpointing frequency. To control the checkpointing frequency, modify your
  training script using the framework's model save functions or checkpoint
  callbacks.
- If you use SageMaker AI checkpoints with SageMaker Debugger and SageMaker AI distributed and are
  facing issues, see the following pages for troubleshooting and
  considerations.
  - [Distributed training supported by
    Amazon SageMaker Debugger](debugger-reference.md#debugger-considerations "debugger-reference.md#debugger-considerations")
  - [Troubleshooting for distributed
    training in Amazon SageMaker AI](distributed-troubleshooting-data-parallel.md "distributed-troubleshooting-data-parallel.md")
  - [Model Parallel
    Troubleshooting](distributed-troubleshooting-model-parallel.md "distributed-troubleshooting-model-parallel.md")
