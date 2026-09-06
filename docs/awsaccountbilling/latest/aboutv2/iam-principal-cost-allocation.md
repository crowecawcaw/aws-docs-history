

# Using IAM principal for cost allocation
<a name="iam-principal-cost-allocation"></a>

## Overview
<a name="iam-principal-cost-allocation-overview"></a>

AWS supports cost allocation for Amazon Bedrock based on IAM principal identity and tags, enabling organizations to track usage and costs by caller identity across applications and organizational structures. This feature integrates with AWS Cost and Usage Reports (CUR 2.0) and AWS Cost Management tools to provide visibility into generative AI spending.

## How IAM principal based cost allocation works
<a name="iam-principal-cost-allocation-how-it-works"></a>

When you enable IAM principal data in CUR 2.0, AWS automatically records the caller identity (IAM principal ARN) for each Bedrock API call in the `line_item_iam_principal` column. When you additionally apply tags to IAM principals (users or roles), those tags are automatically captured with associated costs and token usage. This eliminates manual reconciliation processes that required combining CloudWatch and CloudTrail logs with billing data.

## Key benefits
<a name="iam-principal-cost-allocation-benefits"></a>

This capability transforms how organizations manage their generative AI costs. Once enabled, you gain immediate visibility into which users and roles are invoking Bedrock models through automatic caller identity tracking. When you layer on IAM principal tags, you can map this usage and costs to your organizational structures, teams, projects, and applications.

This visibility enables effective cost allocation across your organization, supports informed AI resource planning decisions, and reveals optimization opportunities to reduce spending. The feature integrates seamlessly with your existing AWS Cost Management workflows through Cost Explorer and AWS Cost and Usage Reports (CUR 2.0), requiring no additional tools or processes.

Organizations can implement accurate chargeback and showback costs, ensuring accountability for AI spending.

## Prerequisites
<a name="iam-principal-cost-allocation-prereqs"></a>

Before you can use IAM principal tags for cost allocation, ensure you have:
+ **IAM identities:** IAM users or roles that make Amazon Bedrock API calls
+ **IAM principal tags:** Tags applied to IAM users or roles in the IAM console
+ **Permissions:** Access to IAM and Billing and AWS Cost Management consoles

## Setting up IAM principal tags for cost allocation
<a name="iam-principal-cost-allocation-setup"></a>

### Step 1: Apply IAM principal tags in the IAM console
<a name="iam-principal-cost-allocation-step1"></a>

1. Navigate to the IAM console.

1. Select the IAM users or roles that access Amazon Bedrock.

1. Apply tags that represent your organizational structure (for example, `department`, `cost-center`, `team`, `project`, `environment`).

**Note**  
For Amazon Bedrock, tags only appear for activation after the IAM principal with the tags has made at least one API call. This applies whether the principal is an IAM user, role, or assumed role session.

### Step 2: Activate IAM principal tags for cost allocation and verify setup
<a name="iam-principal-cost-allocation-step2"></a>

1. Open the Billing and AWS Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the left navigation pane, under **Cost Organization**, choose **Cost Allocation Tags**.

1. Filter for IAM principal type tags.

1. Search for and select the IAM principal tags that you want to activate.

1. Choose **Activate**.

1. Verify that these tags show as **Active**.

**Note**  
After you apply tags to your IAM principals, it can take up to 24 hours for the tag keys to appear on your cost allocation tags page for activation. It can then take up to 24 hours for tag keys to activate.

### Step 3: Enable IAM principal data in CUR 2.0
<a name="iam-principal-cost-allocation-step3"></a>

1. Navigate to the Billing and AWS Cost Management console.

1. Go to the **Data Exports** section.

1. When creating a new data export, select **Standard data export ** (CUR 2.0).

1. Under **Additional export content**, select **Include caller identity (IAM principal) allocation data**.

1. Save the configuration.

This enables the `line_item_iam_principal` column and associated IAM principal tags in your CUR 2.0 export.

**Note**  
Enabling IAM principal data will increase the number of CUR rows by a factor of the number of calling identities accessing each model, resulting in larger file sizes compared to typical CUR exports.

## Viewing IAM principal tags in AWS Cost and Usage Reports
<a name="iam-principal-cost-allocation-cur"></a>

After completing the setup, IAM principal tags appear in your CUR 2.0 alongside other cost allocation tags. When viewing cost data in CUR 2.0, tags from different sources (resources, user attributes, accounts, IAM principals, and cost categories) are distinguished by prefixes to prevent conflicts when the same tag key is used across multiple contexts. For detailed information about how tag prefixes work and examples of overlapping tag keys, see the [CUR 2.0 Tags Column documentation](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-tag-columns.html).

### New CUR 2.0 column
<a name="iam-principal-cost-allocation-cur-column"></a>

The `line_item_iam_principal` column contains the AWS IAM ARN of the principal making Bedrock requests. Format examples:
+ `arn:aws:iam::123456789012:user/userID_A`
+ `arn:aws:iam::123456789012:role/application-role`
+ `arn:aws:sts::123456789012:assumed-role/application-role/session-name`

### IAM principal tags in the tags column
<a name="iam-principal-cost-allocation-cur-tags"></a>

IAM principal tags appear with the prefix `iamPrincipal/` followed by your tag key. For example:
+ `iamPrincipal/department`
+ `iamPrincipal/cost-center`
+ `iamPrincipal/app`

## Using IAM principal tags in Cost Explorer
<a name="iam-principal-cost-allocation-ce"></a>

### Grouping by IAM principal tags
<a name="iam-principal-cost-allocation-ce-group"></a>

Create custom cost views by grouping:

1. In Cost Explorer, select the **Group by** dropdown.

1. Choose **Tag** as the grouping dimension.

1. Select your activated IAM principal tag (for example, `iamPrincipal/department`).

1. View aggregated costs by tag value.

### Filtering by IAM principal tags
<a name="iam-principal-cost-allocation-ce-filter"></a>

1. Open Cost Explorer in the Billing and AWS Cost Management console.

1. Add filters for activated IAM principal tags in the **Tag** dropdown.

1. View costs broken down by these IAM principal tags.

## Best practices
<a name="iam-principal-cost-allocation-best-practices"></a>
+ **Use meaningful tag keys:** Choose tags that align with your organizational structure (`department`, `cost-center`, `team`, `project`).
+ **Avoid high-cardinality tags:** Do not use unique session IDs, timestamps, or random GUIDs as tag values.
+ **Standardize tag naming:** Establish consistent tag key naming conventions across your organization.
+ **Review tag usage regularly:** Monitor which tags are being used for cost allocation and deactivate unused tags.
+ **Plan for CUR file size growth:** Account for increased Amazon S3 storage costs when enabling IAM principal data.