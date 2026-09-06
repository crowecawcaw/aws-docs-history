

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Parameter options for the register-task-with-maintenance-windows command
<a name="mw-cli-task-options"></a>

The **register-task-with-maintenance-window** command provides several options for configuring a task according to your needs. Some are required, some are optional, and some apply to only a single maintenance window task type.

This topic provides information about some of these options to help you work with samples in this tutorial section. For information about all command options, see **[register-task-with-maintenance-window](https://docs.aws.amazon.com/cli/latest/reference/ssm/register-task-with-maintenance-window.html)** in the *AWS CLI Command Reference*.

**Command option: `--task-arn`**  
The option `--task-arn` is used to specify the resource that the task operates on. The value that you specify depends on the type of task you're registering, as described in the following table.


**TaskArn formats for maintenance window tasks**  

| Maintenance window task type | TaskArn value | 
| --- | --- | 
| **`RUN_COMMAND`** and ** `AUTOMATION`** | `TaskArn` is the SSM document name or Amazon Resource Name (ARN). For example: <br />`AWS-RunBatchShellScript` <br />-or-<br />`arn:aws:ssm:{{region}}:111122223333:document/My-Document`. | 
| **`LAMBDA`** | `TaskArn` is the function name or ARN. For example: <br />`SSMMy-Lambda-Function`<br />-or-<br />`arn:aws:lambda:{{region}}:111122223333:function:SSMMyLambdaFunction`. The IAM policy for Maintenance Windows requires that you add the prefix `SSM` to Lambda function (or alias) names. Before you proceed to register this type of task, update its name in AWS Lambda to include `SSM`. For example, if your Lambda function name is `MyLambdaFunction`, change it to `SSMMyLambdaFunction`.  The Lambda function must be in the same account as the maintenance window when using the service-linked role. For cross-account invocation, use `--service-role-arn` with a custom role and add a resource-based policy on the target function.  | 
| **`STEP_FUNCTIONS`** | `TaskArn` is the state machine ARN. For example: <br />`arn:aws:states:us-east-2:111122223333:stateMachine:SSMMyStateMachine`. The IAM policy for maintenance windows requires that you prefix Step Functions state machine names with `SSM`. Before you register this type of task, you must update its name in AWS Step Functions to include `SSM`. For example, if your state machine name is `MyStateMachine`, change it to `SSMMyStateMachine`.  The state machine must be in the same account as the maintenance window. You can't invoke a state machine across accounts.  | 

**Command option: `--service-role-arn`**  
The role for AWS Systems Manager to assume when running the maintenance window task. 

For more information, see [Setting up Maintenance Windows](setting-up-maintenance-windows.md)

**Command option: `--task-invocation-parameters`**  
The `--task-invocation-parameters` option is used to specify the parameters that are unique to each of the four task types. The supported parameters for each of the four task types are described in the following table.

**Note**  
For information about using pseudo parameters in `--task-invocation-parameters` content, such as {{TARGET\_ID}}, see [Using pseudo parameters when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md). 

Task invocation parameters options for maintenance window tasks


| Maintenance window task type | Available parameters  | Example | 
| --- | --- | --- | 
| **`RUN_COMMAND`** | `Comment`<br />`DocumentHash`<br />`DocumentHashType`<br />`NotificationConfig`<br />`OutputS3BucketName`<br />`OutPutS3KeyPrefix`<br />`Parameters`<br />`ServiceRoleArn`<br />`TimeoutSeconds` |  <pre>"TaskInvocationParameters": {<br />        "RunCommand": {<br />            "Comment": "My Run Command task comment",<br />            "DocumentHash": "6554ed3d--truncated--5EXAMPLE",<br />            "DocumentHashType": "Sha256",<br />            "NotificationConfig": {<br />                "NotificationArn": "arn:aws:sns:{{region}}:123456789012:my-sns-topic-name",<br />                "NotificationEvents": [<br />                    "FAILURE"<br />                ],<br />                "NotificationType": "Invocation"<br />            },<br />            "OutputS3BucketName": "amzn-s3-demo-bucket",<br />            "OutputS3KeyPrefix": "{{S3-PREFIX}}",<br />            "Parameters": {<br />                "commands": [<br />                    "Get-ChildItem$env: temp-Recurse|Remove-Item-Recurse-force"<br />                ]<br />            },<br />            "ServiceRoleArn": "arn:aws:iam::123456789012:role/MyMaintenanceWindowServiceRole",<br />            "TimeoutSeconds": 3600<br />        }<br />    }</pre>  | 
| **`AUTOMATION`** | `DocumentVersion`<br />`Parameters` |  <pre>"TaskInvocationParameters": {<br />        "Automation": {<br />            "DocumentVersion": "3",<br />            "Parameters": {<br />                "instanceid": [<br />                    "{{TARGET_ID}}"<br />                ]<br />            }<br />        }<br />    }</pre>  | 
| **`LAMBDA`** | `ClientContext`<br />`Payload`<br />`Qualifier` |  <pre>"TaskInvocationParameters": {<br />        "Lambda": {<br />            "ClientContext": "ew0KICAi--truncated--0KIEXAMPLE",<br />            "Payload": "{ \"targetId\": \"{{TARGET_ID}}\", \"targetType\": \"{{TARGET_TYPE}}\" }",<br />            "Qualifier": "$LATEST"<br />        }<br />    }</pre>  | 
| **`STEP_FUNCTIONS`** | `Input`<br />`Name` |  <pre>"TaskInvocationParameters": {<br />        "StepFunctions": {<br />            "Input": "{ \"targetId\": \"{{TARGET_ID}}\" }",<br />            "Name": "{{INVOCATION_ID}}"<br />        }<br />    }</pre>  | 