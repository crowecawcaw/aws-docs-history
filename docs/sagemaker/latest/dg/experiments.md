# Amazon SageMaker Experiments in Studio Classic

###### Important

Experiment tracking using the SageMaker Experiments Python SDK is only available in Studio Classic. We
recommend using the new Studio experience and creating experiments using the latest SageMaker AI
integrations with MLflow. There is no MLflow UI integration with Studio Classic. If you want to use MLflow with Studio, you must launch the MLflow UI using the AWS CLI.
For more information, see [Launch the MLflow UI using the AWS CLI](mlflow-launch-ui.md#mlflow-launch-ui-cli "mlflow-launch-ui.md#mlflow-launch-ui-cli").

Amazon SageMaker Experiments Classic is a capability of Amazon SageMaker AI that lets you create, manage,
analyze, and compare your machine learning experiments in Studio Classic. Use SageMaker Experiments to
view, manage, analyze, and compare both custom experiments that you programmatically create and
experiments automatically created from SageMaker AI jobs.

Experiments Classic automatically tracks the inputs, parameters, configurations, and results
of your iterations as _runs_. You can assign, group, and
organize these runs into _experiments_. SageMaker Experiments is
integrated with Amazon SageMaker Studio Classic, providing a visual interface to browse your active and past
experiments, compare runs on key performance metrics, and identify the best performing models.
SageMaker Experiments tracks all of the steps and artifacts that went into creating a model, and you
can quickly revisit the origins of a model when you are troubleshooting issues in production, or
auditing your models for compliance verifications.

## Migrate from Experiments Classic to Amazon SageMaker AI with MLflow

Past experiments created using Experiments Classic are still available to view in
Studio Classic. If you want to maintain and use past experiment code with MLflow, you must update
your training code to use the MLflow SDK and run the training experiments again. For more
information on getting started with the MLflow SDK and the AWS MLflow plugin, see [Integrate MLflow with your environment](mlflow-track-experiments.md "mlflow-track-experiments.md").
