# Using Account Tags for Cost Allocation

## Overview

AWS supports cost allocation based on account tags from AWS Organizations. This feature enables organizations to automatically track and
allocate costs according to their internal organizational structure using account-level tags such as business unit, cost center, project, and environment.
Account tags operate at the account level and automatically apply to all metered usage within tagged accounts. Once activated for cost allocation,
these tags provide organization-wide cost visibility and work alongside resource-level tags for comprehensive cost allocation strategies.

## How Account-Based Cost Allocation Works

When you apply tags to AWS accounts in your organization, those tags are automatically recorded with usage and associated costs from that account. All resources and usage within tagged accounts inherit the account-level tags, mitigating manual cost allocation processes at the account level.

## Key Benefits

Account tags for cost allocation map usage to internal organizational structures at the account level.
You can see which business units, projects, or environments are consuming AWS services and the associated costs,
enabling data-driven decisions about resource allocation, budget planning, and optimization opportunities.
Account tags enable cost allocation for untaggable resources and costs within an account, including refunds, credits and certain
service charges that cannot be tagged at the resource level. Account tags ensure these costs are properly allocated to your organizational structure, improving cost allocation coverage in your cost reports.
Account tags integrate with existing AWS Cost Management tools like Cost Explorer and Cost and Usage Reports (CUR2.0 and FOCUS),
giving you access to this new dimension for cost analysis. Once activated, account tags also work across AWS Cost Management products including AWS Budgets,
Cost Categories, and Cost Anomaly Detection—similar to how resource tags function—enabling consistent cost tracking and analysis throughout your cost management workflows.

## Prerequisites

Before you can use account tags for cost allocation, ensure you have:

- **AWS Organizations** A management account with consolidated billing
- **Account Tags:** Tags applied to accounts in AWS Organizations
- **Permissions:** Access to AWS Organizations and Billing and Cost Management consoles

## Setting Up Account Tags for Cost Allocation

### Step 1: Apply Account Tags in AWS Organizations

###### Note

As a best practice, do not use “accountTag" keyword in your tag keys, as this prefix is automatically added by AWS for account tags in cost allocation reports.

1. Navigate to AWS Organizations console
2. Select the accounts you want to tag
3. Apply tags that represent your organizational structure (e.g., business unit, cost center, project, environment)

### Step 2: Activate Account Tags for Cost Allocation and Verify Setup

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the left navigation pane, under Cost Organization, select **Cost Allocation Tags**
3. Filter for **Account Tags**
4. Search and Select the account tags that you want to activate
5. Choose **Activate**
6. Verify tags show as "Active"
7. It can take up to 24 hours for tag activation status to change to “Active”
