# Using the cost estimator

## Accessing the cost estimator

###### To access the Cost Estimator from the Security Hub landing page

1. Sign in to your AWS account with your AWS organization management account credentials.
   Open the Security Hub console in the us-east-1 region at [https://console.aws.amazon.com/securityhub/v2/home](https://us-east-1.console.aws.amazon.com/securityhub/v2/home " https://us-east-1.console.aws.amazon.com/securityhub/v2/home").
2. On the landing page, locate the **Pricing** card.
3. Choose **Estimate cost**.

###### To access the Cost Estimator during Security Hub enable and configuration steps

1. Locate the **Pricing in the new Security Hub** card in the onboarding interface.
2. Choose **View estimates**.

###### To access the cost estimator from GuardDuty, Amazon Inspector, or Security Hub CSPM consoles

1. Navigate to the service dashboard or summary page.
2. Choose **Compare pricing** in the pricing information card.

## Understanding the cost estimator interface

### Page layout

The Cost Estimator page contains three main sections:

- **Overview section** – Explains unified security management and cost optimization benefits.
- **Pricing information** – Expandable panel with capability categories and pricing tiers.
- **Pricing comparison table** – Side-by-side cost comparison with capability details.

### Pricing comparison table

The table header includes view/edit mode controls and a reset option.
The table displays costs in two columns:

- **Individual services** – Current or estimated costs for separate security services.
- **Security Hub** – Estimated costs using simplified pricing model.

### Pricing region

The first column displays pricing context information, including a note that estimates use us-east-1 pricing for calculations.
A badge indicates that enterprise discounts are not included in the estimates.

## Viewing cost estimates

When using the cost estimator you can view, edit, reset, and export estimates.

The cost estimator opens in view mode by default.

###### To view cost estimates

1. Access the Cost Estimator using one of the methods described in [Accessing the cost estimator](#accessing-cost-estimator "#accessing-cost-estimator").
2. Review the total monthly costs in the summary row.
3. Review capability groups and their detailed cost breakdowns.
4. Choose capability names to view descriptions in a popover.

###### Data sources in view mode

The estimator displays data from multiple sources, indicated by labels:

- **Default** – Data from AWS Cost Explorer (past 30 days).
- **$-/mo** – Cost data unavailable (shown when Cost Explorer access is not available).
- **Custom usage** – User-entered values.
- **Not enabled** – Shows when Cost Explorer permissions do not exist.

## Account-specific behavior

The following describes how the cost estimator functions across different types accounts and configurations.

### Delegated administorator and member accounts

**With cross-account access configured:**

- Cost Explorer data is available with organization-wide usage.
- Opens in view mode by default (same as management account). Can switch to edit mode to modify estimates.

**Without cross-account access configured:**

- Alert displays: "Organizational usage data is not available for this account".
- Opens in edit mode by default for manual entry.
- Click "View instructions" in alert for setup guidance.

### Management account

**With cross-account role created:**

- "Cross-account access" section shows configured state.
- Displays recommended policies for verification.
- Provides link to view role in IAM console.

**Without cross-account role created:**

- "Cross-account access" section displays setup guide.
- Provides step-by-step instructions with pre-populated policies.
- Direct link to IAM console for role creation.

**Unable to verify role status:**

- If there is no permission to call `iam:GetRole`, the console cannot determine if you have created the necessary role.
- Shows “Unable to verify” with corresponding error message.

### Standalone account

**Without cross-account role created:**

- No changes to existing behavior.
- Cost Explorer data is available when enabled.
- Opens in view mode by default.

## Editing usage values

Edit mode allows you to modify dimension values and see real-time cost updates.

###### To edit usage values

1. Choose **Edit** in the table header.
2. Enter values in the dimension input fields.
3. View updated costs automatically.
4. Choose **View** to return to view mode.

###### Important

- Edits are not saved when you leave the cost estimator page
- Modified estimates use us-east-1 (N. Virginia) pricing and do not include enterprise discounts
- Editing in "Show current cost only" mode automatically switches back to estimated mode

## Resetting the estimator

This action clears all custom values and reloads default data from Cost Explorer.

###### To reset all values to defaults

1. Choose **Reset** in the table header.
2. In the confirmation dialog, choose **Reset**.

## Exporting estimates

While in the cost estimator the data for your estimate can be exported to a PDF file.

###### To export cost estimates

1. Ensure you are in view mode.
2. Choose **Download PDF** in the page header.

The PDF downloads automatically with filename: `SecurityHub-Cost-Estimate-YYYY-MM-DD.pdf`.

## Troubleshooting

This section covers common issues and solutions that can occur when using the cost estimator

### No Cost Explorer data available

###### Problem

Alert displays "No cost data available for your account".

###### Solutions by account type

The solution depends on your account type:

| Solutions for missing Cost Explorer data | Account Type                                                     | Solution |
| ---------------------------------------- | ---------------------------------------------------------------- | -------- |
| Management Account                       | Enable Cost Explorer and wait 24 hours for data processing       |
| Delegated Administrator                  | Contact Management Account administrator to request access       |
| Member Account                           | Contact Management Account or Delegated Administrator for access |
| Standalone Account                       | Enable Cost Explorer and wait 24 hours for data processing       |

###### Workaround

Enter custom values in edit mode.

### Cross-account access not working

###### Problem

"Delegated administrator or member account displays "Organizational usage data is not available for this account" alert.

###### Possible causes and solutions

1. Cross-account role doesn't exist in management account.
   1. **Solution:** Contact Management Account administrator to create the role.
   2. The cost estimator provides guided setup instructions for management account users.

2. Role name doesn't match exactly.
   1. Required role name: `AwsSecurityHubCostEstimatorCrossAccountRole`.
   2. **Solution:** Verify role name in IAM console matches exactly (case-sensitive).

3. Trust policy doesn't allow your account.
   1. **Solution:** Verify trust policy principal includes your account ID and role name.
   2. Format: `arn:aws:iam::{YOUR_ACCOUNT_ID}:role/{YOUR_ROLE_NAME}`.

4. Missing AssumeRole permission.
   1. **Solution:** Verify your IAM principal has `sts:AssumeRole` permission.
   2. ontact your AWS administrator to add this permission.

**Workaround:**

Enter custom values in edit mode to manually estimate costs without Cost Explorer data.

**Getting detailed instructions**

- Click "View instructions" link in the alert to open a modal with:
  - Step-by-step setup guidance
  - Pre-populated policy templates
  - Troubleshooting tips specific to your error

### Permission errors

###### Problem

"Access denied" error for specific API operations.

###### To resolve permission errors

1. Note the denied operation from the error message (e.g., `ce:GetCostAndUsage`).
2. Choose **Copy** to copy the error details.
3. Send the error details to your AWS administrator.
4. Request the required IAM permissions listed in [Required IAM permissions](security-hub-cost-estimator.md#required-iam-permissions "security-hub-cost-estimator.md#required-iam-permissions").

###### Note

You can still use edit mode to enter manual values when permissions are missing, except when Pricing API access is denied (prevents all cost estimates).

### Capability shows "Not enabled"

###### Problem

Capability displays "Not enabled" status.

###### Explanation

This status appears when you have Cost Explorer access but the capability is not currently active.
If you see $-/mo instead, this indicates that Cost Explorer data is not available for your account type.

###### To view cost estimates

1. Choose **Edit** to enter edit mode.
2. Enter dimension values for the capability.
3. View updated cost estimates.

### Capability shows "Not applicable"

###### Problem

Capability displays "Not applicable" in Individual services column.

###### Explanation

This capability is only available through Security Hub simplified pricing, not as a standalone service.

### Modified costs don't match Cost Explorer

###### Problem

Edited costs differ from original Cost Explorer values.

###### Explanation

Modified estimates use us-east-1 (N. Virginia) pricing rates and do not include enterprise discounts. Cost Explorer data reflects actual costs with applicable discounts.
