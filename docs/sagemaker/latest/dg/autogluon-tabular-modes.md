# How to use SageMaker AI AutoGluon-Tabular

You can use AutoGluon-Tabular as an Amazon SageMaker AI built-in algorithm. The
following section describes how to use AutoGluon-Tabular with the SageMaker Python SDK. For information
on how to use AutoGluon-Tabular from the Amazon SageMaker Studio Classic UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md").

- **Use AutoGluon-Tabular as a built-in algorithm**

Use the AutoGluon-Tabular built-in algorithm to build an AutoGluon-Tabular training container as
shown in the following code example. You can automatically spot the AutoGluon-Tabular
built-in algorithm image URI using the SageMaker AI `image_uris.retrieve` API.

After specifying the AutoGluon-Tabular image URI, you can use the AutoGluon-Tabular container to
construct a ModelTrainer using the SageMaker AI ModelTrainer API and initiate a training job.
The AutoGluon-Tabular built-in algorithm runs in script mode, but the training script is
provided for you and there is no need to replace it. If you have extensive
experience using script mode to create a SageMaker training job, then you can
incorporate your own AutoGluon-Tabular training scripts.

```
from sagemaker.core import image_uris
from sagemaker.core import model_uris, script_uris

train_model_id, train_model_version, train_scope = "autogluon-classification-ensemble", "*", "training"
training_instance_type = "ml.p3.2xlarge"

# Retrieve the docker image
train_image_uri = image_uris.retrieve(
    region=None,
    framework=None,
    model_id=train_model_id,
    model_version=train_model_version,
    image_scope=train_scope,
    instance_type=training_instance_type
)

# Retrieve the training script
train_source_uri = script_uris.retrieve(
    model_id=train_model_id, model_version=train_model_version, script_scope=train_scope
)

train_model_uri = model_uris.retrieve(
    model_id=train_model_id, model_version=train_model_version, model_scope=train_scope
)

# Sample training data is available in this bucket
training_data_bucket = f"jumpstart-cache-prod-{aws_region}"
training_data_prefix = "training-datasets/tabular_binary/"

training_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}/train"
validation_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}/validation"

output_bucket = sess.default_bucket()
output_prefix = "jumpstart-example-tabular-training"

s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"

from sagemaker import hyperparameters

# Retrieve the default hyperparameters for training the model
hyperparameters = hyperparameters.retrieve_default(
    model_id=train_model_id, model_version=train_model_version
)

# [Optional] Override default hyperparameters with custom values
hyperparameters[
    "auto_stack"
] = "True"
print(hyperparameters)

from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.train.configs import SourceCode, Compute, StoppingCondition, OutputDataConfig
from sagemaker.utils import name_from_base

training_job_name = name_from_base(f"built-in-algo-{train_model_id}-training")

# Create SageMaker ModelTrainer instance
tabular_model_trainer = ModelTrainer(
    role=aws_role,
    training_image=train_image_uri,
    source_code=SourceCode(source_dir=train_source_uri, entry_script="transfer_learning.py"),
    # In V3, pre-trained model artifacts are passed via input_data_config
    compute=Compute(instance_type=training_instance_type, instance_count=1),
    stopping_condition=StoppingCondition(max_runtime_in_seconds=360000),
    hyperparameters=hyperparameters,
    output_data_config=OutputDataConfig(s3_output_path=s3_output_location)
)

# Launch a SageMaker Training job by passing the S3 path of the training data
tabular_model_trainer.train(
    input_data_config=[
        InputData(channel_name="training", data_source=training_dataset_s3_path),
        InputData(channel_name="validation", data_source=validation_dataset_s3_path),
        InputData(channel_name="model", data_source=train_model_uri),
    ]
)
```

For more information about how to set up the AutoGluon-Tabular as a built-in algorithm,
see the following notebook examples. Any S3 bucket used in these
examples must be in the same AWS Region as the notebook instance used to run
them.

    + [Tabular classification with Amazon SageMaker AI AutoGluon-Tabular algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Classification_AutoGluon.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Classification_AutoGluon.ipynb")
    + [Tabular regression with Amazon SageMaker AI AutoGluon-Tabular algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Regression_AutoGluon.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Regression_AutoGluon.ipynb")
