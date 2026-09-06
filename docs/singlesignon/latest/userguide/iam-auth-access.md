

# Identity and access management for IAM Identity Center
<a name="iam-auth-access"></a>

Access to IAM Identity Center requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access AWS resources, such as an AWS managed application. 

Authentication to the AWS access portal is controlled by the directory that you have connected to IAM Identity Center. However, authorization to the AWS accounts that are available to users from within the AWS access portal is determined by two factors:

1. Who has been assigned access to those AWS accounts in the IAM Identity Center console. For more information, see [Single sign-on access to AWS accounts](useraccess.md).

1. What level of permissions have been granted to the users in the IAM Identity Center console to allow them the appropriate access to those AWS accounts. For more information, see [Create, manage, and delete permission sets](permissionsets.md).

The following sections explain how you as an administrator can control access to the IAM Identity Center console or can delegate administrative access for day-to-day tasks from the IAM Identity Center console. 
+ [Authentication](#authentication)
+ [Access control](#accesscontrol)

## Authentication
<a name="authentication"></a>

Learn how to access AWS using [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html).

## Access control
<a name="accesscontrol"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions, you cannot create or access IAM Identity Center resources. For example, you must have permissions to create an IAM Identity Center connected directory.

**Note**  
If your IAM Identity Center instance is configured with a customer managed KMS key, your IAM Identity Center administrators and other actors who need access to the KMS key will need additional permissions. Refer to [Implementing customer managed KMS keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md).

The following sections describe how to manage permissions for IAM Identity Center. We recommend that you read the overview first.

 
+ [Overview of managing access permissions to your IAM Identity Center resources](iam-auth-access-overview.md)
+  [Identity-based policy examples for IAM Identity Center](iam-auth-access-using-id-policies.md) 
+  [Resource-based policy example for IAM Identity Center](iam-auth-access-using-resource-based-policies.md) 
+  [Using service-linked roles for IAM Identity Center](using-service-linked-roles.md) 