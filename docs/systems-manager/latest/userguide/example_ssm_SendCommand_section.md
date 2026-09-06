

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `SendCommand` with an AWS SDK or CLI
<a name="example_ssm_SendCommand_section"></a>

The following code examples show how to use `SendCommand`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_ssm_Scenario_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To run a command on one or more remote instances**  
The following `send-command` example runs an `echo` command on a target instance.  

```
aws ssm send-command \
    --document-name {{"AWS-RunShellScript"}} \
    --parameters '{{commands=["echo HelloWorld"]}}' \
    --targets {{"Key=instanceids,Values=i-1234567890abcdef0"}} \
    --comment {{"echo HelloWorld"}}
```
Output:  

```
{
    "Command": {
        "CommandId": "92853adf-ba41-4cd6-9a88-142d1EXAMPLE",
        "DocumentName": "AWS-RunShellScript",
        "DocumentVersion": "",
        "Comment": "echo HelloWorld",
        "ExpiresAfter": 1550181014.717,
        "Parameters": {
            "commands": [
                "echo HelloWorld"
            ]
        },
        "InstanceIds": [
            "i-0f00f008a2dcbefe2"
        ],
        "Targets": [],
        "RequestedDateTime": 1550173814.717,
        "Status": "Pending",
        "StatusDetails": "Pending",
        "OutputS3BucketName": "",
        "OutputS3KeyPrefix": "",
        "MaxConcurrency": "50",
        "MaxErrors": "0",
        "TargetCount": 1,
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
        }
    }
}
```
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To get IP information about an instance**  
The following `send-command` example retrieves the IP information about an instance.  

```
aws ssm send-command \
    --instance-ids {{"i-1234567890abcdef0"}} \
    --document-name {{"AWS-RunShellScript"}} \
    --comment {{"IP config"}} \
    --parameters {{"commands=ifconfig"}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 3: To run a command on instances with specific tags**  
The following `send-command` example runs a command on instances that have the tag key "ENV" and the value "Dev".  

```
aws ssm send-command \
    --targets {{"Key=tag:ENV,Values=Dev"}} \
    --document-name {{"AWS-RunShellScript"}} \
    --parameters {{"commands=ifconfig"}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 4: To run a command that sends SNS notifications**  
The following `send-command` example runs a command that sends SNS notifications for all notification events and the `Command` notification type.  

```
aws ssm send-command \
    --instance-ids {{"i-1234567890abcdef0"}} \
    --document-name {{"AWS-RunShellScript"}} \
    --comment {{"IP config"}} \
    --parameters {{"commands=ifconfig"}} \
    --service-role-arn {{"arn:aws:iam::123456789012:role/SNS_Role"}} \
    --notification-config {{"NotificationArn=arn:aws:sns:us-east-1:123456789012:SNSTopicName,NotificationEvents=All,NotificationType=Command"}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 5: To run a command that outputs to S3 and CloudWatch**  
The following `send-command` example runs a command that outputs command details to an S3 bucket and to a CloudWatch Logs log group.  

```
aws ssm send-command \
    --instance-ids {{"i-1234567890abcdef0"}} \
    --document-name {{"AWS-RunShellScript"}} \
    --comment {{"IP config"}} \
    --parameters {{"commands=ifconfig"}} \
    --output-{{s3-bucket-name}} "s3-bucket-name" \
    --output-s3-key-prefix {{"runcommand"}} \
    --cloud-watch-output-config {{"CloudWatchOutputEnabled=true,CloudWatchLogGroupName=CWLGroupName"}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 6: To run commands on multiple instances with different tags**  
The following `send-command` example runs a command on instances with two different tag keys and values.  

```
aws ssm send-command \
    --document-name {{"AWS-RunPowerShellScript"}} \
    --parameters commands=["echo helloWorld"] \
    --targets {{Key=tag:Env,Values=Dev}} {{Key=tag:Role,Values=WebServers}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 7: To target multiple instances with the same tag key**  
The following `send-command` example runs a command on instances that have the same tag key but with different values.  

```
aws ssm send-command \
    --document-name {{"AWS-RunPowerShellScript"}} \
    --parameters commands=["echo helloWorld"] \
    --targets {{Key=tag:Env,Values=Dev,Test}}
```
See example 1 for sample output.  
For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) in the *AWS Systems Manager User Guide*.  
**Example 8: To run a command that uses a shared document**  
The following `send-command` example runs a shared document on a target instance.  

```
aws ssm send-command \
    --document-name {{"arn:aws:ssm:us-east-1:123456789012:document/ExampleDocument"}} \
    --targets {{"Key=instanceids,Values=i-1234567890abcdef0"}}
```
See example 1 for sample output.  
For more information, see [Using shared SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [SendCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-command.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples). 

```
    /**
     * Sends a SSM command to a managed node asynchronously.
     *
     * @param documentName The name of the document to use.
     * @param instanceId The ID of the instance to send the command to.
     * @return The command ID.
     * <p>
     * This method initiates asynchronous requests to send a SSM command to a managed node.
     * It waits until the document is active, sends the command, and checks the command execution status.
     */
    public String sendSSMCommand(String documentName, String instanceId) throws InterruptedException, SsmException {
        // Before we use Document to send a command - make sure it is active.
        CompletableFuture<Void> documentActiveFuture = CompletableFuture.runAsync(() -> {
            boolean isDocumentActive = false;
            DescribeDocumentRequest request = DescribeDocumentRequest.builder()
                    .name(documentName)
                    .build();

            while (!isDocumentActive) {
                CompletableFuture<DescribeDocumentResponse> response = getAsyncClient().describeDocument(request);
                String documentStatus = response.join().document().statusAsString();
                if (documentStatus.equals("Active")) {
                    System.out.println("The SSM document is active and ready to use.");
                    isDocumentActive = true;
                } else {
                    System.out.println("The SSM document is not active. Status: " + documentStatus);
                    try {
                        Thread.sleep(5000);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
            }
        });

        documentActiveFuture.join();

        // Create the SendCommandRequest.
        SendCommandRequest commandRequest = SendCommandRequest.builder()
                .documentName(documentName)
                .instanceIds(instanceId)
                .build();

        // Send the command.
        CompletableFuture<SendCommandResponse> commandFuture = getAsyncClient().sendCommand(commandRequest);
        final String[] commandId = {null};

        commandFuture.whenComplete((commandResponse, ex) -> {
            if (commandResponse != null) {
                commandId[0] = commandResponse.command().commandId();
                System.out.println("Command ID: " + commandId[0]);

                // Wait for the command execution to complete.
                GetCommandInvocationRequest invocationRequest = GetCommandInvocationRequest.builder()
                        .commandId(commandId[0])
                        .instanceId(instanceId)
                        .build();

                try {
                    System.out.println("Wait 5 secs");
                    TimeUnit.SECONDS.sleep(5);

                    // Retrieve the command execution details.
                    CompletableFuture<GetCommandInvocationResponse> invocationFuture = getAsyncClient().getCommandInvocation(invocationRequest);
                    invocationFuture.whenComplete((commandInvocationResponse, invocationEx) -> {
                        if (commandInvocationResponse != null) {
                            // Check the status of the command execution.
                            CommandInvocationStatus status = commandInvocationResponse.status();
                            if (status == CommandInvocationStatus.SUCCESS) {
                                System.out.println("Command execution successful");
                            } else {
                                System.out.println("Command execution failed. Status: " + status);
                            }
                        } else {
                            Throwable invocationCause = (invocationEx instanceof CompletionException) ? invocationEx.getCause() : invocationEx;
                            throw new CompletionException(invocationCause);
                        }
                    }).join();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            } else {
                Throwable cause = (ex instanceof CompletionException) ? ex.getCause() : ex;
                if (cause instanceof SsmException) {
                    throw (SsmException) cause;
                } else {
                    throw new RuntimeException(cause);
                }
            }
        }).join();

        return commandId[0];
    }
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/SendCommand) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples). 

```
import { SendCommandCommand, SSMClient } from "@aws-sdk/client-ssm";
import { parseArgs } from "node:util";

/**
 * Send an SSM command to a managed node.
 * @param {{ documentName: string }}
 */
export const main = async ({ documentName }) => {
  const client = new SSMClient({});
  try {
    await client.send(
      new SendCommandCommand({
        DocumentName: documentName,
      }),
    );
    console.log("Command sent successfully.");
    return { Success: true };
  } catch (caught) {
    if (caught instanceof Error && caught.name === "ValidationError") {
      console.warn(`${caught.message}. Did you provide a valid document name?`);
    } else {
      throw caught;
    }
  }
};
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/SendCommandCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example runs an echo command on a target instance.**  

```
Send-SSMCommand -DocumentName "AWS-RunPowerShellScript" -Parameter @{commands = "echo helloWorld"} -Target @{Key="instanceids";Values=@("i-0cb2b964d3e14fd9f")}
```
**Output:**  

```
CommandId          : d8d190fc-32c1-4d65-a0df-ff5ff3965524
Comment            : 
CompletedCount     : 0
DocumentName       : AWS-RunPowerShellScript
ErrorCount         : 0
ExpiresAfter       : 3/7/2017 10:48:37 PM
InstanceIds        : {}
MaxConcurrency     : 50
MaxErrors          : 0
NotificationConfig : Amazon.SimpleSystemsManagement.Model.NotificationConfig
OutputS3BucketName : 
OutputS3KeyPrefix  : 
OutputS3Region     : 
Parameters         : {[commands, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
RequestedDateTime  : 3/7/2017 9:48:37 PM
ServiceRole        : 
Status             : Pending
StatusDetails      : Pending
TargetCount        : 0
Targets            : {instanceids}
```
**Example 2: This example shows how to run a command that accepts nested parameters.**  

```
Send-SSMCommand -DocumentName "AWS-RunRemoteScript" -Parameter @{ sourceType="GitHub";sourceInfo='{"owner": "me","repository": "amazon-ssm","path": "Examples/Install-Win32OpenSSH"}'; "commandLine"=".\Install-Win32OpenSSH.ps1"} -InstanceId i-0cb2b964d3e14fd9f
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example runs an echo command on a target instance.**  

```
Send-SSMCommand -DocumentName "AWS-RunPowerShellScript" -Parameter @{commands = "echo helloWorld"} -Target @{Key="instanceids";Values=@("i-0cb2b964d3e14fd9f")}
```
**Output:**  

```
CommandId          : d8d190fc-32c1-4d65-a0df-ff5ff3965524
Comment            : 
CompletedCount     : 0
DocumentName       : AWS-RunPowerShellScript
ErrorCount         : 0
ExpiresAfter       : 3/7/2017 10:48:37 PM
InstanceIds        : {}
MaxConcurrency     : 50
MaxErrors          : 0
NotificationConfig : Amazon.SimpleSystemsManagement.Model.NotificationConfig
OutputS3BucketName : 
OutputS3KeyPrefix  : 
OutputS3Region     : 
Parameters         : {[commands, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
RequestedDateTime  : 3/7/2017 9:48:37 PM
ServiceRole        : 
Status             : Pending
StatusDetails      : Pending
TargetCount        : 0
Targets            : {instanceids}
```
**Example 2: This example shows how to run a command that accepts nested parameters.**  

```
Send-SSMCommand -DocumentName "AWS-RunRemoteScript" -Parameter @{ sourceType="GitHub";sourceInfo='{"owner": "me","repository": "amazon-ssm","path": "Examples/Install-Win32OpenSSH"}'; "commandLine"=".\Install-Win32OpenSSH.ps1"} -InstanceId i-0cb2b964d3e14fd9f
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples). 

```
class DocumentWrapper:
    """Encapsulates AWS Systems Manager Document actions."""

    def __init__(self, ssm_client):
        """
        :param ssm_client: A Boto3 Systems Manager client.
        """
        self.ssm_client = ssm_client
        self.name = None

    @classmethod
    def from_client(cls):
        ssm_client = boto3.client("ssm")
        return cls(ssm_client)


    def send_command(self, instance_ids):
        """
        Sends a command to one or more instances.

        :param instance_ids: The IDs of the instances to send the command to.
        :return: The ID of the command.
        """
        try:
            response = self.ssm_client.send_command(
                InstanceIds=instance_ids, DocumentName=self.name, TimeoutSeconds=3600
            )
            return response["Command"]["CommandId"]
        except ClientError as err:
            logger.error(
                "Couldn't send command to %s. Here's why: %s: %s",
                self.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/SendCommand) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples). 

```
    TRY.
        DATA(lo_result) = lo_ssm->sendcommand(
            it_instanceids = it_instance_ids
            iv_documentname = iv_document_name
            iv_timeoutseconds = 3600 ).
        DATA(lo_command) = lo_result->get_command( ).
        IF lo_command IS BOUND.
          rv_command_id = lo_command->get_commandid( ).
          MESSAGE 'Command sent successfully.' TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_ssminvaliddocument.
        MESSAGE 'Invalid document.' TYPE 'I'.
      CATCH /aws1/cx_ssminvalidinstanceid.
        MESSAGE 'Invalid instance ID.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.