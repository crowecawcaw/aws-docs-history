

# Create a AWS Cloud WAN Flow Logs record that publishes to Amazon CloudWatch Logs
<a name="cwan-flow-logs-cwl-create-flow-log"></a>

You can create flow logs for core networks. If you perform these steps as an IAM user, ensure that you have permissions to use the `iam:PassRole` action. For more information, see [Permissions for IAM users to pass a role](cwan-flow-logs-cwl.md#cwan-flow-logs-iam-user).

You can create an Amazon CloudWatch flow log using either the Network Manager console or the AWS CLI.

**To create a Cloud WAN flow log using the console**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Choose either **Core networks** or **Attachments**, and then select one or more core networks or attachments.

1. Choose **Actions**, **Create flow log**.

1. For **Destination**, choose **Send to CloudWatch Logs**.

1. For **Destination log group**, choose the name of a current destination log group.
**Note**  
If the destination log group does not yet exist, entering a new name in this field will create a new destination log group.

1. For **IAM role**, specify the name of the role that has permissions to publish logs to CloudWatch Logs.

1. For **Log record format**, select the format for the flow log record.
   + To use the default format, choose **AWS default format**.
   + To use a custom format, choose **Custom format** and then select fields from **Log format**.

1. (Optional) Choose **Add new tag** to apply tags to the flow log.

1. Choose **Create flow log**.

Use one of the following commands.

**To create a flow log using the command line**
+ [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) (AWS CLI)
+ [New-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

The following AWS CLI example creates a flow log that captures core network information. The flow logs are delivered to a log group in CloudWatch Logs called `my-flow-logs`, in account 123456789101, using the IAM role `publishFlowLogs`.

```
aws ec2 create-flow-logs --resource-type CoreNetwork --resource-ids core-network-1a2b3c4d --log-group-name my-flow-logs --deliver-logs-permission-arn arn:aws:iam::123456789101:role/publishFlowLogs 
```