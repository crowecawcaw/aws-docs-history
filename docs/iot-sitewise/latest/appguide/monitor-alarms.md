The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use SiteWise Monitor,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](iotsitewise-monitor-availability-change.md "iotsitewise-monitor-availability-change.md")

# Monitor with alarms in AWS IoT SiteWise Monitor

###### Note

The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use SiteWise Monitor,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](iotsitewise-monitor-availability-change.md "iotsitewise-monitor-availability-change.md").

Alarms alert you and your team when equipment or processes perform sub-optimally. Optimal
performance of a machine or process means that the values for certain metrics should be within a
range of high and low limits. When these metrics are outside their operating range, equipment
operators must be notified so that they can fix the issue. Alarms help you quickly identify
issues and notify operators to maximize performance of your equipment and processes.

###### Note

The alarm notifications feature isn't available in the China (Beijing) Region.

AWS IoT SiteWise Monitor supports two types of alarms:

- Alarms that detect in the AWS Cloud – You can view and customize the thresholds
  and notification settings for these alarms. You can also acknowledge and snooze these
  alarms.

###### Important

After you enable the alarms feature for your portals, members of your organization can create only AWS IoT Events alarms in your portals.

- External alarms – These alarms detect on external equipment and then send the
  alarm state to the AWS Cloud. You can't customize, acknowledge, or snooze these alarms.
  These alarms don't have any information other than their state.
  Alarms have the following states:

- **Normal** – The alarm is enabled but inactive. The equipment or
  process operates as expected.
- **Active** – The alarm is active. The equipment or process is
  outside its operating range and needs attention.
- **Acknowledged** – An operator acknowledged the state of the
  alarm.
- **Latched** – The alarm returned to normal but was active and no
  operator acknowledged it. The equipment or process requires attention to reset the alarm to
  normal.
- **Snoozed** – The alarm is inactive because an operator snoozed
  the alarm. The operator defines the duration for which the alarm snoozes. After that
  duration, the alarm returns to normal state.
- **Disabled** – The alarm is inactive and won't detect any
  changes.
  You can perform the following alarm-related tasks.

| Task                                                                                            | Required role                                           | Description                                                                                   |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create alarm definitions](create-alarms.md "create-alarms.md")                                 | Portal administrator                                    | Create alarm definitions on models to monitor properties associated with the models.          |
| [View alarm details in AWS IoT SiteWise Monitor](view-alarm-details.md "view-alarm-details.md") | Portal administrator, project owner, and project viewer | View details about the alarms that you can access.                                            |
| [Respond to alarms in AWS IoT SiteWise](respond-to-alarms.md "respond-to-alarms.md")            | Portal administrator, project owner, project viewer     | Acknowledge or snooze the alarms that you can access.                                         |
| [Configure alarms for AWS IoT SiteWise](configure-alarms.md "configure-alarms.md")              | Portal administrator, project owner                     | Customize the threshold and notification settings for the alarms that you can access.         |
| [Visualize alarms in dashboards](visualize-alarms.md "visualize-alarms.md")                     | Portal administrator, project owner                     | Add alarms to dashboards to visualize alarm state or alarms as thresholds in your dashboards. | ###### Topics <br>• [Create alarm definitions](create-alarms.md "create-alarms.md") <br>• [View alarm details in AWS IoT SiteWise Monitor](view-alarm-details.md "view-alarm-details.md") <br>• [Respond to alarms in AWS IoT SiteWise](respond-to-alarms.md "respond-to-alarms.md") <br>• [Configure alarms for AWS IoT SiteWise](configure-alarms.md "configure-alarms.md") <br>• [Visualize alarms in dashboards](visualize-alarms.md "visualize-alarms.md") |
