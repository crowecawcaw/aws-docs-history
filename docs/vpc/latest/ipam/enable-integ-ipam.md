

# Integrate IPAM with accounts in an AWS Organization
<a name="enable-integ-ipam"></a>

Optionally, you can follow the steps in this section to integrate IPAM with AWS Organizations and delegate a member account as the IPAM account.

The IPAM account is responsible for creating an IPAM and using it to manage and monitor IP address usage.

Integrating IPAM with AWS Organizations and delegating an IPAM admin has the following benefits:
+ **Share your IPAM pools with your organization**: When you delegate an IPAM account, IPAM enables other AWS Organizations member accounts in the organization to allocate CIDRs from IPAM pools that are shared using AWS Resource Access Manager (RAM). For more information on setting up an organization, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *AWS Organizations User Guide*.
+ **Monitor IP address usage in your organization**: When you delegate an IPAM account, you give IPAM permission to monitor IP usage across all of your accounts. As a result, IPAM automatically imports CIDRs that are used by existing VPCs across other AWS Organizations member accounts into IPAM.

If you do not delegate an AWS Organizations member account as an IPAM account, IPAM will monitor resources only in the AWS account that you use to create the IPAM.

**Note**  
When integrating with AWS Organizations:  
You must enable integration with AWS Organizations by using IPAM in the AWS management console or the [enable-ipam-organization-admin-account](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-organization-admin-account.html) AWS CLI command. This ensures that the `AWSServiceRoleForIPAM` service-linked role is created. If you enable trusted access with AWS Organizations by using the AWS Organizations console or the [register-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html) AWS CLI command, the `AWSServiceRoleForIPAM` service-linked role isn't created, and you can't manage or monitor resources within your organization.
**The IPAM account must be an AWS Organizations member account.** You cannot use the AWS Organizations management account as the IPAM account. To check whether your IPAM is already integrated with AWS Organizations, use the steps below and view the details of the integration in *Organization settings*.
IPAM charges you for each active IP address that it monitors in your organization's member accounts. For more information about pricing, see [IPAM pricing](https://aws.amazon.com/vpc/pricing/).
You must have an account in AWS Organizations and a management account set up with one or more member accounts. For more information about account types, see [ Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*. For more information on setting up an organization, see [Getting started with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html).
The IPAM account must use an IAM role that has an IAM policy attached to it that permits the `iam:CreateServiceLinkedRole` action. When you create the IPAM, you automatically create the AWSServiceRoleForIPAM service-linked role.
The user associated with the AWS Organizations management account must use an IAM role that has the following IAM policy actions attached:  
`ec2:EnableIpamOrganizationAdminAccount`
`organizations:EnableAwsServiceAccess`
`organizations:RegisterDelegatedAdministrator`
`iam:CreateServiceLinkedRole`
For more information on creating IAM roles, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
The user associated with the AWS Organizations management account may use an IAM role that has the following IAM policy actions attached to list your current AWS Orgs delegated administrators: `organizations:ListDelegatedAdministrators`

------
#### [ AWS Management Console ]

**To select an IPAM account**

1. Using the AWS Organizations management account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. In the AWS Management Console, choose the AWS Region in which you want to work with IPAM.

1. In the navigation pane, choose **Organization settings**.

1. The **Delegate** option is only available if you've logged in to the console as the AWS Organizations management account. Choose **Delegate**. 

1. Enter the AWS account ID for an IPAM account. The IPAM administrator must be an AWS Organizations member account.

1. Choose **Save changes**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.
+ To delegate an IPAM admin account using AWS CLI, use the following command: [enable-ipam-organization-admin-account](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-organization-admin-account.html)

------

When you delegate an Organizations member account as an IPAM account, IPAM automatically creates a service-linked IAM role in all member accounts in your organization. IPAM monitors the IP address usage in these accounts by assuming the service-linked IAM role in each member account, discovering the resources and their CIDRs, and integrating them with IPAM. The resources within all member accounts will be discoverable by IPAM regardless of their Organizational Unit. If there are member accounts that have created a VPC, for example, you'll see the VPC and its CIDR in the Resources section of the IPAM console.

**Important**  
The role of the AWS Organizations management account that delegated the IPAM admin is now complete. To continue using IPAM, the IPAM admin account must log into Amazon VPC IPAM and create an IPAM. 