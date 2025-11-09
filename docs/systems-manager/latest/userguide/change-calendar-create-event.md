AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating a Change Calendar event

When you add an event to an entry in Change Calendar, a tool in AWS Systems Manager, you're
specifying a period of time during which the default action of the calendar
entry is suspended. For example, if the calendar entry type is closed by
default, the calendar is open to changes during events. (Alternatively, you can
create an advisory event, which serves an informational role on the calendar
only.)

Currently, you can only create a Change Calendar event by using the console. Events
are added to the Change Calendar document that you create when you create a Change Calendar
entry.

###### To create a Change Calendar event

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Change Calendar**.
3. In the list of calendars, choose the name of the calendar entry to
   which you want to add an event.
4. On the calendar entry's details page, choose **Create
   event**.
5. On the **Create scheduled event** page, in
   **Event details**, enter a display name for your
   event. Event names can contain letters, numbers, periods, dashes, and
   underscores. The name should be specific enough to identify the purpose
   of the event. An example is
   `nighttime-hours`.
6. For **Description**, enter a description for your
   event. For example, `The support team isn't available during
these hours`.
7. (Optional) If you want this event to serve as a visual notification or
   reminder only, select the **Advisory** check box.
   Advisory events play no functional role on your calendar. They serve
   informational purposes only for those who view your calendar.
8. For **Event start date**, enter or choose a day in
   the format `MM/DD/YYYY` to start the event, and enter a time
   on the specified day in the format `hh:mm:ss` (hours,
   minutes, and seconds) to start the event.
9. For **Event end date**, enter or choose a day in the
   format `MM/DD/YYYY` to end the event, and enter a time on the
   specified day in the format `hh:mm:ss` (hours, minutes, and
   seconds) to end the event.
10. For **Schedule time zone**, choose a time zone that
    applies to the start and end times of the event. You can enter part of a
    city name or time zone difference from Greenwich Mean Time (GMT) to find
    a time zone faster. The default is Coordinated Universal Time
    (UTC).
11. (Optional) To create an event that recurs daily, weekly, or monthly,
    turn on **Recurrence**, and then specify the frequency
    and optional end date for the recurrence.
12. Choose **Create scheduled event**. The new event is
    added to your calendar entry, and is displayed on the
    **Events** tab of the calendar entry's details
    page.
