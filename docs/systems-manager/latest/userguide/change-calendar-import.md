# Importing events from third-party

calendar providers

Use the following procedure to import an iCalendar (`.ics`)
file from a supported third-party calendar application. The events contained in
the file are incorporated into the rules for your open or closed calendar. You
can import a file into a new calendar you are creating with Change Calendar (a tool in
AWS Systems Manager) or into an existing calendar.

After you import the `.ics` file, you can remove individual
events from it using the Change Calendar interface. For information, see [Deleting a Change Calendar event](change-calendar-delete-event.md "change-calendar-delete-event.md"). You can also delete all
events from the source calendar by deleting the `.ics` file.
For information, see [Deleting all events imported from a
third-party calendar](change-calendar-delete-ics.md "change-calendar-delete-ics.md").

###### To import events from third-party calendar providers

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Change Calendar**.
3. To start with a new calendar, choose **Create
   calendar**. In the **Import calendar**
   area, choose **Choose file**. For information about
   other steps to create a new calendar, see [Creating a change calendar](change-calendar-create.md "change-calendar-create.md").

-or-

To import third-party events into an existing calendar, choose the
name of an existing calendar to open it. 4. Choose **Actions, Edit**, and then in the
**Import calendar** area, choose **Choose
file**. 5. Navigate to and select the exported `.ics` file on
your local computer. 6. If prompted, for **Select a time zone**, select which
time zone applies to the calendar. 7. Choose **Save**.
