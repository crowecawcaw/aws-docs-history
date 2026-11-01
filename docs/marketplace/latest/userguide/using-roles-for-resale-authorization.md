

# Using service-linked roles for Selling Authorization with AWS Marketplace
<a name="using-roles-for-resale-authorization"></a>

AWS Marketplace uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Marketplace. Service-linked roles are predefined by AWS Marketplace and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up AWS Marketplace easier because you don’t have to manually add the necessary permissions. AWS Marketplace defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Marketplace can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your AWS Marketplace resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for AWS Marketplace](#slr-permissions)
+ [Creating a service-linked role for AWS Marketplace](#create-slr)
+ [Editing a service-linked role for AWS Marketplace](#edit-slr)
+ [Deleting a service-linked role for AWS Marketplace](#delete-slr)
+ [Supported Regions for AWS Marketplace service-linked roles](#slr-regions)

## Service-linked role permissions for AWS Marketplace
<a name="slr-permissions"></a>

AWS Marketplace uses the service-linked role named **AWSServiceRoleForMarketplaceResaleAuthorization**, which enables access to AWS services and resources used or managed by AWS Marketplace for Selling Authorizations.

The AWSServiceRoleForMarketplaceResaleAuthorization service-linked role trusts the following services to assume the role:
+ `resale-authorization.marketplace.amazonaws.com`

The role permissions policy named **AWSMarketplaceResaleAuthorizationServiceRolePolicy** allows AWS Marketplace to share ResaleAuthorization resources between manufacturers (ISVs) and channel partners using AWS Resource Access Manager (AWS RAM).

For details about the permissions in this policy, see [AWSMarketplaceResaleAuthorizationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

For information about policy updates, see [AWS managed policy updates](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates) in this guide.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS Marketplace
<a name="create-slr"></a>

You create the AWSServiceRoleForMarketplaceResaleAuthorization service-linked role in AWS Partner Central. You don't need to create it manually in IAM. Both manufacturers (ISVs) and channel partners need this role in the AWS account that they use for Selling Authorizations and channel partner private offers.

To view the role status, you need the `iam:GetRole` permission. To create the role, you also need the `iam:CreateServiceLinkedRole` permission.

**To create a service-linked role**

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) with the AWS account that you sell from.

1. In the navigation pane, under **Settings**, choose **Account**.

1. Choose the **Service roles** tab.

1. In the **Seller service-linked roles** section, check the status of the Resale Authorizations service-linked role.

   If the status is **AWS Marketplace Resale Authorization service-linked role created**, the role already exists in your account and you don't need to create it.

1. Choose **Create service-linked role**.

1. On the **Service-linked role for Resale Authorizations** page, under **Review service-linked role**, review the information about the role.

1. Select **AWS Marketplace Resale Authorization service-linked role for this account**, and then choose **Create service-linked role**.

   The **Service roles** tab opens and shows the message **Service-linked role was successfully created**. The status might take a few minutes to update.

If you delete the service-linked role, you can follow these steps to recreate it.

You can also create the role by using the AWS CLI or the IAM API. For example, run the following command in the account that needs the role.

```
aws iam create-service-linked-role --aws-service-name resale-authorization.marketplace.amazonaws.com
```

For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*.

## Editing a service-linked role for AWS Marketplace
<a name="edit-slr"></a>

AWS Marketplace does not allow you to edit the AWSServiceRoleForMarketplaceResaleAuthorization service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Marketplace
<a name="delete-slr"></a>

If you no longer need a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained.

**Note**  
If independent software vendors (ISVs) don't have the role, AWS Resource Access Manager won't automatically share new Selling Authorizations with the targeted channel partner. If channel partners don't have the role, AWS Resource Access Manager won't automatically accept the Selling Authorization targeted to them.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForMarketplaceResaleAuthorization service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS Marketplace service-linked roles
<a name="slr-regions"></a>

AWS Marketplace supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html#aws-marketplace_region).