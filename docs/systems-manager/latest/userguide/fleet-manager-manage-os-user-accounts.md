AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Managing OS user accounts

and groups on managed nodes using Fleet Manager

You can use Fleet Manager, a tool in AWS Systems Manager, to manage operating system (OS) user
accounts and groups on your managed nodes. For example, you can create and delete
users and groups. Additionally, you can view details like group membership, user
roles, and status.

###### Important

Fleet Manager uses Run Command and Session Manager, tools in AWS Systems Manager, for various user
management operations. As a result, a user could grant permissions to an
operating system user account that they would otherwise be unable to. This is
because AWS Systems Manager Agent (SSM Agent) runs on Amazon Elastic Compute Cloud (Amazon EC2) instances using
root permissions (Linux) or SYSTEM permissions (Windows Server). For more information
about restricting access to root-level commands through SSM Agent, see [Restricting access to
root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md "ssm-agent-restrict-root-level-commands.md"). To restrict access
to this feature, we recommend creating AWS Identity and Access Management (IAM) policies for your users
that only allow access to the actions you define. For more information about
creating IAM policies for Fleet Manager, see [Controlling access to
Fleet Manager](configuring-fleet-manager-permissions.md "configuring-fleet-manager-permissions.md").

###### Topics

- [Creating an OS user or group
  using Fleet Manager](manage-os-user-accounts-create.md "manage-os-user-accounts-create.md")
- [Updating user or group
  membership using Fleet Manager](manage-os-user-accounts-update.md "manage-os-user-accounts-update.md")
- [Deleting an OS user or group
  using Fleet Manager](manage-os-user-accounts-delete.md "manage-os-user-accounts-delete.md")
