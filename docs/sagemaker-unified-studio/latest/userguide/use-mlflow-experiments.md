# Track experiments using MLflow

Amazon SageMaker Unified Studio supports two options for tracking experiments with MLflow: MLflow
Apps and MLflow Tracking Servers. MLflow Apps are the latest offering with faster
startup times and cross-account sharing, while MLflow Tracking Servers provide
traditional MLflow functionality.

###### Topics

- [Use MLflow Apps for experiment
  tracking](#use-mlflow-apps "#use-mlflow-apps")
- [Use MLflow Tracking Servers to
  track experiments](#use-mlflow-tracking-servers "#use-mlflow-tracking-servers")

## Use MLflow Apps for experiment

tracking

###### Note

MLflow Apps are different from MLflow Tracking Servers. MLflow Apps offer
additional features such as faster startup time and cross-account sharing.
For information about connecting to existing MLflow Tracking Servers, see
[Use MLflow Tracking Servers to
track experiments](#use-mlflow-tracking-servers "#use-mlflow-tracking-servers").

MLflow Apps are the latest managed MLflow offering in Amazon SageMaker Unified Studio and
provide faster startup times, cross-account sharing, and integration with SageMaker AI
features. MLflow Apps use MLflow 3.0 and support experiment tracking, model
registry, and tracing for generative AI applications.

### Connect to an MLflow App

You can connect to an existing MLflow App created in SageMaker AI Studio to
track experiments and manage model versions. Note that you can't create a
new MLflow App in Amazon SageMaker Unified Studio. You have to create this using SageMaker AI APIs
or in SageMaker AI Studio.

To connect to an MLflow App, perform the following steps:

1. From your project's main page, choose **MLflow**
   from the left navigation menu.
2. Choose **Connect MLflow App**.
3. Enter an MLflow App Name
4. Provide a Connection name for identification
5. Enter the MLflow App ARN for your project
6. Choose **Connect to app**

### Manage MLflow Apps

After you connect to an MLflow App, you can perform the following actions
from the **MLflow** page:

- Open MLflow – Choose the **Open** button
  next to the MLflow App to launch the MLflow UI and view experiments,
  models, and traces.
- Edit – Update the connection with a new ARN.
- Delete – Remove the connection to the MLflow App.

To access the **MLflow** page, choose
**MLflow** from the left navigation menu.

## Use MLflow Tracking Servers to

track experiments

To get started, you should have an existing MLflow server created in SageMaker AI
Studio. Make sure that you have the ARN to get started.

1. From your project's main page, choose **MLflow** from
   the left navigation menu.
2. Connect to an existing MLflow Tracking Server. Note that you can't
   create a new MLflow Server in Amazon SageMaker Unified Studio. You have to create this
   using SageMaker AI APIs or in SageMaker AI Studio.
3. Choose **Connect Tracking Server**
4. Enter a Tracking Server Name
5. Provide a Connection name for identification
6. Enter the MLflow Tracking Server ARN for your project
7. Choose **Connect to server**
8. Once connected, choose **Open MLflow** to launch the
   MLflow UI.
9. In the MLflow interface, view your experiments:
   - Experiments tab shows all tracked experiments
   - Models tab displays registered model versions
   - Prompts tab contains prompt templates and versions

10. You can perform additional actions such as
    - Stop ML Server
    - Use server to train model – this will launch a sample
      notebook which will provide instructions on how to use MLflow to
      train a linear regression model
    - Edit the connection with new ARNs
    - Delete the connection
