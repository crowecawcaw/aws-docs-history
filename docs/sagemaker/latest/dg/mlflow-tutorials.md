# MLflow tutorials using example Jupyter notebooks

The following tutorials demonstrate how to integrate MLflow experiments into your training
workflows. To clean up resources created by a notebook tutorial, see [Clean up MLflow resources](mlflow-cleanup.md "mlflow-cleanup.md").

You can run SageMaker AI example notebooks using JupyterLab in Studio. For more information on
JupyterLab, see [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md").

Explore the following example notebooks:

- [SageMaker Training with MLflow](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_training_mlflow.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_training_mlflow.html") — Train and
  register a Scikit-Learn model using SageMaker AI in script mode. Learn how to integrate MLflow
  experiments into your training script. For more information on model training, see [Train a Model
  with Amazon SageMaker AI](how-it-works-training.md "how-it-works-training.md").
- [SageMaker AI HPO with MLflow](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_hpo_mlflow.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_hpo_mlflow.html") — Learn how to
  track your ML experiment in MLflow with Amazon SageMaker AI automatic model tuning (AMT) and the SageMaker AI
  Python SDK. Each training iteration is logged as a run within the same
  experiment. For more information about hyperparameter optimization (HPO), see [Perform
  Automatic Model Tuning with Amazon SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").
- [SageMaker Pipelines with MLflow](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_pipelines_mlflow.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_pipelines_mlflow.html") — Use
  Amazon SageMaker Pipelines and MLflow to train, evaluate and register a model. This
  notebook uses the `@step` decorator to build a SageMaker AI Pipeline. For more
  information on pipelines and the `@step` decorator, see [Create a pipeline
  with `@step`-decorated functions](pipelines-step-decorator-create-pipeline.md "pipelines-step-decorator-create-pipeline.md").
- [Deploy an MLflow Model to SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_deployment_mlflow.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-mlflow/sagemaker_deployment_mlflow.html") — Train
  a decision tree model using SciKit-Learn. Then, use Amazon SageMaker AI `ModelBuilder` to
  deploy the model to a SageMaker AI endpoint and run inference using the deployed model. For more
  information about `ModelBuilder`, see [Deploy MLflow models with ModelBuilder](mlflow-track-experiments-model-deployment.md "mlflow-track-experiments-model-deployment.md").
