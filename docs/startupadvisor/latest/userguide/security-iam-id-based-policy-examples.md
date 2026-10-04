

# AWS Startups identity-based policy examples
<a name="security-iam-id-based-policy-examples"></a>

By default, IAM users and roles don’t have permission to create or modify AWS Startups resources. They also can’t perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security-iam-service-with-iam-policy-best-practices)
+ [Allowing access to the AWS credits and cost tracker](#security-iam-id-based-policy-examples-cost-tracker)

## Policy best practices
<a name="security-iam-service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS Startups resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+  **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the AWS managed policies that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+  **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+  **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [IAM JSON policy elements: condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+  **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+  **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or root users in your account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [Configuring MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

## Allowing access to the AWS credits and cost tracker
<a name="security-iam-id-based-policy-examples-cost-tracker"></a>

The following least-privilege identity-based policy allows an identity to call `startups:GetSpendSummary`, which powers the AWS credits and cost tracker widget, along with the downstream AWS Cost Explorer and AWS Billing and Cost Management actions that the operation performs on your behalf. Because the IDE extension calls the operation with your own AWS profile credentials, attach this policy to your identity.

The `startups:GetSpendSummary` action does not support resource-level permissions, so the `Resource` element is set to ` ` (an asterisk). This is expected for this action, and the least-privilege control is the scoped list of actions. Do not use wildcard actions such as `startups:` or `ce:*`.

**Note**  
If your identity is missing one or more of the downstream permissions, the `startups:GetSpendSummary` operation still returns a successful response. However, one or more sections of the response contain an error with the code `ACCESS_DENIED` and a message from the downstream service. If the credits and cost tracker widget shows missing or empty sections, verify that your identity has all of the actions in the following policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowStartupAdvisorCostTracker",
            "Effect": "Allow",
            "Action": [
                "startups:GetSpendSummary",
                "aws-portal:ViewBilling",
                "billing:GetCredits",
                "ce:GetCostAndUsage",
                "ce:GetCostForecast"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about the `aws-portal:ViewBilling` permission, see [AWS Billing identity-based policy examples](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html) in the *AWS Billing User Guide*. For the complete list of actions, resources, and condition keys, see [Actions, resources, and condition keys for AWS Billing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbilling.html) and [Actions, resources, and condition keys for AWS Cost Explorer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostexplorerservice.html) in the *Service Authorization Reference*.