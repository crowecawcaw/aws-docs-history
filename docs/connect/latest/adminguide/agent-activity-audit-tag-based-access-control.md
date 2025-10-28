# Agent activity

audit tag-based access control in Amazon Connect

You can use resource tags and access control tags to apply granular access to
users for the agent activity audit report. For example, you can control who has
access to view agent status history for specific users in the report. The
following images provide example views of the agent activity audit report with
and without tag-based access controls:

**Without tag-based access controls, you see all
agents:**

![Without tag-based access controls, you see all agents.](images/agent-activity-audit-tag-based-access-control-before.png)
**By using tag-based access controls, you can see a
limited set of agents:**

![By using tag-based access controls, you can see a limited set of agents.](images/agent-activity-audit-tag-based-access-control-after.png)
Tag-based access controls are available for real-time metrics; however, they
are not applicable to other historical metric reports or the login/logout
report. For more information, please see [Real-time metrics tag-based access
control in Amazon Connect](rtm-tag-based-access-control.md "rtm-tag-based-access-control.md").

Tag-based access controls enable you to configure granular access to specific
resources based on assigned resource tags. You can configure tag based access
controls by using the API/SDK or the Amazon Connect admin website (for supported resources). You must
configure user resource tags and access control tags before tag-based access
control is applied to users for the agent activity audit report. For more
information, see [Add tags to resources in Amazon Connect](tagging.md "tagging.md") and [Apply tag-based access control in
Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").

## How To Enable Tag-based Access Control for Agent Activity Audit Report

To use tags to control access to users for the agent activity audit
report, you must first configure user resource tags and access control tags.
After your resource tags and access control tags are configured, you need to
apply the appropriate permissions.

After your resource tags, access control tags, and permissions have been
appropriately configured, you will have access controls applied to users for
the agent activity audit report.

For more information on tagging resources and tag-based access control in
Amazon Connect, see [Add tags to resources in Amazon Connect](tagging.md "tagging.md") and [Apply tag-based access control in
Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").

## Permissions

To view agent activity audit reports with tag-based access controls
applied, you need to be assigned to a security profile that has Access
selected for **Agent Activity Audit** or has Access
selected for **Access metrics** permission, along with
access to the user resource. Note that if you enable **Access
metrics**, then **Real-time metrics**,
**Historical Metrics**, and **Agent Activity
Audit** will be filled in automatically, and you therefore will
be enabling users to see all data for historical metrics for which tag-based
access controls are not currently applied.

![The Analytics and Optimization section of the security profiles permissions page.](images/agent-activity-audit-tag-based-access-control-permissions-1.png)

![The Analytics and Optimization section of the security profiles permissions page.](images/agent-activity-audit-tag-based-access-control-permissions-2.png)

![The Analytics and Optimization section of the security profiles permissions page.](images/agent-activity-audit-tag-based-access-control-permissions-3.png)
