# Running jobs

Jobs can be run in multiple ways depending on your workflow requirements.

## Run Methods

Ad-hoc

Run jobs immediately for testing or one-time processing tasks.

Run with custom parameters

Run a job immediately with custom parameter values that override the default job parameters
for this specific run only. This is useful for scenarios like data backfills where you might need
to temporarily increase compute resources without modifying the original job definition.

Workflow orchestration

Include jobs in Workflows for automated, scheduled run as part of data pipelines.

API/AWS CLI

Run jobs programmatically using AWS CLI or SDK for automation scenarios.

###### Note

SageMaker Unified Studio jobs use AWS Glue APIs. For more information, see
[AWS Glue API for Jobs](../../../glue/latest/dg/aws-glue-api-jobs.md "../../../glue/latest/dg/aws-glue-api-jobs.md").

## How to run a job

You can run jobs in SageMaker Unified Studio using several methods, depending on your requirements.

### To run a job:

1. Navigate to the **Jobs** section in your SageMaker Unified Studio project.
2. Select the job you want to run.
3. Choose the **Run** button in the action bar.
4. The job will immediately execute with its default parameters.

### To run a job with custom parameters:

1. Select the job you want to run.
2. Choose **Run with custom parameters** from the actions menu.
3. Modify any parameters you need to change for this specific run.
4. Choose **Run**.

This method is useful for scenarios like data backfills where you might need to temporarily increase compute resources
without modifying the original job definition. The custom parameters will only apply to this specific run and will not
affect the default parameters set on the job.

### To schedule a job

1. Navigate to the **Jobs** section in your SageMaker Unified Studio project.
2. Select the job you want to schedule.
3. Choose on the **Schedules** tab.
4. Choose **Add schedule**.
5. Set up a recurring schedule (daily, weekly, etc.) or use a cron expression.
6. Specify start time and timezone.
7. Choose **Save**.

The job will automatically run according to the schedule you set. This is ideal for jobs that need to run
on a regular basis without manual intervention.

### To run a job as part of a workflow

1. Navigate to the **Workflows** section in your SageMaker Unified Studio project.
2. Create a new workflow or edit an existing one.
3. Add your job to the workflow by selecting **Add node** and choosing **Data processing job**.
4. Select the job you want to include in the workflow.
5. Configure any workflow-specific settings for the job.
6. Save and run the workflow.

Running jobs as part of workflows allows you to orchestrate complex data pipelines with dependencies between different jobs.

### To run a job programmatically

You can use the AWS CLI or SDK to trigger job runs programmatically. SageMaker Unified Studio jobs use AWS Glue APIs under the hood.

Example using AWS CLI:

```

aws glue start-job-run --job-name "my-sagemaker-job" --region us-west-2
```

For more information on available parameters and options, see the
[AWS Glue API for Jobs](../../../glue/latest/dg/aws-glue-api-jobs.md "../../../glue/latest/dg/aws-glue-api-jobs.md") documentation.
