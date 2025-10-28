# CloudWatch alarm groups and templates for monitoring your AWS media workflow

Workflow monitor alarms allow you to use existing CloudWatch metrics as the foundation of
alarms for your signal maps. You can create an alarm template group to sort
and classify the types of alarming that is important to your workflow.
Within each alarm template group, you create alarm templates with specific
CloudWatch metrics and parameters that you want to monitor. You can create your
own alarm templates or import recommended alarm templates created by AWS.
After creating an alarm template group and alarm templates within that
group, you can attach one or more of these alarm template groups to a signal
map.

You must create an alarm template group first. After you have created an
alarm template group, you can create your own templates or use recommended
templates created by AWS. If you want to create your own alarm templates,
continue on this page. For more information about importing recommended
templates, see: [Recommended templates](monitor-with-workflow-monitor-configure-alarms-recommended-templates.md "monitor-with-workflow-monitor-configure-alarms-recommended-templates.md")

This section covers the creation of CloudWatch alarms using workflow monitor. For more
information about how the CloudWatch service handles alarms and details of the
alarm components, see:
[Using CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_

## Creating alarm

template groups

Alarm template groups allow you to sort and classify the types of alarms that are important to your workflow.

###### To create an alarm template group

1. From the workflow monitor console's navigation pane, select **CloudWatch
   alarm templates**.
2. Select **Create alarm template group**.
3. Give the alarm template group a unique **Group name**
   and optional **Description**.
4. Select **Create**, You will be taken to the newly
   created alarm template group's details page.

## Creating alarm templates

You can create alarm templates with the CloudWatch metrics and parameters that you want to monitor.

###### To create an alarm template

1. From the alarm template group's details page, select **Create
   alarm template**.
2. Give the alarm template a unique **Template name**
   and optional **Description**.
3. In the **Choose metric** section:
   1. Select a **Target Resource Type**. The target
      resource type is a resource for the respective service, such as
      a channel for MediaLive and MediaPackage or a flow for MediaConnect.
   2. Select a **Metric Name**. This is the CloudWatch
      metric that acts as the foundation for the alarm. The list of
      metrics will change depending on the selected **Target
      Resource Type**.

4. In the **Alarm settings** section:

###### Note

For more information about how the CloudWatch service handles
alarms and details of the alarm components, see: [Using CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
_Amazon CloudWatch User Guide_

    1. Select the **Statistic**. This is a value
     such as a **Sum** or an
     **Average** that will be used to monitor
     the metric.
    2. Select the **Comparison Operator**. This
     field references the **Threshold** that you set
     in the next step.
    3. Set a **Threshold**. This is a numeric value
     that the **Comparison Operator** uses to
     determine greater than, less than, or equal to status.
    4. Set a **Period**. This is a time value,
     in seconds. The **Period** is the
     length of time that the **Statistic**,
     **Comparison Operator**, and
     **Threshold** interact to determine
     if the alarm gets triggered.
    5. Set the **Datapoints**. This value determines
     how many datapoints are needed to trigger the alarm.
    6. Select how to **Treat Missing Data**. This
     selection determines how this alarm reacts to missing
     data.

5. Select **Create** to complete the process.

An example of a completed alarm template could have the following
parameters: A MediaConnect flow **Target Resource
Type** is monitored for the Disconnections **Metric
Name**. The **Statistic** value is set to
Sum with a **Comparison Operator** of "greater than or
equal to" and a **Threshold** of 10. The
**Period** is set to 60 seconds, and only requires
1 out of 1 **Datapoints**. **Treat Missing
Data** is set to "ignore."

The result of these settings is: workflow monitor will monitor for disconnections on the
flow. If 10 or more disconnections occur within 60 seconds, the alarm will be
triggered. 10 or more disconnections in 60 seconds only needs to happen one time
for the alarm to be triggered.
