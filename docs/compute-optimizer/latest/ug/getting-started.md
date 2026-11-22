

# Getting started with AWS Compute Optimizer

When you first open the AWS Compute Optimizer console, you must opt in with the account that you're signed in with. You must opt in or out before you can use the service. You can also opt in or out with the Compute Optimizer API, the AWS Command Line Interface (AWS CLI), or the AWS SDKs.

When you opt in, you let Compute Optimizer analyze the specifications and utilization metrics of your AWS resources. Examples include EC2 instances and EC2 Auto Scaling groups.

**Note**  
We might use your CloudWatch metrics and configuration data to improve Compute Optimizer recommendations. If you turn on enhanced infrastructure metrics, this includes up to three months (93 days) of metrics. To ask us to stop using this data, contact [AWS Support](https://console.aws.amazon.com/support).

## Required permissions
<a name="required-permissions"></a>

You need the right permissions to opt in to Compute Optimizer, view its recommendations, and opt out. For more information, see [Identity and Access Management for AWS Compute Optimizer](security-iam.md).

When you opt in, Compute Optimizer creates a service-linked role in your account. It uses this role to access its data. For more information, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md).

## Accounts supported by Compute Optimizer
<a name="supported-accounts"></a>

The following AWS account types can opt in to Compute Optimizer:
+ **Standalone AWS account**

  A standalone AWS account doesn't have AWS Organizations turned on. If you opt in with a standalone account, Compute Optimizer analyzes the resources in that account. It then makes recommendations for those resources.
+ **Member account of an organization**

  A member account belongs to an organization. If you opt in with a member account, Compute Optimizer analyzes only the resources in that account. It then makes recommendations for those resources.
+ **Management account of an organization**

  A management account runs an organization. If you opt in with a management account, you can choose what to opt in. You can opt in only the management account. Or you can opt in the management account and all member accounts.
**Important**  
To opt in all member accounts, turn on all features for the organization. For more information, see [Enabling All Features in Your Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.  
If you opt in with the management account and include all member accounts, Compute Optimizer turns on trusted access in your organization account. For more information, see [Trusted access for AWS Organizations](security-iam.md#trusted-service-access).

## Next steps
<a name="next-steps-getting-started"></a>

To opt in your account or your organization's accounts to AWS Compute Optimizer, see [Opting in to AWS Compute Optimizer](account-opt-in.md).

After you opt in, you can view optimization recommendations for your resources. For more information, see [Viewing resource recommendations](viewing-recommendations.md).

## Additional resources
<a name="getting-started-resources"></a>
+ [Identity and Access Management for AWS Compute Optimizer](security-iam.md)
+ [AWS managed policies for AWS Compute Optimizer](managed-policies.md)
+ [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md)