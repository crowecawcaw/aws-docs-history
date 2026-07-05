# How to use the SageMaker AI Object Detection - TensorFlow algorithm

You can use Object Detection - TensorFlow as an Amazon SageMaker AI built-in algorithm. The
following section describes how to use Object Detection - TensorFlow with the SageMaker AI Python
SDK. For information on how to use Object Detection - TensorFlow from the Amazon SageMaker Studio Classic
UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md").

The Object Detection - TensorFlow algorithm supports transfer learning using any of the
compatible pretrained TensorFlow models. For a list of all available pretrained models, see
[TensorFlow Models](object-detection-tensorflow-Models.md "object-detection-tensorflow-Models.md"). Every pretrained model has a
unique `model_id`. The following example uses ResNet50
(`model_id`:
`tensorflow-od1-ssd-resnet50-v1-fpn-640x640-coco17-tpu-8`) to fine-tune
on a custom dataset. The pretrained models are all pre-downloaded from the TensorFlow Hub and
stored in Amazon S3 buckets so that training jobs can run in network isolation. Use these
pre-generated model training artifacts to construct a SageMaker AI ModelTrainer.

First, retrieve the Docker image URI, training script URI, and pretrained model URI.
Then, change the hyperparameters as you see fit. You can see a Python dictionary of all
available hyperparameters and their default values with
`hyperparameters.retrieve_default`. For more information, see [Object Detection - TensorFlow Hyperparameters](object-detection-tensorflow-Hyperparameter.md "object-detection-tensorflow-Hyperparameter.md"). Use these
values to construct a SageMaker AI ModelTrainer.

###### Note

Default hyperparameter values are different for different models. For example, for larger
models, the default number of epochs is smaller.

This example uses the [`PennFudanPed`](https://www.cis.upenn.edu/~jshi/ped_html/#pub1 "https://www.cis.upenn.edu/~jshi/ped_html/#pub1") dataset, which contains images of
pedestriants in the street. We pre-downloaded the dataset and made it available with
Amazon S3. To fine-tune your model, call `.train()` using the Amazon S3 location of your
training dataset.

```
from sagemaker.core import image_uris
from sagemaker.core import model_uris, script_uris, hyperparameters
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.train.configs import SourceCode, Compute, StoppingCondition, OutputDataConfig

model_id, model_version = "tensorflow-od1-ssd-resnet50-v1-fpn-640x640-coco17-tpu-8", "*"
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
training_data_prefix = "training-datasets/PennFudanPed_COCO_format/"

training_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}"

output_bucket = sess.default_bucket()
output_prefix = "jumpstart-example-od-training"
s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"

# Create a ModelTrainer instance
tf_od_model_trainer = ModelTrainer(
    role=aws_role,
    training_image=train_image_uri,
    source_code=SourceCode(source_dir=train_source_uri, entry_script="transfer_learning.py"),
    # In V3, pre-trained model artifacts are passed via input_data_config
    compute=Compute(instance_type=training_instance_type, instance_count=1),
    stopping_condition=StoppingCondition(max_runtime_in_seconds=360000),
    hyperparameters=hyperparameters,
    output_data_config=OutputDataConfig(s3_output_path=s3_output_location),
)

# Launch a training job
tf_od_model_trainer.train(
    input_data_config=[
        InputData(channel_name="training", data_source=training_dataset_s3_path),
        InputData(channel_name="model", data_source=train_model_uri),
    ]
)
```

For more information about how to use the SageMaker AI Object Detection - TensorFlow algorithm for
transfer learning on a custom dataset, see the [Introduction to SageMaker TensorFlow - Object Detection](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb") notebook.
