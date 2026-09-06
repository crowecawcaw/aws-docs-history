

# Creating a storage capacity utilization alarm for your file system
<a name="alarm-low-primary-storage"></a>

We recommend that you do not exceed an average SSD storage capacity utilization of 80% on an ongoing basis. Occasional SSD storage utilization spikes above 80% are acceptable. Maintaining an average utilization under 80% provides you with enough capacity to increase your storage without encountering issues. The following procedure shows how to create a CloudWatch alarm that alerts you to when your file system's SSD storage utilization is approaching 80%. 

**To create a file system storage capacity utilization alarm**

You can use the `StorageCapacityUtilization` metric to create an alarm that is triggered when one or more of your FSx for ONTAP file systems have reached a storage utilization threshold. 

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  In the left navigation pane, under **Alarms**, choose **All alarms**. Then, choose **Create alarm**. Within the create alarm wizard, choose **Select metric**. 

1. In the **graph explorer**, choose the **Multi source query** tab. 

1. In the **query builder**, choose the following: 
   + For **Namespace**, select **AWS/FSx** > **Detailed File System Metrics**. 
   + For **Metric name**, select **MAX(StorageCapacityUtilization)**.
   + For **Filter by**, you can optionally include or exclude specific file systems by their ID. If you leave **Filter by** empty, your alarm will trigger when any of your file systems exceed your alarm’s storage capacity utilization threshold.
   + Leave the rest of the options empty, and choose **Graph query**. 

1. Choose **Select metric**. Back in the wizard, in the **Metric** section, give your metric a **Label**. We recommend keeping the **Period** to 5 minutes.

1.  Under **Conditions**, choose the **Static threshold type**, whenever your metric is **Greater/Equal to 80**. 

1. Choose **Next** to go to the **Configure actions** page. 

**To configure alarm actions**

You can configure a variety of actions for your alarm to trigger when it reaches the threshold you configure. In this example, we choose a Simple Notification Service (SNS) topic, but you can learn about other actions in [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

1. In the **Notification** section, choose an SNS topic to notify when your alarm is in the `ALARM` state. You can choose an existing topic or create a new one. You will receive a subscription notification that you need to confirm before you’ll receive alarm notifications to the email address. 

1. Choose **Next**. 

**To finish the alarm**

Follow these instructions to complete the process of creating your CloudWatch alarm. 

1. On the **Add name and description** page, give your alarm a name, and optionally a description, then choose **Next**. 

1. Review everything you’ve configured in the **Preview and create** page, and then choose **Create alarm**. 