# Create a directory for WorkSpaces Personal

WorkSpaces Personal allows you to use directories managed through Directory Service to store and manage information for your WorkSpaces and users.
Use the following options to create a WorkSpaces Personal directory:

- Create a Simple AD directory.
- Create an AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD.
- Connect to an existing Microsoft
  Active Directory by using Active Directory Connector.
- Create a trust relationship between your
  AWS Managed Microsoft AD directory and your on-premises domain.
- Create a dedicated Microsoft Entra ID WorkSpaces directory.
- Create a dedicated Custom WorkSpaces directory.

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

## Before you create a directory

- WorkSpaces is not available in every Region. Verify the supported Regions and select
  a Region for your WorkSpaces. For more information about the supported Regions,
  see [WorkSpaces Pricing by AWS Region](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/").
- Create a virtual private cloud with at least two private subnets. For more information, see
  [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md "amazon-workspaces-vpc.md"). The VPC must
  be connected to your on-premises network through a virtual private network (VPN)
  connection or Direct Connect. For more information,
  see [AD Connector
  Prerequisites](../../../directoryservice/latest/admin-guide/prereq_connector.md "../../../directoryservice/latest/admin-guide/prereq_connector.md") in the _AWS Directory Service Administration Guide_.
- Provide access to the internet from the WorkSpace. For more information,
  see [Provide internet access for WorkSpaces Personal](amazon-workspaces-internet-access.md "amazon-workspaces-internet-access.md").

For information about how to delete an empty directory, see
[Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md "delete-workspaces-directory.md"). If you delete your
Simple AD or AD Connector directory, you can always create a new one when you want to start using
WorkSpaces again.

###### Contents

- [Identify the computer name for your WorkSpaces Personal directory](wsp-directory-identify-computer.md "wsp-directory-identify-computer.md")
- [Create an AWS Managed Microsoft AD directory for WorkSpaces Personal](launch-workspace-microsoft-ad.md "launch-workspace-microsoft-ad.md")
- [Create a Simple AD directory for WorkSpaces Personal](launch-workspace-simple-ad.md "launch-workspace-simple-ad.md")
- [Create an AD Connector for WorkSpaces Personal](launch-workspace-ad-connector.md "launch-workspace-ad-connector.md")
- [Create a trust relationship between your AWS Managed Microsoft AD directory and your on-premises domain for WorkSpaces Personal](launch-workspace-trusted-domain.md "launch-workspace-trusted-domain.md")
- [Create a dedicated Microsoft Entra ID directory with WorkSpaces Personal](launch-entra-id.md "launch-entra-id.md")
- [Create a dedicated Custom directory with WorkSpaces Personal](launch-custom.md "launch-custom.md")
