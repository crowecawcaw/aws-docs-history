

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# How Amazon Monitron Works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon Monitron, you should understand what IAM features are available to use with Amazon Monitron. To get a high-level view of how Amazon Monitron and other AWS services work with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon Monitron Identity-Based Policies](#security_iam_service-with-iam-id-based-policies)
+ [Amazon Monitron Resource-Based Policies](#security_iam_service-with-iam-resource-based-policies)
+ [Authorization Based on Amazon Monitron Tags](#security_iam_service-with-iam-tags)
+ [Amazon Monitron IAM Roles](#security_iam_service-with-iam-roles)
+ [Amazon Monitron Identity-Based Policy Examples](#security_iam_id-based-policy-examples)
+ [Troubleshooting Amazon Monitron Identity and Access](#security_iam_troubleshoot)

## Amazon Monitron Identity-Based Policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

To specify allowed or denied actions and resources and the conditions under which actions are allowed or denied, use IAM identity-based policies. Amazon Monitron supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

**Topics**
+ [Actions](#security_iam_service-with-iam-id-based-policies-actions)
+ [Resources](#security_iam_service-with-iam-id-based-policies-resources)
+ [Condition Keys](#security_iam_service-with-iam-id-based-policies-conditionkeys)
+ [Examples](#security_iam_service-with-iam-id-based-policies-examples)

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

In Amazon Monitron, policy actions use the following prefix before the action: `monitron:`. For example, to grant someone permission to create a project with the Amazon Monitron `CreateProject` operation, you include the `monitron:CreateProject` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon Monitron defines its own set of actions that describe tasks that you can perform with this service.

**Note**  
With the `deleteProject` operation, you must have the AWS IAM Identity Center (SSO) permissions for deletion. Without these permissions, the delete functionality will still remove the project. However, it will not remove the resources from SSO and you may end up with dangling references on SSO.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "monitron:action1",
      "monitron:action2"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "monitron:List*"
```

### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Amazon Monitron does not support specifying resource ARNs in a policy.

### Condition Keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon Monitron defines its own set of condition keys and also supports using some global condition keys. For a list of all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Amazon Monitron condition keys, see [Actions defined by Amazon Monitron](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmonitron.html#amazonmonitron-actions-as-permissions) in the *IAM User Guide*. To learn with which actions and resources you can use a condition key, see [Condition keys for Amazon Monitron](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmonitron.html#amazonmonitron-policy-keys).

### Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon Monitron identity-based policies, see [Amazon Monitron Identity-Based Policy Examples](#security_iam_id-based-policy-examples).

## Amazon Monitron Resource-Based Policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Amazon Monitron does not support resource-based policies.

## Authorization Based on Amazon Monitron Tags
<a name="security_iam_service-with-iam-tags"></a>

You can associate tags with certain types of Amazon Monitron resources for authorization. To control access based on tags, provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `Amazon Monitron:TagResource/${TagKey}`, `aws:RequestTag/${TagKey}`, or `aws:TagKeys` condition keys. 

## Amazon Monitron IAM Roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using Temporary Credentials with Amazon Monitron
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

Amazon Monitron supports using temporary credentials. 

### Service-Linked Roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles. 

Amazon Monitron supports service-linked roles. 

### Service Roles
<a name="security_iam_service-with-iam-roles-service"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service.

Amazon Monitron supports service roles. 

## Amazon Monitron Identity-Based Policy Examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to create or modify Amazon Monitron resources. They also can't perform tasks using the AWS Management Console. An IAM administrator must give permissions to the IAM users, groups, or roles that require them. Then these users, groups, or roles can perform the specific operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy Best Practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Amazon Monitron Console](#security_iam_id-based-policy-examples-console)
+ [Example: List All Amazon Monitron Projects](#security_iam_id-based-policy-examples-access-one-bucket)
+ [Example: List Amazon Monitron Projects Based on Tags](#security_iam_id-based-policy-examples-view-widget-tags)

### Policy Best Practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon Monitron resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

### Using the Amazon Monitron Console
<a name="security_iam_id-based-policy-examples-console"></a>

To set up Amazon Monitron using the console, please complete the initial setup process using a high privilege user (such as one with the `AdministratorAccess` managed policy attached). 

To access the Amazon Monitron console for day-to-day operations after the initial setup, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Amazon Monitron resources in your AWS account and include a set of permissions related to IAM Identity Center. If you create an identity-based policy that is more restrictive than these minimum required permissions, the console won't function as intended for entities (IAM users or roles) with that policy. For basic Amazon Monitron Console functionality, you need to attach the `AmazonMonitronFullAccess` managed policy. Depending on the circumstances, you may also need additional permissions to the Organizations and SSO service. Contact AWS support if you need more information.

### Example: List All Amazon Monitron Projects
<a name="security_iam_id-based-policy-examples-access-one-bucket"></a>

This example policy grants an IAM user in your AWS account permission to list all projects in your account. 

### Example: List Amazon Monitron Projects Based on Tags
<a name="security_iam_id-based-policy-examples-view-widget-tags"></a>

You can use conditions in your identity-based policy to control access to Amazon Monitron resources based on tags. This example shows how you might create a policy that allows listing projects. However, permission is granted only if the project tag `location` has the value of `Seattle`. This policy also grants the permissions necessary to complete this action on the console.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ListProjectsInConsole",
            "Effect": "Allow",
            "Action": "monitron:ListProjects",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/location": "Seattle"
                }
            }
        }
    ]
}
```

------

For more information, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

## Troubleshooting Amazon Monitron Identity and Access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Monitron and IAM.

**Topics**
+ [I Am Not Authorized to Perform an Action in Amazon Monitron](#security_iam_troubleshoot-no-permissions)
+ [I Want to Allow People Outside of My AWS Account to Access My Amazon Monitron Resources](#security_iam_troubleshoot-cross-account-access)

### I Am Not Authorized to Perform an Action in Amazon Monitron
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `monitron:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: monitron:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `monitron:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

### I Want to Allow People Outside of My AWS Account to Access My Amazon Monitron Resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Amazon Monitron supports these features, see [How Amazon Monitron Works with IAM](#security_iam_service-with-iam).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.