

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Identity-based policy examples for AWS WAF
<a name="security_iam_id-based-policy-examples"></a>

This section provides identity-based policy examples for AWS WAF.

By default, users and roles don't have permission to create or modify AWS WAF resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by AWS WAF, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS WAF V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswafv2.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the AWS WAF console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Grant read-only access to AWS WAF, CloudFront, and CloudWatch](#security_iam_id-based-policy-examples-read-only1)
+ [Grant full access to AWS WAF, CloudFront, and CloudWatch](#security_iam_id-based-policy-examples-full-access1)
+ [Grant access to a single AWS account](#security_iam_id-based-policy-examples-access-to-account)
+ [Grant access to a single protection pack (web ACL)](#security_iam_id-based-policy-examples-access-to-web-acl)
+ [Grant CLI access to a protection pack (web ACL) and rule group](#security_iam_id-based-policy-examples-cli-access-to-web-acl)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS WAF resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the AWS WAF console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS WAF console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the AWS WAF resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can use the AWS WAF console, also attach at least the AWS WAF `AWSWAFConsoleReadOnlyAccess` AWS managed policy to the entities. For information about this managed policy, see [AWS managed policy: AWSWAFConsoleReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWAFConsoleReadOnlyAccess). For more information about attaching a managed policy to a user, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

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

## Grant read-only access to AWS WAF, CloudFront, and CloudWatch
<a name="security_iam_id-based-policy-examples-read-only1"></a>

The following policy grants users read-only access to AWS WAF resources, to Amazon CloudFront web distributions, and to Amazon CloudWatch metrics. It's useful for users who need permission to view the settings in AWS WAF conditions, rules, and protection packs (web ACLs) to see which distribution is associated with a protection pack (web ACL), and to monitor metrics and a sample of requests in CloudWatch. These users can't create, update, or delete AWS WAF resources.

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "wafv2:Get*",
                "wafv2:List*",
                "cloudfront:GetDistribution",
                "cloudfront:GetDistributionConfig",
                "cloudfront:ListDistributions",
                "cloudfront:ListDistributionsByWebACLId",
                "cloudfront:ListDistributionTenantsByCustomization",
                "cloudfront:ListDistributionTenants",
                "cloudfront:GetDistributionTenant",
                "cloudwatch:GetMetricData",
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "ec2:DescribeRegions",
                "pricingplanmanager:GetSubscription",
                "pricingplanmanager:ListSubscriptions",
                "route53:ListHostedZones",
                "route53:GetHostedZone"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

## Grant full access to AWS WAF, CloudFront, and CloudWatch
<a name="security_iam_id-based-policy-examples-full-access1"></a>

The following policy lets users perform any AWS WAF operation, perform any operation on CloudFront web distributions, and monitor metrics and a sample of requests in CloudWatch. It's useful for users who are AWS WAF administrators.

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "wafv2:*",
                "cloudfront:CreateDistribution",
                "cloudfront:ListDistributions",
                "cloudfront:ListDistributionsByWebACLId",
                "cloudfront:UpdateDistribution",
                "cloudfront:GetDistributionConfig",
                "cloudfront:GetDistribution",
                "cloudfront:DisassociateDistributionTenantWebACL",
                "cloudfront:DisassociateDistributionWebACL",
                "cloudfront:AssociateDistributionTenantWebACL",
                "cloudfront:AssociateDistributionWebACL",
                "cloudfront:ListDistributionTenantsByCustomization",
                "cloudfront:ListDistributionTenants",
                "cloudfront:DeleteDistribution",
                "cloudfront:GetDistributionTenant",
                "cloudfront:DeleteDistributionTenant",
                "cloudwatch:GetMetricData",
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "ec2:DescribeRegions",
                "pricingplanmanager:GetSubscription",
                "pricingplanmanager:ListSubscriptions",
                "pricingplanmanager:UpdateSubscription",
                "pricingplanmanager:CancelSubscription",
                "pricingplanmanager:CancelSubscriptionChange",
                "pricingplanmanager:AssociateResourcesToSubscription",
                "pricingplanmanager:DisassociateResourcesFromSubscription",
                "route53:ListHostedZones",
                "route53:GetHostedZone"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

We strongly recommend that you configure multi-factor authentication (MFA) for users who have administrative permissions. For more information, see [Using Multi-Factor Authentication (MFA) Devices with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingMFA.html) in the *IAM User Guide*. 

## Grant access to a single AWS account
<a name="security_iam_id-based-policy-examples-access-to-account"></a>

This policy grants the following permissions to the account 444455556666:
+ Full access to all AWS WAF operations and resources.
+ Read and update access to all CloudFront distributions, which allows you to associate protection packs (web ACLs) and CloudFront distributions.
+ Read access to all CloudWatch metrics and metric statistics, so that you can view CloudWatch data and a sample of requests in the AWS WAF console. 

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
            "wafv2:*"
         ],
         "Resource": [
            "arn:aws:wafv2:us-east-1:444455556666:*"
         ]
      },
      {
         "Effect": "Allow",
         "Action": [
            "cloudfront:GetDistribution",
            "cloudfront:GetDistributionConfig",
            "cloudfront:ListDistributions",
            "cloudfront:ListDistributionsByWebACLId",
            "cloudfront:UpdateDistribution",
            "cloudwatch:ListMetrics",
            "cloudwatch:GetMetricStatistics",
            "ec2:DescribeRegions"
         ],
         "Resource": [
            "*"
         ]
      }
   ]
}
```

------

## Grant access to a single protection pack (web ACL)
<a name="security_iam_id-based-policy-examples-access-to-web-acl"></a>

The following policy lets users perform any AWS WAF operation through the console on a specific protection pack (web ACL) in the account `444455556666`.

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
                "wafv2:*"
            ],
            "Resource": [
                "arn:aws:wafv2:us-east-1:444455556666:regional/webacl/test123/112233d7c-86b2-458b-af83-51c51example"
            ]
        },
        {
            "Sid": "consoleAccess",
            "Effect": "Allow",
            "Action": [
                "wafv2:ListWebACLs",
                "ec2:DescribeRegions"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

## Grant CLI access to a protection pack (web ACL) and rule group
<a name="security_iam_id-based-policy-examples-cli-access-to-web-acl"></a>

The following policy lets users perform any AWS WAF operation through the CLI on a specific protection pack (web ACL) and a specific rule group in the account `444455556666`.

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
            "wafv2:*"
         ],
         "Resource": [
        "arn:aws:wafv2:us-east-1:444455556666:regional/webacl/test123/112233d7c-86b2-458b-af83-51c51example",
        "arn:aws:wafv2:us-east-1:444455556666:regional/rulegroup/test123rulegroup/555555555-6666-1234-abcd-00d11example"
         ]
      }
   ]
}
```

------

The following policy lets users perform any AWS WAF operation through the console on a specific protection pack (web ACL) in the account `444455556666`.

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
                "wafv2:*"
            ],
            "Resource": [
                "arn:aws:wafv2:us-east-1:444455556666:regional/webacl/test123/112233d7c-86b2-458b-af83-51c51example"
            ]
        },
        {
            "Sid": "consoleAccess",
            "Effect": "Allow",
            "Action": [
                "wafv2:ListWebACLs",
                "ec2:DescribeRegions"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------