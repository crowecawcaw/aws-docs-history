# Cross-account analyses for Reachability Analyzer

Reachability Analyzer analyzes the path between a source and destination. To analyze paths across multiple
AWS accounts, enable trusted access for Reachability Analyzer with your organization from AWS Organizations. You can
also register member accounts as delegated administrator accounts. A user in the management
account can define paths and run analyses using sources and destinations from any account in
the organization. A user in a delegated administrator account can define paths and run
analyses using sources and destinations from any account in the organization other than the
management account, plus any resources in the management account that were explicitly shared
with the delegated administrator account.

For more information, see [Visualize and diagnose network reachability across AWS accounts](https://aws.amazon.com/blogs/networking-and-content-delivery/visualize-and-diagnose-network-reachability-across-aws-accounts-using-reachability-analyzer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/visualize-and-diagnose-network-reachability-across-aws-accounts-using-reachability-analyzer/").

###### Pricing

There is no additional charge to run cross-account analyses.

###### Considerations

- Before accounts in the organization can use this feature in an opt-in Region,
  the management account must enable the opt-in Region. For more information, see
  [Enable a Region in your organization](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization") in the _AWS Account Management Guide_.
- The accounts in the organization must be able to make calls to the AWS CloudFormation
  API in US East (N. Virginia) (`us-east-1`).
- AWS CloudTrail logs are always written to US East (N. Virginia) (`us-east-1`).

###### Tasks

- [Enable trusted access in Reachability Analyzer](enable-trusted-access.md "enable-trusted-access.md")
- [IAM role deployments in Reachability Analyzer](manage-role-deployments.md "manage-role-deployments.md")
- [Manage delegated administrator
  accounts in Reachability Analyzer](manage-delegated-administrators.md "manage-delegated-administrators.md")
- [Disable trusted access in Reachability Analyzer](disable-trusted-access.md "disable-trusted-access.md")
- [Troubleshoot cross-account analyses in
  Reachability Analyzer](multi-account-troubleshooting.md "multi-account-troubleshooting.md")
