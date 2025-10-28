# Create notebook job with SageMaker AI Python

SDK example

To run a standalone notebook using the SageMaker Python SDK, you need to create a Notebook
Job step, attach it into a pipeline, and use the utilities provided by Pipelines to run your job
on demand or optionally schedule one or more future jobs. The following sections describe the
basic steps to create an on-demand or scheduled notebook job and track the run. In addition,
refer to the following discussion if you need
to pass parameters to your notebook job or connect to Amazon EMR in your
notebook—additional preparation of your Jupyter notebook is required in these cases.
You can also apply defaults for a subset of the arguments of `NotebookJobStep` so
you don’t have to specify them every time you create a Notebook Job step.

To view sample notebooks that demonstrate how to schedule notebook jobs with the SageMaker AI
Python SDK, see [notebook job sample notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines/notebook-job-step "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines/notebook-job-step").

###### Topics

- [Steps to create a notebook job](#create-notebook-auto-run-overall "#create-notebook-auto-run-overall")
- [View your notebook jobs in the Studio
  UI dashboard](#create-notebook-auto-run-dash "#create-notebook-auto-run-dash")
- [View your pipeline graph in
  Studio](#create-notebook-auto-run-graph "#create-notebook-auto-run-graph")
- [Passing parameters to your
  notebook](#create-notebook-auto-run-passparam "#create-notebook-auto-run-passparam")
- [Connecting to an Amazon EMR cluster in your
  input notebook](#create-notebook-auto-run-emr "#create-notebook-auto-run-emr")
- [Set up default options](#create-notebook-auto-run-intdefaults "#create-notebook-auto-run-intdefaults")

## Steps to create a notebook job

You can either create a notebook job that runs immediately or on a schedule. The
following instructions describe both methods.

###### To schedule a notebook job, complete the following basic steps:

1. Create a `NotebookJobStep` instance. For details about
   `NotebookJobStep` parameters, see [sagemaker.workflow.steps.NotebookJobStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep"). At minimum, you can provide the
   following arguments as shown in the following code snippet:

###### Important

If you schedule your notebook job using the SageMaker Python SDK, you can only
specify certain images to run your notebook job. For more information, see [Image constraints for SageMaker AI
Python SDK notebook jobs](notebook-auto-run-constraints.md#notebook-auto-run-constraints-image-sdk "notebook-auto-run-constraints.md#notebook-auto-run-constraints-image-sdk").

```
notebook_job_step = NotebookJobStep(
    input_notebook=`input-notebook`,
    image_uri=`image-uri`,
    kernel_name=`kernel-name`
)
```

2. Create a pipeline with your `NotebookJobStep` as a single step, as
   shown in the following snippet:

```
pipeline = Pipeline(
    name=`pipeline-name`,
    steps=[notebook_job_step],
    sagemaker_session=`sagemaker-session`,
)
```

3. Run the pipeline on demand or optionally schedule future pipeline runs. To
   initiate an immediate run, use the following command:

```
execution = pipeline.start(
    parameters={...}
)
```

Optionally, you can schedule a single future pipeline run or multiple runs at a
predetermined interval. You specify your schedule in `PipelineSchedule` and
then pass the schedule object to your pipeline with `put_triggers`. For
more information about pipeline scheduling, see [Schedule a pipeline with the SageMaker Python SDK](pipeline-eventbridge.md#build-and-manage-scheduling "pipeline-eventbridge.md#build-and-manage-scheduling").

The following example schedules your pipeline to run once at December 12, 2023 at
10:31:32 UTC.

```
my_schedule = PipelineSchedule(
    name="my-schedule“,
    at=datetime(year=2023, month=12, date=25, hour=10, minute=31, second=32)
)
pipeline.put_triggers(triggers=[my_schedule])
```

The following example schedules your pipeline to run at 10:15am UTC on the last
Friday of each month during the years 2022 to 2023. For details about cron-based
scheduling, see [Cron-based
schedules](../../../scheduler/latest/UserGuide/schedule-types.md#cron-based "../../../scheduler/latest/UserGuide/schedule-types.md#cron-based").

```
my_schedule = PipelineSchedule(
    name="my-schedule“,
    cron="15 10 ? * 6L 2022-2023"
)
pipeline.put_triggers(triggers=[my_schedule])
```

4. (Optional) View your notebook jobs in the SageMaker Notebook Jobs dashboard. The values
   you supply for the `tags` argument of your Notebook Job step control how
   the Studio UI captures and displays the job. For more information, see [View your notebook jobs in the Studio
   UI dashboard](#create-notebook-auto-run-dash "#create-notebook-auto-run-dash").

## View your notebook jobs in the Studio

UI dashboard

The notebook jobs you create as pipeline steps appear in the Studio Notebook Job
dashboard if you specify certain tags.

###### Note

Only notebook jobs created in Studio or local JupyterLab environments create job
definitions. Therefore, if you create your notebook job with the SageMaker Python SDK, you
don’t see job definitions in the Notebook Jobs dashboard. You can, however, view your
notebook jobs as described in [View notebook jobs](view-notebook-jobs.md "view-notebook-jobs.md").

You can control which team members can view your notebook jobs with the following
tags:

- To display the notebook to all user profiles or [spaces](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md") in a
  domain, add the domain tag with your domain name. An example is shown as
  follows:
  - key: `sagemaker:domain-name`, value:
    `d-abcdefghij5k`

- To display the notebook job to a certain user profile in a domain, add both the
  user profile and the domain tags. An example of a user profile tag is shown as
  follows:
  - key: `sagemaker:user-profile-name`, value:
    `studio-user`

- To display the notebook job to a [space](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md"), add both
  the space and the domain tags. An example of a space tag is shown as follows:
  - key: `sagemaker:shared-space-name`, value:
    `my-space-name`

- If you do not attach any domain or user profile or space tags, then the
  Studio UI does not show the notebook job created by pipeline step. In this case,
  you can view the underlying training job in the training job console or you can view
  the status in the [list of pipeline
  executions](pipelines-studio-view-execution.md "pipelines-studio-view-execution.md").

Once you set up the necessary tags to view your jobs in the dashboard, see [View notebook jobs](view-notebook-jobs.md "view-notebook-jobs.md") for instructions about
how to view your jobs and download outputs.

## View your pipeline graph in

Studio

Since your notebook job step is part of a pipeline, you can view the pipeline graph
(DAG) in Studio. In the pipeline graph, you can view the status of the pipeline run
and track lineage. For details, see [View the details of a pipeline run](pipelines-studio-view-execution.md "pipelines-studio-view-execution.md").

## Passing parameters to your

notebook

If you want to pass parameters to your notebook job (using the `parameters`
argument of `NotebookJobStep`), you need to prepare your input notebook to
receive the parameters.

The Papermill-based notebook job executor searches for a Jupyter cell tagged with the
`parameters` tag and applies the new parameters or parameter overrides
immediately after this cell. For details, see [Parameterize your notebook](notebook-auto-run-troubleshoot-override.md "notebook-auto-run-troubleshoot-override.md").

Once you have performed this step, pass your parameters to your
`NotebookJobStep`, as shown in the following example:

```
notebook_job_parameters = {
    "company": "Amazon"
}

notebook_job_step = NotebookJobStep(
    image_uri=`image-uri`,
    kernel_name=`kernel-name`,
    role=`role-name`,
    input_notebook=`input-notebook`,
    parameters=notebook_job_parameters,
    ...
)
```

## Connecting to an Amazon EMR cluster in your

input notebook

If you connect to an Amazon EMR cluster from your Jupyter notebook in Studio, you
might need to further modify your Jupyter notebook. See [Connect to an Amazon EMR cluster from your
notebook](scheduled-notebook-connect-emr.md "scheduled-notebook-connect-emr.md") if you need to perform any of the following tasks in your notebook:

- **Pass parameters into your Amazon EMR connection
  command.** Studio uses Papermill to run notebooks. In SparkMagic
  kernels, parameters you pass to your Amazon EMR connection command may not work as expected
  due to how Papermill passes information to SparkMagic.
- **Passing user credentials to Kerberos, LDAP, or HTTP Basic
  Auth-authenticated Amazon EMR clusters.** You have to pass user credentials
  through the AWS Secrets Manager.

## Set up default options

The SageMaker SDK gives you the option to set defaults for a subset of parameters so you
don’t have to specify these parameters every time you create a
`NotebookJobStep` instance. These parameters are `role`,
`s3_root_uri`, `s3_kms_key`, `volume_kms_key`,
`subnets`, and `security_group_ids`. Use the SageMaker AI config file to
set the defaults for the step. For information about the SageMaker AI configuration file, see
[Configuring and using defaults with the SageMaker Python SDK.](https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk "https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk").

To set up the notebook job defaults, apply your new defaults to the notebook job
section of the config file as shown in the following snippet:

```
SageMaker:
  PythonSDK:
    Modules:
      NotebookJob:
        RoleArn: 'arn:aws:iam::555555555555:role/IMRole'
        S3RootUri: 's3://amzn-s3-demo-bucket/my-project'
        S3KmsKeyId: 's3kmskeyid'
        VolumeKmsKeyId: 'volumekmskeyid1'
        VpcConfig:
          SecurityGroupIds:
            - 'sg123'
          Subnets:
            - 'subnet-1234'
```
