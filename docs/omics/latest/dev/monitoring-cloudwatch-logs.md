

# Monitoring HealthOmics with CloudWatch Logs
<a name="monitoring-cloudwatch-logs"></a>

HealthOmics generates a variety of logs to help you understand and troubleshoot your runs. Logs are available in two places: CloudWatch and Amazon S3. 

By default, runs have logging turned on. You can optionally turn off logging for a run by setting `LogLevel = OFF` in the **startrun** request.

**Note**  
For service updates, configure and monitor your [Personal Health Dashboard](https://health.console.aws.amazon.com/health/home#/account/dashboard/open-issues). For more information on how to manage the dashboard, refer to [Getting started with your AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html).

**Topics**
+ [Log types for HealthOmics workflows](#log-descriptions)
+ [Logs in CloudWatch](#cloudwatch-logs)
+ [Logs in Amazon S3](#s3-logs)
+ [Interactive CloudWatch Logs in the CLI](#cloudwatch-logs-cli)
+ [Accessing CloudWatch Logs from the console](#cloudwatch-logs-console)

## Log types for HealthOmics workflows
<a name="log-descriptions"></a>

HealthOmics provides the following types of logs for workflows:
+ Engine logs – Engine logs such as `.nextflow.log` and `workflow.log` are produced by the underlying workflow engines (Nextflow, WDL, and CWL). These logs can help you troubleshoot workflow definition issues.
+ Run manifest logs – These logs provide high level information about each run task, such as task status, start time, stop time, and fail reason (if the task failed). 

  Run manifest logs also report resource utilization statistics that can be helpful for understanding resource optimization opportunities. These statistics include:
  + cpusAverage
  + cpusMaximum
  + cpusReserved
  + gpusReserved
  + memoryAverageGiB
  + memoryMaximumGiB
  + memoryReservedGiB
  + runningSeconds
+ Run logs – Run logs provide the overall run status and the time when individual tasks are starting, running, stopping, and completed. Run logs also give you visibility into file import and export steps. 
+ Task logs – Task logs provide detailed logging information about individual tasks in your run. The outputs in your task log depend on the task definition and where you use log statements in your code. If your task logs don't provide the level of insight you need, consider adding additional log statements to your task definition to produce more insightful task logs. 
+ Run cache logs – Run cache logs provide the overall status of run caches and the caching of task outputs. Run cache logs give you visibility into cache hits and misses for each run that uses caching. 
+ Outputs.json – For WDL and CWL workflows, HealthOmics delivers an engine-generated file, named `outputs.json`, to your Amazon S3 bucket after run completion. This files includes a list and a map of all outputs for the run. 

## Logs in CloudWatch
<a name="cloudwatch-logs"></a>

CloudWatch generates workflow logs for failed runs and successful runs. All logs are available for successful runs and failed runs.

You can find the CloudWatch workflow logs in the following log group: `/aws/omics/WorkflowLog`. Also, the output of the **get-run** API operation provides the CloudWatch log stream ARNs for the engine logs and run logs.

By default, AWS keeps the CloudWatch Logs indefinitely. You can adjust the retention policy for the log group to set a retention period between 10 years and one day. 

The following table provides a summary of the CloudWatch Logs in HealthOmics. All workflow logs are available for successful runs and failed runs. 


| Log name | Available in CloudWatch Logs | When is log available | Log stream format | 
| --- | --- | --- | --- | 
| Engine logs | Yes | In real time | run/{{runID}}/engine | 
| Run manifest logs | Yes | After run completes | manifest/run/{{runID}}/{{runUUID}} | 
| Run logs | Yes | In real time | run/{{runID}} | 
| Task logs | Yes | In real time | run/{{runID}}/task/{{taskID}} | 
| Run cache logs | Yes | In real time | runCache/{{runCacheId}}/{{runCacheUUID}} | 
| Outputs.json (WDL and CWL) | No | n/a | n/a | 

## Logs in Amazon S3
<a name="s3-logs"></a>

Among the [Log types for HealthOmics workflows](#log-descriptions), only the engine logs and the `outputs.json` file are delivered to Amazon S3.

After a run completes, the engine logs are delivered to your S3 bucket and are available indefinitely until you delete them. These logs are located in the logs directory of the S3 output URI that you specified for the workflow. 

The path to the logs directory has the following format: `s3://{user_provided_path}/logs/`.

The following table provides a summary of the HealthOmics logs available in your Amazon S3 bucket.


| Log name | Available in Amazon S3 | When is log available | Log stream path | 
| --- | --- | --- | --- | 
| Engine logs | Yes | After run completes | s3://{{user\_provided\_path}}/logs/engine.log | 
| Outputs.json (WDL and CWL) | Yes | After run completes | s3://{{user\_provided\_path}}/{{runID}}/{{runUUID}}/logs/outputs.json | 
| Run manifest logs, run logs, and task logs | No | n/a | n/a | 

## Interactive CloudWatch Logs in the CLI
<a name="cloudwatch-logs-cli"></a>

You can interactively view the CloudWatch Logs using the Live Tail command in interactive mode. You can track run progress in real time and define up to 5 keywords to highlight in the logs:

```
aws logs start-live-tail  \
  --mode interactive  \
  --log-group-identifiers arn:aws:logs:{{region}}:{{account-ID}}:log-group:/aws/omics/WorkflowLog
```

For more information, see [ Start live tail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html) in the AWS CLI Command Reference.

## Accessing CloudWatch Logs from the console
<a name="cloudwatch-logs-console"></a>

To access the logs for a run, you can link directly to these logs from the **Run details** page in HealthOmics console.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/).

1.  If required, open the left navigation pane (≡). Choose **Runs**.

1. Select the run from the Runs table.

1. In the run details page, you can choose any of these actions:

   1. From **Run summary**, choose **View run logs**. The console opens the run logs in the CloudWatch console.

   1. From **Run summary**, choose **View logs in Amazon S3**. The console opens the logs folder in the Amazon S3 console.

   1. From **Run tasks**, choose **View logs**, **View run logs** or **View run manifest logs** for a task. The console opens the logs in the CloudWatch console.

You can also navigate to the logs from the CloudWatch console:

1. Open the CloudWatch console [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. From the left menu, choose **Log groups**.

1. Select the `/aws/omics/WorkflowLog` group. 

   If the list of log groups is long, you can enter **omics** in the search text box to narrow down the list.

1. When the **Log group details** page opens, choose the log stream you want to view. The console displays the events for this log stream.