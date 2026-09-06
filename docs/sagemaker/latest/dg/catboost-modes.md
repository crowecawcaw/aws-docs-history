

# How to use SageMaker AI CatBoost
<a name="catboost-modes"></a>

You can use CatBoost as an Amazon SageMaker AI built-in algorithm. The following section describes how to use CatBoost with the SageMaker Python SDK. For information on how to use CatBoost from the Amazon SageMaker Studio Classic UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md).
+ **Use CatBoost as a built-in algorithm**

  Use the CatBoost built-in algorithm to build a CatBoost training container as shown in the following code example. You can automatically spot the CatBoost built-in algorithm image URI using the SageMaker AI `image_uris.retrieve` API.

  After specifying the CatBoost image URI, you can use the CatBoost container to construct a ModelTrainer using the SageMaker AI ModelTrainer API and initiate a training job. The CatBoost built-in algorithm runs in script mode, but the training script is provided for you and there is no need to replace it. If you have extensive experience using script mode to create a SageMaker training job, then you can incorporate your own CatBoost training scripts.

  ```
  from sagemaker.core import image_uris
  from sagemaker.core import model_uris, script_uris
  
  train_model_id, train_model_version, train_scope = "catboost-classification-model", "*", "training"
  training_instance_type = "ml.m5.xlarge"
  
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
  training_data_prefix = "training-datasets/tabular_multiclass/"
  
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
      "iterations"
  ] = "500"
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

  For more information about how to set up CatBoost as a built-in algorithm, see the following notebook examples.
  + [Tabular classification with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Classification_LightGBM_CatBoost.ipynb)
  + [Tabular regression with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Regression_LightGBM_CatBoost.ipynb)