

# Using user attributes for cost allocation
<a name="user-attributes-cost-allocation"></a>

## Overview
<a name="user-attributes-overview"></a>

AWS supports cost allocation based on user attributes for Amazon Q Business, Amazon Q Developer, and Amazon QuickSight. This feature enables organizations to automatically track and allocate costs according to their internal organizational structure using existing workforce user attributes such as cost center, division, organization, and department.

## How user-based cost allocation works
<a name="user-based-cost-allocation-works"></a>

Once you enable user attributes for cost allocation, when employees use AWS applications that charge per user, their usage and associated costs are automatically recorded with their organizational attributes. This helps you eliminate the need for manual cost allocation processes and provides accurate visibility into how different teams and departments are driving AWS costs.

## Key benefits
<a name="user-attributes-key-benefits"></a>

Once you enable user attributes for cost allocation, you can map usage to internal organizational structures. You can use user attributes to see which teams, departments, or cost centers are consuming AWS services and at what rate, enabling data-driven decisions about resource allocation, budget planning, and optimization opportunities. This includes subscription-based charges and feature-specific overage charges, giving organizations a complete picture of their AWS application cost and usage. It works with existing AWS Cost Management tools like Cost Explorer and Cost and Usage Reports (CUR2.0 and FOCUS), giving you access to this new dimension for cost analysis.

## Prerequisites
<a name="user-attributes-prerequisites"></a>

Before you can use user attributes for cost allocation, ensure you have:
+ **AWS Organizations** A management account with consolidated billing
+ **IAM Identity Center:** Configured and managing workforce access to AWS applications
+ **Identity Provider (IdP) Integration:** Connection to Microsoft Entra ID, Okta, or another supported IdP
+ **User Attributes:** Cost center, division, organization, or department attributes in your identity system
+ **Permissions:** Access to IAM Identity Center and Billing and Cost Management consoles

## Setting up user attributes for cost allocation
<a name="setting-up-user-attributes"></a>

### Step 1: Import user attributes in IAM Identity Center
<a name="step1-import-user-attributes"></a>

1. Import these attributes during the next synchronization with your Identity Provider. Attributes will be imported for both new and existing users. The import process typically completes within 24 hours. For more information about mapping user attributes, see [Attribute mapping between IAM Identity Center and External Identity Providers directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html) and [Enable automatic provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html).

**Note**  
 By enabling User-Based Cost Allocation, user attributes stored in AWS IAM Identity Center will be included as user attribute cost allocation tags in AWS cost management products such as Cost and Usage Report 2.0 and Cost Explorer. Such tags do not constitute your content, and we recommend you do not include sensitive, confidential, or personally identifiable information in them. 

### Step 2: Select user attributes for cost allocation
<a name="step2-select-user-attributes"></a>

1. Open the AWS Management Console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the left panel, under Preferences and Settings, select **Cost Management Preferences**

1. In the Cost Management Preferences page, locate the **User attributes for cost allocation** section.

1. Select up to four attributes from the available options: Cost center, Division, Organization, and Department.

1. Choose **Save changes**. These attributes are automatically activated as Cost Allocation Tags.

### Step 3: Verify Setup
<a name="step3-verify-setup"></a>

1. Return to IAM Identity Center Settings and verify that selected attributes show as "Imported". Confirm attribute data is populated for your users.

1. In Billing and Cost Management console, under Cost Organization, select Cost Allocation Tags. Verify tags show as "Active".

## Viewing user attributes in cost and usage reports
<a name="viewing-user-attributes-in-cur-userattribtute"></a>

 After completing the setup, user attributes will appear in your Cost and Usage Report 2.0 (CUR 2.0) alongside other cost allocation tags. When viewing cost data in CUR 2.0, tags from different sources (resources, user attributes, accounts, and cost categories) are distinguished by prefixes to prevent conflicts when the same tag key is used across multiple contexts. For detailed information about how tag prefixes work and examples of overlapping tag keys, see the [CUR 2.0 Tags Column documentation](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-tag-columns.html). 