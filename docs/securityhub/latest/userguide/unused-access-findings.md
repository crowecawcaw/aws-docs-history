# Understanding unused access findings in Security Hub

Security Hub uses IAM Access Analyzer to identify unused IAM permissions, roles, access keys, and passwords in your account. These findings help you implement the security best practice of least-privilege access by highlighting IAM principals and permissions that are not actively being used. This capability is provided to all Security Hub customers at no additional cost.

## How unused access analysis works

When you enable Security Hub, the service automatically creates a service-linked IAM Access Analyzer in your account. This analyzer evaluates all IAM principals (roles and users) against AWS CloudTrail activity data to determine which principals and permissions have not been used within a 90-day lookback period. The lookback period is not configurable.

IAM Access Analyzer re-evaluates all active findings every 24 hours. When a previously unused principal or permission becomes active, the corresponding finding is automatically resolved.

The unused access analyzer runs in US East (N. Virginia) because IAM is a global service. Security Hub replicates findings to all Regions where you have enabled Security Hub. You do not need to enable Security Hub in US East (N. Virginia) for the analyzer to run.

## Unused access finding types

Security Hub generates four types of unused access findings:

| Finding type           | Description                                                                                                          | Resource evaluated   |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------- |
| UnusedIAMRole          | An IAM role that has not been assumed within the 90-day lookback period.                                             | IAM role             |
| UnusedIAMUserAccessKey | An IAM user access key that has not been used to sign API requests within the 90-day lookback period.                | IAM user             |
| UnusedIAMUserPassword  | An IAM user password that has not been used for console sign-in within the 90-day lookback period.                   | IAM user             |
| UnusedPermission       | Specific IAM actions that are granted to a role or user but have not been invoked within the 90-day lookback period. | IAM role or IAM user |

## Service-linked analyzer

The IAM Access Analyzer that Security Hub creates is a service-linked analyzer. You can view it in the IAM Access Analyzer console, but you cannot modify or delete it while Security Hub is enabled.

When you disable Security Hub in all Regions, the service-linked analyzer is automatically deleted. If automatic deletion fails, you can delete the analyzer by calling the IAM Access Analyzer `DeleteServiceLinkedAnalyzer` API operation. This operation succeeds only after Security Hub is fully disabled for your account.

The service-linked analyzer is separate from any customer-managed analyzers you may have created independently in IAM Access Analyzer. Creating or deleting customer-managed analyzers does not affect the service-linked analyzer, and vice versa.

## Viewing unused access findings

Unused access findings appear in the Security Hub console alongside other Security Hub findings.
You can filter findings by type to view only unused access findings.
Unused access findings are formatted in the Open Cybersecurity Schema Framework (OCSF), the same format used by all Security Hub findings.

For UnusedPermission findings, if you remove some unused permissions from the overly permissive policy, but not all, Security Hub closes the existing finding and creates a new finding for the revised policy if it is still overly permissive.

Unused access findings are also accessible from the IAM Access Analyzer console.
Unused access findings in the IAM Access Analyzer console are read only and are only visible in the US East (N. Virginia) region.

## Unused access in exposure findings

Unused access information can appear as contextual traits in Security Hub exposure findings. When an IAM role attached to a resource has unused permissions, the exposure finding includes this as supplementary context. This helps you understand the potential blast radius of a vulnerability — a resource with an over-privileged IAM role presents a higher risk than one with least-privilege permissions.

The following resource types can display unused access contextual traits in their exposure findings:

- Amazon Elastic Compute Cloud instances
- AWS Lambda functions
- Amazon Elastic Container Service services
- Amazon Elastic Kubernetes Service clusters
- IAM users (directly)

For more information about exposure findings, see [Exposure findings in Security Hub](exposure-findings.md "exposure-findings.md").

## Policy recommendations for unused permissions

For UnusedPermission findings, Security Hub can generate least-privilege policy recommendations. These recommendations show you a scoped-down replacement policy that retains only the permissions your principal actually uses. For more information, see [Generating policy recommendations for unused access findings](unused-access-recommendations.md "unused-access-recommendations.md").

## Pricing

The service-linked IAM Access Analyzer is provided to all Security Hub customers at no additional cost. You are not separately charged for the analyzer or for unused access findings.
