# Create a self-managed license in

License Manager

A self-managed license represents the licensing terms in the agreement with your software
vendor. Your self-managed license specifies how your licenses should be counted (for example, by
vCPUs or number of instances). It also specifies limits on your usage, so that you can prevent
usage from going over the number of allocated licenses. Additionally, it can also specify other
constraints on your licenses, such as the tenancy type.

###### Note

Before creating a self-managed license, consider your organizational structure:

- Single account usage: Create self-managed licenses directly in your account
- Multi-account usage: Consider creating License asset groups first, then associate self-managed licenses for centralized management

###### Considerations for Amazon RDS for Oracle and Amazon RDS for Db2 databases

When you add product information to configure automated discovery of Amazon RDS for Oracle or
Amazon RDS for Db2 databases, the following requirements apply:

- The supported license counting type is `vCPU`.
- Rules are not supported.
- Hard license limits are not supported.
- You can track one product version per self-managed license.
- You cannot track Amazon RDS databases and other products using the same self-managed
  license.

###### To create a self-managed license using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **self-managed licenses**.
3. Choose **Create self-managed license**.
4. In the **Configuration details** panel, provide the following
   information:
   - **Self-managed license name** – A name for the self-managed
     license.
   - **Description** – An optional description of the self-managed
     license.
   - **Expiry Date** – An optional expiry date of the self-managed
     license.
   - **License type** – The counting model for this license
     (**vCPUs**, **Cores**, **Sockets**, or
     **Instances**).
   - **Number of <option>** – The option displayed depends on
     the license type. When the license limit is exceeded, License Manager notifies you (soft limit) or
     prevents a resource from deploying (hard limit).
   - **Enforce license limit** – If selected, the license limit is a
     hard limit.
   - **Rules** – One or more rules. For each rule, select a rule type,
     provide a rule value, and choose **Add rule**. The rule types displayed
     depend on the license type. For example, minimum values, maximum values, and tenancy. If you
     do not specify a tenancy type, all are accepted.

5. (Optional) In the **Automated discovery rules** panel, do the following:
   1. Choose the product name, product type, and resource type for each product to discover
      and track using [automated discovery](automated-discovery.md "automated-discovery.md").
   2. Select **Stop tracking instances when software is uninstalled** to make
      the license available for reuse after License Manager detects that the software was uninstalled and any
      license affinity period has elapsed.
   3. (Optional) If your account is a License Manager management account for an Organizations you have to option to define resources to exclude from automated discovery.
      To do so select **Add exclusion rule**, choose the property to filter on, AWS account IDs and resource Tags are supported, then
      enter the information to identify that property.

6. (Optional) Expand the **Tags** panel to add one or more tags to your
   self-managed license. Tags are key/value pairs. Provide the following information for each
   tag:
   - **Key** – The searchable name of the key.
   - **Value** – The value for the key.

7. Choose **Submit**.

###### Note

Once the License Expiry Date is set, License Manager can send notifications on 120 days, 90 days, 60 days, 30 days, 0 day to the Amazon SNS topic that's configured in [Managed license settings in License Manager](settings-managed-licenses.md "settings-managed-licenses.md").

###### To create a self-managed license using the command line

- [create-license-configuration](../../../cli/latest/reference/license-manager/create-license-configuration.md "../../../cli/latest/reference/license-manager/create-license-configuration.md") (AWS CLI)
- [New-LICMLicenseConfiguration](../../../powershell/latest/reference/items/New-LICMLicenseConfiguration.md "../../../powershell/latest/reference/items/New-LICMLicenseConfiguration.md") (AWS Tools for PowerShell)
