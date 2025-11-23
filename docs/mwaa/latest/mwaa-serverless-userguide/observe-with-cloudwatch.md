# Observability with CloudWatch

You may view and manage your workflows on the
[Amazon MWAA Serverless Console](https://us-east-2.console.aws.amazon.com/mwaa/home#serverlessWorkflows "https://us-east-2.console.aws.amazon.com/mwaa/home#serverlessWorkflows") however,
for advanced observability Amazon MWAA Serverless Serverless provides integration with Amazon CloudWatch where tasks logs are stored in a log group provided by you.
If you do not provide a log group name while creating a workflow, Amazon MWAA Serverless will create a new log group.

Amazon MWAA Serverless workflow execution status is returned via the `GetWorkflowRun` function.
The results from function returns details for a particular workflow run. If there are errors in the workflow definition, they are returned under `RunDetail` in the `ErrorMessage` field as in the following example:

JSON

```

{
  "WorkflowVersion": "7bcd36ce4d42f5cf23bfee67a0f816c6",
  "RunId": "d58cxqdClpTVjeN",
  "RunType": "SCHEDULE",
  "RunDetail": {
    "ModifiedAt": "2025-11-03T08:02:47.625851+00:00",
    "ErrorMessage": "expected token ',', got 'create_test_table'",
    "TaskInstances": [],
    "RunState": "FAILED"
  }
}

```

Workflows that are properly defined, but whose tasks fail, will return `"ErrorMessage": "Workflow execution failed":`

JSON

```

{
  "WorkflowVersion": "0ad517eb5e33deca45a2514c0569079d",
  "RunId": "ABC123456789def",
  "RunType": "SCHEDULE",
  "RunDetail": {
    "StartedOn": "2025-11-03T13:12:09.904466+00:00",
    "CompletedOn": "2025-11-03T13:13:57.620605+00:00",
    "ModifiedAt": "2025-11-03T13:16:08.888182+00:00",
    "Duration": "107",
    "ErrorMessage": "Workflow execution failed",
    "TaskInstances": [
      "ex_5496697b-900d-4008-8d6f-5e43767d6e36_create_bucket_1"
    ],
    "RunState": "FAILED"
  }
}

```

Log groups created by Amazon MWAA Serverless are available in Amazon CloudWatch log group `/aws/mwaa-serverless/`workflow id`/` (where `/`workflow id``  
 is the same string as the unique workflow id in the ARN of the workflow).
For specific task log streams, list the tasks for the workflow run and then get each task’s information. You can combine these operations into a single CLI command as shown below

CLI

```

aws mwaa-serverless list-task-instances
--workflow-arn arn:aws:airflow-serverless:us-east-2:111122223333:workflow/simple_s3_test-abc1234def
--run-id ABC123456789def
--region us-east-2
--query 'TaskInstances[].TaskInstanceId'
--output text | xargs -n 1 -I {} aws mwaa-serverless get-task-instance
--workflow-arn arn:aws:airflow-serverless:us-east-2:111122223333:workflow/simple_s3_test-abc1234def
--run-id ABC123456789def
--task-instance-id {}
--region us-east-2
--query '{Status: Status, StartedAt: StartedAt, LogStream: LogStream}'

```

The response of the above command will be similar to following when it runs successfully. When it fails, the status will be returned as `“FAILED”`

JSON

```

{
  "Status": "SUCCESS",
  "StartedAt": "2025-10-28T21:21:31.753447+00:00",
  "LogStream": "//aws/mwaa-serverless/simple_s3_test_3-abc1234def//workflow_id=simple_s3_test-abc1234def/run_id=ABC123456789def/task_id=list_objects/attempt=1.log"
}

```

Use the Amazon CloudWatch `LogStream` output to debug your workflow. For samples of creating detailed metrics and monitoring dashboard using
[AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md"),
[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"),
[Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md"), and
[Amazon EventBridge](../../../Meventbridge/latest/userguide/eb-what-is.md "../../../Meventbridge/latest/userguide/eb-what-is.md"), review the example in this
[GitHub repository](https://github.com/aws-samples/amazon-mwaa-examples/tree/main/serverless/mwaa_serverless_metrics_dashboard "https://github.com/aws-samples/amazon-mwaa-examples/tree/main/serverless/mwaa_serverless_metrics_dashboard").
