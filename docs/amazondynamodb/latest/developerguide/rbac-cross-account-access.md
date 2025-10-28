# Cross-account access with resource-based policies

in DynamoDB

Using a resource-based policy, you can provide cross-account access to resources available
in different AWS accounts. All cross-account access allowed by the resource-based policies
will be reported through IAM Access Analyzer external access findings if you have an analyzer in the
same AWS Region as the resource. IAM Access Analyzer runs policy checks to validate your policy
against IAM [policy
grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") and [best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").
These checks generate findings and provide actionable recommendations to help you author
policies that are functional and conform to security best practices. You can view the active
findings from IAM Access Analyzer in the **Permissions** tab of the
[DynamoDB console](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").

For information about validating policies by using IAM Access Analyzer, see [IAM Access Analyzer policy
validation](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_. To view a
list of the warnings, errors, and suggestions that are returned by IAM Access Analyzer, see [IAM Access Analyzer policy check
reference](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md").

To grant [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md") permission to a
user A in account A for accessing a table B in account B, perform the following steps:

1. Attach a resource-based policy to table B that grants permission to user A for
   performing the `GetItem` action.
2. Attach an identity-based policy to user A that grants it permission to perform the
   `GetItem` action on table B.
   Using the **Preview external access** option available in [DynamoDB console](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/"),
   you can preview how your new policy affects public and cross-account access to your resource.
   Before you save your policy, you can check whether it introduces new IAM Access Analyzer findings or
   resolves existing findings. If you don’t see an active analyzer, choose **Go to Access
   Analyzer** to [create an account analyzer](../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling "../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling") in IAM Access Analyzer. For more information, see [Preview
   access](../../../IAM/latest/UserGuide/access-analyzer-access-preview.md "../../../IAM/latest/UserGuide/access-analyzer-access-preview.md").

The table name parameter in the DynamoDB data plane and control plane APIs accept complete
Amazon Resource Name (ARN) of the table to support cross-account operations. If you only
provide the table name parameter instead of a complete ARN, the API operation will be
performed on the table in the account to which the requestor belongs. For an example of a
policy that uses cross-account access, see [Resource-based policy for cross-account
access](rbac-examples.md#rbac-examples-cross-account "rbac-examples.md#rbac-examples-cross-account").

The resource owner’s account will be charged even when a principal from another account is
reading from or writing to the DynamoDB table in the owner’s account. If the table has
provisioned throughput, the sum of all the requests from the owner accounts and the requestors
in other accounts will determine if the request will be throttled (if autoscaling is disabled)
or scaled up/down if autoscaling is enabled.

The requests will be logged in the CloudTrail logs of both the owner and the requestor accounts
so that each of the two accounts can track which account accessed what data.

###### Note

The cross-account access of [control plane
APIs](HowItWorks.md#HowItWorks.API.ControlPlane "HowItWorks.md#HowItWorks.API.ControlPlane") has a lower transactions per second (TPS) limit of 500 requests.
