

# AWS managed policies for AWS Sign-In
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonManagedSignUpServicePolicy
<a name="security-iam-awsmanpol-AmazonManagedSignUpServicePolicy"></a>

The `AmazonManagedSignUpServicePolicy` policy grants permissions required to complete AWS account sign-up processes.

You can attach `AmazonManagedSignUpServicePolicy` to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ **Customer verification** - Allows creating, retrieving, and updating customer verification details and eligibility status, including creating upload URLs for verification documents.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonManagedSignUpServicePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonManagedSignUpServicePolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: ApplicationProvisioningPolicy
<a name="security-iam-awsmanpol-ApplicationProvisioningPolicy"></a>

The ApplicationProvisioningPolicy policy grants comprehensive permissions for application provisioning and identity management operations, including IAM role and policy management, SSO configuration, and identity store operations.

You can attach `ApplicationProvisioningPolicy` to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ **IAM management** - Allows comprehensive IAM operations including creating, updating, and deleting roles and policies, managing role attachments, and creating service-linked roles.
+ **Research and Engineering Studio on AWS** - Allows all operations on Research and Engineering Studio on AWS resources.
+ **Role passing** - Allows passing IAM roles to other services.
+ **IAM Identity Center** - Allows managing IAM Identity Center instances, applications, assignments, grants, and authentication methods.
+ **Identity Store** - Allows reading user and group information from the Identity Store.
+ **IAM Identity Center OAuth** - Allows authenticating IAM sessions through IAM Identity Center OAuth.
+ **User Profile and Directory** - Allows managing IAM Identity Center connectors, user profiles, and directory configurations including external identity provider setup.
+ **User Subscriptions** - Allows listing user subscriptions.

To view more details about the policy, including the latest version of the JSON policy document, see [ApplicationProvisioningPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ApplicationProvisioningPolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: SignInLocalDevelopmentAccess
<a name="security-iam-awsmanpol-SignInLocalDevelopmentAccess"></a>

The `SignInLocalDevelopmentAccess` policy grants permissions for programmatic access to AWS using your console credentials.

You can attach `SignInLocalDevelopmentAccess` to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ **Authorizing OAuth2 access** - Grants permission to authenticate through a browser and obtain an OAuth 2.0 authorization code for credential exchange 
+ **OAuth2 token creation** - Grants permission to exchange an authorization code for OAuth 2.0 access token and refresh token that can be used to access AWS services from developer tools and applications 

**Note**  
Adding this AWS managed policy gives you permission for both same-device and cross-device authentication. This policy authorizes actions on the following resources:  
`arn:aws:signin:{{region}}:{{account-id}}:oauth2/public-client/localhost` – Used for same-device authentication with `aws login`.
`arn:aws:signin:{{region}}:{{account-id}}:oauth2/public-client/remote` – Used for cross-device authentication with `aws login --remote`.
To control access to either authentication method, you can create your own managed policy or service control policy (SCP). Use these resource ARNs to allow or deny programmatic access to AWS using your console credentials.

For more information, see [Login with console credentials (Recommended)](command-line-sign-in.md#command-line-sign-in-local-development). To view more details about the policy, including the latest version of the JSON policy document, see [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSSignInResourcePolicyManagement
<a name="security-iam-awsmanpol-AWSSignInResourcePolicyManagement"></a>

The `AWSSignInResourcePolicyManagement` policy grants permissions to manage console authorization configuration and resource permission statements for AWS Sign-In.

You can attach `AWSSignInResourcePolicyManagement` to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ `signin:PutConsoleAuthorizationConfiguration` – Create or update console authorization settings.
+ `signin:GetConsoleAuthorizationConfiguration` – Retrieve the current console authorization configuration.
+ `signin:DeleteConsoleAuthorizationConfiguration` – Remove the console authorization configuration.
+ `signin:PutResourcePermissionStatement` – Create or update resource permission statements.
+ `signin:DeleteResourcePermissionStatement` – Remove resource permission statements.
+ `signin:ListResourcePermissionStatements` – List resource permission statements for the account.
+ `signin:GetResourcePolicy` – Retrieve the consolidated resource-based policy.

The following is the policy JSON:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "signin:PutConsoleAuthorizationConfiguration",
                "signin:GetConsoleAuthorizationConfiguration",
                "signin:DeleteConsoleAuthorizationConfiguration",
                "signin:PutResourcePermissionStatement",
                "signin:DeleteResourcePermissionStatement",
                "signin:ListResourcePermissionStatements",
                "signin:GetResourcePolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

Attach this policy to IAM principals (users or roles) who manage resource-based policies for AWS Sign-In. This includes security administrators responsible for configuring network-based access controls, compliance officers who need to audit console access policies, and operations teams managing emergency recovery access configurations.

**Important**  
This policy grants administrative access to console authorization controls. Apply the principle of least privilege when assigning this policy. Consider using IAM conditions to further restrict when and how these permissions can be used.

To view more details about the policy, including the latest version of the JSON policy document, see [AWSSignInResourcePolicyManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSignInResourcePolicyManagement.html) in the *AWS Managed Policy Reference Guide*.

## AWS Sign-In updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Sign-In since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Sign-In Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSSignInResourcePolicyManagement](#security-iam-awsmanpol-AWSSignInResourcePolicyManagement) – New policy | Added a new AWS managed policy that grants permissions to manage console authorization configuration and resource permission statements for AWS Sign-In. | June 10, 2026 | 
| [SignInLocalDevelopmentAccess](#security-iam-awsmanpol-SignInLocalDevelopmentAccess) – New policy | Added a new AWS managed policy that grants permissions for programmatic access to AWS using your existing console credentials. | November 19, 2025 | 
| [ApplicationProvisioningPolicy](#security-iam-awsmanpol-ApplicationProvisioningPolicy) – New policy | Added a new AWS managed policy that grants comprehensive permissions for application provisioning and identity management operations, including IAM role and policy management, IAM Identity Center configuration, and Identity Store operations. | September 30, 2025 | 
| [AmazonManagedSignUpServicePolicy](#security-iam-awsmanpol-AmazonManagedSignUpServicePolicy) – New policy | Added a new AWS managed policy that grants permissions required for AWS account sign-up processes, including customer verification and payment setup operations. | September 30, 2025 | 
| AWS Sign-In started tracking changes | AWS Sign-In started tracking changes for its AWS managed policies. | September 30, 2025 | 