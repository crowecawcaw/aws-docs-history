# Setting up Maintenance Windows

Before users in your AWS account can create and schedule maintenance window tasks
using Maintenance Windows, a tool in AWS Systems Manager, they must be granted the necessary permissions. In
addition, you must create an IAM service role for maintenance windows and the IAM
policy to attach to it.

###### Before you begin

In addition to the permissions you configure in this section, the IAM Entities
(users, roles, or groups that will work with maintenance windows should already have
general maintenance window permissions. You can grant these permissions by assigning
the IAM policy `AmazonSSMFullAccess` to the Entities, or assigning a
custom IAM policy that provides a smaller set of access permissions for Systems Manager that
covers maintenance window tasks.

###### Topics

- [Control access
  to maintenance windows using the console](configuring-maintenance-window-permissions-console.md "configuring-maintenance-window-permissions-console.md")
- [Control access to
  maintenance windows using the AWS CLI](configuring-maintenance-window-permissions-cli.md "configuring-maintenance-window-permissions-cli.md")
