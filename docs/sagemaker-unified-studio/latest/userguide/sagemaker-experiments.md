# Track experiments using MLflow

Use MLflow in Amazon SageMaker Unified Studio to create, manage, analyze, and compare machine learning
experiments.

For more information about MLflow, see [Machine learning experiments using MLflow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
in the _Amazon SageMaker AI Developer Guide_.

###### Topics

- [MLflow Tracking Servers](#sagemaker-experiments-server "#sagemaker-experiments-server")
- [Tracking experiments with MLflow](#sagemaker-experiments-mlflow "#sagemaker-experiments-mlflow")

## MLflow Tracking Servers

MLflow uses compute and storage resources provided by an MLflow Tracking Server. Each
project requires an MLflow Tracking Server. Your domain administrator can configure the
project defaults to automatically create the MLflow Tracking Server during project
creation. Otherwise, you can create an MLflow Tracking Server on demand for the
project.

When you delete a project, Amazon SageMaker Unified Studio automatically deletes the tracking
server.

For more information about MLflow Tracking Servers, see [MLflow Tracking Servers](../../../sagemaker/latest/dg/mlflow-create-tracking-server.md "../../../sagemaker/latest/dg/mlflow-create-tracking-server.md")
in the _Amazon SageMaker AI Developer Guide_.

For more information about project profiles for AI-ML projects, see [Project
profiles](../adminguide/project-profiles.md "../adminguide/project-profiles.md") in the _Amazon SageMaker Unified Studio Admin Guide_.

### Create the MLflow tracking

server

After you create a project, you can create the MLflow Tracking Server for the
project, if it wasn't created automatically during project creation.

To create an MLflow Tracking Server, perform the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the top banner, choose your project from the projects drop-down menu,
   and choose **Project overview**.
3. From the left menu, choose **Compute**.
4. From the tabs in the top banner, choose **MLflow Tracking Servers**.
5. Choose **Create MLflow Tracking Server**.
6. (Optional) Provide values to override the default values for the following fields:
   1. Name – enter a name for the server.
   2. Size – select a size for the server.

7. Choose **Create** to create the server.

### Edit the MLflow Tracking Server

After you create a tracking server, you can change the configured server size, if
the current size isn't sufficient for the project.

To edit a tracking server, perform the following steps, starting at your project's
**MLflow Tracking Servers** page:

1. From the **Actions** drop-down menu, choose
   **Edit**. You can change the following values:
   1. Size – select a new size for the server.
   2. Artifact storage S3 path – enter a new path to the artifact storage.

2. Choose **Save changes** to update the tracking server.

### Start or stop an MLflow server

You can stop a running server or start a stopped server. While the tracking server
is starting or stopping, it's not available for MLflow to use.

To start or stop an MLflow tracking server, perform the following steps from your
project's **Project details** page:

1. From the left menu, choose **Compute**.
2. From the tabs in the top banner, choose **MLflow Tracking Servers**.
3. From the **Actions** drop-down menu, choose **Stop** to stop a running server.
   Choose **Start** to start a stopped server.

### Integrate MLflow with your environment

For information about how to integrate MLflow with your environment, see
[Integrate MLflow with your environment](../../../sagemaker/latest/dg/mlflow-track-experiments.md "../../../sagemaker/latest/dg/mlflow-track-experiments.md") in the _Amazon SageMaker AI Developer Guide_.

### Launching MLflow UI

You can launch MLflow Tracking Server UI from the **MLflow Tracking
Servers** page, by performing the following steps:

1. Navigate to the project details page for your project.
2. From the left menu, choose **Compute**.
3. From the tabs in the top banner, choose **MLflow Tracking Servers**.
4. From the **Actions** drop-down menu, choose **Open MLflow**.
   This action uses a presigned URL to launche MLflow UI in a new tab in your current browser.

For more information, see [Launch the MLflow UI using a presigned URL](../../../sagemaker/latest/dg/mlflow-launch-ui.md "../../../sagemaker/latest/dg/mlflow-launch-ui.md") in the _Amazon SageMaker AI Developer Guide_.

## Tracking experiments with MLflow

From the **Experiments** page, you can view and track the experiments
for the current project. You can also open sample notebooks, such as for logging MLflow
experiments and for registering MLflow models.

### View the list of experiments

To view the list of experiments in your project, perform the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **MLflow**. The **Experiments** page displays the
   MLflow experiments for your project.
3. (Optional) Enter text in the search text box to view a subset of the
   listed experiments.

### Track an experiment

To track an MLflow experiment in your project, perform the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **MLflow**. The **Experiments** page displays the
   MLflow experiments for your project.
3. From the **Experiments** table, choose the experiment to
   track. This launches a new MLflow tab in your current browser.
