AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Updating all events from a

third-party calendar provider

If several events are added to or removed from your source calendar after you
have imported its iCalendar `.ics` file, you can reflect
those changes in Change Calendar. First, re-export the source calendar, and then import
the new file into Change Calendar, which is a tool in AWS Systems Manager. Events in your change
calendar will be updated to reflect the contents of the newer file.

###### To update all events from a third-party calendar provider

1. In your third-party calendar, add or remove events as you want them to
   be reflected in Change Calendar, and then re-export the calendar to a new
   `.ics` file.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. In the navigation pane, choose **Change Calendar**.
4. From the list of calendars, choose the calendar name from the
   list.
5. Choose **Choose file**, and then navigate to and
   select the replacement `.ics` file.
6. In response to the notification about overwriting the existing file,
   choose **Confirm**.
