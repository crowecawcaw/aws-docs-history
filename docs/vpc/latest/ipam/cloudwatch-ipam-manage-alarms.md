# Manage alarms from IPAM console

You can create and manage Amazon CloudWatch alarms directly from the IPAM console. Alarms for [IPAM metrics](cloudwatch-ipam-ip-address-usage.md "cloudwatch-ipam-ip-address-usage.md") or [IPAM resource utilization metrics](cloudwatch-ipam-res-util.md "cloudwatch-ipam-res-util.md") that are in an INSUFFICIENT_DATA or ALARM state will appear as warning bars at the top of the console and as visual indicators in the left navigation next to **Monitoring**.

To manage alarms for specific resources, choose **Resources**, then choose a VPC, subnet, or pool. When the resource details page opens, choose the **Alarms** tab.

The **Alarms** tab displays all CloudWatch alarms associated with the selected resource. From this tab, you can view alarm details, monitor current states, and access alarm configuration options. The tab shows alarms from the `AWS/IPAM` namespace that are relevant to the resource you're viewing.

The following screenshot shows the alarm management interface in the IPAM console:

![](images/alarms.png)
The **Alarms** tab provides a detailed summary of the CloudWatch alarms in the `AWS/IPAM` Amazon CloudWatch namespace in the home Region of your IPAM:

- **Alarm name**: User-defined name of the CloudWatch alarm.
- **State**: Current state of the CloudWatch alarm:
  - **ALARM**: Metric is outside defined threshold.
  - **OK**: Metric is within defined threshold.
  - **INSUFFICIENT_DATA**: Not enough data to determine alarm
    state.

- **Metric**: The specific CloudWatch metric being monitored by the alarm.
- **Resource ID**: The unique identifier of the AWS resource that the alarm is monitoring.
- **Time last updated**: Date and time when the alarm state was last changed or evaluated.
- **Actions enabled**: Indicates whether CloudWatch actions are enabled for the alarm:

      + **Yes**: Alarm can trigger configured actions when conditions are met.
      + **No**: Alarm is monitoring but not executing actions.

  In addition, if you're viewing the utilization graphs on the **Monitoring** tab for a VPC, subnet, or pool, you can choose the option to create an alarm for the resource utilization. You're then redirected to the CloudWatch console with the resource and metric details pre-populated. From there, you can configure an alarm threshold to, for example, be notified when utilization reaches a specific percentage.
