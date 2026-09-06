

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Set up OpsCenter
<a name="OpsCenter-setup"></a>

AWS Systems Manager uses an integrated setup experience to help you get started with OpsCenter and Explorer, which are tools in Systems Manager. Explorer is a customizable operations dashboard that reports information about your AWS resources. In this documentation, Explorer and OpsCenter setup is called *Integrated Setup*.

You must use Integrated Setup to set up OpsCenter with Explorer. Integrated Setup is only available in the AWS Systems Manager console. You can't set up Explorer and OpsCenter programmatically. For more information, see [Getting started with Systems Manager Explorer and OpsCenter](Explorer-setup.md). 

**Before you begin**  
When you set up OpsCenter, you enable default rules in Amazon EventBridge that automatically create OpsItems. The following table describes the default EventBridge rules that automatically create OpsItems. You can disable EventBridge rules in the OpsCenter **Settings** page under **OpsItem rules**. 

**Important**  
Your account is charged for OpsItems created by default rules. For more information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).



| Rule name | Description | 
| --- | --- | 
| SSMOpsItems-Autoscaling-instance-launch-failure | This rule creates OpsItems when the launch of an EC2 auto scaling instance failed.  | 
| SSMOpsItems-Autoscaling-instance-termination-failure | This rule creates OpsItems when the termination of an EC2 auto scaling instance failed. | 
| SSMOpsItems-EBS-snapshot-copy-failed | This rule creates OpsItems when the system failed to copy an Amazon Elastic Block Store (Amazon EBS) snapshot. | 
| SSMOpsItems-EBS-snapshot-creation-failed | This rule creates OpsItems when the system failed to create an Amazon EBS snapshot. | 
| SSMOpsItems-EBS-volume-performance-issue | This rule corresponds to an AWS Health tracking rule. The rule creates OpsItems whenever there is a performance issue with an Amazon EBS volume (health event = `AWS_EBS_DEGRADED_EBS_VOLUME_PERFORMANCE`). | 
| SSMOpsItems-EC2-issue | This rule corresponds to an AWS Health tracking rule for unexpected events that affect AWS services or resources. The rule creates OpsItems when, for example, a service sends communications about operational issues that are causing service degradation or to raise awarness about localized resource-level issues. For example, this rule creates an OpsItem for the following event: `AWS_EC2_OPERATIONAL_ISSUE`. | 
| SSMOpsItems-EC2-scheduled-change | This rule corresponds to an AWS Health tracking rule. AWS can schedule events for your instances, such as rebooting, stopping, or starting instances. The rule creates OpsItems for EC2 scheduled events. For more information about scheduled events, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the *Amazon EC2 User Guide*. | 
| SSMOpsItems-RDS-issue | This rule corresponds to an AWS Health tracking rule for unexpected events that affect AWS services or resources. The rule creates OpsItems when, for example, a service sends communications about operational issues that are causing service degradation or to raise awarness about localized resource-level issues. For example, this rule creates an OpsItem for the following events: `AWS_RDS_MYSQL_DATABASE_CRASHING_REPEATEDLY`, `AWS_RDS_EXPORT_TASK_FAILED`, and `AWS_RDS_CONNECTIVITY_ISSUE`.  | 
| SSMOpsItems-RDS-scheduled-change | This rule corresponds to an AWS Health tracking rule. The rule creates OpsItems for Amazon RDS scheduled events. Scheduled events provide information about upcoming changes to your Amazon RDS resources. Some events might recommend that you take action to avoid service disruptions. Other events occur automatically without any action on your part. Your resource might be temporarily unavailable during the scheduled change activity. For example, this rule creates an OpsItem for the following events: `AWS_RDS_SYSTEM_UPGRADE_SCHEDULED` and `AWS_RDS_MAINTENANCE_SCHEDULED`. For more information about scheduled events, see [Event type categories](https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html#event-type-categories) in the *AWS Health User Guide*.  | 
| SSMOpsItems-SSM-maintenance-window-execution-failed | This rule creates OpsItems when the processing of the Systems Manager maintenance window failed.  | 
| SSMOpsItems-SSM-maintenance-window-execution-timedout | This rule creates OpsItems when the launch of the Systems Manager maintenance window timed out.  | 

Use the following procedure to set up OpsCenter.

**To set up OpsCenter**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **OpsCenter**.

1. On the OpsCenter home page, choose **Get started**.

1. On the OpsCenter setup page, choose **Enable this option to have Explorer configure AWS Config and Amazon CloudWatch events to automatically create OpsItems based on commonly-used rules and events**. If you don't choose this option, OpsCenter remains disabled.
**Note**  
Amazon EventBridge (formerly Amazon CloudWatch Events) provides all functionality of CloudWatch Events and some new features, such as custom event buses, third-party event sources and schema registry.

1. Choose **Enable OpsCenter**.

After you enable OpsCenter, you can do the following from **Settings**:
+ Create CloudWatch alarms using the **Open CloudWatch console** button. For more information, see [Configure CloudWatch alarms to create OpsItems](OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md).
+ Enable operational insights. For more information, see [Analyzing operational insights to reduce OpsItems](OpsCenter-working-operational-insights.md).
+ Enable AWS Security Hub CSPM findings alarms. For more information, see [Understanding OpsCenter integration with AWS Security Hub CSPM](OpsCenter-applications-that-integrate.md#OpsCenter-integrate-with-security-hub).

**Topics**
+ [(Optional) Setting up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-setting-up-cross-account.md)
+ [(Optional) Set up Amazon SNS to receive notifications about OpsItems](OpsCenter-getting-started-sns.md)