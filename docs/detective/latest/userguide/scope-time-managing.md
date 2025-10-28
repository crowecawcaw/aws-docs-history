# Managing the scope time

Customize the scope time used to limit the data displayed on entity profiles.

The charts, timelines, and other data displayed on entity profiles are all based on the
current scope time. Scope time is the summary of activity for an entity over time. This appears at
the top right of each profile in the Amazon Detective console. The data displayed on those charts,
timelines, and other visualizations is based on the scope time. For some profile panels,
additional time is added before and after the scope time to provide context. In Detective, all
timestamps are displayed in UTC by default. You can select your local time zone by changing the
**Timestamp preferences**. To update the **Timestamp
preference**, see [Setting the timestamp format](profile-panel-preferences.md#profile-panel-preferences-timestamp "profile-panel-preferences.md#profile-panel-preferences-timestamp").

Detective analytics uses the scope time when checking for unusual activity. The analytics process
gets the activity during the scope time, then compares it to the activity during the 45 days
before the scope time. It also uses that 45-day timeframe to generate baselines of activity.

On a finding overview, the scope time reflects the first and last time the finding was
observed. For more information about finding overview, see [Analyzing a finding overview in Detective](finding-overview.md "finding-overview.md").

As you work through an investigation, you can adjust the scope time. For example, if the
original analysis was based on activity from a single day, you might want to expand that to a week
or a month. The expanded period could help you get a better sense of whether the activity fits a
normal pattern or is unusual.

You can also set the scope time to match an associated finding for the current entity.

When you change the scope time, Detective repeats its analysis and updates the displayed data
based on the new scope time.

The scope time cannot be shorter than one hour and not longer than one year. The start and
end time must be on an hour.

## Setting specific start and end dates and times

You can set the scope time start and end dates from the Detective console.

###### To set specific start and end times for the new scope time

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. On an entity profile, choose the scope time.
3. On the **Edit scope time** panel, under **Start**,
   choose the new start date and time for the scope time. For the new start time, you choose the
   hour only.
4. Under **End**, choose the new end date and time for the scope time. For
   the new end time, you choose the hour only. The end time must be at least an hour later than
   the start time.
5. When you're finished editing, to save the changes and update the displayed data, choose
   **Update scope time**.

## Edit the length of time for the scope time

When you set a scope time length, Detective sets the scope time to that amount of time from the
current time.

###### To edit the length of time for the scope time

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. On an entity profile, choose the scope time.
3. On the **Edit scope time** panel, next to
   **Historical**, choose the length of time for the scope time.

Specifying a time range updates the **Start** and
**End** settings. 4. When you're finished editing, to save the changes and update the displayed data, choose
**Update scope time**.

## Setting the scope time to a finding time

window

Each finding has an associated time window, which reflects the first and last times the
finding was observed. When you view a finding overview, the scope time changes to the finding
time window.

From an entity profile, you can align the scope time to the time window for an associated
finding. This allows you to investigate the activity that occurred during that time.

To align the scope time to a finding time window, on the **Associated
findings** panel, choose the finding that you want to use.

Detective populates the finding details and sets the scope time to the finding time
window.

## Setting the scope time on the summary page

As you review the **Summary** page, you can adjust the Scope time to view
the activity for any 24-hour time frame in the previous 365 days.

To set the scope time on the Summary page

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Summary**.
3. On the **Scope time** panel, next to **Summary**, you
   can change the **Start date and time**. Start time must be within the last 365
   days.

When you change the **Start date and time**, the **End date and
time** is automatically updated to 24 hours after your chosen start time.

###### Note

With Detective, you can access up to a year of historical event data. For more information on
source data in Detective, see [Source data used in a
behavior graph](detective-source-data-about.md "detective-source-data-about.md"). 4. When you're finished editing, to save the changes and update the displayed data, choose
**Update scope time**.
