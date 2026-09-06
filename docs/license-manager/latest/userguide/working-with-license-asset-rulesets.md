

# Working with license asset rulesets
<a name="working-with-license-asset-rulesets"></a>

This section describes how to create, update, delete, and manage license asset rulesets in AWS License Manager. License asset rulesets define the resource discovery criteria for license asset groups.

## Understanding rulesets
<a name="understanding-rulesets"></a>

A ruleset is a resource within License Manager that defines the resource discovery criteria for a product. It serves as a logical grouping of related rules that can be used for product discovery, with rulesets being able to be used across different products.

There are two different types of rulesets:
+ **AWS Managed Rulesets** - Created and maintained by the License Manager service
+ **Custom Rulesets** - Created and managed by customers

The key benefit of rulesets is that new rules can be added to a ruleset, and those changes are automatically reflected in all license asset groups using the same ruleset, which are automatically used to discover products.

### Ruleset types
<a name="ruleset-types"></a>

License-based  
For self-managed or granted licenses, including AWS Marketplace products

Instance-based  
To discover instances based on certain properties

Each ruleset contains up to 5 rules that define how to discover and track your software. You can create rules to identify licenses, instances, or both, and combine multiple conditions using AND, OR, or exact matching logic to precisely target the resources you want to manage.

The following table shows the available keys you can use when creating license asset ruleset rules:


**License asset ruleset rule keys**  


- **Self-managed License**
  - **Key:** License Configuration ARN / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** Valid ARN
  - **Key:** AWS Account ID / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String

- **Granted License**
  - **Key:** License ARN / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** Valid ARN
  - **Key:** Product SKU / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** Issuer / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** Beneficiary / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** License Status / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** Valid License Status
  - **Key:** Home Region / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** Valid AWS Region

- **Instance**
  - **Key:** Platform / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** Windows, Linux
  - **Key:** EC2 Billing Product / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** windows-server-enterprise, windows-byol, sql-server-standard, sql-server-enterprise, rhel, rhel-byol, rhel-high-availability, ubuntu-pro, suse-linux
  - **Key:** Marketplace Product Code / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** AMI ID / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** Instance Type / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** Instance ID / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** Host ID / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String
  - **Key:** AWS Account ID / **Operator:** Equals, Not Equals / **Value Type:** List / **Accepted Values:** String



## Using AWS-managed rulesets
<a name="using-aws-managed-rulesets"></a>

AWS provides pre-configured rulesets for common software products. These managed rulesets are automatically updated and maintained by AWS.

**To use AWS-managed rulesets**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **License asset discovery and ruleset**.

1. In the **License asset ruleset** section, select **AWS-managed rulesets**.

1. Browse the available managed rulesets and select the ones that match your software products.

Available AWS-managed rulesets include:
+ Microsoft Windows Server Datacenter
+ Microsoft SQL Server Enterprise Edition
+ Microsoft SQL Server Standard Edition
+ Red Hat Enterprise Linux
+ Ubuntu Pro
+ SUSE Enterprise Linux

## Creating custom rulesets
<a name="creating-custom-rulesets"></a>

You can create your own ruleset for defining license and instance tracking rules that are specific to your environment and requirements.

**To create rulesets using the console**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **License asset discovery and ruleset**.

1. In the **License asset ruleset** section, choose **Create Ruleset**.

1. For **Ruleset name**, enter a friendly name for the ruleset.

1. For **Ruleset description**, provide a description of what the ruleset is meant to be.

1. (Optional) Add tags for the ruleset and choose **Next**.

1. In step 2 (Configure discovery of licenses), you can add rules related to your licenses. This ensures the system can use the license to calculate license usage for instances the product is installed on. While configuring discovery of licenses is optional, we recommend adding it if you want license usage calculations.
   + You can add self-managed licenses and provide ARN or account ID
   + You can also add granted licenses (licenses procured from AWS Marketplace) ARN, ProductSKU, etc.
   + You can add multiple rules by choosing **Add rule**

1. In step 3 (Configure discovery of instances), you can add rules on how to discover various instances. This ensures instances can be found based on selection criteria and that those instances are accounted for the product you are configuring your license asset group. You can add one or more rules by selecting the following fields:
   + Platform (Windows or Linux)
   + EC2 billing product code
   + Marketplace product code
   + AMI ID, Host ID, Instance ID, etc.

1. Review your configuration and choose **Submit**.

1. You can see your recently created ruleset under **My rulesets**.

**To create rulesets using the CLI**
+ Use the `create-license-asset-ruleset` command. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/license-manager/create-license-asset-ruleset.html).

  ```
  aws license-manager create-license-asset-ruleset \
      --name "Custom Windows Ruleset" \
      --description "Custom ruleset for Windows Server tracking" \
      --rules '[
        {
          "RuleStatement": {
            "InstanceRuleStatement": {
              "MatchingRuleStatement": {
                "Attribute": "Platform",
                "Values": ["Windows"]
              }
            }
          }
        }
      ]' \
      --client-token unique-token
  ```

## Updating rulesets
<a name="updating-rulesets"></a>

You can update custom rulesets to modify their configuration, add or remove rules, and update tags.

**To update rulesets using the console**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **License asset discovery and ruleset**.

1. In the **License asset ruleset** section, navigate to **My rulesets**.

1. To select a ruleset, select the associated check box and choose **Actions**, **Edit**. Alternatively, choose the ruleset name, then choose the **Edit** button on the ruleset page.

1. From here, you can make the following updates:
   + Edit the ruleset name
   + Edit the ruleset description
   + Add or remove tags associated with the resource

1. Choose **Next** when your changes are complete. From the next screen, you can:
   + Add or remove rules
   + Update license types for existing rules
   + Update conditions for existing rules

1. Choose **Next** when your changes are complete. From the next screen, you can:
   + Add or remove inclusion rules to specify conditions to identify instances you want to include

1. Review and edit changes made on the previous screens. Choose **Submit** to finalize changes.

**To update rulesets using the CLI**
+ Use the `update-license-asset-ruleset` command. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/license-manager/update-license-asset-ruleset.html).

  ```
  aws license-manager update-license-asset-ruleset \
      --license-asset-ruleset-arn arn:aws:license-manager:region:account:ruleset/ruleset-id \
      --name "Updated Custom Windows Ruleset" \
      --description "Updated description for Windows Server tracking"
  ```

## Deleting rulesets
<a name="deleting-rulesets"></a>

You can delete custom rulesets that are no longer needed. Note that rulesets cannot be deleted until they have been removed from all license asset groups.

**To delete rulesets using the console**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **License asset discovery and ruleset**.

1. In the **License asset ruleset** section, navigate to **My rulesets**.

1. To select a ruleset for deletion, select the associated check box and choose **Actions**, **Delete**. Alternatively, choose the ruleset name, then choose the **Delete** button on the ruleset page.

1. To permanently delete the ruleset, type **confirm** in the text box, then choose **Delete**.

**Important**  
This action cannot be undone. Rulesets cannot be deleted until they have been removed from all license asset groups.

**To delete rulesets using the CLI**
+ Use the `delete-license-asset-ruleset` command. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/license-manager/delete-license-asset-ruleset.html).

  ```
  aws license-manager delete-license-asset-ruleset \
      --license-asset-ruleset-arn arn:aws:license-manager:region:account:ruleset/ruleset-id
  ```

## Getting ruleset details
<a name="getting-rulesets"></a>

You can retrieve detailed information about a specific ruleset, including its configuration and rules.

**To get rulesets using the CLI**
+ Use the `get-license-asset-ruleset` command. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/license-manager/get-license-asset-ruleset.html).

  ```
  aws license-manager get-license-asset-ruleset \
      --license-asset-ruleset-arn arn:aws:license-manager:region:account:ruleset/ruleset-id
  ```

## Listing rulesets
<a name="listing-rulesets"></a>

You can list all rulesets in your account to get an overview of your available rulesets.

**To list rulesets using the CLI**
+ Use the `list-license-asset-rulesets` command. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-license-asset-rulesets.html).

  ```
  aws license-manager list-license-asset-rulesets \
      --max-results 50 \
      --next-token token-from-previous-call
  ```