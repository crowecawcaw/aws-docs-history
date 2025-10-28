This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Analytics dashboard

You can use the analytics dashboard to view how your organization is utilizing Wickr.
The following procedure explains how to access the analytics dashboard by using the Wickr
console.

**To access the analytics dashboard**

In the navigation pane, choose **Analytics**.

The **Analytics** page displays the metrics for your network in
different tabs.

On the **Analytics** page, you will find a time frame filter at the top
right corner of each tab. This filter applies to the entire page. Additionally, at the top
right corner of each tab, you can export the data points for the selected time range by
choosing the **Export** option available.

###### Note

The time selected is in UTC (Universal Time Coordinated).

The following tabs are available:

- **Overview** displays:
  - **Registered —** The total number of registered users,
    including active and suspended users on the network in the selected time. It does
    not include pending or invited users.
  - **Pending —** The total number of pending users on the network
    in the selected time.
  - **User Registration —** The graph displays the total number of
    users registered in the selected time range.
  - **Devices —** The number of devices where the app has been
    active.
  - **Client Versions —** The number of active devices categorized
    by their client versions.

- **Members** displays:
  - **Status —** Active users on the network within the time period
    selected.
  - **Active users —**
    - The graph displays the count of active users over time and can be aggregated
      by daily, weekly or monthly (within the above selected time range).
    - The active user count can be broken down by **Platform**,
      **Client Version**, or **Security Group**.
      If a security group was deleted, the total count will be shown as
      **Deleted#**.

- **Messages** displays:
  - **Messages sent —** The count of unique messages sent by all
    users and bots on the network in the selected time period.
  - **Calls —** Number of unique calls made by all users in the
    network.
  - **Files —** Number of files sent by users in the network
    (includes voice memos).
  - **Devices —** The pie chart displays the number of active
    devices categorized by their operating system.
  - **Client Versions —** The number of active devices categorized
    by their client versions.
