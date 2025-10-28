# Create a schedule to automatically

process new data

###### Note

The following section only applies to SageMaker Processing jobs. If you
used the default Canvas settings or EMR Serverless to create a
remote job to apply transforms to your full dataset, this section doesn’t apply.

If you're processing data periodically, you can create a schedule to run the
processing job automatically. For example, you can create a schedule that runs a
processing job automatically when you get new data. For more information about
processing jobs, see [Export to Amazon S3](canvas-export-data.md#canvas-export-data-s3 "canvas-export-data.md#canvas-export-data-s3").

When you create a job, you must specify an IAM role that has permissions to create
the job. You can use the [AmazonSageMakerCanvasDataPrepFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md") policy to add permissions.

Add the following trust policy to the role to allow EventBridge to assume it.

```

{
    "Effect": "Allow",
    "Principal": {
        "Service": "events.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
}

```

###### Important

When you create a schedule, Data Wrangler creates an `eventRule` in EventBridge. You
incur charges for both the event rules that you create and the instances used to run
the processing job.

For information about EventBridge pricing, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/"). For information about
processing job pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

You can set a schedule using one of the following methods:

- [CRON
  expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md")

###### Note

Data Wrangler doesn't support the following expressions:

    + LW#
    + Abbreviations for days
    + Abbreviations for months

- [RATE expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions")
- Recurring – Set an hourly or daily interval to run the job.
- Specific time – Set specific days and times to run the job.
  The following sections provide procedures on scheduling jobs when filling out the SageMaker AI
  Processing job settings while [exporting your data to Amazon S3](canvas-export-data.md#canvas-export-data-s3 "canvas-export-data.md#canvas-export-data-s3").
  All of the following instructions begin in the **Associate schedules** section of
  the SageMaker Processing job settings.

CRON
Use the following procedure to create a schedule with a CRON
expression.

1. In the **Export to Amazon S3** side panel, make sure
   you've turned off the **Auto job configuration** toggle and
   have the **SageMaker Processing** option selected.
2. In the **SageMaker Processing** job settings, open the
   **Associate schedules** section and choose
   **Create new schedule**.
3. The **Create new schedule** dialog box opens.
   For **Schedule Name**, specify the name of the
   schedule.
4. For **Run Frequency**, choose
   **CRON**.
5. For each of the **Minutes**, **Hours**,
   **Days of month**, **Month**,
   and **Day of week** fields, enter valid CRON expression values.
6. Choose **Create**.
7. (Optional) Choose **Add another schedule** to run
   the job on an additional schedule.

###### Note

You can associate a maximum of two schedules. The schedules
are independent and don't affect each other unless the times
overlap. 8. Choose one of the following:

    * **Schedule and run now** – The
     job runs immediately and subsequently runs on the
     schedules.
    * **Schedule only** – The job
     only runs on the schedules that you specify.

9. Choose **Export** after you've filled out the
   rest of the export job settings.

RATE
Use the following procedure to create a schedule with a RATE
expression.

1. In the **Export to Amazon S3** side panel, make sure
   you've turned off the **Auto job configuration** toggle and
   have the **SageMaker Processing** option selected.
2. In the **SageMaker Processing** job settings, open the
   **Associate schedules** section and choose
   **Create new schedule**.
3. The **Create new schedule** dialog box opens.
   For **Schedule Name**, specify the name of the
   schedule.
4. For **Run Frequency**, choose
   **Rate**.
5. For **Value**, specify an integer.
6. For **Unit**, select one of the following:
   - **Minutes**
   - **Hours**
   - **Days**

7. Choose **Create**.
8. (Optional) Choose **Add another schedule** to run
   the job on an additional schedule.

###### Note

You can associate a maximum of two schedules. The schedules
are independent and don't affect each other unless the times
overlap. 9. Choose one of the following:

    * **Schedule and run now** – The
     job runs immediately and subsequently runs on the
     schedules.
    * **Schedule only** – The job
     only runs on the schedules that you specify.

10. Choose **Export** after you've filled out
    the rest of the export job settings.

Recurring
Use the following procedure to create a schedule that runs a job on a
recurring basis.

1. In the **Export to Amazon S3** side panel, make sure
   you've turned off the **Auto job configuration** toggle and
   have the **SageMaker Processing** option selected.
2. In the **SageMaker Processing** job settings, open the
   **Associate schedules** section and choose
   **Create new schedule**.
3. The **Create new schedule** dialog box opens.
   For **Schedule Name**, specify the name of the
   schedule.
4. For **Run Frequency**, choose
   **Recurring**.
5. For **Every x hours**, specify the hourly
   frequency that the job runs during the day. Valid values are
   integers in the inclusive range of `1` and
   `23`.
6. For **On days**, select one of the following
   options:
   - **Every Day**
   - **Weekends**
   - **Weekdays**
   - **Select Days**
   1. (Optional) If you've selected **Select
      Days**, choose the days of the week to run the
      job.###### Note

The schedule resets every day. If you schedule a job to run
every five hours, it runs at the following times during the
day:

    * 00:00
    * 05:00
    * 10:00
    * 15:00
    * 20:00

7. Choose **Create**.
8. (Optional) Choose **Add another schedule** to run
   the job on an additional schedule.

###### Note

You can associate a maximum of two schedules. The schedules
are independent and don't affect each other unless the times
overlap. 9. Choose one of the following:

    * **Schedule and run now** – The
     job runs immediately and subsequently runs on the
     schedules.
    * **Schedule only** – The job
     only runs on the schedules that you specify.

10. Choose **Export** after you've filled out the rest of
    the export job settings.

Specific time
Use the following procedure to create a schedule that runs a job at
specific times.

1. In the **Export to Amazon S3** side panel, make sure
   you've turned off the **Auto job configuration** toggle and
   have the **SageMaker Processing** option selected.
2. In the **SageMaker Processing** job settings, open the
   **Associate schedules** section and choose
   **Create new schedule**.
3. The **Create new schedule** dialog box opens.
   For **Schedule Name**, specify the name of the
   schedule.
4. For **Run Frequency**, choose
   **Start time**.
5. For **Start time**, enter a time in UTC format
   (for example, `09:00`). The start time defaults
   to the time zone where you are located.
6. For **On days**, select one of the following
   options:
   - **Every Day**
   - **Weekends**
   - **Weekdays**
   - **Select Days**
   1. (Optional) If you've selected **Select
      Days**, choose the days of the week to run the
      job.

7. Choose **Create**.
8. (Optional) Choose **Add another schedule** to run
   the job on an additional schedule.

###### Note

You can associate a maximum of two schedules. The schedules
are independent and don't affect each other unless the times
overlap. 9. Choose one of the following:

    * **Schedule and run now** – The
     job runs immediately and subsequently runs on the
     schedules.
    * **Schedule only** – The job
     only runs on the schedules that you specify.

10. Choose **Export** after you've filled out the rest
    of the export job settings.

You can use the SageMaker AI AWS Management Console to view the jobs that are scheduled to run. Your
processing jobs run within Pipelines. Each processing job has its own pipeline. It runs as a
processing step within the pipeline. You can view the schedules that you've created
within a pipeline. For information about viewing a pipeline, see [View the details of a pipeline](pipelines-studio-list.md "pipelines-studio-list.md").

Use the following procedure to view the jobs that you've scheduled.

To view the jobs you've scheduled, do the following.

1. Open Amazon SageMaker Studio Classic.
2. Open Pipelines
3. View the pipelines for the jobs that you've created.

The pipeline running the job uses the job name as a prefix. For example, if
you've created a job named `housing-data-feature-enginnering`, the
name of the pipeline is
`canvas-data-prep-housing-data-feature-engineering`. 4. Choose the pipeline containing your job. 5. View the status of the pipelines. Pipelines with a **Status**
of **Succeeded** have run the processing job
successfully.
To stop the processing job from running, do the following:

To stop a processing job from running, delete the event rule that specifies the
schedule. Deleting an event rule stops all the jobs associated with the schedule from
running. For information about deleting a rule, see [Disabling or deleting an
Amazon EventBridge rule](../../../eventbridge/latest/userguide/eb-delete-rule.md "../../../eventbridge/latest/userguide/eb-delete-rule.md").

You can stop and delete the pipelines associated with the schedules as well. For
information about stopping a pipeline, see [StopPipelineExecution](../APIReference/API_StopPipelineExecution.md "../APIReference/API_StopPipelineExecution.md"). For information about deleting a pipeline, see
[DeletePipeline](../APIReference/API_DeletePipeline.md#API_DeletePipeline_RequestSyntax "../APIReference/API_DeletePipeline.md#API_DeletePipeline_RequestSyntax").
