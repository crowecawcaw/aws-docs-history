# Pipelines

Amazon SageMaker Unified Studio supports SageMaker AI Pipelines, a workflow orchestration service for automating
machine learning (ML) development.

A pipeline defines a series of interconnected steps in a directed acyclic graph (DAG). You
can define the steps using the Amazon SageMaker Unified Studio visual pipeline designer, or by creating a
pipeline definition JSON schema. This DAG JSON definition gives information on the
requirements and relationships between each step of your pipeline.

The structure of a pipeline's DAG is determined by the data dependencies between steps.
These data dependencies are created when the properties of a step's output are passed as the
input to another step.

###### Note

To add a custom tag to a pipeline, add the prefix `ProjectUserTag` to the tag name.
For example:

```
ProjectUserTagMyCustomTag
```

For an overview of pipelines, see [Pipelines overview](../../../sagemaker/latest/dg/pipelines-overview.md "../../../sagemaker/latest/dg/pipelines-overview.md")
in the _Amazon SageMaker AI Developer Guide_.

## Pipeline actions

The following sections describe the actions available in Amazon SageMaker Unified Studio to create and
manage pipelines:

###### Topics

- [Define a pipeline](#sagemaker-pipeline-define "#sagemaker-pipeline-define")
- [Edit a pipeline](#sagemaker-pipeline-edit "#sagemaker-pipeline-edit")
- [Run a pipeline](#sagemaker-pipeline-run "#sagemaker-pipeline-run")
- [Stop a pipeline execution](#sagemaker-pipeline-stop "#sagemaker-pipeline-stop")
- [View the details of a pipeline](#sagemaker-pipeline-details "#sagemaker-pipeline-details")
- [View the details of a pipeline run](#sagemaker-pipeline-run-details "#sagemaker-pipeline-run-details")
- [Download a pipeline definition file](#sagemaker-pipeline-download "#sagemaker-pipeline-download")

### Define a pipeline

You define a pipeline using the visual pipeline designer. You can also create a
[pipeline definition JSON schema](https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/ "https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/").

To define a pipeline using the visual pipeline designer, complete the following
steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose **Create in visual editor**. The system opens the visual editor for
   creating a pipeline. You can also import a pipeline definition file from
   your computer.
4. Use the visual editor to add and connect pipeline steps.
5. Chose the **Save** to save your changes.

For more details, see [Define a pipeline](../../../sagemaker/latest/dg/define-pipeline.md "../../../sagemaker/latest/dg/define-pipeline.md")
in the _Amazon SageMaker AI Developer Guide_.

### Edit a pipeline

You can make changes to a pipeline before running it. To edit a pipeline, complete
the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline to edit.
4. Chose the **Executions** tab.
5. Choose the pipeline execution to edit.
6. Chose the **Visual editor** to edit the pipeline.
7. Chose the **Save** to save your changes.

For more details, see [Edit a pipeline](../../../sagemaker/latest/dg/edit-pipeline-before-execution.md "../../../sagemaker/latest/dg/edit-pipeline-before-execution.md")
in the _Amazon SageMaker AI Developer Guide_.

### Run a pipeline

After defining the steps of your pipeline as a directed acyclic graph (DAG), you
can run your pipeline, which executes the steps defined in your DAG.

To run a pipeline, complete the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline to run.
4. Chose **Execute**.
   1. For **Execution name**, enter a name for this run.
   2. (Optional) For **Description**, enter a description for this run.

5. Chose **Execute** to start the run.

For more details, see [Run a pipeline](../../../sagemaker/latest/dg/run-pipeline.md "../../../sagemaker/latest/dg/run-pipeline.md")
in the _Amazon SageMaker AI Developer Guide_.

### Stop a pipeline execution

To stop a pipeline, complete the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline to stop.
4. Choose the **Executions** tab.
5. Choose the execution to stop.
6. Choose **Stop** to stop the execution.
   To resume the execution from where it was stopped, choose **Resume**.

### View the details of a pipeline

You can view the details of a pipeline to understand its parameters, the
dependencies of its steps, or monitor its progress and status.

To access the details of a given pipeline using Amazon SageMaker Unified Studio, complete the following
steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline to view its details.
4. Choose any of the following tabs to view these details:
   - **Executions** – Details about the executions.
   - **Graph** – The pipeline graph, including all steps.
   - **Parameters** – The run parameters and metrics related to the pipeline.
   - **Information** – The metadata associated with the pipeline, such as
     tags, the pipeline Amazon Resource Name (ARN), and role ARN. You can
     also edit the pipeline description from this location.

### View the details of a pipeline run

You can view the details of a pipeline run, which can help you:

- Identify and resolve problems that may have occurred during the run, such
  as failed steps or unexpected errors.
- Compare the results of different pipeline executions to understand how
  changes in input data or parameters impact the overall workflow.
- Identify bottlenecks and opportunities for optimization.

To view the details of a pipeline run, complete the following steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline to view its details.
4. Choose the **Executions** tab.
5. Choose the pipeline execution to view. The pipeline graph for that execution appears.
6. Choose any of the pipeline steps in the graph to see step settings in the right sidebar.
7. Choose any of the following tabs to view these details:
   - **Graph** – The pipeline graph, including all steps.
   - **Parameters** – The run parameters and metrics related to the pipeline.
   - **Information** – The metadata associated with the pipeline, such as
     tags, the pipeline Amazon Resource Name (ARN), and role ARN. You can
     also edit the pipeline description from this location.

### Download a pipeline definition file

You can download the definition file for your pipeline.
You can use this pipeline definition file for:

- Backup and restoration: Use the downloaded file to create a backup of your
  pipeline configuration, which you can restore in case of infrastructure
  failures or accidental changes.
- Version control: Store the pipeline definition file in a source control
  system to track changes to the pipeline and revert to previous versions if
  needed.
- Programmatic interactions: Use the pipeline definition file as input to
  the SDK or AWS CLI.
- Integration with automation processes: Integrate the pipeline definition
  into your CI/CD workflows or other automation processes.

To download the definition file of a pipeline, complete the following
steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **ML Pipelines**. The system displays the
   pipelines for your project.
3. Choose the pipeline. You can download the pipeline definition from this
   page or any of the execution pages.
4. At the top right of the page, choose the vertical ellipsis and choose
   **Download pipeline definition (JSON)**.

For more information about the pipeline actions, see [Pipelines actions](../../../sagemaker/latest/dg/pipelines-build.md "../../../sagemaker/latest/dg/pipelines-build.md")
in the _Amazon SageMaker AI Developer Guide_.
