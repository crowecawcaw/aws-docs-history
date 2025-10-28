# Working with parameters in Parameter Store using

Run Command commands

You can work with parameters in Run Command, a tool in AWS Systems Manager. For more
information, see [AWS Systems Manager Run Command](run-command.md "run-command.md").

## Running a String parameter using the

console

The following procedure walks you through the process of running a command
that uses a `String` parameter.

###### To run a String parameter using Parameter Store

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
   `AWS-RunPowerShellScript` (Windows) or
   `AWS-RunShellScript` (Linux).
5. For **Command parameters**, enter `echo
{{ssm:`parameter-name`}}`.
   For example: `echo {{ssm:/Test/helloWorld}}`.
6. In the **Targets** section, choose the managed nodes on which you want to
   run this operation by specifying tags, selecting instances or edge devices manually, or
   specifying a resource group.

###### Tip

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips. 7. For **Other parameters**:

    * For **Comment**, enter information about this command.
    * For **Timeout (seconds)**, specify the number of seconds for the
     system to wait before failing the overall command execution.

8. For **Rate control**:
   - For **Concurrency**, specify either a number or a percentage of
     managed nodes on which to run the command at the same time.

   ###### Note

   If you selected targets by specifying tags applied to managed nodes or by
   specifying AWS resource groups, and you aren't certain how many managed
   nodes are targeted, then restrict the number of targets that can run the
   document at the same time by specifying a percentage.
   - For **Error threshold**, specify when to stop running the command
     on other managed nodes after it fails on either a number or a percentage of nodes.
     For example, if you specify three errors, then Systems Manager stops sending the command when
     the fourth error is received. Managed nodes still processing the command might also
     send errors.

9. (Optional) For **Output options**, to save the command output to a file,
   select the **Write command output to an S3 bucket** box. Enter the bucket
   and prefix (folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile (for EC2 instances) or IAM service role (hybrid-activated
machines) assigned to the instance, not those of the IAM user performing this task.
For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") or [Create an IAM service role for a hybrid
environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, make sure that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 10. In the **SNS notifications** section, if you want notifications sent
about the status of the command execution, select the **Enable SNS
notifications** check box.

For more information about configuring Amazon SNS notifications for Run Command, see [Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 11. Choose **Run**. 12. In the **Command ID** page, in the **Targets
and outputs** area, select the button next to the ID of a
node where you ran the command, and then choose **View
output**. Verify that the output of the command is the
value you provided for the parameter, such as `This is my
 first parameter`.

## Running a parameter using the AWS CLI

###### Example 1: Simple command

The following example command includes a Systems Manager parameter named
`DNS-IP`. The value of this parameter is simply the IP
address of a node. This example uses an AWS Command Line Interface (AWS CLI) command to echo
the parameter value.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-RunShellScript" \
    --document-version "1" \
    --targets "Key=instanceids,Values=i-02573cafcfEXAMPLE" \
    --parameters "commands='echo {{ssm:DNS-IP}}'" \
    --timeout-seconds 600 \
    --max-concurrency "50" \
    --max-errors "0" \
    --region us-east-2
```

Windows

```
aws ssm send-command ^
    --document-name "AWS-RunPowerShellScript" ^
    --document-version "1" ^
    --targets "Key=instanceids,Values=i-02573cafcfEXAMPLE" ^
    --parameters "commands='echo {{ssm:DNS-IP}}'" ^
    --timeout-seconds 600 ^
    --max-concurrency "50" ^
    --max-errors "0" ^
    --region us-east-2
```

The command returns information like the following.

```
{
    "Command": {
        "CommandId": "c70a4671-8098-42da-b885-89716EXAMPLE",
        "DocumentName": "AWS-RunShellScript",
        "DocumentVersion": "1",
        "Comment": "",
        "ExpiresAfter": "2023-12-26T15:19:17.771000-05:00",
        "Parameters": {
            "commands": [
                "echo {{ssm:DNS-IP}}"
            ]
        },
        "InstanceIds": [],
        "Targets": [
            {
                "Key": "instanceids",
                "Values": [
                    "i-02573cafcfEXAMPLE"
                ]
            }
        ],
        "RequestedDateTime": "2023-12-26T14:09:17.771000-05:00",
        "Status": "Pending",
        "StatusDetails": "Pending",
        "OutputS3Region": "us-east-2",
        "OutputS3BucketName": "",
        "OutputS3KeyPrefix": "",
        "MaxConcurrency": "50",
        "MaxErrors": "0",
        "TargetCount": 0,
        "CompletedCount": 0,
        "ErrorCount": 0,
        "DeliveryTimedOutCount": 0,
        "ServiceRole": "",
        "NotificationConfig": {
            "NotificationArn": "",
            "NotificationEvents": [],
            "NotificationType": ""
        },
        "CloudWatchOutputConfig": {
            "CloudWatchLogGroupName": "",
            "CloudWatchOutputEnabled": false
        },
        "TimeoutSeconds": 600,
        "AlarmConfiguration": {
            "IgnorePollAlarmFailure": false,
            "Alarms": []
        },
        "TriggeredAlarms": []
    }
}
```

After a command execution completes, you can view more information about it
using the following commands:

- [get-command-invocation](../../../cli/latest/reference/ssm/get-command-invocation.md "../../../cli/latest/reference/ssm/get-command-invocation.md") – View detailed
  information about the command execution.
- [list-command-invocations](../../../cli/latest/reference/ssm/link-cli-ref-list-command-invocations.md "../../../cli/latest/reference/ssm/link-cli-ref-list-command-invocations.md") – View the command
  execution status on a specific managed node.
- [list-commands](../../../cli/latest/reference/ssm/link-cli-ref-list-commands.md "../../../cli/latest/reference/ssm/link-cli-ref-list-commands.md") – View the command execution
  status across managed nodes.

###### Example 2: Decrypt a `SecureString` parameter value

The next example command uses a `SecureString` parameter named
**SecurePassword**. The command used in the
`parameters` field retrieves and decrypts the value of the
`SecureString` parameter, and then resets the local
administrator password without having to pass the password in clear
text.

Linux

```
aws ssm send-command \
        --document-name "AWS-RunShellScript" \
        --document-version "1" \
        --targets "Key=instanceids,Values=i-02573cafcfEXAMPLE" \
        --parameters '{"commands":["secure=$(aws ssm get-parameters --names SecurePassword --with-decryption --query Parameters[0].Value --output text --region us-east-2)","echo $secure | passwd myuser --stdin"]}' \
        --timeout-seconds 600 \
        --max-concurrency "50" \
        --max-errors "0" \
        --region us-east-2
```

Windows

```
aws ssm send-command ^
        --document-name "AWS-RunPowerShellScript" ^
        --document-version "1" ^
        --targets "Key=instanceids,Values=i-02573cafcfEXAMPLE" ^
        --parameters "commands=['$secure = (Get-SSMParameterValue -Names SecurePassword -WithDecryption $True).Parameters[0].Value','net user administrator $secure']" ^
        --timeout-seconds 600 ^
        --max-concurrency "50" ^
        --max-errors "0" ^
        --region us-east-2
```

###### Example 3: Reference a parameter in an SSM document

You can also reference Systems Manager parameters in the
_Parameters_ section of an SSM document, as shown
in the following example.

```
{
   "schemaVersion":"2.0",
   "description":"Sample version 2.0 document v2",
   "parameters":{
      "commands" : {
        "type": "StringList",
        "default": ["**{{ssm:`parameter-name`}}**"]
      }
    },
    "mainSteps":[
       {
          "action":"aws:runShellScript",
          "name":"runShellScript",
          "inputs":{
             "runCommand": "{{commands}}"
          }
       }
    ]
}
```

Don't confuse the similar syntax for _local parameters_
used in the `runtimeConfig` section of SSM documents with Parameter Store
parameters. A local parameter isn't the same as a Systems Manager parameter. You can
distinguish local parameters from Systems Manager parameters by the absence of the
`ssm:` prefix.

```
"runtimeConfig":{
        "aws:runShellScript":{
            "properties":[
                {
                    "id":"0.aws:runShellScript",
                    "runCommand":"**{{ commands }}**",
                    "workingDirectory":"**{{ workingDirectory }}**",
                    "timeoutSeconds":"**{{ executionTimeout }}**"
```

###### Note

SSM documents don't support references to `SecureString`
parameters. This means that to use `SecureString` parameters
with, for example, Run Command, you have to retrieve the parameter value before
passing it to Run Command, as shown in the following examples.

Linux & macOS

```
value=$(aws ssm get-parameters --names `parameter-name` --with-decryption)
```

```
aws ssm send-command \
    --name AWS-JoinDomain \
    --parameters password=`$value` \
    --instance-id `instance-id`
```

Windows

```
aws ssm send-command ^
    --name AWS-JoinDomain ^
    --parameters password=`$value` ^
    --instance-id `instance-id`
```

Powershell

```
$`secure` = (Get-SSMParameterValue -Names `parameter-name` -WithDecryption $True).Parameters[0].Value | ConvertTo-SecureString -AsPlainText -Force
```

```
$cred = New-Object System.Management.Automation.PSCredential -argumentlist `user-name`,$`secure`
```
