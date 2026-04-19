# Feature comparison with and without AWS Config integration

With Landing Zone 4.0, you can disable the AWS Config integration. The following
table summarizes the AWS Control Tower features that are available with and without the AWS Config integration enabled on the landing zone.

| Features                                                                                                                                      | AWS Config Integration Enabled | AWS Config Integration Disabled |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------- |
| [Preventive controls](../controlreference/preventive-controls.md "../controlreference/preventive-controls.md")                                | ✓                              | ✓                               |
| [Proactive controls](../controlreference/proactive-controls.md "../controlreference/proactive-controls.md")                                   | ✓                              | ✓                               |
| [Region Deny control applied to OUs](../controlreference/ou-region-deny.md "../controlreference/ou-region-deny.md")                           | ✓                              | ✓                               |
| [Region Deny control applied to landing zone](region-deny.md "region-deny.md")                                                                | ✓                              |                                 |
| [Detective controls](../controlreference/detective-controls.md "../controlreference/detective-controls.md")                                   | ✓                              |                                 |
| [Account Factory](account-factory.md "account-factory.md")                                                                                    | ✓                              | See alternative                 |
| [Account Factory for Terraform (AFT)](aft-overview.md "aft-overview.md")                                                                      | ✓                              |                                 |
| [Account Factory Customizations (AFC)](af-customization-page.md "af-customization-page.md")                                                   | ✓                              |                                 |
| [AWS Service Catalog integration](service-catalog.md "service-catalog.md") with [Account Factory](account-factory.md "account-factory.md")    | ✓                              |                                 |
| [Customizations for AWS Control Tower (CfCT)](cfct-customizations-dev-guide.md "cfct-customizations-dev-guide.md")                            | ✓                              |                                 |
| [Baselines applied to OUs](types-of-baselines.md#ou-baseline-types "types-of-baselines.md#ou-baseline-types")                                 | ✓                              |                                 |
| [AWS CloudTrail integration and baselines](cloudtrail.md "cloudtrail.md")                                                                     | ✓                              | ✓                               |
| [AWS Backup integration and baselines](with-backup.md "with-backup.md")                                                                       | ✓                              |                                 |
| [AWS IAM Identity Center integration and baselines](sso.md "sso.md")                                                                          | ✓                              |                                 |
| [AWS SNS integration for drift notifications](sns.md "sns.md")                                                                                | ✓                              |                                 |
| [Amazon EventBridge integration for drift notifications](governance-drift.md#eventbridge-creation "governance-drift.md#eventbridge-creation") | ✓                              | ✓                               |
| [Register OU](importing-existing.md "importing-existing.md")                                                                                  | ✓                              | See alternative                 |

**Alternatives**

**Account Factory**

If you have the AWS Config integration disabled, you can enable
[auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md")
and use AWS Organizations to create and move accounts. The accounts will inherit the controls applied to the parent OU.

**Register OU**

If you have the AWS Config integration disabled, you can use AWS Organizations to create OUs. Then, enable controls through the
Control Catalog page in the AWS Control Tower console, reset controls on the Organization page, or use AWS Control Tower APIs.
