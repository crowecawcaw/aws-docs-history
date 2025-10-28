# Manage directories for WorkSpaces Personal

WorkSpaces uses a directory to store and manage information for your WorkSpaces and users. You
can use one of the following options:

- AD Connector — Use your existing on-premises Microsoft Active Directory. Users
  can sign into their WorkSpaces using their on-premises credentials and access on-premises
  resources from their WorkSpaces.
- AWS Managed Microsoft AD — Create a Microsoft Active Directory hosted on AWS.
- Simple AD — Create a directory that is compatible with Microsoft Active Directory,
  powered by Samba 4, and hosted on AWS.
- Cross trust — Create a trust relationship between your AWS Managed Microsoft AD directory and
  your on-premises domain.
- Microsoft Entra ID — Create a directory that uses Microsoft Entra ID as its identity source
  (through IAM Identity Center). Personal WorkSpaces in the directory are joined using Microsoft Entra's native authentication and
  are enrolled into Microsoft Intune through Microsoft Windows Autopilot user-driven mode.
  Directories using Microsoft Entra ID only support Windows 10 and 11 Bring Your Own Licenses WorkSpaces.
- Custom — Create a directory that use an identity provider of your choice (through IAM Identity Center).
  WorkSpaces in the directory are managed using the device management solution of your choice such as JumpCloud.
  Directories using custom identity providers only support Windows 10 and 11 Bring Your Own Licenses WorkSpaces.
  For tutorials that demonstrate how to set up these directories and launch WorkSpaces, see
  [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").

###### Tip

For a detailed exploration of directory and virtual private cloud (VPC) design considerations for
various deployment scenarios, see [Best Practices for Deploying Amazon WorkSpaces](../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/best-practices-deploying-amazon-workspaces.md "../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/best-practices-deploying-amazon-workspaces.md").

After you create a directory, you'll perform most directory administration tasks using tools
such as the Active Directory Administration Tools. You can perform some directory administration
tasks using the WorkSpaces console and other tasks using Group Policy. For more information about
managing users and groups, see [Manage users in WorkSpaces Personal](manage-workspaces-users.md "manage-workspaces-users.md")
and [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

###### Note

- Shared directories are not currently supported for use with Amazon WorkSpaces.
- If you configure your AWS Managed Microsoft AD directory for multi-Region replication,
  only the directory in the primary Region can be registered for use with Amazon WorkSpaces. Attempts
  to register the directory in a replicated Region for use with Amazon WorkSpaces will fail.
  Multi-Region replication with AWS Managed Microsoft AD isn't supported for use with Amazon WorkSpaces
  within replicated Regions.
- Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces.
  If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30
  consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces,
  and you will be charged for this directory as per the
  [AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/").

To delete empty directories, see
[Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md "delete-workspaces-directory.md"). If you delete your
Simple AD or AD Connector directory, you can always create a new one when you want to start using
WorkSpaces again.

###### Contents

- [Register an existing AWS Directory Service directory with WorkSpaces Personal](register-deregister-directory.md "register-deregister-directory.md")
- [Select an organizational unit for WorkSpaces Personal](select-ou.md "select-ou.md")
- [Configure automatic public IP addresses for WorkSpaces Personal](automatic-assignment.md "automatic-assignment.md")
- [Control device access for WorkSpaces Personal](control-device-access.md "control-device-access.md")
- [Manage local administrator permissions for WorkSpaces Personal](local-admin-setting.md "local-admin-setting.md")
- [Update the AD Connector account (AD Connector) for WorkSpaces Personal](connect-account.md "connect-account.md")
- [Multi-factor authentication (AD Connector) for WorkSpaces Personal](connect-mfa.md "connect-mfa.md")
- [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md")
- [Update DNS servers for WorkSpaces Personal](update-dns-server.md "update-dns-server.md")
- [Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md "delete-workspaces-directory.md")
- [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md")
