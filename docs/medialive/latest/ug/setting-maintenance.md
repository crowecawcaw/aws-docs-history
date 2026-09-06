

# Working with a maintenance event
<a name="setting-maintenance"></a>

You receive notification of upcoming maintenance for a channel at least 21 calendar days before the deadline for the maintenance. The notification specifies this deadline. You should decide how you want to handle the upcoming maintenance event. 

**Topics**
+ [How maintenance timing works](#set-maintenance-timing)
+ [Options for handling maintenance](#set-maintenance-change-options)
+ [Stopping a channel during the maintenance event period](#maintenance-stop-channel)
+ [Rescheduling a maintenance event](#set-maintenance-reschedule)

## How maintenance timing works
<a name="set-maintenance-timing"></a>

In the following example, assume that your *maintenance window* is currently set for Thursdays between 4:00 and 5:00 UTC (red date marks in the diagram). Assume that you receive a *maintenance notification* on Tuesday, May 2.
+ The *maintenance deadline* is Tuesday, May 23. 
+ The green bar is the current *maintenance event period*. It is the period between the notification and the deadline. In this example, the maintenance event period is May 2 to May 23. 
+ The purple bar is the *maintenance opening*. It is the period from 7 days before the deadline until the deadline. In this example, the maintenance opening is May 16 to May 23. 
+ The short red marks are *potential maintenance events*. Each potential maintenance event is set on the same day. In this example, there is a potential maintenance event every Thursday.
+ The red mark in the purple bar is the *current maintenance window*. Automatic maintenance is set to occur some time during the maintenance window that occurs during the maintenance opening. In this example, it is set to occur on Thursday, May 18 between 4:00 and 5:00 UTC.

![Calendar view showing a scheduled event spanning Thursday with markers on days 4, 11, and 18.](http://docs.aws.amazon.com/medialive/latest/ug/images/maintenance.png)


## Options for handling maintenance
<a name="set-maintenance-change-options"></a>

You have the following options for maintenance:
+ You can leave the maintenance window (red mark) as it is currently set.
+ You can change the day of the week and the time of the maintenance window. See [Change the maintenance window](set-maintenance-change-steps.md#set-maintenance-edit).
+ You can set a specific date and time for the maintenance window. See [Set a specific date](set-maintenance-change-steps.md#set-maintenance-specific-date)

## Stopping a channel during the maintenance event period
<a name="maintenance-stop-channel"></a>

As part of normal operations, you might stop the channel, for example, to make changes to the channel configuration.

If you stop a channel during the maintenance event period (green bar), maintenance will be performed automatically when you restart. The maintenance event will be considered to be completed. The maintenance status for the channel will change to **Not required**.

## Rescheduling a maintenance event
<a name="set-maintenance-reschedule"></a>

If MediaLive can't perform the maintenance during the maintenance window (red mark), MediaLive will reschedule the maintenance for the same maintenance window in the next week. This date might be after the deadline for the maintenance event period (green bar). Every week, MediaLive will try to perform the maintenance. 

Each time MediaLive reschedules the maintenance event, the new date will appear in the Channels list in the MediaLive console, and on the Health Dashboard.

During this retry period, you can change the maintenance window, but only if the channel is still in the maintenance event period (green bar).