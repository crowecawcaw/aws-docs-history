# Configuring access policies for Performance Insights

To access Performance Insights, a principal must have the appropriate permissions from AWS Identity and Access Management (IAM).

###### Note

To use Performance Insights with a customer-managed key, grant users the `kms:Decrypt` and `kms:GenerateDataKey` permissions for your AWS AWS KMS key.

Access Performance Insights using these methods:

- [Attach the AmazonRDSPerformanceInsightsReadOnly managed policy for read-only access](USER_PerfInsights.access-control.managed-policy.md "USER_PerfInsights.access-control.managed-policy.md")
- [Attach the AmazonRDSPerformanceInsightsFullAccess managed policy for access to all operations of the Performance Insights API](USER_PerfInsights.access-control.FullAccess-managed-policy.md "USER_PerfInsights.access-control.FullAccess-managed-policy.md")
- [Create a custom IAM policy with specific permissions](USER_PerfInsights.access-control.custom-policy.md "USER_PerfInsights.access-control.custom-policy.md")
- [Configure AWS KMS permissions for encrypted Performance Insights data](USER_PerfInsights.access-control.cmk-policy.md "USER_PerfInsights.access-control.cmk-policy.md")
- [Set up fine-grained access using resource-level permissions](USER_PerfInsights.access-control.dimensionAccess-policy.md "USER_PerfInsights.access-control.dimensionAccess-policy.md")
- [Use tag-based access control to manage permissions through resource tags](USER_PerfInsights.access-control.tag-based-policy.md "USER_PerfInsights.access-control.tag-based-policy.md")
