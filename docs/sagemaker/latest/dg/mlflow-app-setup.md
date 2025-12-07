# MLflow App Setup

An [MLflow App](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional "https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional") is a stand-alone HTTP server that serves multiple REST API
endpoints for tracking runs and experiments. An MLflow App is required to begin tracking
your machine learning (ML) experiments with SageMaker AI and MLflow. You can create an MLflow App through the Studio UI, or through the AWS CLI for more granular security
customization.

You must have the correct IAM permissions configured to create an MLflow App.

MLflow Apps are the latest managed MLflow offering on SageMaker and should be preferred over existing MLflow Tracking Servers. MLflow Apps offer additional features such as faster startup time, cross-account sharing, integrations with other SageMaker features, and other features beyond the existing MLflow Tracking Servers.

###### Topics

- [MLflow App Setup Prequisites](mlflow-app-setup-prerequisites.md "mlflow-app-setup-prerequisites.md")
- [Create MLflow App](mlflow-app-setup-create-app.md "mlflow-app-setup-create-app.md")
