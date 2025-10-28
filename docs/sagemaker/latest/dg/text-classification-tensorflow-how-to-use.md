# How to use the SageMaker AI Text Classification - TensorFlow algorithm

You can use Text Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm. The
following section describes how to use Text Classification - TensorFlow with the SageMaker AI Python
SDK. For information on how to use Text Classification - TensorFlow from the Amazon SageMaker Studio Classic
UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md").

The Text Classification - TensorFlow algorithm supports transfer learning using any of the
compatible pretrained TensorFlow models. For a list of all available pretrained models, see
[TensorFlow Hub Models](text-classification-tensorflow-Models.md "text-classification-tensorflow-Models.md"). Every pretrained model has
a unique `model_id`. The following example uses BERT Base Uncased
(`model_id`:
`tensorflow-tc-bert-en-uncased-L-12-H-768-A-12-2`) to fine-tune
on a custom dataset. The pretrained models are all pre-downloaded from the TensorFlow Hub and
stored in Amazon S3 buckets so that training jobs can run in network isolation. Use these
pre-generated model training artifacts to construct a SageMaker AI Estimator.

First, retrieve the Docker image URI, training script URI, and pretrained model URI.
Then, change the hyperparameters as you see fit. You can see a Python dictionary of all
available hyperparameters and their default values with
`hyperparameters.retrieve_default`. For more information, see [Text Classification - TensorFlow
Hyperparameters](text-classification-tensorflow-Hyperparameter.md "text-classification-tensorflow-Hyperparameter.md"). Use these
values to construct a SageMaker AI Estimator.

###### Note

Default hyperparameter values are different for different models. For example, for larger
models, the default batch size is smaller.

This example uses the [`SST2`](https://www.tensorflow.org/datasets/catalog/glue#gluesst2 "https://www.tensorflow.org/datasets/catalog/glue#gluesst2") dataset, which contains positive and negative movie
reviews. We pre-downloaded the dataset and made it available with Amazon S3. To fine-tune
your model, call `.fit` using the Amazon S3 location of your training
dataset. Any S3 bucket used in a notebook must be in the same AWS Region as the notebook instance that accesses it.

```
from sagemaker import image_uris, model_uris, script_uris, hyperparameters
from sagemaker.estimator import Estimator

model_id, model_version = "tensorflow-tc-bert-en-uncased-L-12-H-768-A-12-2", "*"
training_instance_type = "ml.p3.2xlarge"

# Retrieve the Docker image
train_image_uri = image_uris.retrieve(model_id=model_id,model_version=model_version,image_scope="training",instance_type=training_instance_type,region=None,framework=None)

# Retrieve the training script
train_source_uri = script_uris.retrieve(model_id=model_id, model_version=model_version, script_scope="training")

# Retrieve the pretrained model tarball for transfer learning
train_model_uri = model_uris.retrieve(model_id=model_id, model_version=model_version, model_scope="training")

# Retrieve the default hyperparameters for fine-tuning the model
hyperparameters = hyperparameters.retrieve_default(model_id=model_id, model_version=model_version)

# [Optional] Override default hyperparameters with custom values
hyperparameters["epochs"] = "5"

# Sample training data is available in this bucket
training_data_bucket = f"jumpstart-cache-prod-{aws_region}"
training_data_prefix = "training-datasets/SST2/"

training_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}"

output_bucket = sess.default_bucket()
output_prefix = "jumpstart-example-tc-training"
s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"

# Create an Estimator instance
tf_tc_estimator = Estimator(
    role=aws_role,
    image_uri=train_image_uri,
    source_dir=train_source_uri,
    model_uri=train_model_uri,
    entry_point="transfer_learning.py",
    instance_count=1,
    instance_type=training_instance_type,
    max_run=360000,
    hyperparameters=hyperparameters,
    output_path=s3_output_location,
)

# Launch a training job
tf_tc_estimator.fit({"training": training_dataset_s3_path}, logs=True)
```

For more information about how to use the SageMaker Text Classification - TensorFlow
algorithm for transfer learning on a custom dataset, see the [Introduction to JumpStart - Text Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb") notebook.
