# Track experiments using MLflow

Amazon SageMaker Unified Studio supports two options for tracking experiments with MLflow: MLflow Apps and
MLflow Tracking Servers. MLflow Apps are the latest offering with faster startup times and
cross-account sharing, while MLflow Tracking Servers provide traditional MLflow
functionality.

For more information about MLflow, see [Machine learning experiments using MLflow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
in the _Amazon SageMaker AI Developer Guide_.

###### Topics

- [Use MLflow Apps for experiment
  tracking](#sagemaker-experiments-mlflow-apps "#sagemaker-experiments-mlflow-apps")
- [Use MLflow Tracking Servers for
  experiment tracking](#sagemaker-experiments-tracking-servers "#sagemaker-experiments-tracking-servers")

## Use MLflow Apps for experiment

tracking

Use MLflow Apps in Amazon SageMaker Unified Studio to track, manage, analyze, and compare machine
learning experiments. MLflow Apps are the latest managed MLflow offering and provide
faster startup times, cross-account sharing, and integration with other SageMaker AI
features.

MLflow Apps should be preferred over existing MLflow Tracking Servers.

MLflow Apps provide capabilities for experiment tracking, model registry, and tracing
generative AI applications. Each MLflow App includes compute resources, backend metadata
storage, and artifact storage in Amazon S3.

###### Note

MLflow Apps are different from MLflow Tracking Servers. MLflow Apps offer
additional features such as faster startup time, cross-account sharing, and
automatic model registration. For information about MLflow Tracking Servers, see
[Use MLflow Tracking Servers for
experiment tracking](#sagemaker-experiments-tracking-servers "#sagemaker-experiments-tracking-servers").

For more information about MLflow Apps, see [MLflow App Setup](../../../sagemaker/latest/dg/mlflow-app-setup.md "../../../sagemaker/latest/dg/mlflow-app-setup.md") in the
_Amazon SageMaker AI Developer Guide_.

###### Topics

- [MLflow Apps
  overview](#sagemaker-experiments-mlflow-apps-overview "#sagemaker-experiments-mlflow-apps-overview")
- [Prerequisites](#sagemaker-experiments-mlflow-apps-prerequisites "#sagemaker-experiments-mlflow-apps-prerequisites")
- [Create an MLflow
  App](#sagemaker-experiments-mlflow-apps-create "#sagemaker-experiments-mlflow-apps-create")
- [Edit an MLflow App](#sagemaker-experiments-mlflow-apps-edit "#sagemaker-experiments-mlflow-apps-edit")
- [Delete an MLflow
  App](#sagemaker-experiments-mlflow-apps-delete "#sagemaker-experiments-mlflow-apps-delete")
- [Launch the MLflow
  UI](#sagemaker-experiments-mlflow-apps-launch-ui "#sagemaker-experiments-mlflow-apps-launch-ui")
- [Integrate MLflow with
  your environment](#sagemaker-experiments-mlflow-apps-integrate "#sagemaker-experiments-mlflow-apps-integrate")

### MLflow Apps

overview

An MLflow App is a stand-alone HTTP server that serves multiple REST API endpoints
for tracking runs and experiments. MLflow Apps provide the following
capabilities:

- Experiment tracking: Track parameters, metrics, and artifacts across
  multiple training runs to identify the best performing models.
- Model registry: Manage model versions and catalog models for production
  deployment.
- Tracing: Record inputs, outputs, and metadata at every step of a
  generative AI application to identify issues and maintain
  traceability.
- Automatic model registration: Automatically register models from MLflow
  Model Registry to SageMaker AI Model Registry.

You can create MLflow Apps for your project. Your domain administrator can
configure the project profile to automatically create an MLflow App during project
creation, though this is not recommended due to default quota limits and increased
project creation latency. We recommend creating MLflow Apps on demand after project
creation.

When you delete a project, Amazon SageMaker Unified Studio automatically deletes associated MLflow
Apps.

### Prerequisites

Before you create an MLflow App, ensure you have the following:

- An Amazon S3 bucket in the same AWS Region as your project for artifact
  storage. The MLflow App uses this bucket to store model artifacts, images,
  and data files.
- Appropriate IAM permissions to create and manage MLflow Apps. Your domain
  administrator configures these permissions through the following IAM
  policies:
  - SageMakerStudioProjectRoleMachineLearningPolicy
  - SageMakerStudioProjectProvisioningRolePolicy
  - SageMakerStudioUserIAMDefaultExecutionPolicy
  - SageMakerStudioAdminIAMDefaultExecutionPolicy

For more information about IAM permissions, see the Security chapter.

### Create an MLflow

App

After you create a project, you can create an MLflow App for the project if it was
not created automatically during project creation.

To create an MLflow App, perform the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the left menu, choose **Compute**.
3. From the tabs in the top banner, choose
   **MLflow**.
4. Choose **Create MLflow App**.
5. For **Name**, enter a name for the MLflow App. The name
   must start with a letter or number and can contain letters, numbers, and
   hyphens.
6. Choose **Create** to create the MLflow App.

###### Note

It may take 2-3 minutes to complete MLflow App creation. When you successfully
create an MLflow App, it automatically starts.

### Edit an MLflow App

After you create an MLflow App, you can change the artifact storage location. To
edit an MLflow App, perform the following steps:

1. From the left menu, choose **Compute**.
2. From the tabs in the top banner, choose
   **MLflow**.
3. From the **Actions** drop-down menu, choose
   **Edit**.
4. For **Artifact storage S3 path**, enter a new path to the
   artifact storage.
5. Choose **Save changes** to update the MLflow App.

### Delete an MLflow

App

You can delete an MLflow App when you no longer need it. Deleting an MLflow App
removes the compute resources but does not delete the artifacts stored in
Amazon S3.

To delete an MLflow App, perform the following steps:

1. From the left menu, choose **Compute**.
2. From the tabs in the top banner, choose
   **MLflow**.
3. From the **Actions** drop-down menu, choose
   **Delete**.
4. In the confirmation dialog, enter the MLflow App name to confirm
   deletion.

###### Note

An MLflow App is not available for use while it is in certain states, such as
creating, pending deletion, or other transitional states.

- Choose **Delete** to delete the MLflow App.

###### Important

Deleting an MLflow App is permanent and cannot be undone. Ensure you have
backed up any important experiment data before deleting the MLflow App.

### Launch the MLflow

UI

You can launch the MLflow UI to view and manage your experiments, models, and
traces. To launch the MLflow UI, perform the following steps:

1. From the left menu, choose **Compute**.
2. From the tabs in the top banner, choose
   **MLflow**.
3. Choose the **Open** button next to the MLflow App. This
   action uses a presigned URL to launch the MLflow UI in a new tab in your
   current browser.

For more information about using the MLflow UI, see [Launch the MLflow UI using a
presigned URL](../../../sagemaker/latest/dg/mlflow-launch-ui.md "../../../sagemaker/latest/dg/mlflow-launch-ui.md") in the _Amazon SageMaker AI Developer Guide_.

### Integrate MLflow with

your environment

After you create an MLflow App, you can integrate it with your development
environment to track experiments and log metrics.

To integrate MLflow with your environment, you need the MLflow App ARN. You can
find the ARN on the MLflow App details page.

For detailed information about integrating MLflow with your environment, including
code examples for Python notebooks, see [Integrate MLflow with
your environment](../../../sagemaker/latest/dg/mlflow-track-experiments.md "../../../sagemaker/latest/dg/mlflow-track-experiments.md") in the _Amazon SageMaker AI Developer Guide_.

## Use MLflow Tracking Servers for

experiment tracking

Use MLflow Tracking Servers in Amazon SageMaker Unified Studio to track, manage, analyze, and compare
machine learning experiments. MLflow Tracking Servers provide compute and storage
resources for experiment tracking. Each project can have an MLflow Tracking Server. Your
domain administrator can configure the project defaults to automatically create the
MLflow Tracking Server during project creation. Otherwise, you can create an MLflow
Tracking Server on demand for the project.

###### Note

MLflow Tracking Servers are different from MLflow Apps. MLflow Apps offer
additional features such as faster startup time, cross-account sharing, and
automatic model registration. For information about MLflow Apps, see [Use MLflow Apps for experiment
tracking](#sagemaker-experiments-mlflow-apps "#sagemaker-experiments-mlflow-apps").

When you delete a project, Amazon SageMaker Unified Studio automatically deletes the tracking
server.

For more information about MLflow Tracking Servers, see [MLflow Tracking
Servers](../../../sagemaker/latest/dg/mlflow-create-tracking-server.md "../../../sagemaker/latest/dg/mlflow-create-tracking-server.md") in the _Amazon SageMaker AI Developer Guide_.

For more information about project profiles for AI-ML projects, see [Project
profiles](../adminguide/project-profiles.md "../adminguide/project-profiles.md") in the _Amazon SageMaker Unified Studio Admin
Guide_.

### Create an MLflow

Tracking Server

After you create a project, you can create an MLflow Tracking Server for the
project, if it wasn't created automatically during project creation.

To create an MLflow Tracking Server, perform the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the top banner, choose your project from the projects drop-down menu,
   and choose **Project overview**.
3. From the left menu, choose **Compute**.
4. From the tabs in the top banner, choose
   **MLflow**.
5. Choose **Create MLflow Tracking Server**.
6. (Optional) Provide values to override the default values for the following
   fields:
   1. Name – enter a name for the server.
   2. Size – select a size for the server.

7. Choose **Create** to create the server.

### Edit an MLflow

Tracking Server

After you create a tracking server, you can change the configured server size, if
the current size isn't sufficient for the project.

To edit a tracking server, perform the following steps from your project's
**MLflow** tab under **Compute**:

1. From the **Actions** drop-down menu, choose
   **Edit**. You can change the following values:
   1. Size – select a new size for the server.
   2. Artifact storage S3 path – enter a new path to the artifact
      storage.

2. Choose **Save changes** to update the tracking
   server.

### Start or stop an

MLflow Tracking Server

You can stop a running server or start a stopped server. While the tracking server
is starting or stopping, it's not available for MLflow to use.

To start or stop an MLflow tracking server, perform the following steps from your
project's **Project details** page:

1. From the left menu, choose **Compute**.
2. From the tabs in the top banner, choose
   **MLflow**.
3. From the **Actions** drop-down menu, choose
   **Stop** to stop a running server. Choose
   **Start** to start a stopped server.

### Integrate MLflow

with your environment

For information about how to integrate MLflow with your environment, see [Integrate MLflow with your environment](../../../sagemaker/latest/dg/mlflow-track-experiments.md "../../../sagemaker/latest/dg/mlflow-track-experiments.md") in the _Amazon SageMaker AI Developer Guide_.

### Launch the MLflow

UI

You can launch the MLflow Tracking Server UI from the **MLflow**
tab under **Compute**, by performing the following steps:

1. Navigate to the project details page for your project.
2. From the left menu, choose **Compute**.
3. From the tabs in the top banner, choose
   **MLflow**.
4. From the **Actions** drop-down menu, choose
   **Open MLflow**. This action uses a presigned URL to
   launch the MLflow UI in a new tab in your current browser.

For more information, see [Launch the MLflow UI using a
presigned URL](../../../sagemaker/latest/dg/mlflow-launch-ui.md "../../../sagemaker/latest/dg/mlflow-launch-ui.md") in the _Amazon SageMaker AI Developer Guide_.
