

# Identity and access management for License Manager
<a name="identity-access-management"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be authenticated (signed in) and authorized (have permissions) to use AWS resources. With IAM you can create users and groups under your AWS account. You control the permissions that users have to perform tasks using AWS resources. You can use IAM for no additional charge.

By default, users don't have permissions for License Manager resources and operations. To allow users to manage License Manager resources, you must create an IAM policy that explicitly grants them permissions. 

When you attach a policy to a user or group of users, it allows or denies the users permission to perform the specified tasks on the specified resources. For more information, see [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide* guide.

## Create users, groups, and roles
<a name="getting-started-create-users-groups-roles"></a>

You can create users and groups for your AWS account and then assign them the permissions they require. As a best practice, users should acquire the permissions by assuming IAM roles. For more information on how to set up users and groups for your AWS account, see [Get started with License Manager](getting-started.md).

 An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user in that it is an AWS identity with permissions policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session. 

## IAM policy structure
<a name="iam-policy-structure"></a>

An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows.

```
{
  "Statement":[{
    "Effect":"{{effect}}",
    "Action":"{{action}}",
    "Resource":"{{arn}}",
    "Condition":{
      "{{condition}}":{
        "{{key}}":"{{value}}"
        }
      }
    }
  ]
}
```

Various elements make up a statement:
+ **Effect:** The *effect* can be `Allow` or `Deny`. By default, users don't have permission to use resources and API operations, so all requests are denied. An explicit *allow* overrides the default. An explicit *deny* overrides any allows.
+ **Action**: The *action* is the specific API operation for which you are granting or denying permission.
+ **Resource**: The resource is affected by the action. Some License Manager API operations allow you to include specific resources in your policy that can be created or modified by the operation. To specify a resource in the statement, you need to use its Amazon Resource Name (ARN). For more information, see [Actions Defined by AWS License Manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslicensemanager.html#awslicensemanager-actions-as-permissions).
+ **Condition**: Conditions are optional. They can be used to control when your policy is in effect. For more information, see [Condition Keys for AWS License Manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslicensemanager.html#awslicensemanager-policy-keys).

## Create IAM policies for License Manager
<a name="iam-policy-examples"></a>

In an IAM policy statement, you can specify any API operation from any service that supports IAM. License Manager, uses the following prefixes with the name of the API operation:
+ `license-manager:`
+ `license-manager-user-subscriptions:`
+ `license-manager-linux-subscriptions:`

For example:
+ `license-manager:CreateLicenseConfiguration`
+ `license-manager:ListLicenseConfigurations`
+ `license-manager-user-subscriptions:ListIdentityProviders`
+ `license-manager-linux-subscriptions:ListLinuxSubscriptionInstances`

For more information on the available License Manager APIs, see the following API references:
+ [AWS License Manager API Reference](https://docs.aws.amazon.com/license-manager/latest/APIReference/Welcome.html)
+ [AWS License Manager User Subscriptions API Reference](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/Welcome.html)
+ [AWS License Manager Linux Subscriptions API Reference](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/Welcome.html)

To specify multiple operations in a single statement, separate them with commas as follows:

```
"Action": ["license-manager:action1", "license-manager:action2"]
```

You can also specify multiple operations using wildcards. For example, you can specify all License Manager API operations whose name begins with the word *List* as follows:

```
"Action": "license-manager:List*"
```

To specify all License Manager API operations, use the \* wildcard as follows:

```
"Action": "license-manager:*"
```

### Example policy for an ISV using License Manager
<a name="vended-license-requirements"></a>

ISVs that distribute licenses through License Manager require the following permissions:

------
#### [ JSON ]

****  

```
{ 
    "Version":"2012-10-17",		 	 	      
    "Statement": [ 
        { 
        "Sid": "VisualEditor0", 
        "Effect": "Allow",
        "Action": [
            "license-manager:CreateLicense", 
            "license-manager:ListLicenses", 
            "license-manager:CreateLicenseVersion", 
            "license-manager:ListLicenseVersions", 
            "license-manager:GetLicense", 
            "license-manager:DeleteLicense", 
            "license-manager:CheckoutLicense", 
            "license-manager:CheckInLicense", 
            "kms:GetPublicKey"
        ], 
        "Resource": "*"
        } 
    ] 
}
```

------

## Grant permissions to users, groups, and roles
<a name="getting-started-grant-permissions"></a>

Once you have created the IAM policies you require, you must grant these permissions to your users, groups, and roles.

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.