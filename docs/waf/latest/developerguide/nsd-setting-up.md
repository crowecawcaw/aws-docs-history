**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up your account to use AWS Shield network security director

###### Note

AWS Shield network security director is in public preview release and is subject to change.

AWS Shield network security director requires AWS Organizations to manage security across multiple accounts in your organization. This topic describes the preliminary steps to prepare your AWS environment, including setting up Organizations, designating a delegated administrator, and configuring the necessary IAM permissions. You aren't charged for these preliminary setup steps. You are charged only for AWS services that you use.

## Prerequisites

Before you can use AWS Shield network security director, you must have the following in place:

- **AWS Organizations** - AWS Shield network security director works exclusively with AWS Organizations to provide security analysis across multiple accounts. You cannot use AWS Shield network security director with a single standalone account.
- **Management account access** - You need access to the AWS Organizations management account to designate a delegated administrator for AWS Shield network security director.
- **Delegated administrator account** - You need to identify or create an account that will serve as the delegated administrator for AWS Shield network security director. This cannot be the Organizations management account.

###### Important

AWS Shield network security director cannot be used with standalone AWS accounts. You must have AWS Organizations configured with at least one member account in addition to the management account.

## Understanding AWS Organizations integration

AWS Organizations is a global account management service that lets AWS administrators consolidate and manage multiple AWS accounts. AWS Shield network security director integrates with Organizations to provide centralized security analysis and management across your entire organization.

When you integrate AWS Shield network security director with AWS Organizations:

- The Organizations management account designates a delegated administrator for AWS Shield network security director
- The delegated administrator can enable AWS Shield network security director across multiple accounts and regions
- Security analysis and findings are centrally managed through the delegated administrator account
- Service-linked roles are automatically created in member accounts to enable analysis

This approach is similar to other AWS security services like AWS Security Hub and provides consistent governance across your security tools.

## Choosing a delegated administrator

A delegated administrator is an AWS account in your organization that has been granted permissions to manage AWS Shield network security director on behalf of the organization. The delegated administrator can enable the service, create policies, and manage security findings across all member accounts.

**Delegated administrator requirements:**

- Must be a member account in your AWS Organizations structure
- Cannot be the Organizations management account
- Should have appropriate IAM permissions configured (see next section)

###### Note

As a best practice, we recommend using the same delegated administrator account across AWS security services (such as Security Hub, GuardDuty, and AWS Shield network security director) for consistent governance and simplified management.

## IAM requirements for the delegated administrator

The delegated administrator account requires specific IAM permissions to manage AWS Shield network security director effectively. You must attach the following policy to the IAM user or role that will be managing AWS Shield network security director in the delegated administrator account.

**Required IAM policy for AWS Shield network security director delegated administrator:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "network-security-director:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": [
                "arn:aws:iam:::role/aws-service-role/AWSServiceRoleForNetworkSecurityDirector"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "organizations:ListRoots",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListAccountsForParent",
                "organizations:ListAccounts",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListDelegatedAdministrators",
                "organizations:DescribeOrganization",
                "organizations:CreatePolicy",
                "organizations:UpdatePolicy",
                "organizations:DeletePolicy",
                "organizations:AttachPolicy",
                "organizations:DetachPolicy",
                "organizations:EnablePolicyType",
                "organizations:DisablePolicyType",
                "organizations:DescribeOrganization",
                "organizations:DescribeOrganizationalUnit",
                "organizations:DescribeAccount",
                "organizations:ListRoots",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListParents",
                "organizations:ListChildren",
                "organizations:ListAccounts",
                "organizations:ListAccountsForParent",
                "organizations:ListTagsForResource",
                "organizations:ListDelegatedAdministrators",
                "organizations:ListHandshakesForAccount",
                "organizations:DescribePolicy",
                "organizations:DescribeEffectivePolicy",
                "organizations:ListPolicies",
                "organizations:ListPoliciesForTarget",
                "organizations:ListTargetsForPolicy"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

**Policy explanation:**

- **network-security-director:\*** - Grants full access to all AWS Shield network security director operations, including enabling the service, creating policies, and managing findings.
- **IAM permissions** - Allows the delegated administrator to manage the service-linked role that AWS Shield network security director uses to perform analysis across member accounts.

###### To create and attach the IAM policy

1. Sign in to the AWS Management Console using the delegated administrator account.
2. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3. In the navigation pane, choose **Policies**, then choose **Create policy**.
4. Choose the **JSON** tab and paste the policy document shown above.
5. Choose **Next: Tags**, then **Next: Review**.
6. For **Name**, enter `NetworkSecurityDirectorDelegatedAdminPolicy`.
7. Choose **Create policy**.
8. Attach this policy to the IAM user or role that will be managing AWS Shield network security director in the delegated administrator account.

## Setup checklist

Before proceeding to enable AWS Shield network security director, ensure you have completed the following setup tasks:

- ✓ AWS Organizations is configured with a management account and at least one member account
- ✓ You have identified a delegated administrator account (cannot be the management account)
- ✓ The required IAM policy has been created and attached in the delegated administrator account
- ✓ You have access to both the Organizations management account and the delegated administrator account

Once you have completed these setup tasks, you can proceed to [Enabling AWS Shield network security director](nsd-enablement.md "nsd-enablement.md") to enable AWS Shield network security director for your organization.
