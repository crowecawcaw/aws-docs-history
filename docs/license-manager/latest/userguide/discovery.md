# Work with inventory search in License Manager

License Manager uses [Systems Manager inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") to
discover software usage on premises. After you associate a self-managed license with on-premises
servers, License Manager periodically collects software inventory, updates licensing information, and
refreshes its dashboards to report usage.

###### Tasks

- [Set up for inventory search](#discovery-setup "#discovery-setup")
- [Use inventory search](#using-discovery "#using-discovery")
- [Add automated discovery rules to a self-managed
  license](#add-discovery-rule "#add-discovery-rule")
- [Associate a self-managed license with inventory search](#discovered "#discovered")
- [Disassociate a self-managed license and a resource](#disassociate "#disassociate")

## Set up for inventory search

Complete the following requirements before using resource inventory search:

- Enable cross-account inventory discovery by integrating License Manager with your AWS Organizations account.
  For more information, see [Settings in License Manager](settings.md "settings.md").
- Create self-managed licenses for the servers and applications to manage. For example,
  create a self-managed license that reflects the terms of your licensing agreement with
  Microsoft for SQL Server Enterprise.

## Use inventory search

Complete the following steps to search your resource inventory. You can search for
applications by name (for example, names that begin with "SQL Server") and the type of license
included (for example, a license that is not for "SQL Server Web").

###### Search your resource inventory

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Inventory search**.
3. (Optional) You can specify filter options to streamline search results as follows.

| Amazon EC2 resources  | Filter name                                                                                                                                                                      | Description                                          | Logical operators                                                                                           | Supported values |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------- |
| Resource ID           | The ID of the resource.                                                                                                                                                          | `Equals`, `Not equals`                               |                                                                                                             |
| Account ID            | The ID of the AWS account that owns the resource.                                                                                                                                | `Equals`, `Not equals`                               |                                                                                                             |
| Platform name         | The operating system platform for the resource.                                                                                                                                  | `Equals`, `Not equals`,<br>`Begins with`, `Contains` |                                                                                                             |
| Application name      | The name of the application.                                                                                                                                                     | `Equals`, `Begins with`                              |                                                                                                             |
| License included name | The type of license included.                                                                                                                                                    | `Equals`, `Not equals`                               | • `SQL Server Enterprise`<br>• `SQL Server Standard`<br>• `SQL Server Web`<br>• `Windows Server Datacenter` |
| Tag                   | A metadata tag key and optional value that's assigned to the<br>resource.<br>Note, the `Not equals` logical operator is<br>only available if cross-account discovery is enabled. | `Equals`, `Not equals`                               |                                                                                                             |

| Amazon RDS resources       | Filter name                                                           | Description | Logical operators                                                                                                                                              | Supported values |
| -------------------------- | --------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Engine Edition             | The database engine edition.                                          | `Equals`    | • `oracle-ee`<br>• `oracle-se`<br>• `oracle-se1`<br>• `oracle-se2`<br>• `db2-se`<br>• `db2-ae`                                                                 |
| License Pack (Oracle only) | The management pack associated with an Amazon RDS for Oracle license. | `Equals`    | • `Spatial and Graph`<br>• `Active Data Guard`<br>• `Label Security`<br>• `Oracle On-Line Analytical Processing (OLAP)`<br>• `Diagnostic Pack and Tuning Pack` |

For more information about Amazon RDS database product licenses, see [RDS for Oracle licensing options](../../../AmazonRDS/latest/UserGuide/Oracle.Concepts.md "../../../AmazonRDS/latest/UserGuide/Oracle.Concepts.md"), or
[RDS for Db2 licensing options](../../../AmazonRDS/latest/UserGuide/db2-licensing.md "../../../AmazonRDS/latest/UserGuide/db2-licensing.md")
in the _Amazon RDS User Guide_.

## Add automated discovery rules to a self-managed

license

After you add product information to your self-managed license, License Manager can track license
usage for the instances that have those products installed. For more information, see [Automated discovery of inventory in License Manager](automated-discovery.md "automated-discovery.md").

###### To add automated discovery rules to a self-managed license

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Open the **Inventory search** page.
3. Select the resource and choose **Add automated discovery rules**.
4. For **Self-managed license**, select a self-managed license.
5. Specify the products to discover and track.
6. (Optional) Select **Stop tracking instances when software is uninstalled**
   to make the license available for reuse after License Manager detects that the software was uninstalled and
   any license affinity period has elapsed.
7. (Optional) To exclude resources from automated discovery select **Add exclusion rule**.

###### Note

Exclusion rules do not apply to Amazon RDS products (such as RDS for Oracle and RDS for Db2).

    1. Choose a **Property** to filter on, currently **Account ID**, and **Tag** are supported.
    2. Enter the information to identify that property. For an **Account ID** specify the 12 digit AWS Account ID as the value. For **Tags** enter a key/value pair.
    3. Repeat step 7 to add additional rules.

8. Choose **Add**.

## Associate a self-managed license with inventory search

After you have identified the unmanaged resources that you need to manage, you can manually
associate them with a self-managed license, instead of using automated discovery.

###### To associate a self-managed license with a resource

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Open the **Inventory search** page.
3. Select the resource and choose **Associate self-managed
   license**.
4. For **self-managed license name**, select a self-managed license.
5. (Optional) Select **Share self-managed license with all my member
   accounts**.
6. Choose **Associate**.

## Disassociate a self-managed license and a resource

If the licensing terms from your software vendors change, you can disassociate resources
that were associated manually and then delete the self-managed license.

###### To disassociate a self-managed license and a resource

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **self-managed license**.
3. Choose the name of the self-managed license.
4. Choose **Resources**.
5. Select each of the resources to disassociate from the self-managed license and then
   choose **Disassociate resource**.
