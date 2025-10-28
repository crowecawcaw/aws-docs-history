# Create an AWS Transit Gateway Flow Logs record

that publishes to Amazon CloudWatch Logs

You can create flow logs for transit gateways. If you perform these steps as an IAM user,
ensure that you have permissions to use the `iam:PassRole` action. For
more information, see [Permissions for IAM users to pass a
role](flow-logs-cwl.md#flow-logs-iam-user "flow-logs-cwl.md#flow-logs-iam-user").

You can create an Amazon CloudWatch flow log
using either the Amazon VPC Console or the AWS CLI.

###### To create a transit gateway flow log using the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateways**.
3. Choose the checkboxes for one or more transit gateways and choose
   **Actions**, **Create flow
   log**.
4. For **Destination**, choose **Send to CloudWatch
   Logs**.
5. For **Destination log group**, choose the name of a
   current destination log group.

###### Note

If the destination log group does not yet exist, entering a new name
in this field will create a new destination log group. 6. For **IAM role**, specify the name of the role that has
permissions to publish logs to CloudWatch Logs. 7. For **Log record format**, select the format for the flow
log record.

    * To use the default format, choose **AWS default
     format**.
    * To use a custom format, choose **Custom format**
     and then select fields from **Log format**.

8. (Optional) Choose **Add new tag** to apply tags to the
   flow log.
9. Choose **Create flow log**.

###### To create a flow log using the command line

Use one of the following commands.

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md") (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md") (AWS Tools for Windows PowerShell)
  The following AWS CLI example creates a flow log that captures transit gateway information.
  The flow logs are delivered to a log group in CloudWatch Logs called
  `my-flow-logs`, in account 123456789101, using the IAM role
  `publishFlowLogs`.

```
aws ec2 create-flow-logs --resource-type TransitGateway --resource-ids tgw-1a2b3c4d --log-group-name my-flow-logs --deliver-logs-permission-arn arn:aws:iam::123456789101:role/publishFlowLogs
```
