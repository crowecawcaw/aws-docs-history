# EUCCOST03-BP01 Determine the level of self-service capabilities to provide your users

Amazon WorkSpaces offers self-service capabilities that you can
enable for your users. Assess the impact of granting access to
these self-service capabilities and selectively disable or
enable them based on your requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Evaluate the cost impact of enabling certain self-service WorkSpaces management
capabilities for your users, and then select which of these self-service capabilities you
want to provide to your users. For more information, see [Enable self-service WorkSpaces management capabilities for your users in WorkSpaces
Personal](../../../workspaces/latest/adminguide/enable-user-self-service-workspace-management.md "../../../workspaces/latest/adminguide/enable-user-self-service-workspace-management.md") . Consider creating internal policies to govern which capabilities are
allowed. Changing the compute type (bundle), increasing the root and user volume size, and
changing the running mode may increase your cost. Instead of enabling these capabilities
for your users, you may consider providing these capabilities through your IT service
management so that changes requested by a user requires prior approval.
