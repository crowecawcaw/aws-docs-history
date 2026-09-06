

# Using the cost estimator
<a name="using-cost-estimator"></a>

## Accessing the cost estimator
<a name="accessing-cost-estimator"></a>

**To access the Cost Estimator from the Security Hub landing page**

1.  Sign in to your AWS account with your AWS organization management or delegated administrator account credentials. Open the Security Hub console in the us-east-1 region at [https://console.aws.amazon.com/securityhub/v2/home](https://us-east-1.console.aws.amazon.com/securityhub/v2/home).

1. On the landing page, locate the **Pricing** card.

1. Choose **Estimate cost**.

**To access the Cost Estimator during Security Hub enable and configuration steps**

1. Locate the **Pricing in the new Security Hub** card in the onboarding interface.

1. Choose **View estimates**.

**To access the cost estimator from GuardDuty, Amazon Inspector, or Security Hub CSPM consoles**

1. Navigate to the service dashboard or summary page.

1. Choose **Compare pricing** in the pricing information card.

## Understanding the cost estimator interface
<a name="understanding-estimator-interface"></a>

### Page layout
<a name="page-layout"></a>

The Cost Estimator page contains three main sections:
+ **Overview section** – Explains unified security management and cost optimization benefits.
+ **Pricing information** – Expandable panel with capability categories and pricing tiers.
+ **Pricing comparison table** – Side-by-side cost comparison with capability details.

### Pricing comparison table
<a name="pricing-comparison-table"></a>

 The table header includes view/edit mode controls and a reset option. The table displays costs in two columns: 
+ **Individual services** – Current or estimated costs for separate security services.
+ **Security Hub** – Estimated costs using simplified pricing model.

### Pricing region
<a name="pricing-region"></a>

 The first column displays pricing context information, including a note that estimates use us-east-1 pricing for calculations. A badge indicates that enterprise discounts are not included in the estimates. 

## Viewing cost estimates
<a name="viewing-cost-estimates"></a>

When using the cost estimator you can view, edit, reset, and export estimates.

The cost estimator opens in view mode by default.

**To view cost estimates**

1. Access the Cost Estimator using one of the methods described in [Accessing the cost estimator](#accessing-cost-estimator).

1. Review the total monthly costs in the summary row.

1. Review capability groups and their detailed cost breakdowns.

1. Choose capability names to view descriptions in a popover.

**Data sources in view mode**  
The estimator displays data from multiple sources, indicated by labels:
+ **Default** – Data from AWS Cost Explorer (past 30 days).
+ **$-/mo** – Cost data unavailable (shown when Cost Explorer access is not available).
+ **Custom usage** – User-entered values.
+ **Not enabled** – Shows when Cost Explorer permissions do not exist.

## Account-specific behavior
<a name="account-specific-behavior"></a>

 The following describes how the cost estimator functions across different types accounts and configurations. 

### Delegated administrator and member accounts
<a name="behavior-delegated-admin-member-account"></a>

 **With cross-account access configured:** 
+  Cost Explorer data is available with organization-wide usage. 
+  Opens in view mode by default (same as management account). You can switch to edit mode to modify estimates. 

 **Without cross-account access configured:** 
+  Alert displays: "Organizational usage data is not available for this account". 
+  Opens in edit mode by default for manual entry. 
+  Choose **View instructions** in the alert for setup guidance. 

### Management account
<a name="behavior-management-account"></a>

 **With cross-account role created:** 
+  "Cross-account access" section shows configured state. 
+  Displays recommended policies for verification. 
+  Provides link to view role in IAM console. 

 **Without cross-account role created:** 
+  "Cross-account access" section displays setup guide. 
+  Provides step-by-step instructions with pre-populated policies. 
+  Direct link to IAM console for role creation. 

 **Unable to verify role status:** 
+  If there is no permission to call `iam:GetRole`, the console cannot determine if you have created the necessary role. 
+  Shows “Unable to verify” with corresponding error message. 

### Standalone account
<a name="behavior-standalone-account"></a>

 **Without cross-account role created:** 
+  No changes to existing behavior. 
+  Cost Explorer data is available when enabled. 
+  Opens in view mode by default. 

## Editing usage values
<a name="editing-usage-values"></a>

Edit mode allows you to modify dimension values and see real-time cost updates.

**To edit usage values**

1. Choose **Edit** in the table header.

1. Enter values in the dimension input fields.

1. View updated costs automatically.

1. Choose **View** to return to view mode.

**Important**  
Edits are not saved when you leave the cost estimator page
Modified estimates use us-east-1 (N. Virginia) pricing and do not include enterprise discounts
Editing in "Show current cost only" mode automatically switches back to estimated mode

## Resetting the estimator
<a name="resetting-estimator"></a>

This action clears all custom values and reloads default data from Cost Explorer.

**To reset all values to defaults**

1. Choose **Reset** in the table header.

1. In the confirmation dialog, choose **Reset**.

## Exporting estimates
<a name="exporting-estimates"></a>

While in the cost estimator the data for your estimate can be exported to a PDF file.

**To export cost estimates**

1. Ensure you are in view mode.

1. Choose **Download PDF** in the page header.

The PDF downloads automatically with filename: `SecurityHub-Cost-Estimate-YYYY-MM-DD.pdf`.

## Troubleshooting
<a name="troubleshooting"></a>

This section covers common issues and solutions that can occur when using the cost estimator

### No Cost Explorer data available
<a name="no-cost-explorer-data"></a>

**Problem**  
Alert displays "No cost data available for your account".

**Solutions by account type**  
The solution depends on your account type:


**Solutions for missing Cost Explorer data**  

| Account Type | Solution | 
| --- | --- | 
| Management Account | Enable Cost Explorer and wait 24 hours for data processing | 
| Delegated Administrator | Contact Management Account administrator to request access | 
| Member Account | Contact Management Account or Delegated Administrator for access | 
| Standalone Account | Enable Cost Explorer and wait 24 hours for data processing | 

**Workaround**  
Enter custom values in edit mode.

### Cross-account access not working
<a name="cross-account-access-not-working"></a>

**Problem**  
Delegated administrator or member account displays "Organizational usage data is not available for this account" alert.

 **Review the following common causes and their solutions:** 

Cross-account role does not exist in management account  
Contact Management Account administrator to create the role. The cost estimator provides guided setup instructions for management account users.

Role name does not match exactly  
Required role name: `AwsSecurityHubCostEstimatorCrossAccountRole`. Verify role name in IAM console matches exactly (case-sensitive).

Trust policy does not allow your account  
Verify trust policy principal includes your account ID and role name. Format: `arn:aws:iam::{YOUR_ACCOUNT_ID}:role/{YOUR_ROLE_NAME}`.

Missing AssumeRole permission  
Verify your IAM principal has `sts:AssumeRole` permission. Contact your AWS administrator to add this permission.

 **Workaround:** 

 Enter custom values in edit mode to manually estimate costs without Cost Explorer data. 

 **Getting detailed instructions** 
+ Choose **View instructions** in the alert to open a modal with: 
  + Step-by-step setup guidance 
  + Pre-populated policy templates 
  + Troubleshooting tips specific to your error

### Permission errors
<a name="permission-errors"></a>

**Problem**  
"Access denied" error for specific API operations.

**To resolve permission errors**

1. Note the denied operation from the error message (for example, `ce:GetCostAndUsage`).

1. Choose **Copy** to copy the error details.

1. Send the error details to your AWS administrator.

1. Request the required IAM permissions listed in [Required IAM permissions](security-hub-cost-estimator.md#required-iam-permissions).

**Note**  
You can still use edit mode to enter manual values when permissions are missing, except when Pricing API access is denied (prevents all cost estimates).

### Capability shows "Not enabled"
<a name="capability-not-enabled"></a>

**Problem**  
Capability displays "Not enabled" status.

**Explanation**  
 This status appears when you have Cost Explorer access but the capability is not currently active. If you see $-/mo instead, this indicates that Cost Explorer data is not available for your account type. 

**To view cost estimates**

1. Choose **Edit** to enter edit mode.

1. Enter dimension values for the capability.

1. View updated cost estimates.

### Capability shows "Not applicable"
<a name="capability-not-applicable"></a>

**Problem**  
Capability displays "Not applicable" in Individual services column.

**Explanation**  
This capability is only available through Security Hub simplified pricing, not as a standalone service.

### Modified costs do not match Cost Explorer
<a name="modified-costs-dont-match"></a>

**Problem**  
Edited costs differ from original Cost Explorer values.

**Explanation**  
Modified estimates use us-east-1 (N. Virginia) pricing rates and do not include enterprise discounts. Cost Explorer data reflects actual costs with applicable discounts.