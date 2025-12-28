# AWS Security Hub Cost Estimator

The Security Hub cost estimator is a console feature that provides estimates for capabilities across your AWS environnment.
The cost estimator shows you what your individual service costs are across AWS Security Hub CSPM, Amazon Inspector, and Amazon GuardDuty and what your estimated costs would be in Security Hub with Security Hub's simplied pricing plans.
You can adjust estimated usage and resource counts to match your AWS usage to increase the accuracy of your estimate.
The cost estimator is available in all regions where Security Hub is available.

The cost estimator estimates montly costs for security capabilities using two pricing models:

- **Individual services pricing** – Pay for each security feature separately (GuardDuty, Amazon Inspector, Security Hub CSPM).
- **Security Hub simplified pricing** – Unified pricing across 3 pricing plans, essentials plan with per-resource pricing, threat analytics with per-event and per-GB logs pricing, and Lambda Code scanning with per-resource pricing.
  The estimator uses AWS Cost Explorer data when available. When Cost Explorer data is unavailable, you can manually enter usage data.
  Cost estimates are based on observed and user provided usage, and public pricing infomation. Estimates may not reflect enterprise discounts.

Key benefits of the cost estimator include:

- See how the cost with unified pricing, when enabling Security Hub, compares against cost with individual service without enabling Security Hub
- Estimate costs before enabling capabilities
- Adjust usage parameters to model different scenarios
- Export estimates as PDF for stakeholder review

## Access by account type

###### Note

This feature automatically retrieves information on actual past usage to estimate the cost for certain account types.
The estimator also provides sample data that you can update, in the absence of actual past usage data.
See below for details on each of the account types and the data that is available for each account type.

| Access permissions by account type | Account Type   | Cost Explorer Data        | Data Entry        | Scope |
| ---------------------------------- | -------------- | ------------------------- | ----------------- | ----- |
| Management Account (MA)            | Auto-populated | Manual override available | Organization-wide |
| Delegated Administrator (DA)       | Not available  | Manual entry only         | Manual entry only |
| Member Account                     | Not available  | Manual entry only         | Manual entry only |
| Standalone Account (SA)            | Auto-populated | Manual override available | Single account    |

## Prerequisites

### Required IAM permissions

In order to use the all of the cost estimator's capabilties your IAM principal must have the following permissions:

| Required IAM permissions for Cost Estimator | API Operation     | Service                                 | Purpose |
| ------------------------------------------- | ----------------- | --------------------------------------- | ------- |
| `ce:GetCostAndUsage`                        | AWS Cost Explorer | Retrieve historical usage and cost data |
| `pricing:GetProducts`                       | AWS Pricing       | Get current pricing rates               |
| `organizations:ListAccounts`                | AWS Organizations | Count accounts in organization          |
| `organizations:DescribeOrganization`        | AWS Organizations | Determine account type                  |
| `securityhub:ListOrganizationAdminAccounts` | Security Hub      | List organization admin accounts        |

### Additional requirements

**Cost Explorer**

Must be enabled for automatic data population (24-hour processing delay after enablement).

## Important notes

- **Estimates are based on observed and user provided usage, and public pricing infomation** – Actual costs may vary based on usage patterns and enterprise agreements
- **30-day look back** – Cost Explorer data reflects the past 30 days of usage
- **Pricing region** – All estimates use us-east-1 (N. Virgina) rates
- **No impact on settings** – Changes in the estimator do not affect your current Security Hub or service configurations
- **Enterprise discounts** – Modified estimates do not include enterprise discounts; only Cost Explorer data reflects actual discounted costs
- **Data refresh** – Cost Explorer data updates daily; refresh the page to see the latest data

## Related information

- [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/")
- [AWS Cost Explorer User Guide](../../../cost-management/latest/userguide.md "../../../cost-management/latest/userguide.md")
- [AWS Pricing API Reference](../../../aws-cost-management/latest/APIReference.md "../../../aws-cost-management/latest/APIReference.md")
- [Enabling Security Hub](securityhub-settingup.md "securityhub-settingup.md")
