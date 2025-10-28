# Automated discovery of inventory in License Manager

License Manager uses [Systems Manager inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") to
discover software usage on Amazon EC2 instances and on-premises instances. You can add product
information to your self-managed license, and License Manager will track the instances that have those
products installed. Additionally, you can specify exclusion rules based on your licensing
agreement to decide which instances to exclude. You can exclude instances belonging to AWS
account IDs or associated with resource tags from being considered for automated discovery

Automated discovery can be added to a new license set, to an existing self-managed license,
or resources in your inventory. Rules for automated discovery can be edited at any time through
the CLI using the [UpdateLicenseConfiguration](../APIReference/API_UpdateLicenseConfiguration.md "../APIReference/API_UpdateLicenseConfiguration.md") API command. To edit rules in the console, you must delete
the existing self-managed license and create a new one.

To use automated discovery, you must add product information to your self-managed license.
You can do so when you create the self-managed license using **Inventory
search**.

You cannot manually disassociate instances tracked by automated discovery. By default,
automated discovery does not disassociate tracked instances after the software is uninstalled.
You can configure automated discovery to stop tracking instances when the software is uninstalled.

After you configure automated discovery, you can track license usage through the License Manager
dashboard.

###### Prerequisites

- Enable cross-account inventory search by integrating License Manager with your AWS Organizations account.
  For more information, see [Settings in License Manager](settings.md "settings.md").

###### Note

Single accounts can set up automated discovery but cannot add exclusion rules.

- Install Systems Manager inventory on your instances.

###### To configure automated discovery when you create a self-managed license

You can configure automated discovery rules and exclusion rules when you create a
self-managed license. For more information, see [Create a self-managed license in
License Manager](create-license-configuration.md "create-license-configuration.md").

###### To add automated discovery rules to an existing self-managed license

Use the process below to add automated discovery rules to existing self-managed licenses
through the console, you can also do this from the **Inventory search** pane by
selecting an resource ID and selecting **Add automated discovery
rules**.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Self-managed licenses**.
3. Choose the name of the self-managed license to open the license details page.
4. On the **Automated discovery rules** tab, choose **Add automated
   discovery rules**.
5. Specify the products to discover and track.

###### Note

The following limitations apply to Amazon RDS database products (such as Amazon RDS for Oracle and
Amazon RDS for Db2):

    * A maximum of one rule specifying an Amazon RDS database product is supported.
    * Only one license configuration is allowed for each Amazon RDS database product.

6. (Optional) Select **Stop tracking instances when software is uninstalled**
   to make the license available for reuse after License Manager detects that the software was uninstalled and
   any license affinity period has elapsed.
7. (Optional) To define resources to exclude from automated discovery select **Add exclusion rule**.

###### Note

    * Exclusion rules do not apply to RDS database products (such as Amazon RDS
     for Oracle and Amazon RDS for Db2).
    * Exclusion rules are only available if [Cross-account resource discovery](settings-managed-licenses.md#settings-resource-discovery "settings-managed-licenses.md#settings-resource-discovery") has been enabled.
    1. Choose a **Property** to filter on, currently **Account ID**, and **Tag** are supported.
    2. Enter the information to identify that property. For an **Account ID** specify the 12 digit AWS account ID as the value. For **Tags** enter a key/value pair.
    3. Repeat step 7 to add additional rules.

8. When you are finished choose **Add** to apply your automated discovery rule.
