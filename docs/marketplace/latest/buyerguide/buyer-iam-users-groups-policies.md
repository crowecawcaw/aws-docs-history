

# Controlling access to AWS Marketplace subscriptions
<a name="buyer-iam-users-groups-policies"></a>

AWS IAM Identity Center helps you securely create or connect your workforce identities and manage their access centrally across AWS accounts and applications. IAM Identity Center is the recommended approach for workforce authentication and authorization in AWS for organizations of any size and type. For additional configuration guidance, review the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html#mgmt-sso).

IAM Identity Center provides a user portal where your users can find and access their assigned AWS account, roles, cloud applications, and custom applications in one place. IAM Identity Center assigns single sign-on access to users and groups in your connected directory and uses permission sets to determine their level of access. This enables temporary security credentials. You can define their level of access by assigning specific AWS managed roles for AWS Marketplace access to delegate the management of AWS Marketplace subscriptions across your AWS organization. 

For example, Customer A assumes a role through federation with the `ManagedMarketplace_ViewOnly` policy attached to the role. This means Customer A can only view subscriptions in AWS Marketplace. You can create an IAM role with permissions to view subscriptions and grant permission to Customer A to [assume this role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html).

## Creating IAM roles for AWS Marketplace access
<a name="buyer-creating-iam-role-for-marketplace-access"></a>

You can use IAM roles to delegate access to your AWS resources.

**To create IAM roles for assigning AWS Marketplace permissions**

1. Open the [IAM Console](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles** and then choose **Create role**.

1. Choose your AWS account.

1. From **Add permissions**, select one of the following policies:
   + To allow permissions only to view subscriptions, but not change them, choose **AWSMarketplaceRead-only**.
   + To allow permissions to subscribe and unsubscribe, choose **AWSMarketplaceManageSubscriptions**.
   + To allow complete control of your subscriptions, choose **AWSMarketplaceFullAccess**.

1. Choose **Next**.

1. For **Role name**, enter a name for the role. For example, {{MarketplaceReadOnly}} or {{MarketplaceFullAccess}}. Then choose **Create role**. For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html).

**Note**  
The administrator of the specified account can grant permission to assume this role to any user in that account.

Repeat the preceding steps to create more roles with different permission sets so that each user persona can use the IAM role with customized permissions.

You're not limited to the permissions in the AWS managed policies that are described here. You can use IAM to create policies with custom permissions and then add those policies to IAM roles. For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) and [Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) in the *IAM User Guide*.

## AWS managed policies for AWS Marketplace
<a name="buyer-iam-builtin-policies"></a>

You can use AWS managed policies to provide basic AWS Marketplace permissions. Then, for any unique scenarios, you can create your own policies and apply them to the roles with the specific requirements for your scenario. The following basic AWS Marketplace managed policies are available to you to control who has which permissions.

The following links take you to the [AWS Managed Policy Reference](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html).
+ [AWSMarketplaceRead-only](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceRead-only.html)``
+ [AWSMarketplaceManageSubscriptions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html)
+ [AWSPrivateMarketplaceRequests](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.html)
+ [AWSPrivateMarketplaceAdminFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.html)
+ [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html)

AWS Marketplace also provides specialized managed policies for specific scenarios. For a full list of AWS managed policies for AWS Marketplace buyers, as well as descriptions of what permissions they provide, see [AWS managed policies for AWS Marketplace buyers](buyer-security-iam-awsmanpol.md) in this section.

## Permissions for working with License Manager
<a name="buyer-iam-permissions-for-license-manager"></a>

AWS Marketplace integrates with AWS License Manager to manage and share licenses for products that you subscribe to between accounts in your organization. To view the full details of your subscriptions in AWS Marketplace, a user must be able to list license information from AWS License Manager.

To make sure that your users have the permissions they need to see all the data about their AWS Marketplace products and subscriptions, add the following permission:
+ `license-manager:ListReceivedLicenses`

For more information about setting permissions, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide*.

## Additional resources
<a name="buyer-iam-permissions-for-more-information"></a>

For more information about managing IAM roles, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*. 

For more information about managing IAM permissions and policies, see [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html) in the *IAM User Guide*. 

For more information about managing IAM permissions and policies for data products in AWS Data Exchange, see [Identity and access management in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/auth-access.html) in the *AWS Data Exchange User Guide*.