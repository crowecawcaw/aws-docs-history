# Apply granular access control to

historical metrics reports in Amazon Connect

You can use resource tags and access control tags to apply granular access to
users, queues, and routing profiles for historical metrics. For example, you can
control who has access to view specific users, queues, and routing profile
historical metrics.

Amazon Connect also supports tag-based access controls for real-time metrics and the agent
activity audit, but it does not support dashboards and the login/logout report. For
more information, see [Real-time metrics tag-based access
control in Amazon Connect](rtm-tag-based-access-control.md "rtm-tag-based-access-control.md") and [Agent activity
audit tag-based access control in Amazon Connect](agent-activity-audit-tag-based-access-control.md "agent-activity-audit-tag-based-access-control.md").

Tag-based access controls enable you to configure granular access to specific
resources based on assigned resource tags. You can configure tag-based access
controls by using the API or the Amazon Connect admin website for supported resources. You must configure
resource tags and access control tags before tag-based access control is applied to
users, queues, and routing profiles for real-time metrics. For more information, see
[Add tags to resources in Amazon Connect](tagging.md "tagging.md") and [Apply tag-based access control in
Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").

## How to enable tag-based

access control for historical metrics reports

To apply tags to control access to users, queues, and routing profiles metrics
in historical metrics reports:

1.  Apply tags to the resources that you're going use in the historical
    metrics report, such as users, queues, and routing profiles. For more
    information, see [Add tags to resources in Amazon Connect](tagging.md "tagging.md").
2.  You need to be assigned to a security profile that specifically grants
    you access to the resources that have been tagged. On the Security
    profiles page, choose **Show advanced** options to
    assign these permissions.
3.  In addition, you need the one of following permissions to view the
    historical metrics reports:

        * **Analytics and Optimization - Access metrics -
         Access**: If you choose this option, access is also
         granted to Real-time metrics, Historical metrics, Agent activity
         audit, and Dashboards. This means you are granting users
         permission see all data for Dashboards where tag-based access
         controls are not currently applied.

    OR

        * **Analytics and Optimization - Historical metrics -
         Access**

## Limitations

The following limitations apply when you use tag-based access controls with
historical metrics:

- You can only filter and group by the same resource (user, queue, or
  routing profile). For example, you cannot filter by queue for an agent
  grouping and you cannot group by queue and routing profile. The only
  additional grouping you can do is channel (for example, Group by queue
  and channel).
- You can filter for 500 resources per report.
- You can't group by agent hierarchy, phone numbers, or email address.
  You can't filter by agent hierarchy, phone numbers, email address, or
  agent queues.
- Access to the homepage service level dashboard is disabled.

## How to transition to tag-based access

control

If you open a saved report containing tables with users, queues, or routing
profiles that you don't have access to anymore due to tag-based access control,
or if groupings or non-primary filters are applied to tables, you won't see data
in those tables.

To view the data, perform one of the following steps:

- Edit your table filters to include the agents, queues, or routing
  profiles that you have access to.
- Create a new report that includes the resources you have access
  to.
- Remove the groupings and non-primary filters from the table.
