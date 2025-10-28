# Set a refresh schedule for a custom dashboard

with the CloudTrail console

This section describes how to set a dashboard refresh schedule. You can set a refresh
schedule to allow CloudTrail Lake to refresh a dashboard every 1 hour, 6 hours, 12 hours, or
24 hours (1 day).

When you set a refresh schedule using the CloudTrail console, CloudTrail attaches a
resource-based policy to the dashboard that allows CloudTrail to refresh the dashboard on your
behalf.

###### To set a refresh schedule

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
   **Dashboard**.
3. Choose the **Managed and custom dashboards** tab.
4. In **Custom dashboards**, choose the dashboard that you want
   to set a refresh schedule for.
5. Choose the refresh frequency from the dropdown list.
6. To create a refresh schedule, CloudTrail attaches a resource-based policy to
   the dashboard to allow CloudTrail to refresh the dashboard on your behalf. Expand
   **Dashboard resource policy** to view the resource-based
   policy that CloudTrail will attach to the dashboard.
7. Because running queries incurs costs, CloudTrail asks you to confirm that you want
   CloudTrail to run queries for the scheduled frequency. Choose
   **Confirm** to set a refresh schedule.
