# Get started with AWS IoT SiteWise Monitor (Classic)

###### Note

The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use SiteWise Monitor,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](../appguide/iotsitewise-monitor-availability-change.md "../appguide/iotsitewise-monitor-availability-change.md").

If you're the AWS administrator for your organization, you create portals from the
AWS IoT SiteWise console. Complete the following steps to create a portal so that members of your
organization can view your AWS IoT SiteWise data:

1. Configure and create a portal
2. Add portal administrators and send invitation emails
3. Add portal users
   After you create a portal, the portal administrator can view your AWS IoT SiteWise assets and assign
   them to projects in the portal. Project owners can then create dashboards to visualize the
   properties of the assets that help project viewers understand how your devices, processes, and
   equipment are performing.

###### Note

When adding users or administrators to the portal,
avoid creating AWS Identity and Access Management (IAM) policies that restrict user permissions, such as limited IP.
Any attached policies with restricted permissions will not be able to connect to the AWS IoT SiteWise portal.

You can follow a tutorial that walks through the steps required to set up a portal with a
project, dashboards, and multiple users for a specific scenario using wind farm data. For more
information, see [Visualize and share wind farm data in SiteWise Monitor](monitor-wind-farm.md "monitor-wind-farm.md").

###### Topics

- [Create a portal in SiteWise Monitor](monitor-create-portal.md "monitor-create-portal.md")
- [Configure your portal in SiteWise Monitor](monitor-configure-portal.md "monitor-configure-portal.md")
- [Invite administrators in SiteWise Monitor](monitor-invite-administrators.md "monitor-invite-administrators.md")
- [Add portal users in SiteWise Monitor](monitor-add-portal-users.md "monitor-add-portal-users.md")
- [Create AWS IoT SiteWise dashboards (AWS CLI)](create-dashboards-using-aws-cli.md "create-dashboards-using-aws-cli.md")
- [Turn on alarms for your portals in AWS IoT SiteWise](monitor-enable-alarms.md "monitor-enable-alarms.md")
- [Enabling your AWS IoT SiteWise portal at the edge](monitor-enable-edge.md "monitor-enable-edge.md")
- [Administer your SiteWise Monitor portals](administer-portals.md "administer-portals.md")
