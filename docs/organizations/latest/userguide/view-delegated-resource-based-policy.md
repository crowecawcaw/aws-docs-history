# View a resource-based delegation

policy with AWS Organizations

From the management account, view your organization’s resource-based delegation policy
to understand which delegated administrators have access to manage which policy
types.

###### Minimum permissions

To view the resource-based delegation policy, you need permissions to run the
following action: `organizations:DescribeResourcePolicy`.

AWS Management Console

###### To view a delegation policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Choose **Settings**.
3. In the **Delegated administrator for AWS Organizations**
   section, scroll to view the full delegation policy.

AWS CLI & AWS SDKs

###### View a delegation policy

You can use the following command to view a delegation policy:

- AWS CLI: [describe-resource-policy](../../../cli/latest/reference/organizations/describe-resource-policy.md "../../../cli/latest/reference/organizations/describe-resource-policy.md")

The following example retrieves the policy.

```
`$` **aws organizations describe-resource-policy**
```

- AWS SDK: [DescribeResourcePolicy](../APIReference/API_DescribeResourcePolicy.md "../APIReference/API_DescribeResourcePolicy.md")
