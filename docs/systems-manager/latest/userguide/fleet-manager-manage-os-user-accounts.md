

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Managing OS user accounts and groups on managed nodes using Fleet Manager
<a name="fleet-manager-manage-os-user-accounts"></a>

You can use Fleet Manager to manage operating system (OS) user accounts and groups on your managed nodes. For example, you can create and delete users and groups. Additionally, you can view details like group membership, user roles, and status.

This section includes the following topics.
+ [Creating an OS user or group using Fleet Manager](manage-os-user-accounts-create.md)
+ [Updating user or group membership using Fleet Manager](manage-os-user-accounts-update.md)
+ [Deleting an OS user or group using Fleet Manager](manage-os-user-accounts-delete.md)

**Important**  
Fleet Manager uses Run Command and Session Manager, tools in AWS Systems Manager, for various user management operations. As a result, a user could grant permissions to an operating system user account that they would otherwise be unable to. This is because AWS Systems Manager Agent (SSM Agent) runs on Amazon Elastic Compute Cloud (Amazon EC2) instances using root permissions (Linux) or SYSTEM permissions (Windows Server). For more information about restricting access to root-level commands through SSM Agent, see [Restricting access to root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md). To restrict access to this feature, we recommend creating AWS Identity and Access Management (IAM) policies for your users that only allow access to the actions you define. For more information about creating IAM policies for Fleet Manager, see [Controlling access to Fleet Manager](configuring-fleet-manager-permissions.md).