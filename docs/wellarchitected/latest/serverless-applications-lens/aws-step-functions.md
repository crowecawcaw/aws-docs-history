# AWS Step Functions

AWS Step Functions offers both Standard or Express Workflow types. Standard Workflows are ideal
for long-running, durable, and auditable workflows. Express Workflows are ideal for
high-volume, event-processing workloads such as IoT data ingestion, streaming data
processing and transformation, and mobile application backends. A Standard Workflow has a
maximum duration of 1 year, compared to 5 minutes for an Express Workflow. Both Standard and
Express Workflows support execution history logging to Amazon CloudWatch Logs. Publishing logs doesn't
block or slow down executions, allowing you to select the log level required for the
workflow. When inspecting a workflow consider using [Amazon CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") to
interactively search and analyze your workflow log data. Using the [GetExecutionHistory](../../../step-functions/latest/apireference/API_GetExecutionHistory.md "../../../step-functions/latest/apireference/API_GetExecutionHistory.md") API to explore the execution history for Standard Workflows
may save you from writing code. AWS Step Functions state transitions are throttled using a token
bucket scheme. Estimate the state transitions expected and match to quotas for bucket size
and refill rates. Trade off between Standard Workflow with throttling, or Express Workflow
with unlimited bucket size and refill rate.

An Express Workflow can start either synchronously or asynchronously. Select a synchronous
invocation when you can wait for the result and prefer to develop applications without the
need to develop additional code to handle errors, retries, or execute parallel tasks.
Synchronous Express execution API calls do not contribute to the existing account capacity
limits. Step Functions will provide capacity on demand and will automatically scale with
sustained workloads. Surges in workloads may be throttled until capacity is available. A
Synchronous Express Workflow can be invoked from Amazon API Gateway, AWS Lambda, or by using the
[StartSyncExecution](../../../step-functions/latest/apireference/API_StartSyncExecution.md "../../../step-functions/latest/apireference/API_StartSyncExecution.md") API call.

Invoke an Asynchronous Express Workflow if you don’t require an immediate response
output such as messaging services, or data processing that other services don’t depend on.
An Asynchronous Express Workflow returns a confirmation the workflow has started, and you
poll Amazon CloudWatch Logs for the result. An Asynchronous Express Workflow can be started in response
to an event, by a nested workflow in Step Functions, or by using the [StartExecution](../../../step-functions/latest/apireference/API_StartExecution.md "../../../step-functions/latest/apireference/API_StartExecution.md") API call.
