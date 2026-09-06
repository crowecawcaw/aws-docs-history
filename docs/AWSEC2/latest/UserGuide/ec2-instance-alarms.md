

# Manage CloudWatch alarms for your EC2 instances in the Amazon EC2 console
<a name="ec2-instance-alarms"></a>

From the **Instances** screen in the Amazon EC2 console, you can manage the Amazon CloudWatch alarms for your instances. In the **Instances** table, the **Alarm status** column provides two console controls: a control for viewing alarms, and another for creating or editing them. The following screenshot indicates these console controls, numbered **1** (**View alarms**) and **2** (a **\+** sign for creating or editing an alarm).

![The Instances table controls for viewing and creating alarms.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/instance-alarms.png)


## View alarms from the Instances screen
<a name="view-ec2-instance-alarms"></a>

You can view each instance's alarms from the **Instances** screen.

**To view an instance's alarm from the Instances screen**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. In the **Instances** table, for your chosen instance, choose **View alarms** (numbered **1** in the preceding screenshot).

1. In the **Alarm details for {{i-1234567890abcdef0}}** window, choose the alarm name to view the alarm in the CloudWatch console.

## Create alarms from the Instances screen
<a name="create-ec2-instance-alarms"></a>

You can create an alarm for each instance from the **Instances** screen.

**To create an alarm for an instance from the Instances screen**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. In the **Instances** table, for your chosen instance, choose the plus sign (numbered **2** in the preceding screenshot).

1. In the **Manage CloudWatch alarms** screen, create your alarm. For more information, see [Create a CloudWatch alarm for an instance](using-cloudwatch-createalarm.md).

## Edit alarms from the Instances screen
<a name="edit-ec2-instance-alarms"></a>

You can edit the alarm for an instance from the **Instances** screen.

**To edit an alarm for an instance from the Instances screen**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. In the **Instances** table, for your chosen instance, choose the plus sign (numbered **2** in the preceding screenshot).

1. In the **Manage CloudWatch alarms** screen, edit your alarm. For more information, see [Edit or delete a CloudWatch alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Manage-CloudWatch-Alarm.html#Edit-CloudWatch-Alarm) in the *Amazon CloudWatch User Guide*.