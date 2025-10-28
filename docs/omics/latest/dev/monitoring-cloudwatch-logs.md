AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Monitoring HealthOmics with CloudWatch Logs

HealthOmics generates a variety of logs to help you understand and troubleshoot your runs. Logs are available in two
places: CloudWatch and Amazon S3.

By default, runs have logging turned on. You can optionally turn off logging for a run by setting `LogLevel
 = OFF` in the **startrun** request.

###### Note

For service updates, configure and monitor your [Personal Health Dashboard](https://health.console.aws.amazon.com/health/home#/account/dashboard/open-issues "https://health.console.aws.amazon.com/health/home#/account/dashboard/open-issues").
For more information on how to manage the dashboard, refer to
[Getting started with your AWS Health Dashboard](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md").

###### Topics

- [Log types for HealthOmics workflows](#log-descriptions "#log-descriptions")
- [Logs in CloudWatch](#cloudwatch-logs "#cloudwatch-logs")
- [Logs in Amazon S3](#s3-logs "#s3-logs")
- [Interactive CloudWatch Logs in the CLI](#cloudwatch-logs-cli "#cloudwatch-logs-cli")
- [Accessing CloudWatch Logs from the console](#cloudwatch-logs-console "#cloudwatch-logs-console")

## Log types for HealthOmics workflows

HealthOmics provides the following types of logs for workflows:

- Engine logs – The underlying workflow engines (Nextflow, WDL, and CWL) produce engine logs for runs.
  These logs can help you troubleshoot workflow definition issues.
- Run manifest logs – These logs provide high level information about each run task, such as task status,
  start time, stop time, and fail reason (if the task failed).

Run manifest logs also report resource utilization statistics that can be helpful for understanding
resource optimization opportunities. These statistics include:

    + cpusAverage
    + cpusMaximum
    + cpusReserved
    + gpusReserved
    + memoryAverageGiB
    + memoryMaximumGiB
    + memoryReservedGiB
    + runningSeconds

- Run logs – Run logs provide the overall run status and the time when individual tasks are starting,
  running, stopping, and completed. Run logs also give you visibility into file import and export steps.
- Task logs – Task logs provide detailed logging information about individual tasks in your run. The
  outputs in your task log depend on the task definition and where you use log statements in your code. If your
  task logs don't provide the level of insight you need, consider adding additional log statements to your task
  definition to produce more insightful task logs.
- Run cache logs – Run cache logs provide the overall status of run caches and the caching of task outputs.
  Run cache logs give you visibility into cache hits and misses for each run that uses caching.
- Outputs.json – For WDL and CWL workflows, HealthOmics delivers an engine-generated file, named
  `outputs.json`, to your Amazon S3 bucket after run completion. This files includes a list and a map of
  all outputs for the run.

## Logs in CloudWatch

CloudWatch generates workflow logs for failed runs and successful runs. All logs are available for failed runs and
successful runs, except engine logs are available only for failed runs.

You can find the CloudWatch workflow logs in the following log group: `/aws/omics/WorkflowLog`. Also, the
output of the **get-run** API operation provides the CloudWatch log stream ARNs for the engine logs and
run logs.

By default, AWS keeps the CloudWatch Logs indefinitely. You can adjust the retention policy for the log group to set
a retention period between 10 years and one day.

The following table provides a summary of the CloudWatch Logs in HealthOmics. All workflow logs are available for successful
runs and failed runs, except engine logs are available only for failed runs.

| Log name                                   | Available in CloudWatch Logs | When is log available | Log stream format                                             |
| ------------------------------------------ | ---------------------------- | --------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Engine logs                                | Yes, for failed runs         | After run completes   | run/`runID`/engine                                            |
| Run manifest logs                          | Yes                          | After run completes   | manifest/run/`runID`/`runUUID`                                |
| Run logs                                   | Yes                          | In real time          | run/`runID`                                                   |
| Task logs                                  | Yes                          | In real time          | run/`runID`/task/`taskID`                                     |
| Run cache logs                             | Yes                          | In real time          | runCache/`runCacheId`/`runCacheUUID`                          |
| Outputs.json (WDL and CWL)                 | No                           | n/a                   | n/a                                                           | ## Logs in Amazon S3 Only the engine logs and the `outputs.json` file are delivered to Amazon S3. After a run completes, the engine logs are delivered to your S3 bucket and are available indefinitely until you delete them. These logs are located in the logs directory of the S3 output URI that you specified for the workflow. The path to the logs directory has the following format: `s3://{user_provided_path}/logs/`. The following table provides a summary of the HealthOmics logs available in your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Log name                                   | Available in Amazon S3       | When is log available | Log stream path                                               |
| ---                                        | ---                          | ---                   | ---                                                           |
| Engine logs                                | Yes                          | After run completes   | s3://`user_provided_path`/logs/engine.log                     |
| Outputs.json (WDL and CWL)                 | Yes                          | After run completes   | s3://`user_provided_path`/`runID`/`runUUID`/logs/outputs.json |
| Run manifest logs, run logs, and task logs | No                           | n/a                   | n/a                                                           | ## Interactive CloudWatch Logs in the CLI You can interactively view the CloudWatch Logs using the Live Tail command in interactive mode. You can track run progress in real time and define up to 5 keywords to highlight in the logs: ``aws logs start-live-tail  \ --mode interactive  \ --log-group-identifiers arn:aws:logs:`region`:`account-ID`:log-group:/aws/omics/WorkflowLog`` For more information, see [Start live tail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html") in the AWS CLI Command Reference. ## Accessing CloudWatch Logs from the console To access the logs for a run, you can link directly to these logs from the **Run details** page in HealthOmics console. 1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/"). 2. If required, open the left navigation pane (≡). Choose **Runs**. 3. Select the run from the Runs table. 4. In the run details page, you can choose any of these actions: 1. From **Run summary**, choose **View run logs**. The console opens the run logs in the CloudWatch console. 2. From **Run summary**, choose **View logs in Amazon S3**. The console opens the logs folder in the Amazon S3 console. 3. From **Run tasks**, choose **View logs**, **View run logs** or **View run manifest logs** for a task. The console opens the logs in the CloudWatch console. You can also navigate to the logs from the CloudWatch console: 1. Open the CloudWatch console [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). 2. From the left menu, choose **Log groups**. 3. Select the `/aws/omics/WorkflowLog` group. If the list of log groups is long, you can enter **omics** in the search text box to narrow down the list. 4. When the **Log group details** page opens, choose the log stream you want to view. The console displays the events for this log stream. |
