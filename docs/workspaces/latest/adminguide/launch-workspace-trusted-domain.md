# Create a trust relationship between your AWS Managed Microsoft AD directory and your on-premises domain for WorkSpaces Personal

In this tutorial, we create a trust relationship between your
AWS Managed Microsoft AD directory and your on-premises domain. For tutorials
that use the other options, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").

###### Note

Launching WorkSpaces with AWS accounts in a separate trusted domain works with AWS Managed Microsoft AD
when it is configured with a trust relationship to your on-premises directory. However, WorkSpaces using Simple AD
or AD Connector cannot launch WorkSpaces for users from a trusted domain.

###### To set up the trust relationship

1. Set up AWS Managed Microsoft AD in your virtual private cloud (VPC). For more information, see
   [Create Your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/create_managed_ad.md "../../../directoryservice/latest/admin-guide/create_managed_ad.md")
   in the _AWS Directory Service Administration Guide_.

###### Note

    * Shared directories are not currently supported for use with Amazon WorkSpaces.
    * If your AWS Managed Microsoft AD directory has been configured for multi-Region replication,
     only the directory in the primary Region can be registered for use with Amazon WorkSpaces. Attempts
     to register the directory in a replicated Region for use with Amazon WorkSpaces will fail.
     Multi-Region replication with AWS Managed Microsoft AD isn't supported for use with Amazon WorkSpaces
     within replicated Regions.

2. Create a trust relationship between your AWS Managed Microsoft AD and your on-premises domain.
   Ensure that the trust is configured as a two-way trust.
   For more information, see [Tutorial:
   Create a Trust Relationship Between Your AWS Managed Microsoft AD and Your On-Premises Domain](../../../directoryservice/latest/admin-guide/tutorial_setup_trust.md "../../../directoryservice/latest/admin-guide/tutorial_setup_trust.md")
   in the _AWS Directory Service Administration Guide_.
   A one-way or two-way trust can be used to manage and authenticate with WorkSpaces, and so that WorkSpaces
   can be provisioned to on-premises users and groups. For more information, see
   [Deploy Amazon WorkSpaces
   using a One-Way Trust Resource Domain with AWS Directory Service](https://aws.amazon.com/getting-started/hands-on/deploy-workspaces-one-way-trust/ "https://aws.amazon.com/getting-started/hands-on/deploy-workspaces-one-way-trust/").

###### Note

- Red Hat Enterprise Linux, Rocky Linux, and Ubuntu WorkSpaces use System Security Services
  Daemon (SSSD) for Active Directory integration, and SSSD does not support forest trust.
  Configure external trust instead. Two-way trust is recommended for Amazon Linux, Ubuntu, Rocky Linux,
  and Red Hat Enterprise Linux WorkSpaces.
- You cannot use a web browser (Web Access) to connect to Linux WorkSpaces.
