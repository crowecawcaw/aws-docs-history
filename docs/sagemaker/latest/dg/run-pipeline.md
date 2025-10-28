# Run a pipeline

After defining the steps of your pipeline as a directed acyclic graph (DAG), you can
run your pipeline, which executes the steps defined in your DAG. The following walkthroughs
show you how to run an Amazon SageMaker AI pipeline using either the drag-and-drop visual editor in
Amazon SageMaker Studio or the Amazon SageMaker Python SDK.

To start a new execution of your pipeline, do the following:

Studio

1. Open SageMaker Studio by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose **Pipelines**.
3. (Optional) To filter the list of pipelines by name, enter a full or partial
   pipeline name in the search field.
4. Choose a pipeline name to open the pipeline details view.
5. Choose **Visual Editor** on the top right.
6. To start an execution from the latest version, choose
   **Executions**.
7. To start an execution from a specific version, follow these steps:
   - Choose the version icon in the bottom toolbar to open the version
     panel.
   - Choose the pipeline version you want to execute.
   - Hover over the version item to reveal the three-dot menu, choose
     **Execute**.
   - (Optional) To view a previous version of the pipeline, choose
     **Preview** from the three-dot menu in the version panel.
     You can also edit the version by choosing **Edit** in the
     notification bar.

###### Note

If your pipeline fails, the status banner will show a **Failed**
status. After troubleshooting the failed step, choose **Retry** on
the status banner to resume running the pipeline from that step.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Select **Pipelines** from the menu.
4. To narrow the list of pipelines by name, enter a full or partial pipeline name
   in the search field.
5. Select a pipeline name.
6. From the **Executions** or **Graph** tab in
   the execution list, choose **Create execution**.
7. Enter or update the following required information:
   - **Name** – Must be unique to your account in the
     AWS Region.
   - **ProcessingInstanceCount** – The number of
     instances to use for processing.
   - **ModelApprovalStatus** – For your
     convenience.
   - **InputDataUrl** – The Amazon S3 URI of the input
     data.

8. Choose **Start**.

Once your pipeline is running, you can view the details of the execution by
choosing **View details** on the status banner.

To stop the run, choose **Stop** on the status banner. To resume
the execution from where it was stopped, choose **Resume** on the
status banner.

###### Note

If your pipeline fails, the status banner will show a **Failed**
status. After troubleshooting the failed step, choose **Retry** on
the status banner to resume running the pipeline from that step.

After you’ve created a pipeline definition using the SageMaker AI Python SDK, you can submit it to
SageMaker AI to start your execution. The following tutorial shows how to submit a pipeline, start an
execution, examine the results of that execution, and delete your pipeline.

###### Topics

- [Prerequisites](#run-pipeline-prereq "#run-pipeline-prereq")
- [Step 1: Start the Pipeline](#run-pipeline-submit "#run-pipeline-submit")
- [Step 2: Examine a Pipeline Execution](#run-pipeline-examine "#run-pipeline-examine")
- [Step 3: Override Default Parameters for a Pipeline
  Execution](#run-pipeline-parametrized "#run-pipeline-parametrized")
- [Step 4: Stop and Delete a Pipeline Execution](#run-pipeline-delete "#run-pipeline-delete")

### Prerequisites

This tutorial requires the following:

- A SageMaker notebook instance.
- A Pipelines pipeline definition. This tutorial assumes you're using the pipeline definition
  created by completing the [Define a pipeline](define-pipeline.md "define-pipeline.md") tutorial.

### Step 1: Start the Pipeline

First, you need to start the pipeline.

###### To start the pipeline

1. Examine the JSON pipeline definition to ensure that it's well-formed.

```
import json

json.loads(pipeline.definition())
```

2. Submit the pipeline definition to the Pipelines service to create a pipeline if it doesn't
   exist, or update the pipeline if it does. The role passed in is used by Pipelines to create
   all of the jobs defined in the steps.

```
pipeline.upsert(role_arn=role)
```

3. Start a pipeline execution.

```
execution = pipeline.start()
```

### Step 2: Examine a Pipeline Execution

Next, you need to examine the pipeline execution.

###### To examine a pipeline execution

1. Describe the pipeline execution status to ensure that it has been created and started
   successfully.

```
execution.describe()
```

2. Wait for the execution to finish.

```
execution.wait()
```

3. List the execution steps and their status.

```
execution.list_steps()
```

Your output should look like the following:

```
[{'StepName': 'AbaloneTransform',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 41, 27, 870000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 45, 50, 492000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'TransformJob': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:transform-job/pipelines-cfvy1tjuxdq8-abalonetransform-ptyjoef3jy'}}},
 {'StepName': 'AbaloneRegisterModel',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 41, 26, 929000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 41, 28, 15000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'RegisterModel': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:model-package/abalonemodelpackagegroupname/1'}}},
 {'StepName': 'AbaloneCreateModel',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 41, 26, 895000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 41, 27, 708000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'Model': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:model/pipelines-cfvy1tjuxdq8-abalonecreatemodel-jl94rai0ra'}}},
 {'StepName': 'AbaloneMSECond',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 41, 25, 558000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 41, 26, 329000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'Condition': {'Outcome': 'True'}}},
 {'StepName': 'AbaloneEval',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 37, 34, 767000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 41, 18, 80000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'ProcessingJob': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:processing-job/pipelines-cfvy1tjuxdq8-abaloneeval-zfraozhmny'}}},
 {'StepName': 'AbaloneTrain',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 34, 55, 867000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 37, 34, 34000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'TrainingJob': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:training-job/pipelines-cfvy1tjuxdq8-abalonetrain-tavd6f3wdf'}}},
 {'StepName': 'AbaloneProcess',
  'StartTime': datetime.datetime(2020, 11, 21, 2, 30, 27, 160000, tzinfo=tzlocal()),
  'EndTime': datetime.datetime(2020, 11, 21, 2, 34, 48, 390000, tzinfo=tzlocal()),
  'StepStatus': 'Succeeded',
  'CacheHitResult': {'SourcePipelineExecutionArn': ''},
  'Metadata': {'ProcessingJob': {'Arn': 'arn:aws:sagemaker:us-east-2:111122223333:processing-job/pipelines-cfvy1tjuxdq8-abaloneprocess-mgqyfdujcj'}}}]
```

4. After your pipeline execution is complete, download the resulting 
   `evaluation.json` file from Amazon S3 to examine the report.

```
evaluation_json = sagemaker.s3.S3Downloader.read_file("{}/evaluation.json".format(
    step_eval.arguments["ProcessingOutputConfig"]["Outputs"][0]["S3Output"]["S3Uri"]
))
json.loads(evaluation_json)
```

### Step 3: Override Default Parameters for a Pipeline

Execution

You can run additional executions of the pipeline by specifying different pipeline
parameters to override the defaults.

###### To override default parameters

1. Create the pipeline execution. This starts another pipeline execution with the model
   approval status override set to "Approved". This
   means that the model package version generated by the `RegisterModel` step is
   automatically ready for deployment through CI/CD pipelines, such as with SageMaker Projects. For more information, see [MLOps Automation With SageMaker Projects](sagemaker-projects.md "sagemaker-projects.md").

```
execution = pipeline.start(
    parameters=dict(
        ModelApprovalStatus="Approved",
    )
)
```

2. Wait for the execution to finish.

```
execution.wait()
```

3. List the execution steps and their status.

```
execution.list_steps()
```

4. After your pipeline execution is complete, download the resulting 
   `evaluation.json` file from Amazon S3 to examine the report.

```
evaluation_json = sagemaker.s3.S3Downloader.read_file("{}/evaluation.json".format(
    step_eval.arguments["ProcessingOutputConfig"]["Outputs"][0]["S3Output"]["S3Uri"]
))
json.loads(evaluation_json)
```

### Step 4: Stop and Delete a Pipeline Execution

When you're finished with your pipeline, you can stop any ongoing executions and delete
the pipeline.

###### To stop and delete a pipeline execution

1. Stop the pipeline execution.

```
execution.stop()
```

2. Delete the pipeline.

```
pipeline.delete()
```
