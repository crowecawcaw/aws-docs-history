# MLflow Tracking Servers

An [MLflow Tracking Server](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional "https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional") is a stand-alone HTTP server that serves multiple REST API
endpoints for tracking runs and experiments. A tracking server is required to begin tracking
your machine learning (ML) experiments with SageMaker AI and MLflow. You can create a tracking
server through the Studio UI, or through the AWS CLI for more granular security
customization.

You must have the correct IAM permissions configured to create an MLflow Tracking Server.

###### Topics

- [Set up IAM permissions for MLflow](mlflow-create-tracking-server-iam.md "mlflow-create-tracking-server-iam.md")
- [Create a tracking server using Studio](mlflow-create-tracking-server-studio.md "mlflow-create-tracking-server-studio.md")
- [Create a tracking server using the AWS CLI](mlflow-create-tracking-server-cli.md "mlflow-create-tracking-server-cli.md")
