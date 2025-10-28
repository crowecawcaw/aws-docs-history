# MediaConnect flow maintenance

AWS Elemental MediaConnect routinely performs maintenance on underlying systems for security, reliability,
and operational performance. The maintenance activities include actions such as patching the
operating system, updating drivers, or installing software and patches.

###### Note

As part of the maintenance process, your flow must be restarted.

You can select the day and time that maintenance events occur. This is called a _maintenance window_ and is used every time a maintenance event
is required. If you need to change the day and time, you can edit the maintenance
window.

When maintenance is required for your flow, AWS will assign your flow a
**Required by** date. If you do not have a maintenance window
configured for the flow, visit [Setting maintenance
windows](setting-flow-maintenance.md "setting-flow-maintenance.md"). You can view the flows that require maintenance on the MediaConnect console or
by using the AWS CLI, visit [Viewing flows that
require maintenance](viewing-flows-maintenance.md "viewing-flows-maintenance.md"). When a **Required by** date has been
assigned to your flow, you can select a specific date for that maintenance to occur. The
selected **Maintenance date** will only apply to the next maintenance
event.

If you do not configure a maintenance window, AWS selects a maintenance window for
you—automatically. We recommend that you set a maintenance window for each flow and allow
MediaConnect to perform the restart automatically during that window. Allowing MediaConnect to perform the
restart results in less downtime for your flow. If a flow requires maintenance and you
choose to manually restart the flow, the status of that flow's maintenance will change to
**Canceled**. The manually restarted flow will still apply the required
updates, but you will not receive the **Completed successfully** status.
Since you performed the restart manually, the maintenance is considered
**Canceled** because MediaConnect no longer requires updates for that flow.

The
duration of the maintenance window is two hours.

###### Important

The two hour window duration does not mean the flow will be affected for two hours.
The flow will perform a normal stop and start at some point within the two hour
window.

Example: If you configure a flow's maintenance window **Start hour** to
be 02:00, the flow will restart at some point between 02:00 and
04:00.

In the event that maintenance does not occur at the scheduled date and time, MediaConnect will
reschedule it to occur in the following week’s maintenance window, or automatically set a
new window if you don't have one configured.

###### Topics

- [Viewing MediaConnect flows that require maintenance](viewing-flows-maintenance.md "viewing-flows-maintenance.md")
- [Setting maintenance windows](setting-flow-maintenance.md "setting-flow-maintenance.md")
