

# Managing logging for workflows
<a name="cloudwatch-workflows"></a>

CloudWatch provides consolidated auditing and logging for workflow progress and results. Additionally, AWS Transfer Family provides several metrics for workflows. You can view metrics for how many workflows executions started, completed successfully, and failed in the previous minute. All of the CloudWatch metrics for Transfer Family are described in [Using CloudWatch metrics for Transfer Family servers](metrics.md).

AWS Transfer Family provides two ways to deliver managed workflow execution logs to Amazon CloudWatch:
+ **A log group that you specify (structured log destination)** – You specify a CloudWatch Logs log group as a structured log destination for the workflow, and Transfer Family delivers the workflow execution logs to that log group for you. This option does not require a logging role. To use it, provide the Amazon Resource Name (ARN) of a log group in the `StructuredLogDestinations` parameter when you create the workflow (see [StructuredLogDestinations](https://docs.aws.amazon.com/transfer/latest/APIReference/API_CreateWorkflow.html#TransferFamily-CreateWorkflow-request-StructuredLogDestinations) in the *AWS Transfer Family API Reference*). The log group must be in the same AWS account and AWS Region as the workflow.

  To configure a structured log destination, the IAM policy for the principal that creates the workflow must contain the following permissions:
  + `logs:CreateLogDelivery`
  + `logs:DeleteLogDelivery`
  + `logs:DescribeLogGroups`
  + `logs:DescribeResourcePolicies`
  + `logs:GetLogDelivery`
  + `logs:ListLogDeliveries`
  + `logs:PutResourcePolicy`
  + `logs:UpdateLogDelivery`
+ **A logging role** – You attach an IAM logging role to the server that the workflow is attached to. Transfer Family assumes the role to write the workflow execution logs to a log group named `/aws/transfer/{{server-id}}`. For details, see [Configure CloudWatch logging role](configure-cw-logging-role.md).

Both mechanisms write the same workflow execution log content in the same JSON format. The difference is only where the logs are delivered: to the log group that you specify, or to the `/aws/transfer/{{server-id}}` log group on the server by way of the logging role.

**View Amazon CloudWatch logs for workflows**

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **Logs**, then choose **Log groups**.

1. On the **Log groups** page, on the navigation bar, choose the correct Region for your AWS Transfer Family server.

1. Choose the log group that contains your workflow logs.
   + If the workflow uses a structured log destination, choose the log group whose ARN you specified in the `StructuredLogDestinations` parameter of the workflow.
   + If the workflow uses a logging role on the server, choose the log group that corresponds to your server. For example, if your server ID is `s-1234567890abcdef0`, your log group is `/aws/transfer/s-1234567890abcdef0`.

1. On the log group details page, the most recent log streams are displayed. The log stream name for the workflow depends on which logging mechanism the workflow uses:
   + For a structured log destination, the workflow log stream is named `{{workflowID}}/{{executionID}}`. For example:

     ```
     w-abcdef01234567890/021345abcdef6789
     ```
   + For a logging role, the server log group contains two log streams for the user that you are exploring: one for each Secure Shell (SSH) File Transfer Protocol (SFTP) session, and one for the workflow that is being executed. The format for the workflow log stream is `{{username}}.{{workflowID}}.{{uniqueStreamSuffix}}`.

   For example, if your user is `mary-major`, you have the following log streams:

   ```
   mary-major-east.1234567890abcdef0
   mary.w-abcdef01234567890.021345abcdef6789
   ```
**Note**  
 The 16-digit alphanumeric identifiers listed in this example are fictitious. The values that you see in Amazon CloudWatch are different. 

The **Log events** page for a workflow log stream contains the details for the workflow execution. If the workflow uses a logging role, the `mary-major-usa-east.1234567890abcdef0` stream displays the details for each user session, and the `mary.w-abcdef01234567890.021345abcdef6789` stream contains the details for the workflow. If the workflow uses a structured log destination, the `w-abcdef01234567890/021345abcdef6789` stream contains the details for the workflow. 

 The following is a sample log stream for `mary.w-abcdef01234567890.021345abcdef6789`, based on a workflow (`w-abcdef01234567890`) that contains a copy step. 

```
{
    "type": "ExecutionStarted",
    "details": {
        "input": {
            "initialFileLocation": {
                "bucket": "amzn-s3-demo-bucket",
                "key": "mary/workflowSteps2.json",
                "versionId": "{{version-id}}",
                "etag": "{{etag-id}}"
            }
        }
    },
    "workflowId":"w-abcdef01234567890",
    "executionId":"{{execution-id}}",
    "transferDetails": {
        "serverId":"s-{{server-id}}",
        "username":"mary",
        "sessionId":"{{session-id}}"
    }
},
{
    "type":"StepStarted",
    "details": {
        "input": {
            "fileLocation": {
                "backingStore":"S3",
                "bucket":"amzn-s3-demo-bucket",
                "key":"mary/workflowSteps2.json",
                "versionId":"{{version-id}}",
                "etag":"{{etag-id}}"
            }
        },
        "stepType":"COPY",
        "stepName":"copyToShared"
    },
    "workflowId":"w-abcdef01234567890",
    "executionId":"{{execution-id}}",
    "transferDetails": {
        "serverId":"s-{{server-id}}",
        "username":"mary",
        "sessionId":"{{session-id}}"
    }
},
{
    "type":"StepCompleted",
    "details":{
        "output":{},
        "stepType":"COPY",
        "stepName":"copyToShared"
    },
    "workflowId":"w-abcdef01234567890",
    "executionId":"{{execution-id}}",
    "transferDetails":{
        "serverId":"{{server-id}}",
        "username":"mary",
        "sessionId":"{{session-id}}"
    }
},
{
    "type":"ExecutionCompleted",
    "details": {},
    "workflowId":"w-abcdef01234567890",
    "executionId":"{{execution-id}}",
    "transferDetails":{
        "serverId":"s-{{server-id}}",
        "username":"mary",
        "sessionId":"{{session-id}}"
    }
}
```