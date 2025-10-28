# Controlling access to AWS Marketplace

subscriptions

AWS IAM Identity Center helps you securely create or connect your workforce identities and manage their
access centrally across AWS accounts and applications. IAM Identity Center is the recommended approach for
workforce authentication and authorization in AWS for organizations of any size and type. For
additional configuration guidance, review the [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/org-management.md#mgmt-sso "../../../prescriptive-guidance/latest/security-reference-architecture/org-management.md#mgmt-sso").

IAM Identity Center provides a user portal where your users can find and access their assigned
AWS account, roles, cloud applications, and custom applications in one place. IAM Identity Center assigns
single sign-on access to users and groups in your connected directory and uses permission sets
to determine their level of access. This enables temporary security credentials. You can define
their level of access by assigning specific AWS managed roles for AWS Marketplace access to delegate the
management of AWS Marketplace subscriptions across your AWS organization.

For example, Customer A assumes a role through federation with the
`ManagedMarketplace_ViewOnly` policy attached to the role. This means Customer A
can only view subscriptions in AWS Marketplace. You can create an IAM role with permissions to view
subscriptions and grant permission to Customer A to [assume this role](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").

## Creating IAM roles for

AWS Marketplace access

You can use IAM roles to delegate access to your AWS resources.

###### To create IAM roles for assigning AWS Marketplace permissions

1. Open the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles** and then choose
   **Create role**.
3. Choose your AWS account.
4. From **Add permissions**, select one of the following
   policies:
   - To allow permissions only to view subscriptions, but not change them, choose
     **AWSMarketplaceRead-only**.
   - To allow permissions to subscribe and unsubscribe, choose
     **AWSMarketplaceManageSubscriptions**.
   - To allow complete control of your subscriptions, choose
     **AWSMarketplaceFullAccess**.

5. Choose **Next**.
6. For **Role name**, enter a name for the role. For example,
   `MarketplaceReadOnly` or
   `MarketplaceFullAccess`. Then choose **Create
   role**. For more information, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

###### Note

The administrator of the specified account can grant permission to assume this role to
any user in that account.

Repeat the preceding steps to create more roles with different permission sets so that
each user persona can use the IAM role with customized permissions.

You're not limited to the permissions in the AWS managed policies that are described
here. You can use IAM to create policies with custom permissions and then add those policies
to IAM roles. For more information, see [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") and [Adding IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the _IAM User Guide_.

## AWS managed policies for AWS Marketplace

You can use AWS managed policies to provide basic AWS Marketplace permissions. Then, for any
unique scenarios, you can create your own policies and apply them to the roles with the
specific requirements for your scenario. The following basic AWS Marketplace managed policies are
available to you to control who has which permissions.

The following links take you to the [AWS Managed Policy Reference](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

- [AWSMarketplaceRead-only](../../../aws-managed-policy/latest/reference/AWSMarketplaceRead-only.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceRead-only.md")
- [AWSMarketplaceManageSubscriptions](../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md")
- [AWSPrivateMarketplaceRequests](../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.md "../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.md")
- [AWSPrivateMarketplaceAdminFullAccess](../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.md")
- [AWSMarketplaceFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md")

AWS Marketplace also provides specialized managed policies for specific scenarios. For a full
list of AWS managed policies for AWS Marketplace buyers, as well as descriptions of what permissions
they provide, see [AWS managed policies for AWS Marketplace
buyers](buyer-security-iam-awsmanpol.md "buyer-security-iam-awsmanpol.md") in this section.

## Permissions for working with

License Manager

AWS Marketplace integrates with AWS License Manager to manage and share licenses for products that you
subscribe to between accounts in your organization. To view the full details of your
subscriptions in AWS Marketplace, a user must be able to list license information from AWS License Manager.

To make sure that your users have the permissions they need to see all the data about
their AWS Marketplace products and subscriptions, add the following permission:

- `license-manager:ListReceivedLicenses`

For more information about setting permissions, see [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the
_IAM User Guide_.

## Additional resources

For more information about managing IAM roles, see [IAM Identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the
_IAM User Guide_.

For more information about managing IAM permissions and policies, see [Controlling access to AWS resources using
policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.

For more information about managing IAM permissions and policies for data products in
AWS Data Exchange, see [Identity and access management in AWS Data Exchange](../../../data-exchange/latest/userguide/auth-access.md "../../../data-exchange/latest/userguide/auth-access.md") in the _AWS Data Exchange User
Guide_.
