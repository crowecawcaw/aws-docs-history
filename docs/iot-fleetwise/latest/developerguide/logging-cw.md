

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Configure AWS IoT FleetWise logging
<a name="logging-cw"></a>

You can send your AWS IoT FleetWise log data to a CloudWatch log group. CloudWatch Logs give visibility in case AWS IoT FleetWise fails to process messages from vehicles. For example, this can happen because of a faulty configuration or other client errors. You're notified of any errors so you can identify and mitigate issues.

Before you can send logs to CloudWatch, you must create a CloudWatch log group. Configure the log group with the same account and in the same Region that you used with AWS IoT FleetWise. When you enable logging in AWS IoT FleetWise, provide the log group name. After logging is enabled, AWS IoT FleetWise delivers logs to the CloudWatch log group in log streams.

You can view log data sent from AWS IoT FleetWise in the CloudWatch console. For more information about configuring a CloudWatch log group and viewing log data, see [Working with Log Groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html). For more information on setting up logging for AWS services, see [AWS services that publish logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

## Permissions to publish logs to CloudWatch
<a name="cw-logs-permissions"></a>

Configuring logging for a CloudWatch log group requires the permissions settings described in this section. For information about managing permissions, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.

With these permissions, you can change the logging configuration, configure log delivery for CloudWatch, and retrieve information about your log group. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "iotfleetwise:PutLoggingOptions",
                "iotfleetwise:GetLoggingOptions"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow",
            "Sid": "IoTFleetwiseLoggingOptionsAPI"
        },
        {
            "Sid": "IoTFleetwiseLoggingCWL",
            "Action": [
                "logs:CreateLogDelivery",
                "logs:GetLogDelivery",
                "logs:UpdateLogDelivery",
                "logs:DeleteLogDelivery",
                "logs:ListLogDeliveries",
                "logs:PutResourcePolicy",
                "logs:DescribeResourcePolicies",
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

------

When actions are permitted on all AWS resources, it's indicated in the policy with a `"Resource"` setting of `"*"`. This means that the actions are permitted on all AWS resources *that each action supports*.

## Configure logging using the console
<a name="logging-console"></a>

This section describes how to use the AWS IoT FleetWise console to configure logging.

**To use the AWS IoT FleetWise console to configure logging**

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise/).

1. In the left pane, choose **Settings**.

1. In the **Logging** section of the **Settings** page, choose **Edit**.

1. In the **CloudWatch logging** section, enter the **Log group**.

1. To save your changes, choose **Submit**.

After you enable logging, you can view your log data in the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

## Configure logging using the CLI
<a name="logging-cli"></a>

This section describes how to configure logging for AWS IoT FleetWise by using the CLI.

You can also perform this procedure with the API by using the methods in the AWS API that correspond to the CLI commands shown here. You can use the [GetLoggingOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetLoggingOptions.html) API operation to fetch the current configuration and the [PutLoggingOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_PutLoggingOptions.html) API operation to modify the configuration.

**To use the CLI to configure logging for AWS IoT FleetWise**

1. To get the logging options for your account, use the **get-logging-options** command.

   ```
   aws iotfleetwise get-logging-options
   ```

1. To enable logging, use the **put-logging-options** command.

   ```
   aws iotfleetwise put-logging-options --cloud-watch-log-delivery logType={{ERROR}},logGroupName={{MyLogGroup}}
   ```

   where:  
**logType**  
The type of log to send data to CloudWatch Logs. To disable logging, change the value to `OFF`.  
**logGroupName**  
The CloudWatch Logs group the operation sends data to. Make sure you create the log group name before you enable logging for AWS IoT FleetWise.

After you enable logging, see [Search log entries using the AWS CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html#search-log-entries-cli).