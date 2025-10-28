# Logging and monitoring in AWS Control Tower

Monitoring allows you to plan for and respond to potential incidents. The results of
monitoring activities are stored in log files. Therefore, logging and monitoring are closely
related concepts, and they are an important part of the well-architected nature of
AWS Control Tower.

When you set up your landing zone, one of the shared accounts created is the _log archive_ account. It is dedicated to collecting all logs
centrally, including logs for all of your shared and member accounts. Log files are stored in an
Amazon S3 bucket. These log files allow administrators and auditors to review actions and events that
have occurred.

As a best practice, you should collect monitoring data from all of the parts of your AWS
setup into your logs, so that you can more easily debug a multi-point failure if one occurs.
AWS provides several tools for monitoring your resources and activity in your landing zone.

For example, the status of your controls is monitored constantly. You can see their status
at a glance in the AWS Control Tower console, or programmatically by means of [the AWS Control Tower APIs](../APIReference/API_Operations.md "../APIReference/API_Operations.md"). The
health and status of the accounts you provisioned in Account Factory also is monitored
constantly.

**View logged actions from the Activities page**

In the AWS Control Tower console, the **Activities** page provides an overview of
AWS Control Tower management account actions. To navigate to the AWS Control Tower **Activities**
page, select **Activities** from the left navigation.

The activities shown in the **Activities** page are the same ones reported
in the AWS CloudTrail events log for AWS Control Tower, but they're shown in a table format. To learn more
about a specific activity, select the activity from the table and then choose **View
details**.

You can view member account actions and events in the log archive files.

The following sections describe monitoring and logging in AWS Control Tower with more detail:

###### Topics

- [Integrated tools for monitoring](monitoring-overview.md "monitoring-overview.md")
- [Logging AWS Control Tower Actions with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Lifecycle Events in AWS Control Tower](lifecycle-events.md "lifecycle-events.md")
- [Using AWS User Notifications with AWS Control Tower](using-user-notifications.md "using-user-notifications.md")
