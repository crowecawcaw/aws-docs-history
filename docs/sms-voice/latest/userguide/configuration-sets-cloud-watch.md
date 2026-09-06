

# Set up an Amazon CloudWatch event destination in AWS End User Messaging SMS
<a name="configuration-sets-cloud-watch"></a>

Amazon CloudWatch Logs is an AWS service that you can use to monitor, store, and access log files. When you create a CloudWatch event destination, AWS End User Messaging SMS sends the types of events you specified in the event destination to a CloudWatch group. To learn more about CloudWatch, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

**Prerequisites**

1. Before you can create a CloudWatch event destination, you must first create a CloudWatch group. For more information about creating log groups, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
**Important**  
You will need the Amazon Resource Name (ARN) of the CloudWatch group to create the event destination.

1. You must create an [IAM role](configuration-sets-cloud-watch-creating-role.md#configuration-sets-cloud-watch-creating-role.title) that allows AWS End User Messaging SMS to write to the log group.
**Important**  
You will need the Amazon Resource Name (ARN) of the IAM role to create the event destination.

1. You also have setup a configuration set to associate the event destinations with, see [Create a configuration set in AWS End User Messaging SMS](configuration-set-create.md).