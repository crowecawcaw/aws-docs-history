

# Automation events
<a name="automation-events"></a>

The Automation events page is centralized dashboard that displays information about the automated actions initiated through Compute Optimizer. You can review summary information and get details for individual automation events. By default, the dashboard shows information automation events from the last 6 months. You can view events from the past year using the date filter.

The Events summary section summarizes the estimated monthly savings and count for your automation events by status.

You can track events completed over time by viewing the Monthly events summary chart, which summarizes the estimated monthly savings and count for your automation events, grouped by status and the month in which the automation event was created. The chart displays estimated monthly savings (not cumulative savings) for events executed in each month. These savings estimates represent the potential monthly savings calculated at the time of modification and do not reflect actual realized savings in that month or any subsequent months. The Monthly events summary chart shows the sum of all events shown in the Automation events table based on your selected filters. Estimated monthly savings are only displayed for events with Complete and Rollback Complete status.

This Automation events table displays automation events implemented by Compute Optimizer. Review details such as event type, description, status, and estimated monthly savings. These savings estimates represent the potential monthly savings calculated at the time of modification and do not reflect actual realized savings in that month or any subsequent months.

Select an automation event ID to view Event details and step history. The step history table provides a chronological record of operations performed during the automation event. Each step shows the specific action taken to modify your resource, along with its own step status, start time, and completion time.

## Rollback
<a name="automation-events-rollback"></a>

Rollback capabilities that allow you to reverse automated optimization actions if needed. You can initiate rollback from the Automation events page, where you can select and roll back up to 10 automation events at a time. You can only initiate rollback for events with Complete status. 

The specific rollback steps depend on the event type:
+ Snapshot and delete unattached EBS volume: Rolling back volume deletion creates a new EBS volume from the snapshot of the deleted volume. The new volume will have a different volume ID, and all user-created tags on the original volume will be restored to the new volume.
+ Upgrade EBS volume type: Rolling back volume type upgrades will modify the volume to the previous volume type configuration.

There are several considerations for rollback:
+ Compute Optimizer requires the original EBS snapshot created by Compute Optimizer to perform rollback operations for volume deletions. If you delete this snapshot and attempt to roll back the automation event, the rollback operation will fail. 
+ Amazon EBS supports up to four Elastic Volumes modifications per volume within a rolling 24-hour period. Volume modifications applied through Compute Optimizer count toward this limit. After Compute Optimizer completes a volume modification, you can roll back the event as long as the total number of volume modifications in the past 24 hours is fewer than four. Similarly, after a rollback completes, you can initiate additional modifications as long as the total number of modifications remains within the limit. For more information, see the [Amazon EBS User Guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html).
+ Compute Optimizer validates that the current Amazon EBS volume configuration matches the configuration at the time the automation event completed. If you modify the volume configuration after Compute Optimizer completes the automation event and then attempt to roll back the automation event, the rollback operation will fail.

## Automation event statuses
<a name="automation-events-status"></a>

Automation events reports the following status details:


| Event status | Event status reason | 
| --- | --- | 
| Ready | The automation has not started running. | 
| In-Progress | The automation is running. | 
| Complete | The automation completed successfully. | 
| Failed | The automation did not complete successfully. | 
| Rollback Ready | The rollback has not started running. | 
| Rollback In-Progress | The rollback is running. | 
| Rollback Complete | The rollback has completed successfully. | 
| Rollback Failed | The rollback did not complete successfully. | 