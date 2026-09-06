

# Identity-based policy examples for AWS Organizations
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Organizations resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Organizations, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Granting full admin permissions to a user](#orgs_permissions_grant-admin-actions)
+ [Granting limited access by actions](#orgs_permissions_grant-limited-actions)
+ [Granting access to specific resources](#orgs_permissions_grant-limited-resources)
+ [Granting the ability to enable trusted access to limited service principals](#orgs_permissions_grant-trusted-access-condition)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Organizations resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the Organizations console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS Organizations console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Organizations resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the Organizations console, also attach the Organizations [`AWSOrganizationsFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.html) or [`AWSOrganizationsReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.html) AWS managed policy to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Granting full admin permissions to a user
<a name="orgs_permissions_grant-admin-actions"></a>

You can create an IAM policy that grants full AWS Organizations administrator permissions to an IAM user in your organization. You can do this using the JSON policy editor in the IAM console. 

**To use the JSON policy editor to create a policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

   If this is your first time choosing **Policies**, the **Welcome to Managed Policies** page appears. Choose **Get Started**.

1. At the top of the page, choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter the following JSON policy document:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": {
           "Effect": "Allow",
           "Action": "organizations:*",
           "Resource": "*"
       }
   }
   ```

1. Choose **Next**.
**Note**  
You can switch between the **Visual** and **JSON** editor options anytime. However, if you make changes or choose **Next** in the **Visual** editor, IAM might restructure your policy to optimize it for the visual editor. For more information, see [Policy restructuring](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure) in the *IAM User Guide*.

1. On the **Review and create** page, enter a **Policy name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. Choose **Create policy** to save your new policy.

To learn more about creating an IAM policy, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

## Granting limited access by actions
<a name="orgs_permissions_grant-limited-actions"></a>

If you want to grant limited permissions instead of full permissions, you can create a policy that lists individual permissions that you want to allow in the `Action` element of the IAM permissions policy. As shown in the following example, you can use wildcard (\*) characters to grant only the `Describe*` and `List*` permissions, essentially providing read-only access to the organization.

**Note**  
In a service control policy (SCP), the wildcard (\*) character in an `Action` element can be used only by itself or at the end of the string. It can't appear at the beginning or middle of the string. Therefore, `"servicename:action*"` is valid, but `"servicename:*action"` and `"servicename:some*action"` are both invalid in SCPs.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "organizations:Describe*", 
            "organizations:List*" 
        ],
        "Resource": "*"
    }
}
```

------

For a list of all the permissions that are available to assign in an IAM policy, see [Actions defined by AWS Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-actions-as-permissions) in the *Service Authorization Reference*.

## Granting access to specific resources
<a name="orgs_permissions_grant-limited-resources"></a>

In addition to restricting access to specific actions, you can restrict access to specific entities in your organization. The `Resource` elements in the examples in the preceding sections both specify the wildcard character ("\*"), which means "any resource that the action can access." Instead, you can replace the "\*" with the Amazon Resource Name (ARN) of specific entities to which you want to allow access. 

**Example: Granting permissions to a single OU**  
The first statement of the following policy allows an IAM user read access to the entire organization, but the second statement allows the user to perform AWS Organizations administrative actions only within a single, specified organizational unit (OU). This does not extend to any child OUs. No billing access is granted. Note that this doesn't give you administrative access to the AWS accounts in the OU. It grants only permissions to perform AWS Organizations operations on the accounts within the specified OU:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:Describe*",
                "organizations:List*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "organizations:*",
            "Resource": "arn:aws:organizations::{{123456789012}}:ou/{{o-<organizationId>}}/{{ou-<organizationalUnitId>}}"
        }
    ]
}
```

------

You get the IDs for the OU and the organization from the AWS Organizations console or by calling the `List*` APIs. The user or group that you apply this policy to can perform any action (`"organizations:*"`) on any entity that is directly contained in the specified OU. The OU is identified by the Amazon Resource Name (ARN). 

For more information about the ARNs for various resources, see [Resources types defined by AWS Organizations](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Service Authorization Reference*. 

## Granting the ability to enable trusted access to limited service principals
<a name="orgs_permissions_grant-trusted-access-condition"></a>

You can use the `Condition` element of a policy statement to further limit the circumstances where the policy statement matches.

**Example: Granting permissions to enable trusted access to one specified service**  
The following statement shows how you can restrict the ability to enable trusted access to only those services that you specify. If the user tries to call the API with a different service principal than the one for AWS IAM Identity Center, this policy doesn't match and the request is denied:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "organizations:EnableAWSServiceAccess",
            "Resource": "*",
            "Condition": { 
                "StringEquals" : {
                    "organizations:ServicePrincipal" : "sso.amazonaws.com"
                }
            }
        }
    ]
}
```

------

For more information about the ARNs for various resources, see [Resources types defined by AWS Organizations](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the *Service Authorization Reference*.