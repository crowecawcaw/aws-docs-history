

# Create a flow log that publishes to CloudWatch Logs
<a name="flow-logs-cwl-create-flow-log"></a>

You can create flow logs for your VPCs, subnets, or network interfaces. If you perform these steps as a user using a particular IAM role, ensure that the role has permissions to use the `iam:PassRole` action.

**Prerequisite**  
Verify that the IAM principal that you are using to make the request has permissions to call the `iam:PassRole` action.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{flow-log-role-name}}"
        }
    ]
}
```

------

**To create a flow log using the console**

1. Do one of the following:
   + Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/). In the navigation pane, choose **Network Interfaces**. Select the checkbox for the network interface.
   + Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). In the navigation pane, choose **Your VPCs**. Select the checkbox for the VPC.
   + Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). In the navigation pane, choose **Subnets**. Select the checkbox for the subnet.

1. Choose **Actions**, **Create flow log**.

1. For **Filter**, specify the type of traffic to log. Choose **All** to log accepted and rejected traffic, **Reject** to log only rejected traffic, or **Accept** to log only accepted traffic.

1. For **Maximum aggregation interval**, choose the maximum period of time during which a flow is captured and aggregated into one flow log record.

1. For **Destination**, choose **Send to CloudWatch Logs**.

1. For **Destination log group**, choose the name of an existing log group or enter the name of a new log group. If you enter a name, we create the log group when there is traffic to log.

1. For **Service access**, choose an existing [IAM service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) that has permissions to publish logs to CloudWatch Logs or choose to create a new service role.

1. For **Log record format**, select the format for the flow log record.
   + To use the default format, choose **AWS default format**.
   + To use a custom format, choose **Custom format** and then select fields from **Log format**.

1. For **Additional metadata**, select if you want to include metadata from Amazon ECS in the log format.

1. (Optional) Choose **Add new tag** to apply tags to the flow log.

1. Choose **Create flow log**.

**To create a flow log using the command line**

Use one of the following commands.
+ [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) (AWS CLI)
+ [New-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

The following AWS CLI example creates a flow log that captures all accepted traffic for the specified subnet. The flow logs are delivered to the specified log group. The `--deliver-logs-permission-arn` parameter specifies the IAM role required to publish to CloudWatch Logs.

```
aws ec2 create-flow-logs --resource-type {{Subnet}} --resource-ids {{subnet-1a2b3c4d}} --traffic-type ACCEPT --log-group-name {{my-flow-logs}} --deliver-logs-permission-arn arn:aws:iam::{{123456789101}}:role/{{publishFlowLogs}}
```