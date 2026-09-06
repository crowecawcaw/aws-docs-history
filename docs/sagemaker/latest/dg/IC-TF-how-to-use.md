

# How to use the SageMaker Image Classification - TensorFlow algorithm
<a name="IC-TF-how-to-use"></a>

You can use Image Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm. The following section describes how to use Image Classification - TensorFlow with the SageMaker AI Python SDK. For information on how to use Image Classification - TensorFlow from the Amazon SageMaker Studio Classic UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md).

The Image Classification - TensorFlow algorithm supports transfer learning using any of the compatible pretrained TensorFlow Hub models. For a list of all available pretrained models, see [TensorFlow Hub Models](IC-TF-Models.md). Every pretrained model has a unique `model_id`. The following example uses MobileNet V2 1.00 224 (`model_id`: `tensorflow-ic-imagenet-mobilenet-v2-100-224-classification-4`) to fine-tune on a custom dataset. The pretrained models are all pre-downloaded from the TensorFlow Hub and stored in Amazon S3 buckets so that training jobs can run in network isolation. Use these pre-generated model training artifacts to construct a SageMaker AI ModelTrainer.

First, retrieve the Docker image URI, training script URI, and pretrained model URI. Then, change the hyperparameters as you see fit. You can see a Python dictionary of all available hyperparameters and their default values with `hyperparameters.retrieve_default`. For more information, see [Image Classification - TensorFlow Hyperparameters](IC-TF-Hyperparameter.md). Use these values to construct a SageMaker AI ModelTrainer.

**Note**  
Default hyperparameter values are different for different models. For larger models, the default batch size is smaller and the `train_only_top_layer` hyperparameter is set to `"True"`.

This example uses the [`tf_flowers`](https://www.tensorflow.org/datasets/catalog/tf_flowers) dataset, which contains five classes of flower images. We pre-downloaded the dataset from TensorFlow under the Apache 2.0 license and made it available with Amazon S3. To fine-tune your model, call `.fit` using the Amazon S3 location of your training dataset.

```
from sagemaker.core import image_uris
from sagemaker.core import model_uris, script_uris, hyperparameters
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.train.configs import SourceCode, Compute, StoppingCondition, OutputDataConfig

model_id, model_version = {{"tensorflow-ic-imagenet-mobilenet-v2-100-224-classification-4"}}, "*"
training_instance_type = {{"ml.p3.2xlarge"}}

# Retrieve the Docker image
train_image_uri = image_uris.retrieve(model_id=model_id,model_version=model_version,image_scope="training",instance_type=training_instance_type,region=None,framework=None)

# Retrieve the training script
train_source_uri = script_uris.retrieve(model_id=model_id, model_version=model_version, script_scope="training")

# Retrieve the pretrained model tarball for transfer learning
train_model_uri = model_uris.retrieve(model_id=model_id, model_version=model_version, model_scope="training")

# Retrieve the default hyper-parameters for fine-tuning the model
hyperparameters = hyperparameters.retrieve_default(model_id=model_id, model_version=model_version)

# [Optional] Override default hyperparameters with custom values
hyperparameters["epochs"] = "5"

# The sample training data is available in the following S3 bucket
training_data_bucket = f"jumpstart-cache-prod-{aws_region}"
training_data_prefix = "training-datasets/tf_flowers/"

training_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}"

output_bucket = sess.default_bucket()
output_prefix = "jumpstart-example-ic-training"
s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"

# Create SageMaker ModelTrainer instance
tf_ic_model_trainer = ModelTrainer(
    role=aws_role,
    training_image=train_image_uri,
    source_code=SourceCode(source_dir=train_source_uri, entry_script="transfer_learning.py"),
    # In V3, pre-trained model artifacts are passed via input_data_config
    compute=Compute(instance_type=training_instance_type, instance_count=1),
    stopping_condition=StoppingCondition(max_runtime_in_seconds=360000),
    hyperparameters=hyperparameters,
    output_data_config=OutputDataConfig(s3_output_path=s3_output_location),
)

# Use S3 path of the training data to launch SageMaker TrainingJob
tf_ic_model_trainer.train(
    input_data_config=[
        InputData(channel_name="training", data_source=training_dataset_s3_path),
        InputData(channel_name="model", data_source=train_model_uri),
    ]
)
```